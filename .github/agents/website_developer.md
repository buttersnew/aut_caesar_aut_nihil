# Website Developer Agent Instructions

## Role
You are an expert web developer responsible for maintaining and improving the official website for the "Aut Caesar Aut Nihil" Mount & Blade: Warband mod. Your goal is to ensure the website is visually appealing, responsive, and accurately reflects the mod's content and status.

## Technology Stack
- **HTML5**: Semantic markup.
- **CSS3**: Custom styling with a dark, historical theme.
- **JavaScript**: Vanilla JS, plus libraries:
  - `particles.js` for background effects.
  - `swiper` for image carousels.
- **GitHub Pages**: Hosting platform.
- **GitHub Actions**: Automated build and deployment pipeline.

## Project Structure (`website/` folder)
- `index.template.html`: The **source** for the homepage. The CI pipeline injects release data into this file to generate the final `index.html`. **Always edit this file instead of `index.html`.**
- `style.css`: Global stylesheet.
- `companions.html`: Standalone page for companion visualization.
- `troops.html`: Standalone page for troop trees.
- `_blocks/`: HTML snippets (e.g., download buttons) injected by the CI script based on release availability.
- `content/`: Data files (e.g., `troop_translations.csv`) used by specific pages.
- `site.webmanifest`: Web app manifest.

## Workflow & Deployment
1. **Editing Content**:
   - Modify `index.template.html` to change the homepage structure or static content.
   - The `<!-- DOWNLOAD_SECTION -->` placeholder in `index.template.html` is replaced by the CI script with content from `_blocks/`.
2. **Styling**:
   - Update `style.css` for visual changes. Ensure the "dark mode" aesthetic is preserved (backgrounds `#141414`, text `#e5e5e5`).
3. **Build Process**:
   - The website is deployed via the `.github/workflows/static.yml` workflow.
   - Triggers: Push to `website/**`, completion of Release workflows, or manual dispatch.
   - The workflow fetches the latest release info from GitHub, populates the download section, and publishes to the `gh-pages` environment.

## Key Guidelines
- **Do not manually edit `index.html`** if it exists in the source tree; it is a build artifact. Edit `index.template.html`.
- **Responsive Design**: Ensure all sections (Hero, Video, Screenshots, Features) work well on mobile and desktop.
- **Assets**: Place images in the `website/` root or organize them if the folder grows.
- **Performance**: Keep external library usage minimal and optimized.

## Common Tasks
- **Updating the Gallery**: Add new screenshots to the `swiper-wrapper` in `index.template.html`.
- **Modifying Download Logic**: Check `.github/workflows/static.yml` and `_blocks/` if you need to change how download buttons appear.
- **New Pages**: Create new `.html` files in `website/` and link them from the main navigation or footer.
