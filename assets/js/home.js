/* Home — "L'Atlante della Misura": loader, hero, the Ruler and Plates I–VIII.
   Scroll is the timeline; each plate uses exactly one instrument. */
(function () {
  'use strict';
  var Site = (window.Site = window.Site || {});

  Site.initHome = function () {
    var gsap = window.gsap, ST = window.ScrollTrigger, q = Site.q, qa = Site.qa, reduce = Site.reduce;
    var MEASURE = 'power2.inOut', SETTLE = 'expo.out';
    var mm = gsap.matchMedia();
    var DESK = '(min-width: 901px)', MOB = '(max-width: 900px)';

    /* ============ Loader: calibrating 0 → 100 mm (first visit of the session) ============ */
    var loader = q('[data-loader]'), seen = false;
    try { seen = sessionStorage.getItem('gc-cal') === '1'; sessionStorage.setItem('gc-cal', '1'); } catch (e) {}

    /* ============ Hero: the slit opens, the rulers measure ============ */
    var fig = q('.hero__fig'), img = q('.hero__img'), photo = q('.hero__img img'), slit = q('.hero__slit');
    var lines = qa('.hero__title .hl > span'), ins = qa('[data-hero-in]'), rules = qa('.hero .rule'), cap = q('.hero__cap');
    if (!reduce) {
      gsap.set(img, { clipPath: 'inset(0 50% 0 50%)' });
      gsap.set(photo, { scale: 1.14 });
      gsap.set(lines, { yPercent: 112 });
      gsap.set(ins, { opacity: 0, y: 18 });
      gsap.set(rules[0], { scaleX: 0 }); gsap.set(rules[1], { scaleY: 0 });
      gsap.set(cap, { opacity: 0 });
    }
    function heroIntro() {
      if (reduce) return;
      gsap.timeline()
        .to(slit, { scaleY: 1, duration: .55, ease: MEASURE })
        .to(img, { clipPath: 'inset(0 0% 0 0%)', duration: 1.25, ease: MEASURE }, .45)
        .to(slit, { opacity: 0, duration: .4 }, 1.3)
        .to(photo, { scale: 1, duration: 1.8, ease: SETTLE }, .45)
        .to(lines, { yPercent: 0, duration: 1.2, ease: SETTLE, stagger: .1 }, .7)
        .to(ins, { opacity: 1, y: 0, duration: 1, ease: SETTLE, stagger: .1 }, 1.1)
        .to(rules[0], { scaleX: 1, duration: 1, ease: MEASURE }, 1.4)
        .to(rules[1], { scaleY: 1, duration: 1, ease: MEASURE }, 1.5)
        .to(cap, { opacity: 1, duration: .8 }, 2);
    }
    if (loader) {
      if (seen || reduce) { loader.classList.add('is-skipped'); heroIntro(); }
      else {
        var fill = q('[data-loader-fill]', loader), n = q('[data-loader-n]', loader), o = { v: 0 };
        gsap.timeline()
          .to(fill, { scaleX: 1, duration: 1.05, ease: MEASURE }, 0)
          .to(o, { v: 100, duration: 1.05, ease: MEASURE, onUpdate: function () { n.textContent = String(Math.round(o.v)).padStart(3, '0'); } }, 0)
          .to(loader, { yPercent: -100, duration: .85, ease: 'expo.inOut' }, 1.25)
          .add(heroIntro, 1.45)
          .set(loader, { display: 'none' });
      }
    } else heroIntro();

    if (!reduce) {
      gsap.to('.hero__fig', { yPercent: -10, ease: 'none', scrollTrigger: { trigger: '.hero', start: 'top top', end: 'bottom top', scrub: 1 } });
      gsap.to('.hero__text', { yPercent: -22, opacity: 0, ease: 'none', scrollTrigger: { trigger: '.hero', start: '25% top', end: 'bottom top', scrub: 1 } });
    }

    /* ============ The Ruler (D1): the whole story is 100 mm ============ */
    var ruler = q('[data-ruler]'), marker = q('[data-ruler-marker]'), mmEl = q('[data-ruler-mm]');
    var plates = qa('[data-plate]'), plateLis = qa('[data-ruler-plate]');
    var mbar = q('.mbar'), mbarMm = q('[data-mbar-mm]');
    var still = false, held = 0;
    function docMax() { return Math.max(1, document.documentElement.scrollHeight - window.innerHeight); }
    function layoutRuler() {
      var h = ruler.getBoundingClientRect().height, max = docMax();
      plateLis.forEach(function (li, i) {
        var sec = plates[i]; if (!sec) return;
        var top = sec.getBoundingClientRect().top + window.scrollY;
        li.style.top = (Math.min(1, top / max) * h) + 'px';
      });
    }
    function updateRuler(y) {
      var p = Math.min(1, Math.max(0, y / docMax())), h = ruler.getBoundingClientRect().height;
      if (still) p = held; else held = p;
      marker.style.transform = 'translateY(' + (p * h) + 'px)';
      var v = String(Math.round(p * 100)).padStart(3, '0');
      mmEl.textContent = v;
      if (mbar) { mbar.style.setProperty('--p', p); mbarMm.textContent = v + ' mm'; }
      ruler.classList.toggle('is-on', y > window.innerHeight * .55);
      var active = -1;
      plates.forEach(function (sec, i) { var r = sec.getBoundingClientRect(); if (r.top < window.innerHeight * .5) active = i; });
      plateLis.forEach(function (li, i) { li.classList.toggle('is-active', i === active); });
    }
    ST.addEventListener('refresh', layoutRuler);
    if (Site.lenis) Site.lenis.on('scroll', function (e) { updateRuler(e.scroll); }); else window.addEventListener('scroll', function () { updateRuler(window.scrollY); }, { passive: true });
    qa('[data-theme="dark"]').forEach(function (sec) {
      ST.create({ trigger: sec, start: 'top 55%', end: 'bottom 55%', toggleClass: { targets: ruler, className: 'on-dark' } });
    });
    ST.create({ trigger: '.p7', start: 'top 40%', end: 'bottom 60%', onToggle: function (s) { still = s.isActive; ruler.classList.toggle('is-still', s.isActive); } });
    layoutRuler(); updateRuler(window.scrollY);

    if (reduce) {
      qa('.mark path').forEach(function (p) { p.style.strokeDashoffset = 0; });
      qa('.map__arc').forEach(function (a) { a.style.strokeDashoffset = 0; });
      return;
    }

    /* ============ TAV. I · Measure: the thirds are drawn, then released ============ */
    (function () {
      var plate = q('.p1__portrait'), tl3 = qa('.thirds__line', plate), labs = qa('.thirds__lab', plate), br = q('.thirds__bracket', plate);
      var head = q('.p1__h'), headLines = Site.splitLines(head), rest = qa('.p1__text > :not(.p1__h)');
      gsap.set(tl3, { scaleX: 0 }); gsap.set(labs, { opacity: 0, x: 12 }); gsap.set(br, { scaleY: 0, transformOrigin: 'top' });
      gsap.set(headLines, { yPercent: 112 }); gsap.set(rest, { opacity: 0, y: 20 });
      function build() {
        return gsap.timeline({ defaults: { ease: 'none' } })
          .to(tl3, { scaleX: 1, duration: 1, stagger: .25, ease: MEASURE }, 0)
          .to(br, { scaleY: 1, duration: .8, ease: MEASURE }, .5)
          .to(labs, { opacity: 1, x: 0, duration: .6, stagger: .2 }, .9)
          .to(headLines, { yPercent: 0, duration: 1, stagger: .15, ease: SETTLE }, 1.4)
          .to(rest, { opacity: 1, y: 0, duration: .8, stagger: .2, ease: SETTLE }, 2.2)
          .to([tl3, labs, br], { opacity: .22, duration: 1 }, 3.6) /* measure, then restraint */
          .to({}, { duration: .5 });
      }
      mm.add(DESK, function () { ST.create({ trigger: '.p1', start: 'top top', end: '+=170%', pin: '.p1__pin', scrub: 1, animation: build(), anticipatePin: 1 }); });
      mm.add(MOB, function () { ST.create({ trigger: '.p1', start: 'top 70%', end: 'bottom 60%', scrub: 1, animation: build() }); });
    })();

    /* ============ TAV. III · Breast: the tape measures, four figures lock ============ */
    (function () {
      var track = q('.p3 [data-tape]'), figs = qa('.p3 .bfig');
      gsap.set(figs, { opacity: 0, y: 40 });
      function build() {
        var tl = gsap.timeline({ defaults: { ease: 'none' } });
        tl.to(track, { x: -720, duration: 4 }, 0);
        figs.forEach(function (f, i) { tl.to(f, { opacity: 1, y: 0, duration: .6, ease: SETTLE }, .4 + i * .85); });
        return tl;
      }
      mm.add(DESK, function () { ST.create({ trigger: '.p3', start: 'top top', end: '+=140%', pin: '.p3__pin', scrub: 1, animation: build(), anticipatePin: 1 }); });
      mm.add(MOB, function () { ST.create({ trigger: '.p3', start: 'top 70%', end: 'bottom 70%', scrub: 1, animation: build() }); });
    })();

    /* ============ TAV. IV · Restore: the suture closes, stitch by stitch ============ */
    (function () {
      var svg = q('.p4 [data-suture]'), stitches = Site.buildSuture(svg), techs = qa('.p4 .tech');
      gsap.set(svg, { clipPath: 'inset(0 100% 0 0)' }); gsap.set(stitches, { opacity: 0, scale: .2, transformOrigin: 'center' }); gsap.set(techs, { opacity: 0, y: 26 });
      function build() {
        var tl = gsap.timeline({ defaults: { ease: 'none' } });
        tl.to(svg, { clipPath: 'inset(0 0% 0 0)', duration: 2, ease: MEASURE }, 0)
          .to(stitches, { opacity: 1, scale: 1, duration: .25, stagger: .1, ease: 'back.out(2)' }, .4);
        techs.forEach(function (t, i) { tl.to(t, { opacity: 1, y: 0, duration: .5, ease: SETTLE }, .8 + i * .55); });
        return tl.to({}, { duration: .4 });
      }
      mm.add(DESK, function () { ST.create({ trigger: '.p4', start: 'top top', end: '+=120%', pin: '.p4__pin', scrub: 1, animation: build(), anticipatePin: 1 }); });
      mm.add(MOB, function () { ST.create({ trigger: '.p4', start: 'top 70%', end: 'bottom 70%', scrub: 1, animation: build() }); });
    })();

    /* ============ TAV. V · Atlas & papers: the book opens, the index scrolls ============ */
    (function () {
      var book = q('.p5 [data-book3d]'), body = q('.book3d__body', book), cover = q('.book3d__cover', book), num = q('.p5 .book3d__n [data-count]');
      var list = q('[data-papers]'), win = q('.papers__window'), stats = qa('.papers__stats [data-count]');
      var o = { v: 0 };
      num.textContent = '0';
      stats.forEach(function (s) { s.textContent = '0'; });
      function build() {
        var dist = function () { return Math.max(0, list.scrollHeight - win.clientHeight); };
        var tl = gsap.timeline({ defaults: { ease: 'none' } });
        tl.fromTo(body, { rotateY: -36, rotateX: 9 }, { rotateY: -8, rotateX: 2, duration: 1.2, ease: MEASURE }, 0)
          .to(cover, { rotateY: -158, duration: 1.4, ease: MEASURE }, .7)
          .to(o, { v: 320, duration: 1.1, onUpdate: function () { num.textContent = Math.round(o.v); } }, 1.3);
        stats.forEach(function (s) { var to = +s.getAttribute('data-count'), so = { v: 0 }; tl.to(so, { v: to, duration: .8, onUpdate: function () { s.textContent = Math.round(so.v); } }, 1.6); });
        tl.to(list, { y: function () { return -dist(); }, duration: 2.6 }, 2.2).to({}, { duration: .3 });
        return tl;
      }
      mm.add(DESK, function () { ST.create({ trigger: '.p5', start: 'top top', end: '+=220%', pin: '.p5__pin', scrub: 1, animation: build(), anticipatePin: 1, invalidateOnRefresh: true }); });
      mm.add(MOB, function () { ST.create({ trigger: '.p5', start: 'top 70%', end: 'bottom 60%', scrub: 1, animation: build(), invalidateOnRefresh: true }); });
    })();

    /* ============ TAV. VI · Teaching: film strip + map, city by city ============ */
    (function () {
      var ctl = Site.stripController(q('.p6'));
      mm.add(DESK, function () {
        var dist = function () { return Math.max(0, ctl.track.scrollWidth - window.innerWidth + 60); };
        gsap.to(ctl.track, { x: function () { return -dist(); }, ease: 'none',
          scrollTrigger: { trigger: '.p6', start: 'top top', end: function () { return '+=' + dist(); }, pin: '.p6__pin', scrub: 1, invalidateOnRefresh: true, anticipatePin: 1, onUpdate: ctl.update } });
        ctl.update();
      });
      mm.add(MOB, function () {
        var strip = q('.p6 .strip'); strip.style.overflowX = 'auto';
        strip.addEventListener('scroll', ctl.update, { passive: true }); ctl.update();
      });
    })();

    /* ============ TAV. VII · Discretion: stillness ============ */
    (function () {
      var qs = qa('.p7__q p'), fig = q('.p7__fig');
      gsap.set(qs, { opacity: 0 }); gsap.set(fig, { opacity: 0 });
      ST.create({ trigger: '.p7', start: 'top 55%', once: true, onEnter: function () {
        gsap.to(qs[0], { opacity: 1, duration: 2.2, ease: 'power1.inOut' });
        if (qs[1]) gsap.to(qs[1], { opacity: 1, duration: 1.4, delay: 1.6 });
        gsap.to(fig, { opacity: .55, duration: 2, delay: 2.2 });
      } });
    })();

    /* ============ TAV. VIII · Lugano: dusk, coordinates ============ */
    (function () {
      var sky = q('.p8__sky'), h = q('.p8__h'), coords = qa('.p8 [data-coord]'), water = qa('.p8__water i'), txt = qa('.p8__text > :not(.p8__h)');
      gsap.set(h, { yPercent: 40, opacity: 0 }); gsap.set(txt, { opacity: 0, y: 20 });
      coords.forEach(function (c) { c.textContent = '0.0000'; });
      function build() {
        var tl = gsap.timeline({ defaults: { ease: 'none' } });
        tl.to(h, { yPercent: 0, opacity: 1, duration: 1, ease: SETTLE }, 0)
          .to(txt, { opacity: 1, y: 0, duration: .8, stagger: .15, ease: SETTLE }, .3)
          .to(sky, { '--dusk': 1, duration: 3 }, .6)
          .to(water, { xPercent: function (i) { return (i % 2 ? -1 : 1) * (40 + (i % 5) * 20); }, opacity: function (i) { return .2 + (i % 4) * .15; }, duration: 3 }, .6);
        coords.forEach(function (c) { var to = +c.getAttribute('data-coord'), o = { v: 0 }; tl.to(o, { v: to, duration: 1.6, ease: 'power2.out', onUpdate: function () { c.textContent = o.v.toFixed(4); } }, .4); });
        return tl.to({}, { duration: .4 });
      }
      mm.add(DESK, function () { ST.create({ trigger: '.p8', start: 'top top', end: '+=140%', pin: '.p8__pin', scrub: 1, animation: build(), anticipatePin: 1 }); });
      mm.add(MOB, function () { ST.create({ trigger: '.p8', start: 'top top', end: '+=90%', pin: '.p8__pin', scrub: 1, animation: build() }); });
    })();

    /* ============ Finale: 100 mm — the marking line underlines "conversation" ============ */
    (function () {
      var p = q('.fin .mark path'), mono = q('.fin__mono');
      var l = p.getTotalLength(); p.style.strokeDasharray = l; p.style.strokeDashoffset = l;
      gsap.set(mono, { opacity: 0, scale: .8 });
      ST.create({ trigger: '.fin', start: 'top 70%', once: true, onEnter: function () {
        gsap.to(mono, { opacity: 1, scale: 1, duration: 1.2, ease: SETTLE });
        gsap.to(p, { strokeDashoffset: 0, duration: 1.4, ease: MEASURE, delay: .9 });
      } });
    })();
  };
})();
