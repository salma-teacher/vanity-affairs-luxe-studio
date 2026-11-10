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
import hashlib
from datetime import date
# Changes whenever style.css changes, so browsers always load the latest design
CSS_VERSION = hashlib.md5((ROOT / "assets" / "style.css").read_bytes() + (ROOT / "assets" / "site.js").read_bytes()).hexdigest()[:8]

# ---------------------------------------------------------------- settings
SITE = {
    "name": "Vanity Affairs Luxe Studio",
    "tag": "Serving Canada Since 2015",
    "artist": "Salma Sami Khan",
    "city": "Toronto & the GTA",
    # TODO: replace with real details
    # Email and WhatsApp are never written into the HTML as plain text:
    # they are split up and reassembled in the browser, so spam bots that
    # scan web pages can't harvest them. The phone number is not displayed.
    "email": "salmaqs@gmail.com",
    "whatsapp": "16479221139",   # digits only, with country code
    "phone": "",          # leave blank to keep the number off the page
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
            "Creative, fantasy and body-art looks",
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

# YouTube videos (id, caption) shown on the Music Videos and Movies pages
VIDEOS = {
    "music-videos": [
        ("5KL-JAe4KfM", "Jassi Sidhu & DJ K Square – Haa Kurvakeh"),
        ("s8pLOGoWd3A", "Sukh Jay – Challenge"),
        ("jx51Xw-hhew", "Astha Tamang – Jealous"),
        ("U0UZb8HMa1s", "Yashvi ft. DJ K Square – Come Here"),
        ("YidUdtDNGk0", "Astha Tamang – Ride"),
    ],
    "commercials": [
        ("IFmXWZLXHQU", "Handi Rice – Ali Kazmi"),
        ("nEVvzlXOSyo", "Tandoori Flame"),
        ("9WwiOdnqYaA", "Alokozay Tea – Hindi"),
        ("vIeYGq2Zz3I", "Alokozay Tea – Arabic"),
        ("pPQ52opbelw", "401 Dixie Mazda"),
        ("-dtbf3XrHPM", "Brar's Mango Rasmalai"),
        ("897LKUx6NNI", "Nanak Lassi"),
        ("cNagTCO7ix0", "Handi Spices"),
    ],
    "movies": [
        ("oJsH4sM5BdM", "Taken Too Far"),
        ("SiF-yi6oTCk", "On the Twelfth Day of Christmas"),
        ("2DZi444H6-E", "On Again Off Again by Arsalan Shirazi"),
        ("6Pv9e4Rd5_4", "Mrs. Jones by OJ Oboirah"),
    ],
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


def videos(slug):
    items = VIDEOS.get(slug, [])
    return "\n".join(
        f"""<figure class="video{' featured' if i == 0 and len(items) % 2 else ''}">
  <div class="video-frame"><iframe src="https://www.youtube-nocookie.com/embed/{vid}?rel=0" title="{e(cap)}" loading="lazy" allow="accelerometer; encrypted-media; gyroscope; picture-in-picture; fullscreen" allowfullscreen></iframe></div>
  <figcaption>{e(cap)}</figcaption>
</figure>"""
        for i, (vid, cap) in enumerate(items)
    )


def has_photos(slug):
    folder = ROOT / "images" / slug
    return folder.exists() and any(p.suffix.lower() in IMG_EXT for p in folder.glob("*"))


def cover(slug, wide=False):
    folder = ROOT / "images" / slug
    files = sorted(p for p in folder.glob("*") if p.suffix.lower() in IMG_EXT) if folder.exists() else []
    cls = "photo wide" if wide else "photo"
    if not files and VIDEOS.get(slug):
        vid = VIDEOS[slug][0][0]
        return f'<div class="{cls} thumb"><img src="https://i.ytimg.com/vi/{vid}/hqdefault.jpg" alt="" loading="lazy"></div>'
    if files:
        return f'<div class="{cls}"><img src="images/{slug}/{files[0].name}" alt="" loading="lazy"></div>'
    return f'<div class="{cls} placeholder" data-label="{e(PAGES[slug]["eyebrow"]) if slug in PAGES else ""}"></div>'


def _split(text):
    h = len(text) // 2
    return text[:h], text[h:]


def wa_link(label="Message on WhatsApp", cls=""):
    a, b = _split(SITE["whatsapp"])
    return f'<a class="js-wa {cls}" href="contact.html" data-a="{a}" data-b="{b}" target="_blank" rel="noopener">{label}</a>'


def email_link(cls=""):
    user, dom = SITE["email"].split("@")
    return f'<a class="js-mail {cls}" href="contact.html" data-u="{user[::-1]}" data-d="{dom[::-1]}">Email us</a>'


def contact_lines():
    items = []
    if SITE["phone"]:
        items.append(f'<li><a href="tel:{e(SITE["phone"].replace(" ", ""))}">{e(SITE["phone"])}</a></li>')
    if SITE["whatsapp"]:
        items.append(f"<li>{wa_link('WhatsApp')}</li>")
    if SITE["email"]:
        items.append(f"<li>{email_link()}</li>")
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
      <img class="brand-logo" src="assets/logo.png" alt="Vanity Affairs Luxe Studio logo" width="56" height="56">
      <span class="brand-text">
      <span class="brand-name">{e(SITE['name'])}</span>
      <span class="brand-tag">{e(SITE['tag'])}</span>
      </span>
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
        <img class="footer-logo" src="assets/logo.png" alt="" width="96" height="96">
        <span class="brand-name">{e(SITE['name'])}</span>
        <p class="script">Enhance. Empower. Radiate.</p>
        <p>Professional makeup artistry for brides, events, fashion, film and television. Serving Canada since 2015.</p>
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
{wa_link('<svg viewBox="0 0 32 32" width="28" height="28" aria-hidden="true"><path fill="currentColor" d="M16 3C9 3 3.3 8.6 3.3 15.6c0 2.4.7 4.7 1.9 6.7L3 29l6.9-2.2a12.8 12.8 0 0 0 6.1 1.5c7 0 12.7-5.6 12.7-12.6S23 3 16 3zm0 23c-2 0-3.9-.5-5.5-1.5l-.4-.2-4.1 1.3 1.3-4-.3-.4a10.3 10.3 0 0 1-1.6-5.6C5.4 9.9 10.2 5.3 16 5.3s10.6 4.6 10.6 10.3S21.8 26 16 26zm5.8-7.7c-.3-.2-1.9-.9-2.2-1s-.5-.2-.7.2-.8 1-1 1.2-.4.2-.7.1a8.7 8.7 0 0 1-4.3-3.7c-.3-.6.3-.5 1-1.7.1-.2 0-.4 0-.6l-1-2.4c-.3-.6-.5-.5-.7-.5h-.6c-.2 0-.6.1-.9.4s-1.2 1.1-1.2 2.7 1.2 3.1 1.4 3.4c.2.2 2.3 3.5 5.6 4.9 2.1.9 2.9 1 4 .8.6-.1 1.9-.8 2.2-1.5.3-.8.3-1.4.2-1.5-.1-.2-.3-.3-.6-.4z"/></svg><span>Chat on WhatsApp</span>', 'wa-float')}
<button class="to-top" aria-label="Back to top">↑</button>
<script src="assets/site.js?v={CSS_VERSION}" defer></script>
<script>
  document.getElementById('year').textContent = new Date().getFullYear();
  const msg = encodeURIComponent("Hi! I found Vanity Affairs Luxe Studio online and I'd like to ask about booking.");
  document.querySelectorAll('.js-wa').forEach(a => {{ a.href = 'https://wa.me/' + a.dataset.a + a.dataset.b + '?text=' + msg; }});
  document.querySelectorAll('.js-mail').forEach(a => {{
    const m = a.dataset.u.split('').reverse().join('') + '@' + a.dataset.d.split('').reverse().join('');
    a.href = 'mailto:' + m + '?subject=' + encodeURIComponent('Booking enquiry');
    if (a.dataset.show) a.textContent = m;
  }});
  document.querySelectorAll('form.js-form').forEach(f => {{
    f.action = 'https://formsubmit.co/' + f.dataset.u.split('').reverse().join('') + '@' + f.dataset.d.split('').reverse().join('');
  }});
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
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;1,400&family=Jost:wght@300;400&family=Great+Vibes&display=swap" rel="stylesheet">
<link rel="icon" type="image/png" href="assets/favicon.png">
<link rel="apple-touch-icon" href="assets/apple-touch-icon.png">
<meta property="og:image" content="assets/logo-full.jpg">
<meta name="theme-color" content="#1f0e20">
<link rel="stylesheet" href="assets/style.css?v={CSS_VERSION}">
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
    bg = '<div class="hero-bg" style="background-image: url(images/home/hero.jpg)"></div>' if hero_img.exists() else ""
    body = f"""<section class="hero has-bg">
  {bg}
  <div class="hero-inner">
    <p class="eyebrow">Toronto Makeup Artist · Serving Canada Since 2015</p>
    <h1>Luxury makeup for life's most beautiful moments</h1>
    <p class="script">Enhance. Empower. Radiate.</p>
    <p class="lead">Makeup for <span class="rotator" data-words="brides|red carpets|runways|film sets|music videos|celebrations">brides</span>, by certified makeup artist {e(SITE['artist'])}.</p>
    <a class="btn" href="contact.html">Book your appointment</a>
    <a class="btn btn-ghost" href="#portfolio">View portfolio</a>
  </div>
</section>

<section>
  <div class="wrap intro-grid">
    <div>
      <p class="eyebrow">Welcome</p>
      <h2>Artistry that feels like you, only more radiant</h2>
      <p>Vanity Affairs Luxe Studio has been creating beautiful, long-lasting makeup for clients across Canada since 2015. From intimate bridal mornings to busy film sets and runway shows, every look is tailored to the person, the occasion and the camera.</p>
      <p>The goal is simple: you should look like the most confident version of yourself, and feel completely at ease in the chair.</p>
      <a class="btn btn-ghost" href="about.html">About the artist</a>
    </div>
    <div class="photo"><img src="images/bridal/02.jpg" alt="Bride with soft glam makeup holding a white bouquet" loading="lazy"></div>
  </div>
</section>

<section class="stats">
  <div class="wrap stats-grid">
    <div class="stat"><span class="num" data-count="{date.today().year - 2015}">{date.today().year - 2015}</span><span class="plus">+</span><p>Years serving Canada</p></div>
    <div class="stat"><span class="num" data-count="{sum(len(v) for v in VIDEOS.values())}">{sum(len(v) for v in VIDEOS.values())}</span><p>Music videos, films &amp; commercials</p></div>
    <div class="stat"><span class="num" data-count="{len(PORTFOLIO)}">{len(PORTFOLIO)}</span><p>Specialities, from bridal to film</p></div>
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
         "Vanity Affairs Luxe Studio: luxury bridal, party, fashion, film and television makeup in Toronto, serving Canada since 2015.",
         body)


# ---------------------------------------------------------------- portfolio pages
def build_portfolio(slug, label):
    p = PAGES[slug]
    paras = "\n".join(f"<p>{e(x)}</p>" for x in p["body"])
    feats = "\n".join(f"<li>{e(x)}</li>" for x in p["features"])
    media = ""
    if VIDEOS.get(slug):
        media += f"""<section>
  <div class="wrap">
    <div class="video-grid">
{videos(slug)}
    </div>
  </div>
</section>"""
    if has_photos(slug) or not VIDEOS.get(slug):
        media += f"""
<section>
  <div class="wrap">
    <div class="gallery">
{photos(slug)}
    </div>
  </div>
</section>"""
    body = f"""<section class="page-hero">
  <div class="wrap">
    <p class="eyebrow">{e(p['eyebrow'])}</p>
    <h1>{e(p['title'])}</h1>
    <p>{e(p['intro'])}</p>
  </div>
</section>

{media}

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
        <li>Serving clients across Canada since 2015</li>
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
    if SITE["whatsapp"]:
        items.append(f'<div class="contact-item"><span>WhatsApp</span>{wa_link("Chat with me on WhatsApp →")}</div>')
    if SITE["email"]:
        items.append(f'<div class="contact-item"><span>Email</span>{email_link()}</div>')
    if SITE["instagram"]:
        items.append(f'<div class="contact-item"><span>Instagram</span><a href="https://instagram.com/{e(SITE["instagram"])}" target="_blank" rel="noopener">@{e(SITE["instagram"])}</a></div>')
    items.append(f'<div class="contact-item"><span>Service area</span><strong>{e(SITE["city"])}</strong></div>')
    services = "\n".join(f"<option>{e(t)}</option>" for _, t in PORTFOLIO)
    user, dom = SITE["email"].split("@")
    form_action = f'class="js-form" method="POST" data-u="{user[::-1]}" data-d="{dom[::-1]}"'
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
      <input type="hidden" name="_subject" value="New booking enquiry – Vanity Affairs Luxe Studio">
      <input type="hidden" name="_template" value="table">
      <input type="text" name="_honey" style="display:none" tabindex="-1" autocomplete="off">
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
