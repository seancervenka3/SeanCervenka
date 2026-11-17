# Sean Cervenka’s portfolio

## Style

The opening gives Sean’s name the largest type, followed by his fields and current role. Projects lists the two projects and links to their full entries in About. About uses a tinted band, with a section title on the left and the résumé on the right when there is enough room. On smaller screens, the page reads in one column.

| Color | Hex | Use |
| --- | --- | --- |
| Warm cream | `#F7F2E8` | Main background and button text |
| Charcoal | `#252C32` | Headings and body text |
| Slate blue | `#31566C` | Links, buttons, and contour lines |
| Dusty pink | `#DAB4C1` | Illustration and section border |
| Soft pink tint | `#F3E9E3` | About background |
| Warm gray | `#D2C6BE` | Header divider |

The pink and blue draw on the TV Girl palette Sean likes. The original contour lines reference cartography and time outdoors, and the curved frame takes inspiration from Alphonse Mucha’s ornament. The illustration sits beside the introduction on wide screens. Georgia gives the headings their shape, and the device’s standard sans-serif font keeps navigation and body text easy to read. The page stays still, including when scrolling to a section.

## Where to make edits

- Open `index.html` in a browser to view the portfolio. Edit this file to change the opening, project links, résumé entries, contact links, and navigation. Each project has a short link in Projects pointing to its full entry in About.
- Edit `style.css` to change colors, fonts, and spacing. Shared values are at the top. The wide-screen rules are at the bottom.
- Put approved images and documents in `assets/`. For example, `assets/resume.pdf` points to a file named `resume.pdf` in that folder. Use descriptive alt text for map previews.
- Navigation, the Home actions, and the **Skip to content** link use HTML links. Hover and keyboard focus styles live in `style.css`.

## Approved public facts

### Education

- University of Wisconsin-Madison, September 2024 - May 2027
- Bachelor of Science: Cartography and Geographic Information Systems; Physical Geography
- Certificate in Geospatial Data Science

### Experience

| Organization | Location | Role | Dates |
| --- | --- | --- | --- |
| Esri \| Educational & Support Services | Redlands, CA | Technical Support Intern | May 2026 - August 2026 |
| State Cartographer’s Office \| WISDOT Right-Of-Way Team | Madison, WI | Project Manager | September 2026 - Present |
| State Cartographer’s Office \| WISDOT Right-Of-Way Team | Madison, WI | GIS Intern | October 2025 - May 2026 |
| Sauk County \| Land Information | Baraboo, WI | GIS Intern & Land Records Assistant | May 2025 - August 2025 |

### Projects

- Esri’s Weekend of Innovation Hackathon | Rugged SystEMS | Overall Winner, July 2026
- Bicycle Infrastructure and Intermodal Connectivity in Greater Madison, WI, May 2025

The full approved responsibilities, achievements, and project descriptions are in About in `index.html`.

### Skills and coursework

- Technical: ArcGIS Pro, ArcGIS Online, ArcGIS Enterprise, ArcGIS Field Maps, QGIS, Adobe Illustrator, Python, R, SQL
- Analytical: Spatial Modeling, Data Quality Assurance, Change Detection / Temporal Analysis

| GIS & Cartography | Data Science & Analysis |
| --- | --- |
| Remote Sensing (371) | Advanced Geocomputing & Geospatial Big Data Analytics (573) |
| GIS Applications (578) | Geospatial Database Design & Development (574) |
| GIS and Spatial Analysis (579) | Advanced Quantitative methods (560) |
| Graphic Design in cartography (572) | |

### Contact

- Email [seancervenka@gmail.com](mailto:seancervenka@gmail.com)
- [LinkedIn](https://www.linkedin.com/in/seancervenka)

## Planned additions

- **Resume.** Once a resume PDF is supplied and approved for public sharing, save it in `assets/`. Add **Download Resume** first in the opening actions and give it the strongest button style. Link to the actual file with its relative path and the HTML `download` attribute. Use a quieter style for the other actions.
