/* Vanity Affairs Luxe Studio — interactive touches */
(function () {
  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---------- Header: shrink + shadow once the page scrolls ---------- */
  const header = document.querySelector('.site-header');
  const toTop = document.querySelector('.to-top');
  const onScroll = () => {
    const y = window.scrollY;
    header && header.classList.toggle('scrolled', y > 40);
    toTop && toTop.classList.toggle('show', y > 700);
  };
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();
  toTop && toTop.addEventListener('click', () => window.scrollTo({ top: 0, behavior: reduceMotion ? 'auto' : 'smooth' }));

  /* ---------- Reveal on scroll ---------- */
  const revealTargets = document.querySelectorAll(
    '.section-head, .intro-grid > *, .card, .gallery .photo, .video, .step, .two-col > *, .contact-grid > *, .stat, .cta-band .wrap > *'
  );
  if (!reduceMotion && 'IntersectionObserver' in window) {
    revealTargets.forEach((el) => {
      el.classList.add('reveal');
      // stagger items that sit side by side in a grid
      const parent = el.parentElement;
      if (parent) {
        const idx = Array.prototype.indexOf.call(parent.children, el);
        el.style.transitionDelay = (Math.min(idx % 3, 2) * 0.12) + 's';
      }
    });
    const io = new IntersectionObserver((entries) => {
      entries.forEach((en) => {
        if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
    revealTargets.forEach((el) => io.observe(el));
  }

  /* ---------- Count-up numbers ---------- */
  const counters = document.querySelectorAll('[data-count]');
  const runCount = (el) => {
    const end = parseInt(el.dataset.count, 10);
    if (reduceMotion) { el.textContent = end; return; }
    const start = performance.now(), dur = 1600;
    const tick = (t) => {
      const p = Math.min((t - start) / dur, 1);
      el.textContent = Math.round(end * (1 - Math.pow(1 - p, 3)));
      if (p < 1) requestAnimationFrame(tick);
    };
    requestAnimationFrame(tick);
  };
  if ('IntersectionObserver' in window) {
    const co = new IntersectionObserver((entries) => {
      entries.forEach((en) => { if (en.isIntersecting) { runCount(en.target); co.unobserve(en.target); } });
    }, { threshold: 0.6 });
    counters.forEach((c) => co.observe(c));
  } else {
    counters.forEach((c) => (c.textContent = c.dataset.count));
  }

  /* ---------- Rotating word in the hero ---------- */
  const rot = document.querySelector('.rotator');
  if (rot && !reduceMotion) {
    const words = rot.dataset.words.split('|');
    let i = 0;
    setInterval(() => {
      rot.classList.add('out');
      setTimeout(() => {
        i = (i + 1) % words.length;
        rot.textContent = words[i];
        rot.classList.remove('out');
      }, 450);
    }, 2600);
  }

  /* ---------- Lightbox for photo galleries ---------- */
  const imgs = Array.from(document.querySelectorAll('.gallery .photo img'));
  if (imgs.length) {
    const box = document.createElement('div');
    box.className = 'lightbox';
    box.setAttribute('role', 'dialog');
    box.setAttribute('aria-modal', 'true');
    box.setAttribute('aria-label', 'Photo viewer');
    box.innerHTML =
      '<button class="lb-close" aria-label="Close">×</button>' +
      '<button class="lb-prev" aria-label="Previous photo">‹</button>' +
      '<figure><img alt=""><figcaption></figcaption></figure>' +
      '<button class="lb-next" aria-label="Next photo">›</button>';
    document.body.appendChild(box);
    const big = box.querySelector('img'), cap = box.querySelector('figcaption');
    let cur = 0, lastFocus = null;

    const show = (n) => {
      cur = (n + imgs.length) % imgs.length;
      big.classList.remove('loaded');
      big.src = imgs[cur].src;
      big.alt = imgs[cur].alt;
      cap.textContent = (cur + 1) + ' / ' + imgs.length;
    };
    big.addEventListener('load', () => big.classList.add('loaded'));
    const open = (n) => {
      lastFocus = document.activeElement;
      show(n);
      box.classList.add('open');
      document.body.style.overflow = 'hidden';
      box.querySelector('.lb-close').focus();
    };
    const close = () => {
      box.classList.remove('open');
      document.body.style.overflow = '';
      lastFocus && lastFocus.focus();
    };

    imgs.forEach((im, n) => {
      const tile = im.closest('.photo');
      tile.classList.add('zoomable');
      tile.tabIndex = 0;
      tile.setAttribute('role', 'button');
      tile.setAttribute('aria-label', 'Enlarge photo ' + (n + 1));
      tile.addEventListener('click', () => open(n));
      tile.addEventListener('keydown', (ev) => { if (ev.key === 'Enter' || ev.key === ' ') { ev.preventDefault(); open(n); } });
    });
    box.querySelector('.lb-close').addEventListener('click', close);
    box.querySelector('.lb-prev').addEventListener('click', (ev) => { ev.stopPropagation(); show(cur - 1); });
    box.querySelector('.lb-next').addEventListener('click', (ev) => { ev.stopPropagation(); show(cur + 1); });
    box.addEventListener('click', (ev) => { if (ev.target === box) close(); });
    document.addEventListener('keydown', (ev) => {
      if (!box.classList.contains('open')) return;
      if (ev.key === 'Escape') close();
      if (ev.key === 'ArrowLeft') show(cur - 1);
      if (ev.key === 'ArrowRight') show(cur + 1);
    });
    // swipe on phones
    let sx = null;
    box.addEventListener('touchstart', (ev) => { sx = ev.touches[0].clientX; }, { passive: true });
    box.addEventListener('touchend', (ev) => {
      if (sx === null) return;
      const dx = ev.changedTouches[0].clientX - sx;
      if (Math.abs(dx) > 50) show(cur + (dx < 0 ? 1 : -1));
      sx = null;
    });
  }

  /* ---------- Gentle tilt on portfolio cards (desktop only) ---------- */
  if (!reduceMotion && window.matchMedia('(hover: hover) and (pointer: fine)').matches) {
    document.querySelectorAll('.card').forEach((card) => {
      card.addEventListener('mousemove', (ev) => {
        const r = card.getBoundingClientRect();
        const x = (ev.clientX - r.left) / r.width - 0.5;
        const y = (ev.clientY - r.top) / r.height - 0.5;
        card.style.transform = 'translateY(-6px) rotateX(' + (-y * 4) + 'deg) rotateY(' + (x * 4) + 'deg)';
      });
      card.addEventListener('mouseleave', () => { card.style.transform = ''; });
    });
  }
})();
