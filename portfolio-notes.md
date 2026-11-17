# Sean Cervenka’s portfolio

## Style

The opening gives Sean’s name the largest type, followed by his fields and a short introduction. About uses a tinted band and two columns when there is enough room. On smaller screens, the page reads in one column.

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

- Open `index.html` in a browser to view the portfolio. Edit this file to change the opening, About copy, and navigation. The About section includes Sean’s Esri internship.
- Edit `style.css` to change colors, fonts, and spacing. Shared values are at the top. The wide-screen rules are at the bottom.
- Put approved images and documents in `assets/`. For example, `assets/resume.pdf` points to a file named `resume.pdf` in that folder. Use descriptive alt text for map previews.
- Navigation, the **About me** button, and the **Skip to content** link use HTML links to jump down the page. Hover and keyboard focus styles live in `style.css`.

## Planned additions

- **Resume.** Once a resume PDF is supplied and approved for public sharing, save it in `assets/`. Add **Download Resume** first in the opening actions and give it the strongest button style. Link to the actual file with its relative path and the HTML `download` attribute. Use a quieter style for the other actions.
- **Projects.** Add the section between Home and About once there is at least one approved project. Use a vertical list with each project’s title, Sean’s contribution, and an approved map preview or link when available. Add **Projects** to the navigation and **View projects** to the opening actions alongside **About me**.
- **Contact and LinkedIn.** Add the approved LinkedIn URL as an easy-to-find secondary link in the opening. Add a Contact footer with approved links or details, and connect **Contact** in the navigation to it.
