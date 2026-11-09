"""Builds the Vanity Affairs Luxe Studio website.

Edit the text in this file, then run:  python3 _src/build.py
It writes the .html pages into the repository root.

Photos: drop images into images/<page-slug>/ (e.g. images/bridal/01.jpg).
Any .jpg/.jpeg/.png/.webp found there replaces the placeholders on that page.
"""
from pathlib import Path
import html

ROOT = Path(__file__).resolve().parent.parent
IMG_EXT = {".jpg", ".jpeg", ".png", ".webp"}

# ---------------------------------------------------------------- settings
SITE = {
    "name": "Vanity Affairs Luxe Studio",
    "tag": "Makeup Artistry · Since 2008",
    "artist": "Salma Sami Khan",
    "city": "Toronto & the GTA",
    # TODO: replace with real details
    "email": "",          # e.g. "hello@vanityaffairsluxestudio.com"
    "phone": "",          # e.g. "+1 416 555 0123"
    "instagram": "",      # e.g. "vanityaffairsluxestudio"
}

PORTFOLIO = [
    ("bridal", "Bridal"),
    ("party-fashion", "Party & Fashion"),
    ("celebrities", "Celebrities"),
    ("commercials", "Commercials"),
    ("music-videos", "Music Videos"),
    ("movies", "Movies"),
]

# ---------------------------------------------------------------- page content
PAGES = {
    "bridal": {
        "title": "Bridal Makeup",
        "eyebrow": "Bridal",
        "intro": "Timeless, camera-ready bridal makeup that looks beautiful in person, in photographs and from the first look to the last dance.",
        "card": "Elegant, long-wearing looks for the bride and her party, designed around you.",
        "body_title": "Your day, your look",
        "body": [
            "Every bride is different, so every bridal look starts with a conversation. We talk about your dress, your style, your skin and the feeling you want to have when you see yourself in the mirror.",
            "From soft, natural glamour to a bold, classic finish, your makeup is built to last through tears, hugs, heat and hours of photographs, while still feeling light on your skin.",
        ],
        "features": [
            "Bridal makeup trial before the big day",
            "Long-wearing, photo-friendly products",
            "Makeup for the bridal party and family",
            "On-location service to your home, hotel or venue",
            "Looks for engagement shoots, mehndi, nikah, reception and multi-day celebrations",
        ],
    },
    "party-fashion": {
        "title": "Party & Fashion Makeup",
        "eyebrow": "Party & Fashion",
        "intro": "Polished looks for special events, editorial shoots and the runway, from effortless glow to statement glamour.",
        "card": "Event glamour, editorial shoots and runway looks with a professional finish.",
        "body_title": "Made for the moment",
        "body": [
            "Whether it is a gala, a birthday, a graduation or a photoshoot, you deserve to feel confident and look your best all evening.",
            "Fashion and runway work calls for speed, precision and creativity. Looks are designed to match the designer's vision, the lighting and the camera.",
        ],
        "features": [
            "Special-event and evening makeup",
            "Editorial and fashion photoshoots",
            "Runway and backstage teams",
            "Lash application and skin preparation",
        ],
    },
    "celebrities": {
        "title": "Celebrity Makeup",
        "eyebrow": "Celebrities",
        "intro": "Discreet, professional makeup for public figures, red-carpet appearances, press events and personal appearances.",
        "card": "Red-carpet, press and personal appearances, handled with discretion.",
        "body_title": "Camera-ready, every time",
        "body": [
            "High-profile appearances leave no room for error. Makeup is designed for flashes, close-ups and long days, and delivered with complete discretion and professionalism.",
        ],
        "features": [
            "Red-carpet and gala appearances",
            "Press junkets, interviews and TV appearances",
            "Photoshoots and promotional campaigns",
            "Touch-ups throughout the event",
        ],
    },
    "commercials": {
        "title": "Commercial Makeup",
        "eyebrow": "Commercials",
        "intro": "Clean, consistent makeup for advertising, brand campaigns and corporate productions that holds up under studio lights.",
        "card": "Advertising, brand campaigns and corporate shoots under studio lights.",
        "body_title": "On brief, on schedule",
        "body": [
            "Commercial sets move quickly. Makeup is planned with the director and photographer so every talent looks consistent from the first take to the last.",
        ],
        "features": [
            "TV and online advertising",
            "Brand and product campaigns",
            "Corporate headshots and video",
            "Continuity and on-set touch-ups",
        ],
    },
    "music-videos": {
        "title": "Music Video Makeup",
        "eyebrow": "Music Videos",
        "intro": "Creative, bold and story-driven makeup for artists and performers, built to match the concept and the camera.",
        "card": "Bold, creative looks for artists, dancers and performers.",
        "body_title": "Bring the concept to life",
        "body": [
            "Music videos are where makeup becomes part of the story. From natural looks to dramatic, artistic concepts, every look is developed with the artist and the creative team.",
        ],
        "features": [
            "Concept development with the creative team",
            "Artist, dancer and cast makeup",
            "Creative, colourful and special-effect looks",
            "Long shoot days with on-set touch-ups",
        ],
    },
    "movies": {
        "title": "Film Makeup",
        "eyebrow": "Movies",
        "intro": "Character, continuity and on-set makeup for film and television productions.",
        "card": "Character work and continuity for film and television sets.",
        "body_title": "Character and continuity",
        "body": [
            "Film makeup is about more than looking good. It is about telling the story, keeping continuity across long shoot schedules and working smoothly with the rest of the crew.",
        ],
        "features": [
            "Character and period looks",
            "Continuity notes and photographs",
            "HD- and camera-ready application",
            "Experience working on set with production crews",
        ],
    },
}

# ---------------------------------------------------------------- helpers
e = html.escape


def photos(slug, count=6, label="Photo coming soon"):
    folder = ROOT / "images" / slug
    files = sorted(p for p in folder.glob("*") if p.suffix.lower() in IMG_EXT) if folder.exists() else []
    if files:
        return "\n".join(
            f'<div class="photo"><img src="images/{slug}/{p.name}" alt="{e(PAGES.get(slug, {}).get("title", SITE["name"]))} by {e(SITE["name"])}" loading="lazy"></div>'
            for p in files
        )
    return "\n".join(f'<div class="photo placeholder" data-label="{e(label)}"></div>' for _ in range(count))


def cover(slug, wide=False):
    folder = ROOT / "images" / slug
    files = sorted(p for p in folder.glob("*") if p.suffix.lower() in IMG_EXT) if folder.exists() else []
    cls = "photo wide" if wide else "photo"
    if files:
        return f'<div class="{cls}"><img src="images/{slug}/{files[0].name}" alt="" loading="lazy"></div>'
    return f'<div class="{cls} placeholder" data-label="{e(PAGES[slug]["eyebrow"]) if slug in PAGES else ""}"></div>'


def contact_lines():
    items = []
    if SITE["phone"]:
        items.append(f'<li><a href="tel:{e(SITE["phone"].replace(" ", ""))}">{e(SITE["phone"])}</a></li>')
    if SITE["email"]:
        items.append(f'<li><a href="mailto:{e(SITE["email"])}">{e(SITE["email"])}</a></li>')
    if SITE["instagram"]:
        items.append(f'<li><a href="https://instagram.com/{e(SITE["instagram"])}" target="_blank" rel="noopener">Instagram @{e(SITE["instagram"])}</a></li>')
    items.append(f"<li>{e(SITE['city'])}</li>")
    return "\n".join(items)


def header(current):
    def link(href, text):
        cur = ' aria-current="page"' if href == current else ""
        return f'<a href="{href}"{cur}>{text}</a>'

    portfolio_links = "\n".join(link(f"{s}.html", e(t)) for s, t in PORTFOLIO)
    return f"""<header class="site-header">
  <div class="wrap header-inner">
    <a class="brand" href="index.html">
      <span class="brand-name">{e(SITE['name'])}</span>
      <span class="brand-tag">{e(SITE['tag'])}</span>
    </a>
    <button class="menu-toggle" aria-label="Open menu" aria-expanded="false"><span></span><span></span><span></span></button>
    <nav class="nav" aria-label="Main">
      {link('index.html', 'Home')}
      <div class="dropdown">
        <button type="button">Portfolio</button>
        <div class="dropdown-menu">
{portfolio_links}
        </div>
      </div>
      {link('about.html', 'About')}
      <a class="btn" href="contact.html">Book Now</a>
    </nav>
  </div>
</header>"""


def footer():
    portfolio_links = "\n".join(f'<li><a href="{s}.html">{e(t)}</a></li>' for s, t in PORTFOLIO)
    return f"""<footer class="site-footer">
  <div class="wrap">
    <div class="footer-grid">
      <div>
        <span class="brand-name">{e(SITE['name'])}</span>
        <p>Professional makeup artistry for brides, events, fashion, film and television. Serving {e(SITE['city'])} since 2008.</p>
      </div>
      <div>
        <h4>Portfolio</h4>
        <ul>
{portfolio_links}
        </ul>
      </div>
      <div>
        <h4>Get in touch</h4>
        <ul>
{contact_lines()}
          <li><a href="contact.html">Booking enquiry</a></li>
        </ul>
      </div>
    </div>
    <p class="copyright">© <span id="year">2026</span> {e(SITE['name'])}. All rights reserved.</p>
  </div>
</footer>
<script>
  document.getElementById('year').textContent = new Date().getFullYear();
  const t = document.querySelector('.menu-toggle'), n = document.querySelector('.nav');
  t.addEventListener('click', () => {{ const o = n.classList.toggle('open'); t.setAttribute('aria-expanded', o); }});
</script>"""


def page(filename, title, description, body, hero_style=""):
    full_title = f"{title} | {SITE['name']}" if filename != "index.html" else f"{SITE['name']} | Bridal, Film & Fashion Makeup Artist in Toronto"
    out = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(full_title)}</title>
<meta name="description" content="{e(description)}">
<meta property="og:title" content="{e(full_title)}">
<meta property="og:description" content="{e(description)}">
<meta property="og:type" content="website">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;1,400&family=Jost:wght@300;400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/style.css">
</head>
<body>
{header(filename)}
<main>
{body}
</main>
{footer()}
</body>
</html>
"""
    (ROOT / filename).write_text(out, encoding="utf-8")


CTA = """<section class="cta-band">
  <div class="wrap">
    <p class="eyebrow">Now booking</p>
    <h2>Let's create your look</h2>
    <p>Tell me about your date, your event and the look you have in mind, and I'll get back to you with availability and a personalised quote.</p>
    <a class="btn" href="contact.html">Make an enquiry</a>
  </div>
</section>"""

# ---------------------------------------------------------------- home
def build_home():
    cards = "\n".join(
        f"""<a class="card" href="{s}.html">
  {cover(s)}
  <div class="card-body"><h3>{e(t)}</h3><p>{e(PAGES[s]['card'])}</p><span class="card-link">View portfolio →</span></div>
</a>"""
        for s, t in PORTFOLIO
    )
    hero_img = ROOT / "images" / "home" / "hero.jpg"
    style = ' style="--hero-img: url(images/home/hero.jpg)"' if hero_img.exists() else ""
    body = f"""<section class="hero"{style}>
  <div class="hero-inner">
    <p class="eyebrow">Toronto Makeup Artist · Since 2008</p>
    <h1>Luxury makeup for life's most beautiful moments</h1>
    <p class="lead">Bridal, fashion, film and television makeup by certified makeup artist {e(SITE['artist'])}.</p>
    <a class="btn" href="contact.html">Book your appointment</a>
    <a class="btn btn-ghost" href="#portfolio">View portfolio</a>
  </div>
</section>

<section>
  <div class="wrap intro-grid">
    <div>
      <p class="eyebrow">Welcome</p>
      <h2>Artistry that feels like you, only more radiant</h2>
      <p>Vanity Affairs Luxe Studio has been creating beautiful, long-lasting makeup since 2008. From intimate bridal mornings to busy film sets and runway shows, every look is tailored to the person, the occasion and the camera.</p>
      <p>The goal is simple: you should look like the most confident version of yourself, and feel completely at ease in the chair.</p>
      <a class="btn btn-ghost" href="about.html">About the artist</a>
    </div>
    {cover('bridal')}
  </div>
</section>

<section class="alt" id="portfolio">
  <div class="wrap">
    <div class="section-head">
      <p class="eyebrow">Portfolio & Services</p>
      <h2>Makeup for every stage and screen</h2>
      <p>Explore my work across weddings, events, fashion, film and television.</p>
    </div>
    <div class="cards">
{cards}
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head">
      <p class="eyebrow">How it works</p>
      <h2>From enquiry to final touch</h2>
    </div>
    <div class="steps">
      <div class="step"><h3>Enquire</h3><p>Send your date, location and the type of look you would like.</p></div>
      <div class="step"><h3>Consult</h3><p>We discuss your style, skin and inspiration, and plan the look together.</p></div>
      <div class="step"><h3>Trial</h3><p>For brides and major events, a trial lets us perfect every detail in advance.</p></div>
      <div class="step"><h3>The day</h3><p>Relax while your makeup is applied, with touch-ups available if needed.</p></div>
    </div>
  </div>
</section>

{CTA}"""
    page("index.html", SITE["name"],
         "Vanity Affairs Luxe Studio: luxury bridal, party, fashion, film and television makeup in Toronto and the GTA since 2008.",
         body)


# ---------------------------------------------------------------- portfolio pages
def build_portfolio(slug, label):
    p = PAGES[slug]
    paras = "\n".join(f"<p>{e(x)}</p>" for x in p["body"])
    feats = "\n".join(f"<li>{e(x)}</li>" for x in p["features"])
    body = f"""<section class="page-hero">
  <div class="wrap">
    <p class="eyebrow">{e(p['eyebrow'])}</p>
    <h1>{e(p['title'])}</h1>
    <p>{e(p['intro'])}</p>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="gallery">
{photos(slug)}
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap two-col">
    <div>
      <h2>{e(p['body_title'])}</h2>
      {paras}
    </div>
    <div>
      <h3>What's included</h3>
      <ul class="feature-list">
{feats}
      </ul>
    </div>
  </div>
</section>

{CTA}"""
    page(f"{slug}.html", p["title"], f"{p['intro']} {SITE['name']}, {SITE['city']}.", body)


# ---------------------------------------------------------------- about
def build_about():
    body = f"""<section class="page-hero">
  <div class="wrap">
    <p class="eyebrow">About me</p>
    <h1>Meet the artist</h1>
    <p>The face and hands behind Vanity Affairs Luxe Studio.</p>
  </div>
</section>

<section>
  <div class="wrap intro-grid">
    {photos('about', count=1, label='Your portrait here')}
    <div>
      <p class="eyebrow">{e(SITE['artist'])}</p>
      <h2>Certified makeup artist for brides, film and the runway</h2>
      <p>I'm {e(SITE['artist'])}, the founder of Vanity Affairs Luxe Studio. I've been working as a professional makeup artist since 2008, creating looks for brides, special events, fashion shows, film and television.</p>
      <p>Over the years I have learned that great makeup is equal parts technique and trust. I listen carefully, plan every look around your features and the occasion, and work calmly, even on the busiest wedding morning or film set.</p>
      <p>Having worked with clients from many cultures and backgrounds, I'm comfortable with a wide range of skin tones, traditions and styles, from soft, natural looks to full glamour.</p>
      <ul class="feature-list">
        <li>Certified makeup artist: bridal, film and runway</li>
        <li>Running Vanity Affairs Luxe Studio since 2008</li>
        <li>Based in Toronto, available for travel across the GTA</li>
      </ul>
    </div>
  </div>
</section>

{CTA}"""
    page("about.html", "About the Artist",
         f"Meet {SITE['artist']}, certified bridal, film and runway makeup artist and founder of Vanity Affairs Luxe Studio in Toronto.",
         body)


# ---------------------------------------------------------------- contact
def build_contact():
    items = []
    if SITE["phone"]:
        items.append(f'<div class="contact-item"><span>Phone</span><a href="tel:{e(SITE["phone"].replace(" ", ""))}">{e(SITE["phone"])}</a></div>')
    if SITE["email"]:
        items.append(f'<div class="contact-item"><span>Email</span><a href="mailto:{e(SITE["email"])}">{e(SITE["email"])}</a></div>')
    if SITE["instagram"]:
        items.append(f'<div class="contact-item"><span>Instagram</span><a href="https://instagram.com/{e(SITE["instagram"])}" target="_blank" rel="noopener">@{e(SITE["instagram"])}</a></div>')
    items.append(f'<div class="contact-item"><span>Service area</span><strong>{e(SITE["city"])}</strong></div>')
    services = "\n".join(f"<option>{e(t)}</option>" for _, t in PORTFOLIO)
    mail_to = SITE["email"]
    form_action = f'action="mailto:{e(mail_to)}" method="post" enctype="text/plain"' if mail_to else 'action="#" onsubmit="alert(\'The booking form will be connected soon. Please contact us directly in the meantime.\'); return false;"'
    body = f"""<section class="page-hero">
  <div class="wrap">
    <p class="eyebrow">Contact</p>
    <h1>Book your appointment</h1>
    <p>Share a few details about your event and I'll reply with availability and a personalised quote.</p>
  </div>
</section>

<section>
  <div class="wrap contact-grid">
    <div>
      <h2>Get in touch</h2>
      <p class="note">Popular dates, especially wedding weekends, book up early. I recommend enquiring as soon as your date is confirmed.</p>
      {''.join(items)}
    </div>
    <form {form_action}>
      <div class="form-row">
        <label>Name<input name="name" required></label>
        <label>Email<input type="email" name="email" required></label>
      </div>
      <div class="form-row">
        <label>Phone<input type="tel" name="phone"></label>
        <label>Event date<input type="date" name="date"></label>
      </div>
      <div class="form-row">
        <label>Service
          <select name="service">
{services}
            <option>Other</option>
          </select>
        </label>
        <label>Number of people<input type="number" name="people" min="1" value="1"></label>
      </div>
      <label>Location<input name="location" placeholder="City or venue"></label>
      <label>Tell me about your look<textarea name="message" rows="5"></textarea></label>
      <div><button class="btn" type="submit">Send enquiry</button></div>
    </form>
  </div>
</section>"""
    page("contact.html", "Contact & Booking",
         f"Book bridal, event, fashion or film makeup with {SITE['name']} in {SITE['city']}.",
         body)


if __name__ == "__main__":
    build_home()
    for s, t in PORTFOLIO:
        build_portfolio(s, t)
    build_about()
    build_contact()
    print("Built", len(PORTFOLIO) + 3, "pages")
