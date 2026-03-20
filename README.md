# FUSSI EDITORIAL

A premium editorial platform and streetwear label defining the intersection of technical performance and high-fashion aesthetics.

## Folder Structure

- `/`: Root directory (contains `index.html`, `404.html`)
- `/assets/`: Shared assets
  - `/css/`: Stylesheets
  - `/js/`: JavaScript files
  - `/images/`: Image assets
  - `/icons/`: SVG/Icon assets
  - `/fonts/`: Web fonts
- `/cart/`: Shopping cart page
- `/collection/`: Product collection/listing page
- `/product/`: Product detail page
- `/pitch-noir/`: Editorial/Design system page

## Local Preview

To preview the website locally, you can use any static file server. For example, if you have Python installed:

```powershell
python -m http.server 8000
```

Then open `http://localhost:8000` in your browser.

## Deployment to GitHub Pages

1. Push this repository to GitHub.
2. Go to **Settings > Pages**.
3. Under **Build and deployment > Source**, select **Deploy from a branch**.
4. Select your main branch and the root folder (`/`).
5. Click **Save**.

The site will be live at `https://<your-username>.github.io/<repository-name>/`.

## Maintenance

- **Shared Assets**: Put all global CSS and JS in the `/assets` folder and reference them using relative paths.
- **Adding Pages**: Create a new folder with an `index.html` file to create a clean URL (e.g., `/new-page/`).
