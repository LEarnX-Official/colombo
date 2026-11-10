/* Dr. Giuseppe Colombo — site behaviour
   GSAP + ScrollTrigger + Lenis. Every effect has a reduced-motion fallback. */
(function () {
  'use strict';
  var html = document.documentElement;
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var hasGsap = typeof window.gsap !== 'undefined';
  if (!hasGsap) { html.classList.remove('js'); return; }
  window.__siteReady = true;
  if (reduce) html.classList.add('no-motion');

  var gsap = window.gsap, ST = window.ScrollTrigger;
  gsap.registerPlugin(ST);
  var EASE = 'expo.out';
  var Site = (window.Site = { reduce: reduce });
  var T = window.I18N || {};
  function tr(k, fallback) { return T[k] || fallback; }

  /* ---------------------------------------------------- smooth scroll */
  var lenis = null;
  if (!reduce && typeof window.Lenis !== 'undefined') {
    lenis = new window.Lenis({ duration: 1.15, easing: function (t) { return Math.min(1, 1.001 - Math.pow(2, -10 * t)); } });
    lenis.on('scroll', ST.update);
    gsap.ticker.add(function (t) { lenis.raf(t * 1000); });
    gsap.ticker.lagSmoothing(0);
  }
  Site.lenis = lenis;
  Site.scrollTo = function (target) {
    if (lenis) lenis.scrollTo(target, { offset: -80 }); else {
      var el = typeof target === 'string' ? document.querySelector(target) : target;
      if (el) el.scrollIntoView({ behavior: reduce ? 'auto' : 'smooth' });
    }
  };

  /* ---------------------------------------------------- line drawings */
  function prepLines(svg) {
    if (svg.__paths) return svg.__paths;
    var paths = Array.prototype.slice.call(svg.querySelectorAll('path')).filter(function (p) { return p.getAttribute('fill') !== 'currentColor'; });
    paths.forEach(function (p) {
      var len = 0;
      try { len = p.getTotalLength(); } catch (e) { len = 1000; }
      p.__len = len;
      p.style.strokeDasharray = len + ' ' + len;
      p.style.strokeDashoffset = len;
    });
    svg.__paths = paths;
    svg.classList.add('is-ready');
    return paths;
  }
  function showLines(svg) { svg.classList.add('is-ready'); svg.querySelectorAll('path').forEach(function (p) { p.style.strokeDashoffset = 0; }); }
  function drawTween(svg, opts) {
    opts = opts || {};
    var paths = prepLines(svg);
    return gsap.to(paths, {
      strokeDashoffset: 0, duration: opts.duration || 1.8, ease: opts.ease || 'power2.inOut',
      stagger: { amount: opts.amount != null ? opts.amount : 1.1 }, delay: opts.delay || 0, paused: opts.paused
    });
  }
  Site.prepLines = prepLines; Site.drawTween = drawTween; Site.showLines = showLines;

  function initLines() {
    document.querySelectorAll('svg.ln[data-draw]').forEach(function (svg) {
      var mode = svg.getAttribute('data-draw');
      if (mode === 'none') return;
      if (reduce) { showLines(svg); return; }
      if (mode === 'load') { prepLines(svg); svg.__pending = true; }
      else if (mode === 'enter') {
        prepLines(svg);
        ST.create({ trigger: svg, start: 'top 88%', once: true, onEnter: function () { drawTween(svg, { duration: 1.6, amount: .9 }); } });
      } else if (mode === 'hover') {
        var host = svg.closest('a, button') || svg;
        host.addEventListener('mouseenter', function () {
          var paths = prepLines(svg);
          gsap.killTweensOf(paths);
          gsap.set(paths, { strokeDashoffset: function (i, p) { return p.__len; } });
          drawTween(svg, { duration: 1.1, amount: .4 });
        });
      }
      /* mode 'scene' is driven by home.js */
    });
  }
  function drawLoadLines() {
    document.querySelectorAll('svg.ln[data-draw="load"]').forEach(function (svg) {
      if (svg.__pending) { svg.__pending = false; drawTween(svg, { duration: 2.2, amount: 1.2, delay: .15 }); }
    });
  }

  /* ---------------------------------------------------- text reveals */
  function splitLines(el) {
    if (el.__split) return el.__split;
    var parts = el.innerHTML.split(/<br\s*\/?>/i);
    el.innerHTML = parts.map(function (h) { return '<span class="line-mask"><span>' + h.trim() + '</span></span>'; }).join('');
    el.__split = el.querySelectorAll('.line-mask > span');
    return el.__split;
  }
  Site.splitLines = splitLines;

  function initReveals() {
    if (reduce) return;
    document.querySelectorAll('[data-lines]').forEach(function (el) {
      if (el.closest('[data-manual]')) return;
      var lines = splitLines(el);
      gsap.set(el, { opacity: 1 });
      gsap.set(lines, { yPercent: 110 });
      ST.create({ trigger: el, start: 'top 88%', once: true, onEnter: function () {
        gsap.to(lines, { yPercent: 0, duration: 1.3, ease: EASE, stagger: .09 });
      } });
    });
    var items = gsap.utils.toArray('[data-reveal]').filter(function (el) { return !el.closest('[data-manual]'); });
    gsap.set(items, { y: 22 });
    ST.batch(items, {
      start: 'top 90%', once: true,
      onEnter: function (batch) { gsap.to(batch, { opacity: 1, y: 0, duration: 1.2, ease: EASE, stagger: .08 }); }
    });
  }

  /* ---------------------------------------------------- header */
  function initHeader() {
    var hdr = document.querySelector('[data-hdr]');
    if (!hdr) return;
    var lastY = 0;
    function onScroll(y) {
      hdr.classList.toggle('is-scrolled', y > 60);
      if (!html.classList.contains('menu-open')) hdr.classList.toggle('is-hidden', y > lastY && y > 400);
      lastY = y;
    }
    if (lenis) lenis.on('scroll', function (e) { onScroll(e.scroll); });
    else window.addEventListener('scroll', function () { onScroll(window.scrollY); }, { passive: true });
    document.querySelectorAll('[data-theme="dark"]').forEach(function (sec) {
      ST.create({ trigger: sec, start: 'top 40px', end: 'bottom 40px', toggleClass: { targets: hdr, className: 'on-dark' } });
    });
  }

  /* ---------------------------------------------------- menu */
  function initMenu() {
    var btn = document.querySelector('[data-menu-toggle]'), menu = document.querySelector('[data-menu]');
    if (!btn || !menu) return;
    function set(open) {
      menu.classList.toggle('is-open', open);
      menu.setAttribute('aria-hidden', String(!open));
      btn.setAttribute('aria-expanded', String(open));
      btn.textContent = open ? tr('close', 'Close') : tr('menu', 'Menu');
      html.classList.toggle('menu-open', open);
      if (lenis) open ? lenis.stop() : lenis.start();
      if (open && !reduce) gsap.fromTo(menu.querySelectorAll('.menu__link'), { yPercent: 60, opacity: 0 }, { yPercent: 0, opacity: 1, duration: 1, ease: EASE, stagger: .06, delay: .25 });
    }
    btn.addEventListener('click', function () { set(!menu.classList.contains('is-open')); });
    menu.addEventListener('click', function (e) { if (e.target.closest('a') || e.target.closest('[data-book]')) set(false); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && menu.classList.contains('is-open')) set(false); });
  }

  /* ---------------------------------------------------- booking panel */
  function initBooking() {
    var bk = document.querySelector('[data-booking]');
    if (!bk) return;
    var form = bk.querySelector('[data-bk-form]'), steps = bk.querySelectorAll('.bk__step');
    var next = bk.querySelector('[data-bk-next]'), back = bk.querySelector('[data-bk-back]');
    var bar = bk.querySelector('[data-bk-progress]'), err = bk.querySelector('[data-bk-error]');
    var step = 1, last = 4, lastFocus = null;

    function show(n) {
      step = n;
      steps.forEach(function (s) { s.classList.toggle('is-active', +s.dataset.step === n); });
      bar.style.width = Math.min(100, n / last * 100) + '%';
      back.style.visibility = n > 1 && n <= last ? 'visible' : 'hidden';
      next.style.display = n > last ? 'none' : '';
      next.textContent = n === last ? tr('send', 'Send request') : tr('continue', 'Continue');
      err.textContent = '';
      var f = bk.querySelector('.bk__step.is-active input, .bk__step.is-active textarea');
      if (f) setTimeout(function () { f.focus({ preventScroll: true }); }, 350);
    }
    function open(location) {
      lastFocus = document.activeElement;
      form.reset(); show(1);
      var langSel = form.querySelector('select[name="language"] option[selected]');
      if (langSel) langSel.selected = true;
      if (location) {
        var r = form.querySelector('input[name="location"][value="' + location + '"]');
        if (r) r.checked = true;
      }
      bk.classList.add('is-open'); bk.setAttribute('aria-hidden', 'false');
      html.classList.add('bk-open'); if (lenis) lenis.stop();
    }
    function close() {
      bk.classList.remove('is-open'); bk.setAttribute('aria-hidden', 'true');
      html.classList.remove('bk-open'); if (lenis) lenis.start();
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
      if (form.website.value) return; // honeypot
      var loc = form.querySelector('input[name="location"]:checked');
      var locLabel = loc ? loc.getAttribute('data-label') : '';
      var body = [
        tr('interest', 'Interest') + ': ' + form.interest.value,
        tr('location', 'Location') + ': ' + locLabel,
        tr('name', 'Name') + ': ' + form.name.value.trim(),
        tr('email', 'Email') + ': ' + form.email.value.trim(),
        tr('phone', 'Phone') + ': ' + (form.phone.value.trim() || '—'),
        tr('language', 'Preferred language') + ': ' + form.language.value,
        '', form.message.value.trim()
      ].join('\n');
      var subject = tr('subject', 'Consultation request') + ' — ' + form.interest.value + ' (' + locLabel + ')';
      window.location.href = 'mailto:' + 'info@drgiuseppecolombo.com' + '?subject=' + encodeURIComponent(subject) + '&body=' + encodeURIComponent(body);
      show(5);
    }
    next.addEventListener('click', function () {
      var m = valid(); if (m) { err.textContent = m; return; }
      if (step === last) submit(); else show(step + 1);
    });
    back.addEventListener('click', function () { if (step > 1) show(step - 1); });
    form.addEventListener('change', function (e) {
      if (e.target.type === 'radio') setTimeout(function () { if (!valid()) show(step + 1); }, 280);
    });
    form.addEventListener('submit', function (e) { e.preventDefault(); next.click(); });
    document.addEventListener('click', function (e) {
      var t = e.target.closest('[data-book]');
      if (t) { e.preventDefault(); open(t.getAttribute('data-book-location')); }
      if (e.target.closest('[data-book-close]')) close();
    });
    document.addEventListener('keydown', function (e) {
      if (!bk.classList.contains('is-open')) return;
      if (e.key === 'Escape') close();
      if (e.key === 'Tab') { // focus trap
        var f = bk.querySelectorAll('button:not([style*="hidden"]), input:not(.hp), select, textarea, a[href]');
        f = Array.prototype.filter.call(f, function (x) { return x.offsetParent !== null; });
        if (!f.length) return;
        if (e.shiftKey && document.activeElement === f[0]) { e.preventDefault(); f[f.length - 1].focus(); }
        else if (!e.shiftKey && document.activeElement === f[f.length - 1]) { e.preventDefault(); f[0].focus(); }
      }
    });
  }

  /* ---------------------------------------------------- page transitions */
  function initTransitions() {
    var pt = document.querySelector('.pt');
    function enter() {
      if (reduce) { gsap.set(pt, { scaleY: 0 }); drawLoadLines(); return; }
      gsap.to(pt, { scaleY: 0, transformOrigin: 'top', duration: .9, ease: 'expo.inOut', delay: .05, onComplete: drawLoadLines });
      gsap.delayedCall(.45, function () { if (window.Site.onEnter) window.Site.onEnter(); });
    }
    enter();
    window.addEventListener('pageshow', function (e) { if (e.persisted) gsap.set(pt, { scaleY: 0 }); });
    document.addEventListener('click', function (e) {
      var a = e.target.closest('a[href]');
      if (!a || e.defaultPrevented || e.metaKey || e.ctrlKey || e.shiftKey || a.target === '_blank') return;
      var href = a.getAttribute('href');
      if (!href || href.charAt(0) === '#' || href.indexOf('mailto:') === 0 || href.indexOf('tel:') === 0) return;
      var url = new URL(href, location.href);
      if (url.origin !== location.origin) return;
      if (url.pathname === location.pathname && url.hash) return;
      e.preventDefault();
      if (reduce) { location.href = url.href; return; }
      gsap.fromTo(pt, { scaleY: 0, transformOrigin: 'bottom' }, { scaleY: 1, duration: .6, ease: 'expo.inOut', onComplete: function () { location.href = url.href; } });
    });
    document.querySelectorAll('a[href^="#"]').forEach(function (a) {
      a.addEventListener('click', function (e) { var t = document.querySelector(a.getAttribute('href')); if (t) { e.preventDefault(); Site.scrollTo(t); } });
    });
  }

  /* ---------------------------------------------------- small details */
  function initCursor() {
    var c = document.querySelector('.cursor');
    if (!c || reduce || window.matchMedia('(hover: none)').matches) return;
    var x = gsap.quickTo(c, 'x', { duration: .35, ease: 'power3' }), y = gsap.quickTo(c, 'y', { duration: .35, ease: 'power3' });
    window.addEventListener('mousemove', function (e) { x(e.clientX); y(e.clientY); c.classList.add('is-on'); });
    document.addEventListener('mouseleave', function () { c.classList.remove('is-on'); });
    document.addEventListener('mouseover', function (e) { c.classList.toggle('is-link', !!e.target.closest('a, button, label, summary')); });
  }
  function initClock() {
    var t = document.querySelector('[data-clock]');
    if (!t) return;
    var f = new Intl.DateTimeFormat('en-GB', { hour: '2-digit', minute: '2-digit', timeZone: 'Europe/Zurich' });
    function tick() { t.textContent = f.format(new Date()); }
    tick(); setInterval(tick, 20000);
  }
  function initVideos() {
    document.addEventListener('click', function (e) {
      var v = e.target.closest('[data-yt]');
      if (!v) return;
      var id = v.getAttribute('data-yt');
      var wrap = document.createElement('div');
      wrap.className = 'vid';
      wrap.innerHTML = '<iframe src="https://www.youtube-nocookie.com/embed/' + id + '?autoplay=1&rel=0" title="' + v.getAttribute('aria-label') + '" allow="autoplay; encrypted-media; picture-in-picture" allowfullscreen></iframe>';
      v.replaceWith(wrap);
    });
  }
  function initMap() {
    var box = document.querySelector('[data-map]');
    if (!box) return;
    box.querySelector('[data-map-load]').addEventListener('click', function () {
      var q = encodeURIComponent(box.getAttribute('data-map'));
      box.insertAdjacentHTML('beforeend', '<iframe title="' + tr('map', 'Map') + '" loading="lazy" src="https://maps.google.com/maps?q=' + q + '&t=m&z=14&hl=' + document.documentElement.lang + '&output=embed"></iframe>');
    });
  }
  function initFilters() {
    document.querySelectorAll('[data-filter]').forEach(function (b) {
      b.addEventListener('click', function () {
        var f = b.getAttribute('data-filter');
        document.querySelectorAll('[data-filter]').forEach(function (x) { x.classList.toggle('is-active', x === b); });
        document.querySelectorAll('.pub').forEach(function (p) { p.classList.toggle('is-hidden', f !== 'all' && p.getAttribute('data-topic') !== f); });
        ST.refresh();
      });
    });
    document.querySelectorAll('[data-jfilter]').forEach(function (b) {
      b.addEventListener('click', function () {
        var f = b.getAttribute('data-jfilter');
        document.querySelectorAll('[data-jfilter]').forEach(function (x) { x.classList.toggle('is-active', x === b); });
        document.querySelectorAll('[data-cat]').forEach(function (p) {
          var hide = f !== 'all' && p.getAttribute('data-cat') !== f;
          p.classList.toggle('is-hidden', hide);
          if (!hide) gsap.set(p, { opacity: 1, y: 0 });
        });
        ST.refresh();
      });
    });
  }
  function initTilt() {
    if (reduce) return;
    document.querySelectorAll('[data-tilt]').forEach(function (wrap) {
      var book = wrap.querySelector('.book');
      gsap.fromTo(book, { rotateY: -28, rotateX: 8 }, { rotateY: -10, rotateX: 2, ease: 'none', scrollTrigger: { trigger: wrap, start: 'top bottom', end: 'bottom top', scrub: 1 } });
      if (window.matchMedia('(hover: none)').matches) return;
      wrap.addEventListener('mousemove', function (e) {
        var r = wrap.getBoundingClientRect(), dx = (e.clientX - r.left) / r.width - .5, dy = (e.clientY - r.top) / r.height - .5;
        gsap.to(wrap, { rotateY: dx * 12, rotateX: -dy * 10, duration: .8, ease: 'power3' });
      });
      wrap.addEventListener('mouseleave', function () { gsap.to(wrap, { rotateY: 0, rotateX: 0, duration: 1.2, ease: 'power3' }); });
    });
  }
  function initCounts() {
    document.querySelectorAll('[data-count]').forEach(function (el) {
      if (reduce) return;
      var to = +el.getAttribute('data-count'), o = { v: 0 };
      ST.create({ trigger: el, start: 'top 90%', once: true, onEnter: function () {
        gsap.to(o, { v: to, duration: 1.6, ease: 'power2.out', onUpdate: function () { el.textContent = Math.round(o.v); } });
      } });
    });
  }
  function initHScroll() {
    var track = document.querySelector('[data-hscroll]');
    if (!track || reduce) return;
    var mm = gsap.matchMedia();
    mm.add('(min-width: 901px)', function () {
      var list = track.querySelector('ol'), sec = track.closest('section');
      var dist = function () { return Math.max(0, list.scrollWidth - window.innerWidth); };
      gsap.to(list, { x: function () { return -dist(); }, ease: 'none',
        scrollTrigger: { trigger: sec, start: 'top top', end: function () { return '+=' + dist(); }, pin: true, scrub: 1, invalidateOnRefresh: true } });
    });
  }
  function initReadbar() {
    var bar = document.querySelector('[data-readbar]'), art = document.querySelector('.art__body');
    if (!bar || !art) return;
    gsap.to(bar, { scaleX: 1, ease: 'none', scrollTrigger: { trigger: art, start: 'top 30%', end: 'bottom bottom', scrub: true } });
  }

  /* ---------------------------------------------------- boot */
  function boot() {
    initLines(); initReveals(); initHeader(); initMenu(); initBooking(); initCursor(); initClock();
    initVideos(); initMap(); initFilters(); initTilt(); initCounts(); initHScroll(); initReadbar();
    if (window.Site.initHome) window.Site.initHome();
    initTransitions();
    window.addEventListener('load', function () { ST.refresh(); });
    if (document.fonts && document.fonts.ready) document.fonts.ready.then(function () { ST.refresh(); });
  }
  /* deferred scripts run before DOMContentLoaded: wait for it so home.js is registered too */
  if (document.readyState !== 'complete') document.addEventListener('DOMContentLoaded', boot); else boot();
})();
