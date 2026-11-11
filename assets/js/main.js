/* Dr. Giuseppe Colombo — "Luce naturale"
   Shared behaviour: soft light fields (WebGL), arch + soft-focus reveals,
   concern chooser, journey line, booking, transitions. GSAP + ScrollTrigger + Lenis.
   ScrollTriggers are created top-to-bottom; every effect has a reduced-motion state. */
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
  var tr = function (k, f) { return T[k] || f; };
  var q = function (s, c) { return (c || document).querySelector(s); };
  var qa = function (s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); };
  var SOFT = 'expo.out', SILK = 'power3.inOut';
  var Site = (window.Site = window.Site || {});
  Site.reduce = reduce; Site.q = q; Site.qa = qa;

  /* ------------------------------------------------ smooth scroll */
  var lenis = null;
  if (!reduce && typeof window.Lenis !== 'undefined') {
    lenis = new window.Lenis({ duration: 1.25, easing: function (t) { return Math.min(1, 1.001 - Math.pow(2, -10 * t)); } });
    lenis.on('scroll', ST.update);
    gsap.ticker.add(function (t) { lenis.raf(t * 1000); });
    gsap.ticker.lagSmoothing(0);
  }
  Site.lenis = lenis;
  Site.scrollTo = function (el) { if (lenis) lenis.scrollTo(el, { offset: -70, duration: 1.6 }); else if (el) el.scrollIntoView({ behavior: reduce ? 'auto' : 'smooth' }); };

  /* ------------------------------------------------ light fields (WebGL) */
  var PALETTES = {
    warm: [[.957, .910, .862], [.925, .808, .725], [.839, .655, .588], [1, .902, .749]],
    lake: [[.835, .886, .882], [.663, .753, .765], [.498, .620, .643], [1, .941, .839]]
  };
  var FRAG = [
    'precision mediump float;uniform vec2 r;uniform float t;uniform vec3 c1,c2,c3,c4;',
    'float h(vec2 p){return fract(sin(dot(p,vec2(127.1,311.7)))*43758.5453);}',
    'float n(vec2 p){vec2 i=floor(p),f=fract(p);f=f*f*(3.-2.*f);return mix(mix(h(i),h(i+vec2(1,0)),f.x),mix(h(i+vec2(0,1)),h(i+vec2(1,1)),f.x),f.y);}',
    'float fbm(vec2 p){float v=0.,a=.5;for(int i=0;i<5;i++){v+=a*n(p);p*=2.03;a*=.5;}return v;}',
    'void main(){vec2 uv=gl_FragCoord.xy/r;vec2 p=uv*vec2(r.x/r.y,1.)*1.5;float s=t*.035;',
    'vec2 a=vec2(fbm(p+s),fbm(p+vec2(5.2,1.3)-s));vec2 w=vec2(fbm(p+3.*a+vec2(1.7,9.2)+s*1.2),fbm(p+3.*a+vec2(8.3,2.8)-s));',
    'float f=fbm(p+2.4*w);vec3 col=mix(c1,c2,smoothstep(.2,.7,f));col=mix(col,c3,smoothstep(.55,1.0,length(w))*.6);',
    'float k=pow(abs(sin((p.x+w.x*2.)*2.6+s*7.)*sin((p.y+w.y*2.)*2.6-s*6.)),7.);col=mix(col,c4,k*.35);',
    'col=mix(col,c4,.28*smoothstep(1.,0.,distance(uv,vec2(.78,.85))));gl_FragColor=vec4(col,1.);}'
  ].join('');
  var VERT = 'attribute vec2 p;void main(){gl_Position=vec4(p,0.,1.);}';
  var fields = [];
  function initGlows() {
    qa('canvas[data-glow]').forEach(function (cv) {
      var gl = cv.getContext('webgl', { antialias: false, alpha: false, preserveDrawingBuffer: false });
      if (!gl) return;
      function sh(type, src) { var s = gl.createShader(type); gl.shaderSource(s, src); gl.compileShader(s); return s; }
      var pr = gl.createProgram();
      gl.attachShader(pr, sh(gl.VERTEX_SHADER, VERT)); gl.attachShader(pr, sh(gl.FRAGMENT_SHADER, FRAG)); gl.linkProgram(pr);
      if (!gl.getProgramParameter(pr, gl.LINK_STATUS)) return;
      gl.useProgram(pr);
      var buf = gl.createBuffer(); gl.bindBuffer(gl.ARRAY_BUFFER, buf);
      gl.bufferData(gl.ARRAY_BUFFER, new Float32Array([-1, -1, 1, -1, -1, 1, 1, 1]), gl.STATIC_DRAW);
      var loc = gl.getAttribLocation(pr, 'p'); gl.enableVertexAttribArray(loc); gl.vertexAttribPointer(loc, 2, gl.FLOAT, false, 0, 0);
      var u = { r: gl.getUniformLocation(pr, 'r'), t: gl.getUniformLocation(pr, 't') };
      var pal = PALETTES[cv.getAttribute('data-glow')] || PALETTES.warm;
      ['c1', 'c2', 'c3', 'c4'].forEach(function (c, i) { gl.uniform3fv(gl.getUniformLocation(pr, c), pal[i]); });
      var f = { cv: cv, gl: gl, u: u, visible: false, t0: Math.random() * 40 };
      function size() {
        var scale = 0.5, w = Math.max(2, Math.round(cv.clientWidth * scale)), h = Math.max(2, Math.round(cv.clientHeight * scale));
        if (cv.width !== w || cv.height !== h) { cv.width = w; cv.height = h; gl.viewport(0, 0, w, h); gl.uniform2f(u.r, w, h); }
      }
      f.draw = function (time) { size(); gl.uniform1f(u.t, f.t0 + time); gl.drawArrays(gl.TRIANGLE_STRIP, 0, 4); };
      fields.push(f);
      new IntersectionObserver(function (es) { f.visible = es[0].isIntersecting; if (f.visible) f.draw(performance.now() / 1000); }, { rootMargin: '100px' }).observe(cv);
      f.draw(0);
      /* only switch from the CSS gradient to WebGL if the GPU really drew something */
      var px = new Uint8Array(4); gl.readPixels(1, 1, 1, 1, gl.RGBA, gl.UNSIGNED_BYTE, px);
      var ok = !(px[0] > 250 && px[1] > 250 && px[2] > 250) && (px[0] + px[1] + px[2] > 30);
      if (ok || cv.clientWidth === 0) cv.parentNode.classList.add('is-live'); else { fields.pop(); }
    });
    if (!fields.length || reduce) return;
    gsap.ticker.add(function () {
      var time = performance.now() / 1000;
      for (var i = 0; i < fields.length; i++) if (fields[i].visible) fields[i].draw(time);
    });
  }

  /* ------------------------------------------------ text: line masks, fades, soft focus */
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
      gsap.set(el, { opacity: 1 }); gsap.set(lines, { yPercent: 110 });
      ST.create({ trigger: el, start: 'top 88%', once: true, onEnter: function () { gsap.to(lines, { yPercent: 0, duration: 1.4, ease: SOFT, stagger: .1 }); } });
    });
    var items = qa('[data-reveal]');
    gsap.set(items, { y: 26 });
    ST.batch(items, { start: 'top 92%', once: true, onEnter: function (b) { gsap.to(b, { opacity: 1, y: 0, duration: 1.3, ease: SOFT, stagger: .08 }); } });
    /* soft focus: blur → clarity, the visual metaphor of a natural result */
    qa('[data-focus]').forEach(function (el) {
      gsap.set(el, { filter: 'blur(14px)', scale: 1.03 });
      ST.create({ trigger: el, start: 'top 85%', once: true, onEnter: function () { gsap.to(el, { opacity: 1, filter: 'blur(0px)', scale: 1, duration: 2, ease: SOFT }); } });
    });
  }

  /* ------------------------------------------------ arches: a window of light opens */
  function archTimeline(fig, opts) {
    opts = opts || {};
    var inner = q('.arch__in', fig), img = q('img', fig), sweep = q('.arch__sweep', fig);
    var tl = gsap.timeline({ paused: true, delay: opts.delay || 0 });
    tl.fromTo(inner, { clipPath: 'inset(100% 0% 0% 0%)' }, { clipPath: 'inset(0% 0% 0% 0%)', duration: 1.6, ease: SILK }, 0);
    if (img) tl.fromTo(img, { scale: 1.18 }, { scale: 1, duration: 2.2, ease: SOFT }, 0);
    tl.fromTo(fig, { '--o': 0 }, { '--o': 1, duration: 1 }, .4);
    if (sweep) tl.fromTo(sweep, { xPercent: -130 }, { xPercent: 130, duration: 1.8, ease: 'power2.inOut' }, 1.1);
    return tl;
  }
  Site.archTimeline = archTimeline;
  function initArches() {
    if (reduce) return;
    qa('[data-arch]').forEach(function (fig) {
      if (fig.closest('.hero')) return; // hero is choreographed by home.js
      var tl = archTimeline(fig);
      gsap.set(q('.arch__in', fig), { clipPath: 'inset(100% 0% 0% 0%)' });
      ST.create({ trigger: fig, start: 'top 85%', once: true, onEnter: function () { tl.play(); } });
      var img = q('img', fig);
      if (img && !fig.closest('.cn')) gsap.to(img, { yPercent: -6, ease: 'none', scrollTrigger: { trigger: fig, start: 'top bottom', end: 'bottom top', scrub: 1 } });
    });
  }

  /* ------------------------------------------------ concern chooser (tabs) */
  function initConcerns() {
    qa('[data-concerns]').forEach(function (box) {
      var tabs = qa('[data-concern]', box), panels = qa('[data-panel]', box), current = tabs[0] && tabs[0].getAttribute('data-concern');
      function show(key, focus) {
        if (key === current) return;
        current = key;
        tabs.forEach(function (t) { var on = t.getAttribute('data-concern') === key; t.classList.toggle('is-active', on); t.setAttribute('aria-selected', String(on)); t.tabIndex = on ? 0 : -1; if (on && focus) t.focus(); });
        panels.forEach(function (p) {
          var on = p.getAttribute('data-panel') === key;
          p.hidden = !on; p.classList.toggle('is-active', on);
          if (on && !reduce) {
            gsap.fromTo(p, { opacity: 0, filter: 'blur(10px)', y: 14 }, { opacity: 1, filter: 'blur(0px)', y: 0, duration: 1, ease: SOFT });
            var arch = q('[data-arch]', p); if (arch) { gsap.set(q('.arch__in', arch), { clipPath: 'inset(0%)' }); var sw = q('.arch__sweep', arch); if (sw) gsap.fromTo(sw, { xPercent: -130 }, { xPercent: 130, duration: 1.6, ease: 'power2.inOut' }); }
            gsap.fromTo(qa('li', p), { opacity: 0, y: 12 }, { opacity: 1, y: 0, duration: .8, ease: SOFT, stagger: .06, delay: .1 });
          }
        });
        ST.refresh();
      }
      tabs.forEach(function (t, i) {
        t.tabIndex = i === 0 ? 0 : -1;
        t.addEventListener('click', function () { show(t.getAttribute('data-concern')); });
        t.addEventListener('keydown', function (e) {
          var d = e.key === 'ArrowDown' || e.key === 'ArrowRight' ? 1 : e.key === 'ArrowUp' || e.key === 'ArrowLeft' ? -1 : 0;
          if (!d) return; e.preventDefault();
          var n = tabs[(i + d + tabs.length) % tabs.length]; show(n.getAttribute('data-concern'), true);
        });
      });
    });
  }

  /* ------------------------------------------------ journey: a line of light */
  function initJourneys() {
    qa('[data-journey]').forEach(function (list) {
      var line = q('[data-journey-line]', list), steps = qa('[data-step]', list);
      if (reduce) { gsap.set(line, { scaleY: 1 }); steps.forEach(function (s) { s.classList.add('is-on'); }); return; }
      gsap.fromTo(line, { scaleY: 0 }, { scaleY: 1, ease: 'none', scrollTrigger: { trigger: list, start: 'top 65%', end: 'bottom 65%', scrub: .6 } });
      steps.forEach(function (s) { ST.create({ trigger: s, start: 'top 66%', onEnter: function () { s.classList.add('is-on'); }, onLeaveBack: function () { s.classList.remove('is-on'); } }); });
    });
  }

  /* ------------------------------------------------ anatomy plates: focus, then a lens inspects the drawing */
  function initAnatomy() {
    qa('[data-anat]').forEach(function (fig) {
      var img = q('img', fig), lens = q('.anat__lens', fig);
      if (reduce) return;
      gsap.set(img, { scale: 1.12, filter: 'blur(8px)' });
      ST.create({ trigger: fig, start: 'top 80%', once: true, onEnter: function () { gsap.to(img, { scale: 1, filter: 'blur(0px)', duration: 2, ease: SOFT }); } });
      gsap.timeline({ scrollTrigger: { trigger: fig, start: 'top 70%', end: 'bottom 25%', scrub: 1 } })
        .fromTo(lens, { opacity: 0, left: '22%', top: '62%' }, { opacity: 1, duration: .2 })
        .to(lens, { left: '50%', top: '42%', duration: .4, ease: 'sine.inOut' })
        .to(lens, { left: '76%', top: '55%', duration: .4, ease: 'sine.inOut' })
        .to(lens, { opacity: 0, duration: .2 });
    });
  }

  /* ------------------------------------------------ counters + tilt */
  function initCounters() {
    if (reduce) return;
    qa('[data-count]').forEach(function (el) {
      var to = +el.getAttribute('data-count'), suf = el.getAttribute('data-suffix') || '', o = { v: 0 };
      el.textContent = '0' + suf;
      ST.create({ trigger: el, start: 'top 90%', once: true, onEnter: function () {
        gsap.to(o, { v: to, duration: 1.8, ease: 'power2.out', onUpdate: function () { el.textContent = Math.round(o.v) + suf; } });
      } });
    });
  }
  function initTilt() {
    if (reduce) return;
    qa('[data-tilt]').forEach(function (el) {
      gsap.fromTo(el, { rotateY: -24, rotateX: 6 }, { rotateY: -6, rotateX: 1, ease: 'none', scrollTrigger: { trigger: el, start: 'top bottom', end: 'bottom top', scrub: 1 } });
      if (window.matchMedia('(hover: none)').matches) return;
      var wrap = el.parentNode;
      wrap.addEventListener('mousemove', function (e) { var r = wrap.getBoundingClientRect(); gsap.to(wrap, { rotateY: ((e.clientX - r.left) / r.width - .5) * 10, rotateX: -((e.clientY - r.top) / r.height - .5) * 8, duration: .9, ease: 'power3' }); });
      wrap.addEventListener('mouseleave', function () { gsap.to(wrap, { rotateY: 0, rotateX: 0, duration: 1.2, ease: 'power3' }); });
    });
  }

  /* ------------------------------------------------ header */
  function initHeader() {
    var hdr = q('[data-hdr]'); if (!hdr) return;
    var last = 0;
    function on(y) { hdr.classList.toggle('is-scrolled', y > 30); if (!html.classList.contains('menu-open')) hdr.classList.toggle('is-hidden', y > last && y > 480); last = y; }
    if (lenis) lenis.on('scroll', function (e) { on(e.scroll); }); else window.addEventListener('scroll', function () { on(window.scrollY); }, { passive: true });
    qa('.tr, .pull, .ftr').forEach(function (sec) { ST.create({ trigger: sec, start: 'top 40px', end: 'bottom 40px', toggleClass: { targets: hdr, className: 'on-dark' } }); });
  }

  /* ------------------------------------------------ menu */
  function initMenu() {
    var btn = q('[data-menu-toggle]'), menu = q('[data-menu]'); if (!btn || !menu) return;
    var label = q('.hdr__menu-t', btn);
    function set(open) {
      menu.classList.toggle('is-open', open); menu.setAttribute('aria-hidden', String(!open)); btn.setAttribute('aria-expanded', String(open));
      label.textContent = open ? tr('close', 'Close') : tr('menu', 'Menu'); html.classList.toggle('menu-open', open);
      if (lenis) { if (open) lenis.stop(); else lenis.start(); }
      if (open && !reduce) gsap.fromTo(qa('.menu__link', menu), { y: 40, opacity: 0, filter: 'blur(8px)' }, { y: 0, opacity: 1, filter: 'blur(0px)', duration: 1.1, ease: SOFT, stagger: .06, delay: .35 });
    }
    btn.addEventListener('click', function () { set(!menu.classList.contains('is-open')); });
    menu.addEventListener('click', function (e) { if (e.target.closest('a') || e.target.closest('[data-book]')) set(false); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && menu.classList.contains('is-open')) set(false); });
  }

  /* ------------------------------------------------ booking panel */
  function initBooking() {
    var bk = q('[data-booking]'); if (!bk) return;
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
    function close() { bk.classList.remove('is-open'); bk.setAttribute('aria-hidden', 'true'); html.classList.remove('bk-open'); if (lenis) lenis.start(); if (lastFocus) lastFocus.focus({ preventScroll: true }); }
    function valid() {
      if (step === 1 && !form.interest.value) return tr('e1', 'Please choose one option.');
      if (step === 2 && !form.location.value) return tr('e2', 'Please choose a location.');
      if (step === 3) { if (!form.name.value.trim()) return tr('e3', 'Please enter your name.'); if (!/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(form.email.value.trim())) return tr('e4', 'Please enter a valid email address.'); }
      if (step === 4 && !form.privacy.checked) return tr('e5', 'Please confirm the privacy consent.');
      return '';
    }
    function submit() {
      if (form.website.value) return;
      var loc = q('input[name="location"]:checked', form), ll = loc ? loc.getAttribute('data-label') : '';
      var body = [tr('interest', 'Interest') + ': ' + form.interest.value, tr('location', 'Location') + ': ' + ll, tr('name', 'Name') + ': ' + form.name.value.trim(),
        tr('email', 'Email') + ': ' + form.email.value.trim(), tr('phone', 'Phone') + ': ' + (form.phone.value.trim() || '—'), tr('language', 'Preferred language') + ': ' + form.language.value, '', form.message.value.trim()].join('\n');
      window.location.href = 'mailto:info@drgiuseppecolombo.com?subject=' + encodeURIComponent(tr('subject', 'Consultation request') + ' — ' + form.interest.value + ' (' + ll + ')') + '&body=' + encodeURIComponent(body);
      show(5);
    }
    next.addEventListener('click', function () { var m = valid(); if (m) { err.textContent = m; return; } if (step === last) submit(); else show(step + 1); });
    back.addEventListener('click', function () { if (step > 1) show(step - 1); });
    form.addEventListener('change', function (e) { if (e.target.type === 'radio') setTimeout(function () { if (!valid()) show(step + 1); }, 300); });
    form.addEventListener('submit', function (e) { e.preventDefault(); next.click(); });
    document.addEventListener('click', function (e) { var t = e.target.closest('[data-book]'); if (t) { e.preventDefault(); open(t.getAttribute('data-book-location')); } if (e.target.closest('[data-book-close]')) close(); });
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

  /* ------------------------------------------------ page transitions: light fades in and out */
  function initTransitions() {
    var pt = q('.pt'), mono = q('.pt__mono');
    if (reduce) gsap.set(pt, { autoAlpha: 0 });
    else gsap.timeline().to(mono, { scale: 1.08, opacity: 0, duration: .7, ease: 'power2.in' }, 0).to(pt, { autoAlpha: 0, duration: .9, ease: 'power2.out' }, .25);
    window.addEventListener('pageshow', function (e) { if (e.persisted) gsap.set(pt, { autoAlpha: 0 }); });
    document.addEventListener('click', function (e) {
      var a = e.target.closest('a[href]');
      if (!a || e.defaultPrevented || e.metaKey || e.ctrlKey || e.shiftKey || a.target === '_blank') return;
      var href = a.getAttribute('href');
      if (!href || href.charAt(0) === '#' || /^(mailto|tel):/.test(href)) return;
      var url = new URL(href, location.href);
      if (url.origin !== location.origin) return;
      if (url.pathname === location.pathname && url.hash) { var tg = q(url.hash); if (tg) { e.preventDefault(); Site.scrollTo(tg); } return; }
      e.preventDefault();
      if (reduce) { location.href = url.href; return; }
      gsap.timeline({ onComplete: function () { location.href = url.href; } })
        .set(mono, { scale: .94, opacity: 0 }).to(pt, { autoAlpha: 1, duration: .55, ease: 'power2.inOut' }).to(mono, { scale: 1, opacity: 1, duration: .4, ease: SOFT }, '-=.25');
    });
    qa('a[href^="#"]').forEach(function (a) { a.addEventListener('click', function (e) { var tg = q(a.getAttribute('href')); if (tg) { e.preventDefault(); Site.scrollTo(tg); } }); });
  }

  /* ------------------------------------------------ small things */
  function initClock() { var t = q('[data-clock]'); if (!t) return; var f = new Intl.DateTimeFormat('en-GB', { hour: '2-digit', minute: '2-digit', timeZone: 'Europe/Zurich' }); var k = function () { t.textContent = f.format(new Date()); }; k(); setInterval(k, 20000); }
  function initVideos() { document.addEventListener('click', function (e) { var v = e.target.closest('[data-yt]'); if (!v) return; var w = document.createElement('div'); w.className = 'vid'; w.innerHTML = '<iframe src="https://www.youtube-nocookie.com/embed/' + v.getAttribute('data-yt') + '?autoplay=1&rel=0" title="' + v.getAttribute('aria-label') + '" allow="autoplay; encrypted-media; picture-in-picture" allowfullscreen></iframe>'; v.replaceWith(w); }); }
  function initMap() { var box = q('[data-map]'); if (!box) return; q('[data-map-load]', box).addEventListener('click', function () { box.insertAdjacentHTML('beforeend', '<iframe title="' + tr('map', 'Map') + '" loading="lazy" src="https://maps.google.com/maps?q=' + encodeURIComponent(box.getAttribute('data-map')) + '&t=m&z=14&hl=' + html.lang + '&output=embed"></iframe>'); }); }
  function initFilters() {
    qa('[data-filter]').forEach(function (b) { b.addEventListener('click', function () { var f = b.getAttribute('data-filter'); qa('[data-filter]').forEach(function (x) { x.classList.toggle('is-active', x === b); }); qa('.pub').forEach(function (p) { p.classList.toggle('is-hidden', f !== 'all' && p.getAttribute('data-topic') !== f); }); ST.refresh(); }); });
    qa('[data-jfilter]').forEach(function (b) { b.addEventListener('click', function () { var f = b.getAttribute('data-jfilter'); qa('[data-jfilter]').forEach(function (x) { x.classList.toggle('is-active', x === b); }); qa('[data-cat]').forEach(function (p) { var h = f !== 'all' && p.getAttribute('data-cat') !== f; p.classList.toggle('is-hidden', h); if (!h) gsap.set(p, { opacity: 1, y: 0 }); }); ST.refresh(); }); });
  }
  function initReadbar() { var bar = q('[data-readbar]'), art = q('.art__body'); if (!bar || !art) return; gsap.to(bar, { scaleX: 1, ease: 'none', scrollTrigger: { trigger: art, start: 'top 30%', end: 'bottom bottom', scrub: true } }); }

  /* ------------------------------------------------ boot (home first: its pinned scenes sit near the top) */
  function boot() {
    initGlows();
    if (Site.initHome) Site.initHome();
    initReveals(); initArches(); initConcerns(); initJourneys(); initAnatomy(); initCounters(); initTilt();
    initHeader(); initMenu(); initBooking(); initClock(); initVideos(); initMap(); initFilters(); initReadbar();
    initTransitions();
    window.addEventListener('load', function () { ST.refresh(); });
    if (document.fonts && document.fonts.ready) document.fonts.ready.then(function () { ST.refresh(); });
  }
  if (document.readyState !== 'complete') document.addEventListener('DOMContentLoaded', boot); else boot();
})();
