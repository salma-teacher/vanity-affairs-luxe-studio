# Vanity Affairs Luxe Studio — website

Website for Vanity Affairs Luxe Studio, a makeup artistry studio in Toronto (bridal, party and fashion, celebrity, commercial, music video and film makeup).

Hosted with GitHub Pages.

## Editing

- Page text and contact details live in `_src/build.py` (see `SITE` and `PAGES` at the top).
- Photos go in `images/<page>/`, e.g. `images/bridal/01.jpg`. The home page hero image is `images/home/hero.jpg`, and the About portrait goes in `images/about/`.
- Rebuild the pages after any change:

```
python3 _src/build.py
```
