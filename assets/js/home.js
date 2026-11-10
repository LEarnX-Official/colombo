/* Home: the eight scenes of the storyline (scroll = the film's timeline). */
(function () {
  'use strict';
  var Site = (window.Site = window.Site || {});

  Site.initHome = function () {
    var gsap = window.gsap, ST = window.ScrollTrigger, reduce = Site.reduce;
    var q = function (s, c) { return (c || document).querySelector(s); };
    var qa = function (s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); };

    /* -------- reduced motion: show every final state, no pinning -------- */
    if (reduce) {
      qa('.doc__lines, .anat__ln').forEach(Site.showLines);
      gsap.set('.doc__lines', { opacity: 0 });
      gsap.set('.anat__x', { opacity: 1 });
      gsap.set('.anat__face', { opacity: .15 });
      qa('.anat__steps li').forEach(function (li) { li.classList.add('is-active'); });
      return;
    }

    var mm = gsap.matchMedia();
    var isDesk = '(min-width: 901px)', isMob = '(max-width: 900px)';

    /* ========== Scene 1 · The line: drawing drifts away as the camera moves on ========== */
    var heroArt = q('.hero__art'), heroText = q('.hero__text');
    gsap.to(heroArt, { yPercent: -12, scale: .94, opacity: .25, ease: 'none', scrollTrigger: { trigger: '.hero', start: 'top top', end: 'bottom top', scrub: 1 } });
    gsap.to(heroText, { yPercent: -18, opacity: 0, ease: 'none', scrollTrigger: { trigger: '.hero', start: '30% top', end: 'bottom top', scrub: 1 } });
    gsap.to('.scrollhint', { opacity: 0, scrollTrigger: { trigger: '.hero', start: 'top top', end: '15% top', scrub: true } });

    var heroTitle = q('.hero__title');
    var heroLines = Site.splitLines(heroTitle);
    gsap.set(heroTitle, { opacity: 1 });
    gsap.set(heroLines, { yPercent: 110 });
    Site.onEnter = function () {
      gsap.to(heroLines, { yPercent: 0, duration: 1.6, ease: 'expo.out', stagger: .12, delay: .6 });
    };

    /* ========== Scene 2 · From line to person ========== */
    var docLines = q('.doc__lines'), docPhoto = q('.doc__photo');
    var docText = qa('.doc__text > *');
    Site.prepLines(docLines);
    var docLinePaths = docLines.__paths;
    gsap.set(docPhoto, { opacity: 0, filter: 'grayscale(1) sepia(.18) contrast(1.06) brightness(.96) blur(14px)', scale: 1.06 });
    gsap.set(docText, { opacity: 0, y: 24 });

    function docTimeline() {
      var tl = gsap.timeline({ defaults: { ease: 'none' } });
      tl.to(docLinePaths, { strokeDashoffset: 0, duration: 3, stagger: { amount: 1.2 } }, 0)
        .to(docPhoto, { opacity: 1, duration: 2.2 }, 3.2)
        .to(docPhoto, { filter: 'grayscale(1) sepia(.18) contrast(1.06) brightness(.96) blur(0px)', scale: 1, duration: 2.6 }, 3.2)
        .to(docLines, { opacity: 0, duration: 1.6 }, 4.0)
        .to(docText, { opacity: 1, y: 0, duration: 1.4, stagger: .35, ease: 'power2.out' }, 5.6);
      return tl;
    }
    mm.add(isDesk, function () {
      ST.create({ trigger: '.doc', start: 'top top', end: '+=180%', pin: '.doc__pin', scrub: 1, animation: docTimeline(), anticipatePin: 1 });
    });
    mm.add(isMob, function () {
      ST.create({ trigger: '.doc__frame', start: 'top 80%', end: 'bottom 20%', scrub: 1, animation: docTimeline() });
    });

    /* ========== Scene 3 · Beneath the surface ========== */
    var face = q('.anat__face'), faceLn = q('.anat__ln'), cross = q('.anat__x');
    var steps = qa('.anat__steps li'), close = q('.anat__close');
    Site.prepLines(faceLn);
    var layers = qa('.anat .layer').map(function (g) {
      var paths = qa('path', g);
      paths.forEach(function (p) { var l = p.getTotalLength(); p.__len = l; p.style.strokeDasharray = l + ' ' + l; p.style.strokeDashoffset = l; });
      return paths;
    });
    gsap.set(close, { opacity: 0, y: 20 });
    /* the profile draws itself as the scene arrives, so the pinned shot never opens on an empty frame */
    ST.create({ trigger: '.anat', start: 'top 70%', once: true, onEnter: function () { Site.drawTween(faceLn, { duration: 1.8, amount: .5 }); } });
    function setStep(i) { steps.forEach(function (li, k) { li.classList.toggle('is-active', k === i); }); }

    function anatTimeline() {
      var tl = gsap.timeline({ defaults: { ease: 'none' } });
      tl.to({}, { duration: 1.2 }, 0)
        .to(face, { scale: 3.4, duration: 3, ease: 'power2.in' }, 1.2)
        .to(face, { opacity: 0, duration: 1 }, 3.4)
        .to(cross, { opacity: 1, duration: 1 }, 3.6)
        .to(layers[0], { strokeDashoffset: 0, duration: 1.2, stagger: { amount: .3 } }, 4.0)
        .to(layers[1], { strokeDashoffset: 0, duration: 1.4, stagger: { amount: .9 } }, 5.4)
        .to(layers[2], { strokeDashoffset: 0, duration: 1.4, stagger: { amount: .6 } }, 7.0)
        .to(layers[3], { strokeDashoffset: 0, duration: 1.4, stagger: { amount: .6 } }, 8.6)
        .to(close, { opacity: 1, y: 0, duration: 1, ease: 'power2.out' }, 10.0)
        .to({}, { duration: .8 });
      /* the active caption follows the animation's playhead (not the raw scroll), so text and drawing stay in sync */
      tl.eventCallback('onUpdate', function () { var t = tl.time(); setStep(t < 5.3 ? 0 : t < 6.9 ? 1 : t < 8.5 ? 2 : 3); });
      return tl;
    }
    mm.add(isDesk, function () {
      var tl = anatTimeline();
      ST.create({ trigger: '.anat', start: 'top top', end: '+=320%', pin: '.anat__pin', scrub: 1, animation: tl, anticipatePin: 1 });
    });
    mm.add(isMob, function () {
      var tl = anatTimeline();
      ST.create({ trigger: '.anat', start: 'top top', end: '+=220%', pin: '.anat__pin', scrub: 1, animation: tl });
    });

    /* ========== Scene 6 · Discretion: stillness ========== */
    gsap.set(['.still__it', '.still__en'], { opacity: 0 });
    ST.create({ trigger: '.still', start: 'top 55%', once: true, onEnter: function () {
      gsap.to('.still__it', { opacity: 1, duration: 2.2, ease: 'power1.inOut' });
      gsap.to('.still__en', { opacity: 1, duration: 1.6, ease: 'power1.inOut', delay: 1.4 });
    } });

    /* ========== Scene 7 · Lugano: afternoon to dusk ========== */
    var sky = q('.lugano__sky'), lake = q('.lake');
    var lineEls = qa('.lake .mount, .lake .horizon, .lake .refl');
    var horizon = q('.lake .horizon');
    var hl = horizon.getTotalLength();
    gsap.set(horizon, { strokeDasharray: hl, strokeDashoffset: hl });
    function lakeTimeline() {
      var tl = gsap.timeline({ defaults: { ease: 'none' } });
      tl.to(horizon, { strokeDashoffset: 0, duration: 1.2, ease: 'power2.out' }, 0)
        .fromTo(qa('.lake .mount'), { opacity: 0 }, { opacity: 1, duration: 1 }, .4)
        .fromTo('.lugano__text > *', { opacity: 0, y: 30 }, { opacity: 1, y: 0, duration: 1, stagger: .25, ease: 'power2.out' }, .6)
        .to(sky, { '--dusk': 1, duration: 3 }, 2)
        .to('.lake .sun', { attr: { cy: 430 }, duration: 3 }, 2)
        .to(lineEls, { stroke: '#EDE7DC', duration: 2 }, 3)
        .to('.lugano__text', { color: '#EDE7DC', duration: 2 }, 3)
        .to(qa('.lake .light'), { opacity: 1, duration: .6, stagger: { amount: 1.4, from: 'random' } }, 3.8)
        .to({}, { duration: .6 });
      return tl;
    }
    mm.add(isDesk, function () {
      ST.create({ trigger: '.lugano', start: 'top top', end: '+=170%', pin: '.lugano__pin', scrub: 1, animation: lakeTimeline(), anticipatePin: 1 });
    });
    mm.add(isMob, function () {
      ST.create({ trigger: '.lugano', start: 'top top', end: '+=120%', pin: '.lugano__pin', scrub: 1, animation: lakeTimeline() });
    });

    /* ========== Scene 8 · the horizon becomes the underline ========== */
    var u = q('.u path');
    if (u) {
      var ul = u.getTotalLength();
      gsap.set(u, { strokeDasharray: ul, strokeDashoffset: ul });
      ST.create({ trigger: '.convo__h', start: 'top 75%', once: true, onEnter: function () {
        gsap.to(u, { strokeDashoffset: 0, duration: 1.6, ease: 'power2.inOut', delay: .6 });
      } });
    }
  };
})();
