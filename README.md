# More than checking tickets

A responsive, static web edition of the approved `More than checking tickets_v3.pdf`. Includes the full case study and practitioner account, 41 quotations across five themes, the supplied cover artwork, and the complete PDF download.

## Preview

Open `public/index.html` directly in a browser, or serve the `public` folder:

```sh
python3 -m http.server 8080 --directory public
```

Then open http://localhost:8080.

## Deploy to Render

1. Add the contents of this folder to a GitHub or GitLab repository. Keep `render.yaml` at its root.
2. In Render, choose **New → Blueprint**, connect that repository and apply the included configuration.
3. Alternatively choose **New → Static Site**, connect the repository, set the build command to `python3 build.py`, and the publish directory to `public`.
4. Review the resulting Render URL before connecting a custom domain.

There are no third-party dependencies, API keys, database, tracking scripts or external fonts. The prebuilt `public` folder can also be hosted by any static web host.

Render references: https://render.com/docs/static-sites and https://render.com/docs/blueprint-spec.

## Edit the site

- `content.json`: checked report paragraphs, statistics and quotations. After editing, run `python3 build.py` to regenerate the HTML. Preserve the current array structure.
- `build.py`: page structure and interface wording.
- `public/styles.css`: colours, typography, mobile and print layouts.
- `public/app.js`: mobile navigation and theme filters.
- `public/assets/cover.png`: the existing embedded cover artwork extracted from the final PDF, used without AI reconstruction. The hero shows its photograph through a CSS window.
- `public/assets/more-than-checking-tickets.pdf`: the supplied finished PDF, unchanged.

Text content was checked against the final PDF, including the revised coach-locking paragraph. Quotations retain the wording in that document. The original survey metadata was not provided, so figures are linked to the relevant report page, with no new source or verification claims.

All testimony is present in the HTML and visible without JavaScript. The optional filters, keyboard-accessible menu, skip link, visible focus styles, reduced-motion setting and print styles provide additional navigation options. This is not a formal accessibility audit.

This package is ready to deploy, but has not been published to Render.
