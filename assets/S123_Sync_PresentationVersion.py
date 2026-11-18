from arcgis.gis import GIS
from arcgis.features import FeatureLayer
from arcgis.apps.survey123 import SurveyManager
import pandas as pd
from datetime import datetime

# ---------------------------
# Helper: Build match ID using CreationDate
# ---------------------------
def build_match_id(creation_date):
    dt = pd.to_datetime(creation_date, unit="ms", errors="coerce")

    if pd.notnull(dt):
        dt = dt.floor("min")
        dt = dt.strftime("%Y-%m-%d %H:%M")
    else:
        dt = ""

    return dt

# ---------------------------
# Connect to AGOL
# ---------------------------
agol = GIS("home")
survey_manager = SurveyManager(agol)
print(survey_manager)

survey = survey_manager.get("<SurveyID>")
df = survey.download("DF")

# ---------------------------
# Clean dataframe
# ---------------------------
df = df.where(pd.notnull(df), None)

date_fields = [
    "date_time",
    "CreationDate",
    "EditDate",
    "date_assigned",
    "date_completed"
]

for field in date_fields:
    if field in df.columns:
        df[field] = pd.to_datetime(df[field], errors="coerce")
        df[field] = df[field].apply(lambda x: None if pd.isna(x) else x)

now = datetime.now()
df["CreationDate"] = df["CreationDate"].apply(lambda x: x if x else now)
df["EditDate"] = df["EditDate"].apply(lambda x: x if x else now)

# ---------------------------
# Build match_id (AGOL)
# ---------------------------
df["match_id"] = df["CreationDate"].apply(build_match_id)

# ---------------------------
# Allowed fields (ADD ONLY)
# ---------------------------
allowed_fields = [
    "date_time",
    "DateOnly",
    "date_cansee",
    "trail_name",
    "trail_name_other",
    "issue",
    "issue_other",
    "internal_maintenance_tracking",
    "maintenance_notes",
    "field_15"
]

# ---------------------------
# Connect to Enterprise
# ---------------------------
enterprise = GIS(
    "portal_url",
    "username",
    "password"
)

enterprise_url = "enterprise server url"
enterprise_layer = FeatureLayer(enterprise_url, gis=enterprise)

# ---------------------------
# Inspect fields
# ---------------------------
for f in enterprise_layer.properties.fields:
    print(f["name"])

# ---------------------------
# Get existing records
# ---------------------------
existing = enterprise_layer.query(
    where="1=1",
    out_fields="CreationDate"
)

# ---------------------------
# Build existing key set
# ---------------------------
existing_keys = set()

for f in existing.features:
    attrs = f.attributes
    key = build_match_id(attrs.get("CreationDate"))
    existing_keys.add(key)

# ---------------------------
# Identify NEW records only
# ---------------------------
add_df = df[~df["match_id"].isin(existing_keys)]

print(f"New records to ADD: {len(add_df)}")

# ---------------------------
# Add records ONE BY ONE (for logging)
# ---------------------------
for _, row in add_df.iterrows():
    add_attrs = {}

    for field in allowed_fields:
        value = row.get(field)

        if pd.isna(value):
            value = None

        add_attrs[field] = value

    try:
        result = enterprise_layer.edit_features(
            adds=[{"attributes": add_attrs}]
        )
        print("ADD SUCCESS:", result)

    except Exception as e:
        print("ADD FAILED:", add_attrs)
        print(e)
        break
