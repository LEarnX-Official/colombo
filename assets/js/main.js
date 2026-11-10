/* Dr. Giuseppe Colombo — "L'Atlante della Misura"
   Shared behaviour + the measuring instruments. GSAP + ScrollTrigger + Lenis.
   Every effect has a reduced-motion fallback (final, measured state). */
(function () {
  'use strict';
  var html = document.documentElement;
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (typeof window.gsap === 'undefined') { html.classList.remove('js'); return; }
  window.__siteReady = true;
  if (reduce) html.classList.add('no-motion');

  var gsap = window.gsap, ST = window.ScrollTrigger;
  gsap.registerPlugin(ST);
  var T = window.I18N || {};
  function tr(k, f) { return T[k] || f; }
  var q = function (s, c) { return (c || document).querySelector(s); };
  var qa = function (s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); };
  var MEASURE = 'power2.inOut', SETTLE = 'expo.out';
  var Site = (window.Site = window.Site || {});
  Site.reduce = reduce; Site.q = q; Site.qa = qa;
  Site.isDesk = function () { return window.matchMedia('(min-width: 901px)').matches; };

  /* ------------------------------------------------ smooth scroll */
  var lenis = null;
  if (!reduce && typeof window.Lenis !== 'undefined') {
    lenis = new window.Lenis({ duration: 1.1, easing: function (t) { return Math.min(1, 1.001 - Math.pow(2, -10 * t)); } });
    lenis.on('scroll', ST.update);
    gsap.ticker.add(function (t) { lenis.raf(t * 1000); });
    gsap.ticker.lagSmoothing(0);
  }
  Site.lenis = lenis;
  Site.scrollTo = function (target) {
    if (lenis) lenis.scrollTo(target, { offset: -70, duration: 1.4 });
    else if (target && target.scrollIntoView) target.scrollIntoView({ behavior: reduce ? 'auto' : 'smooth' });
  };

  /* ------------------------------------------------ text reveals */
  function splitLines(el) {
    if (el.__split) return el.__split;
    el.innerHTML = el.innerHTML.split(/<br\s*\/?>/i).map(function (h) { return '<span class="line-mask"><span>' + h.trim() + '</span></span>'; }).join('');
    return (el.__split = qa('.line-mask > span', el));
  }
  Site.splitLines = splitLines;
  function initReveals() {
    if (reduce) return;
    qa('[data-lines]').forEach(function (el) {
      var lines = splitLines(el);
      gsap.set(el, { opacity: 1 });
      gsap.set(lines, { yPercent: 112 });
      ST.create({ trigger: el, start: 'top 88%', once: true, onEnter: function () { gsap.to(lines, { yPercent: 0, duration: 1.2, ease: SETTLE, stagger: .08 }); } });
    });
    var items = qa('[data-reveal]');
    gsap.set(items, { y: 24 });
    ST.batch(items, { start: 'top 92%', once: true, onEnter: function (b) { gsap.to(b, { opacity: 1, y: 0, duration: 1.1, ease: SETTLE, stagger: .07 }); } });
  }

  /* ------------------------------------------------ counters */
  function countTo(el, to, opts) {
    opts = opts || {};
    var dec = opts.decimals || 0, o = { v: opts.from || 0 };
    return gsap.to(o, { v: to, duration: opts.duration || 1.5, ease: 'power2.out', delay: opts.delay || 0, paused: opts.paused,
      onUpdate: function () { el.textContent = dec ? o.v.toFixed(dec) : Math.round(o.v); } });
  }
  Site.countTo = countTo;
  function initCounters() {
    if (reduce) return;
    qa('[data-count]').forEach(function (el) {
      if (el.closest('[data-book3d]') || el.closest('.p5')) return; // driven by their own scenes
      var to = parseFloat(el.getAttribute('data-count'));
      el.textContent = '0';
      ST.create({ trigger: el, start: 'top 92%', once: true, onEnter: function () { countTo(el, to); } });
    });
    qa('[data-coord]').forEach(function (el) {
      if (el.closest('.p8')) return;
      var to = parseFloat(el.getAttribute('data-coord'));
      el.textContent = '0.0000';
      ST.create({ trigger: el, start: 'top 92%', once: true, onEnter: function () { countTo(el, to, { decimals: 4, duration: 1.8 }); } });
    });
  }

  /* ------------------------------------------------ D2 · facial thirds (sticky portrait + three blocks) */
  function initThirds() {
    qa('[data-thirds-scope]').forEach(function (scope) {
      var plate = q('.pplate', scope), blocks = qa('.third', scope);
      if (!plate || !blocks.length) return;
      function set(key) {
        plate.setAttribute('data-active', key);
        blocks.forEach(function (b) { b.classList.toggle('is-active', b.getAttribute('data-third') === key); });
      }
      set(blocks[0].getAttribute('data-third'));
      blocks.forEach(function (b) {
        ST.create({ trigger: b, start: 'top 62%', end: 'bottom 62%', onToggle: function (self) { if (self.isActive) set(b.getAttribute('data-third')); } });
      });
    });
    if (reduce) return;
    qa('.pplate[data-draw-thirds]').forEach(function (plate) {
      var lines = qa('.thirds__line', plate), labs = qa('.thirds__lab', plate), br = q('.thirds__bracket', plate);
      gsap.set(lines, { scaleX: 0 }); gsap.set(labs, { opacity: 0, x: 10 }); gsap.set(br, { scaleY: 0, transformOrigin: 'top' });
      ST.create({ trigger: plate, start: 'top 75%', once: true, onEnter: function () {
        gsap.timeline()
          .to(lines, { scaleX: 1, duration: 1, ease: MEASURE, stagger: .12 })
          .to(br, { scaleY: 1, duration: .8, ease: MEASURE }, .3)
          .to(labs, { opacity: 1, x: 0, duration: .7, ease: SETTLE, stagger: .1 }, .6);
      } });
    });
  }

  /* ------------------------------------------------ D4 · suture: stitches along the cut */
  function buildSuture(svg) {
    if (svg.__stitches) return svg.__stitches;
    var cut = q('.suture__cut', svg), g = q('.suture__stitches', svg), L = cut.getTotalLength(), n = 22, out = [];
    for (var i = 1; i < n; i++) {
      var d = L * i / n, p = cut.getPointAtLength(d), p2 = cut.getPointAtLength(Math.min(L, d + 1));
      var a = Math.atan2(p2.y - p.y, p2.x - p.x) + Math.PI / 2 + .45, len = 16;
      var dx = Math.cos(a) * len, dy = Math.sin(a) * len;
      var path = document.createElementNS('http://www.w3.org/2000/svg', 'path');
      path.setAttribute('d', 'M' + (p.x - dx).toFixed(1) + ' ' + (p.y - dy).toFixed(1) + ' L' + (p.x + dx).toFixed(1) + ' ' + (p.y + dy).toFixed(1));
      g.appendChild(path); out.push(path);
    }
    return (svg.__stitches = out);
  }
  Site.buildSuture = buildSuture;
  function initSutures() {
    qa('[data-suture]').forEach(function (svg) {
      var st = buildSuture(svg);
      if (reduce || svg.closest('.p4')) return; // home plate IV is scrubbed by home.js
      gsap.set(svg, { clipPath: 'inset(0 100% 0 0)' });
      gsap.set(st, { opacity: 0, scale: .2, transformOrigin: 'center' });
      ST.create({ trigger: svg, start: 'top 85%', once: true, onEnter: function () {
        gsap.timeline().to(svg, { clipPath: 'inset(0 0% 0 0)', duration: 1.6, ease: MEASURE })
          .to(st, { opacity: 1, scale: 1, duration: .35, stagger: .06, ease: 'back.out(2)' }, .3);
      } });
    });
  }

  /* ------------------------------------------------ D5 · tape measure (inner pages) */
  function initTapes() {
    if (reduce) return;
    qa('[data-tape]').forEach(function (track) {
      if (track.closest('.p3')) return; // home plate III
      gsap.fromTo(track, { x: 0 }, { x: -360, ease: 'none', scrollTrigger: { trigger: track, start: 'top bottom', end: 'bottom top', scrub: 1 } });
    });
  }

  /* ------------------------------------------------ 3D book (academy, inner) */
  function openBookTimeline(book) {
    var body = q('.book3d__body', book), cover = q('.book3d__cover', book), num = q('[data-count]', book);
    var tl = gsap.timeline({ paused: true });
    tl.fromTo(body, { rotateY: -34, rotateX: 8 }, { rotateY: -8, rotateX: 2, duration: 1.2, ease: MEASURE }, 0)
      .to(cover, { rotateY: -158, duration: 1.4, ease: MEASURE }, .5);
    if (num) { var to = parseFloat(num.getAttribute('data-count')); num.textContent = '0'; tl.add(countTo(num, to, { duration: 1.2 }), 1.2); }
    return tl;
  }
  Site.openBookTimeline = openBookTimeline;
  function initBooks() {
    qa('[data-book3d]').forEach(function (book) {
      if (book.closest('.p5')) return;
      if (reduce) return;
      var tl = openBookTimeline(book);
      ST.create({ trigger: book, start: 'top 70%', once: true, onEnter: function () { tl.play(); } });
    });
  }

  /* ------------------------------------------------ film strip + map (academy) */
  function stripController(scope) {
    var track = q('[data-strip]', scope), items = qa('.strip__item', scope), cities = qa('.map__city', scope), arcs = qa('.map__arc', scope);
    arcs.forEach(function (a) { var l = a.getTotalLength(); a.style.strokeDasharray = l; a.style.strokeDashoffset = l; a.__len = l; });
    var route = ['madrid', 'nice', 'savona', 'nice', 'cremona', 'lugano'];
    function update() {
      var mid = window.innerWidth / 2, current = null, best = 1e9;
      items.forEach(function (it) {
        var r = it.getBoundingClientRect(), c = r.left + r.width / 2, d = Math.abs(c - mid);
        if (d < best) { best = d; current = it; }
      });
      if (!current) return;
      var city = current.getAttribute('data-city');
      cities.forEach(function (c) { c.classList.toggle('is-on', c.getAttribute('data-city') === city); });
      var idx = items.indexOf(current), stage = 0;
      for (var i = 0; i <= idx; i++) { var cc = items[i].getAttribute('data-city'); var ri = route.indexOf(cc, stage); if (ri > stage) stage = ri; }
      arcs.forEach(function (a, n) { gsap.to(a, { strokeDashoffset: n < stage ? 0 : a.__len, duration: .8, ease: MEASURE, overwrite: true }); });
    }
    return { track: track, update: update };
  }
  Site.stripController = stripController;
  function initStrips() {
    qa('[data-strip-pin]').forEach(function (sec) {
      var ctl = stripController(sec);
      if (reduce || !Site.isDesk()) { sec.querySelector('.strip').style.overflowX = 'auto'; sec.querySelector('.strip').addEventListener('scroll', ctl.update, { passive: true }); ctl.update(); return; }
      var dist = function () { return Math.max(0, ctl.track.scrollWidth - window.innerWidth); };
      gsap.to(ctl.track, { x: function () { return -dist(); }, ease: 'none',
        scrollTrigger: { trigger: sec.querySelector('[data-strip-pinbox]') || sec, start: 'top top', end: function () { return '+=' + dist(); }, pin: true, scrub: 1, invalidateOnRefresh: true, onUpdate: ctl.update } });
      ctl.update();
    });
  }

  /* ------------------------------------------------ ruler timeline (philosophy) */
  function initRulerTimeline() {
    var track = q('[data-hscroll]');
    if (!track || reduce) return;
    gsap.matchMedia().add('(min-width: 901px)', function () {
      var list = q('ol', track), sec = track.closest('section');
      var dist = function () { return Math.max(0, list.scrollWidth - window.innerWidth); };
      gsap.to(list, { x: function () { return -dist(); }, ease: 'none', scrollTrigger: { trigger: sec, start: 'top top', end: function () { return '+=' + dist(); }, pin: true, scrub: 1, invalidateOnRefresh: true } });
    });
  }

  /* ------------------------------------------------ marking lines (D3) */
  function initMarks() {
    qa('.mark path').forEach(function (p) {
      if (p.closest('.fin')) return; // home finale handled in home.js
      if (reduce) return;
      var l = p.getTotalLength(); p.style.strokeDasharray = l; p.style.strokeDashoffset = l;
      ST.create({ trigger: p.closest('svg'), start: 'top 85%', once: true, onEnter: function () { gsap.to(p, { strokeDashoffset: 0, duration: 1.2, ease: MEASURE, delay: .4 }); } });
    });
  }

  /* ------------------------------------------------ header + dark sections */
  function initHeader() {
    var hdr = q('[data-hdr]');
    if (!hdr) return;
    var last = 0;
    function on(y) {
      hdr.classList.toggle('is-scrolled', y > 40);
      if (!html.classList.contains('menu-open')) hdr.classList.toggle('is-hidden', y > last && y > 420);
      last = y;
    }
    if (lenis) lenis.on('scroll', function (e) { on(e.scroll); }); else window.addEventListener('scroll', function () { on(window.scrollY); }, { passive: true });
    qa('[data-theme="dark"], .hero, .phead--dark, .ftr, .cta, .pull, .fellow, .atlas-sec, .still, .nf').forEach(function (sec) {
      ST.create({ trigger: sec, start: 'top 36px', end: 'bottom 36px', toggleClass: { targets: hdr, className: 'on-dark' } });
    });
  }

  /* ------------------------------------------------ menu */
  function initMenu() {
    var btn = q('[data-menu-toggle]'), menu = q('[data-menu]');
    if (!btn || !menu) return;
    var label = q('.hdr__menu-t', btn);
    function set(open) {
      menu.classList.toggle('is-open', open); menu.setAttribute('aria-hidden', String(!open)); btn.setAttribute('aria-expanded', String(open));
      label.textContent = open ? tr('close', 'Close') : tr('menu', 'Menu');
      html.classList.toggle('menu-open', open);
      if (lenis) { if (open) lenis.stop(); else lenis.start(); }
      if (open && !reduce) gsap.fromTo(qa('.menu__link', menu), { yPercent: 60, opacity: 0 }, { yPercent: 0, opacity: 1, duration: 1, ease: SETTLE, stagger: .06, delay: .3 });
    }
    btn.addEventListener('click', function () { set(!menu.classList.contains('is-open')); });
    menu.addEventListener('click', function (e) { if (e.target.closest('a') || e.target.closest('[data-book]')) set(false); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && menu.classList.contains('is-open')) set(false); });
  }

  /* ------------------------------------------------ booking panel */
  function initBooking() {
    var bk = q('[data-booking]');
    if (!bk) return;
    var form = q('[data-bk-form]', bk), steps = qa('.bk__step', bk), next = q('[data-bk-next]', bk), back = q('[data-bk-back]', bk);
    var bar = q('[data-bk-progress]', bk), err = q('[data-bk-error]', bk), step = 1, last = 4, lastFocus = null;
    function show(n) {
      step = n;
      steps.forEach(function (s) { s.classList.toggle('is-active', +s.dataset.step === n); });
      bar.style.width = Math.min(100, n / last * 100) + '%';
      back.style.visibility = n > 1 && n <= last ? 'visible' : 'hidden';
      next.style.display = n > last ? 'none' : '';
      next.textContent = n === last ? tr('send', 'Send request') : tr('continue', 'Continue');
      err.textContent = '';
      var f = q('.bk__step.is-active input:not([type=radio]), .bk__step.is-active textarea', bk);
      if (f) setTimeout(function () { f.focus({ preventScroll: true }); }, 350);
    }
    function open(loc) {
      lastFocus = document.activeElement; form.reset(); show(1);
      var sel = q('select[name="language"] option[selected]', form); if (sel) sel.selected = true;
      if (loc) { var r = q('input[name="location"][value="' + loc + '"]', form); if (r) r.checked = true; }
      bk.classList.add('is-open'); bk.setAttribute('aria-hidden', 'false'); html.classList.add('bk-open'); if (lenis) lenis.stop();
    }
    function close() {
      bk.classList.remove('is-open'); bk.setAttribute('aria-hidden', 'true'); html.classList.remove('bk-open'); if (lenis) lenis.start();
      if (lastFocus) lastFocus.focus({ preventScroll: true });
    }
    function valid() {
      if (step === 1 && !form.interest.value) return tr('e1', 'Please choose one option.');
      if (step === 2 && !form.location.value) return tr('e2', 'Please choose a location.');
      if (step === 3) {
        if (!form.name.value.trim()) return tr('e3', 'Please enter your name.');
        if (!/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(form.email.value.trim())) return tr('e4', 'Please enter a valid email address.');
      }
      if (step === 4 && !form.privacy.checked) return tr('e5', 'Please confirm the privacy consent.');
      return '';
    }
    function submit() {
      if (form.website.value) return;
      var loc = q('input[name="location"]:checked', form), locLabel = loc ? loc.getAttribute('data-label') : '';
      var body = [
        tr('interest', 'Interest') + ': ' + form.interest.value, tr('location', 'Location') + ': ' + locLabel,
        tr('name', 'Name') + ': ' + form.name.value.trim(), tr('email', 'Email') + ': ' + form.email.value.trim(),
        tr('phone', 'Phone') + ': ' + (form.phone.value.trim() || '—'), tr('language', 'Preferred language') + ': ' + form.language.value,
        '', form.message.value.trim()
      ].join('\n');
      var subject = tr('subject', 'Consultation request') + ' — ' + form.interest.value + ' (' + locLabel + ')';
      window.location.href = 'mailto:info@drgiuseppecolombo.com?subject=' + encodeURIComponent(subject) + '&body=' + encodeURIComponent(body);
      show(5);
    }
    next.addEventListener('click', function () { var m = valid(); if (m) { err.textContent = m; return; } if (step === last) submit(); else show(step + 1); });
    back.addEventListener('click', function () { if (step > 1) show(step - 1); });
    form.addEventListener('change', function (e) { if (e.target.type === 'radio') setTimeout(function () { if (!valid()) show(step + 1); }, 280); });
    form.addEventListener('submit', function (e) { e.preventDefault(); next.click(); });
    document.addEventListener('click', function (e) {
      var t = e.target.closest('[data-book]');
      if (t) { e.preventDefault(); open(t.getAttribute('data-book-location')); }
      if (e.target.closest('[data-book-close]')) close();
    });
    document.addEventListener('keydown', function (e) {
      if (!bk.classList.contains('is-open')) return;
      if (e.key === 'Escape') close();
      if (e.key === 'Tab') {
        var f = qa('button, input:not(.hp), select, textarea, a[href]', bk).filter(function (x) { return x.offsetParent !== null && x.style.visibility !== 'hidden'; });
        if (!f.length) return;
        if (e.shiftKey && document.activeElement === f[0]) { e.preventDefault(); f[f.length - 1].focus(); }
        else if (!e.shiftKey && document.activeElement === f[f.length - 1]) { e.preventDefault(); f[0].focus(); }
      }
    });
  }

  /* ------------------------------------------------ page transitions (bordeaux curtain) */
  function initTransitions() {
    var pt = q('.pt');
    if (reduce) gsap.set(pt, { yPercent: -100 });
    else gsap.to(pt, { yPercent: -100, duration: .85, ease: 'expo.inOut', delay: .05 });
    window.addEventListener('pageshow', function (e) { if (e.persisted) gsap.set(pt, { yPercent: -100 }); });
    document.addEventListener('click', function (e) {
      var a = e.target.closest('a[href]');
      if (!a || e.defaultPrevented || e.metaKey || e.ctrlKey || e.shiftKey || a.target === '_blank') return;
      var href = a.getAttribute('href');
      if (!href || href.charAt(0) === '#' || /^(mailto|tel):/.test(href)) return;
      var url = new URL(href, location.href);
      if (url.origin !== location.origin) return;
      if (url.pathname === location.pathname && url.hash) { var t = q(url.hash); if (t) { e.preventDefault(); Site.scrollTo(t); } return; }
      e.preventDefault();
      if (reduce) { location.href = url.href; return; }
      gsap.fromTo(pt, { yPercent: 100 }, { yPercent: 0, duration: .6, ease: 'expo.inOut', onComplete: function () { location.href = url.href; } });
    });
    qa('a[href^="#"]').forEach(function (a) {
      a.addEventListener('click', function (e) { var t = q(a.getAttribute('href')); if (t) { e.preventDefault(); Site.scrollTo(t); } });
    });
  }

  /* ------------------------------------------------ small things */
  function initClock() {
    var t = q('[data-clock]'); if (!t) return;
    var f = new Intl.DateTimeFormat('en-GB', { hour: '2-digit', minute: '2-digit', timeZone: 'Europe/Zurich' });
    var tick = function () { t.textContent = f.format(new Date()); }; tick(); setInterval(tick, 20000);
  }
  function initVideos() {
    document.addEventListener('click', function (e) {
      var v = e.target.closest('[data-yt]'); if (!v) return;
      var w = document.createElement('div'); w.className = 'vid';
      w.innerHTML = '<iframe src="https://www.youtube-nocookie.com/embed/' + v.getAttribute('data-yt') + '?autoplay=1&rel=0" title="' + v.getAttribute('aria-label') + '" allow="autoplay; encrypted-media; picture-in-picture" allowfullscreen></iframe>';
      v.replaceWith(w);
    });
  }
  function initMap() {
    var box = q('[data-map]'); if (!box) return;
    q('[data-map-load]', box).addEventListener('click', function () {
      box.insertAdjacentHTML('beforeend', '<iframe title="' + tr('map', 'Map') + '" loading="lazy" src="https://maps.google.com/maps?q=' + encodeURIComponent(box.getAttribute('data-map')) + '&t=m&z=14&hl=' + html.lang + '&output=embed"></iframe>');
    });
  }
  function initFilters() {
    qa('[data-filter]').forEach(function (b) {
      b.addEventListener('click', function () {
        var f = b.getAttribute('data-filter');
        qa('[data-filter]').forEach(function (x) { x.classList.toggle('is-active', x === b); });
        qa('.pub').forEach(function (p) { p.classList.toggle('is-hidden', f !== 'all' && p.getAttribute('data-topic') !== f); });
        ST.refresh();
      });
    });
    qa('[data-jfilter]').forEach(function (b) {
      b.addEventListener('click', function () {
        var f = b.getAttribute('data-jfilter');
        qa('[data-jfilter]').forEach(function (x) { x.classList.toggle('is-active', x === b); });
        qa('[data-cat]').forEach(function (p) { var h = f !== 'all' && p.getAttribute('data-cat') !== f; p.classList.toggle('is-hidden', h); if (!h) gsap.set(p, { opacity: 1, y: 0 }); });
        ST.refresh();
      });
    });
  }
  function initReadbar() {
    var bar = q('[data-readbar]'), art = q('.art__body'); if (!bar || !art) return;
    gsap.to(bar, { scaleX: 1, ease: 'none', scrollTrigger: { trigger: art, start: 'top 30%', end: 'bottom bottom', scrub: true } });
  }
  function initSlit() {
    qa('[data-slit]').forEach(function (fig) {
      if (reduce) return;
      var img = q('img', fig);
      gsap.set(fig, { clipPath: 'inset(0 50% 0 50%)' }); gsap.set(img, { scale: 1.14 });
      ST.create({ trigger: fig, start: 'top 85%', once: true, onEnter: function () {
        gsap.to(fig, { clipPath: 'inset(0 0% 0 0%)', duration: 1.4, ease: MEASURE, delay: .3 });
        gsap.to(img, { scale: 1, duration: 1.8, ease: SETTLE, delay: .3 });
      } });
    });
  }

  /* ------------------------------------------------ boot */
  function boot() {
    initReveals(); initCounters(); initThirds(); initSutures(); initTapes(); initBooks(); initStrips(); initRulerTimeline();
    initMarks(); initHeader(); initMenu(); initBooking(); initClock(); initVideos(); initMap(); initFilters(); initReadbar(); initSlit();
    if (Site.initHome) Site.initHome();
    initTransitions();
    window.addEventListener('load', function () { ST.refresh(); });
    if (document.fonts && document.fonts.ready) document.fonts.ready.then(function () { ST.refresh(); });
  }
  if (document.readyState !== 'complete') document.addEventListener('DOMContentLoaded', boot); else boot();
})();
