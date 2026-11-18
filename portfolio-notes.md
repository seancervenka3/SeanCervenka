# Sean Cervenka’s portfolio

## Style

The opening gives Sean’s name the largest type, followed by his fields and current role. Projects uses compact rows with matching thumbnail frames and expandable details. About uses a tinted band, with a section title on the left and the résumé on the right when there is enough room. On smaller screens, the page reads in one column.

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

- Open `index.html` in a browser to view the portfolio. Edit this file to change the opening, projects, résumé entries, contact links, and navigation. In Projects, each `article` contains the thumbnail, summary, role, and an expandable `details` area for supporting materials.
- Edit `style.css` to change colors, fonts, and spacing. Shared values are at the top. The wide-screen rules are at the bottom.
- Put approved images and documents in `assets/`. For example, `assets/resume.pdf` points to a file named `resume.pdf` in that folder. Use descriptive alt text for map previews.
- Navigation, the Home actions, and the **Skip to content** link use HTML links. **Project details** opens and closes with a click or the keyboard. Hover and keyboard focus styles live in `style.css`.

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
- Bicycle Infrastructure and Intermodal Connectivity in Greater Madison, WI, May 2025, co-authored with Isaac Lebeck
- Trails Manager, two technical presentations about ArcGIS apps and data workflows
- European Airports, a map of the top 20 European airports by 2023 passenger count
- Geographic Features of Africa, a shaded-relief reference map

The résumé descriptions and responsibilities are in About in `index.html`. The Projects section includes the supporting materials listed below.

### Skills and coursework

- Technical: GIS Software & Application Development, Geospatial Data Management, GIS Automation & Scripting, Cartographic Design
- Analytical: Spatial Analysis & Modeling, Spatial Statistics, Data Quality Assessment, Geospatial Problem Solving

| GIS & Cartography | Data Science & Analysis |
| --- | --- |
| Remote Sensing (371) | Advanced Geocomputing & Geospatial Big Data Analytics (573) |
| GIS Applications (578) | Geospatial Database Design & Development (574) |
| GIS and Spatial Analysis (579) | Advanced Quantitative Methods (560) |
| Graphic Design in Cartography (572) | |

### Contact

- Email [seancervenka@gmail.com](mailto:seancervenka@gmail.com)
- [LinkedIn](https://www.linkedin.com/in/seancervenka)

## Project media

Previews are separate JPEGs in `assets/` with a longest side of 800 pixels. The site uses matching frames and keeps the original maps available for reading at full size.

| Project | Preview source and supporting files |
| --- | --- |
| Rugged SystEMS | `rugged-systems-cost-distance-preview.jpg` comes from `Screenshot 2026-08-07 135602.png`. It illustrates the final cost-distance layer. The app used a separate setup for A* routing. The details also link to the supplied Devpost submission and hackathon recording. |
| Bicycle infrastructure | `madison-bicycle-crashes-preview.jpg` comes from `Madison Crash Density_Final.png`. The gallery has matching previews from `Overall Score.png`, `Quanatative.final.png` (qualitative), and `Quantitative.actual.png`. It links to all four originals and the complete report PDF. |
| Trails Manager | `trails-manager-web-map-preview.jpg` is cropped to the map on slide 7 of `Apps & APIs.pptx`. The details describe both presentations and link to the supplied `Apps & APIs.pdf` and revised `S123_Sync_PresentationVersion.py`. |
| European Airports | `european-airports-preview.jpg` comes from page 1 of `Airports_Final.pdf`. The full PDF is linked in the details. |
| Geographic Features of Africa | `geographic-features-of-africa-preview.jpg` comes from page 1 of `FinalAfricaMap(2).pdf`. The full PDF is linked in the details. |

Both original PowerPoint decks stay local through `.gitignore`. Add a link to an approved Data &amp; Services PDF or publicly shared deck when it is ready. A signed-out browser window can verify whether visitors can watch the Drive recording.

## Planned additions

- **Resume.** Once a resume PDF is supplied and approved for public sharing, save it in `assets/`. Add **Download Resume** first in the opening actions and give it the strongest button style. Link to the actual file with its relative path and the HTML `download` attribute. Use a quieter style for the other actions.
