/* Home — "Luce naturale": the patient's story, told with light.
   1 Light  2 Naturalezza (soft focus → clarity)  3 Where to begin  4 Journey
   5 Experience  6 Discretion  7 A window on Lugano  8 Conversation */
(function () {
  'use strict';
  var Site = (window.Site = window.Site || {});

  Site.initHome = function () {
    var gsap = window.gsap, ST = window.ScrollTrigger, q = Site.q, qa = Site.qa, reduce = Site.reduce;
    var SOFT = 'expo.out';
    var mm = gsap.matchMedia();

    /* ===== 1 · Light: the arch opens, the words rise, the light settles ===== */
    var arch = q('.hero [data-arch]'), lines = qa('.hero__title .hl > span'), ins = qa('[data-hero-in]');
    if (!reduce) {
      gsap.set(q('.arch__in', arch), { clipPath: 'inset(100% 0% 0% 0%)' });
      gsap.set(lines, { yPercent: 110 });
      gsap.set(ins, { opacity: 0, y: 20, filter: 'blur(8px)' });
      var intro = Site.archTimeline(arch);
      gsap.timeline({ delay: .45 })
        .add(function () { intro.play(); }, 0)
        .to(lines, { yPercent: 0, duration: 1.6, ease: SOFT, stagger: .14 }, .35)
        .to(ins, { opacity: 1, y: 0, filter: 'blur(0px)', duration: 1.4, ease: SOFT, stagger: .12 }, .9);
      gsap.to('.hero__media', { yPercent: -8, ease: 'none', scrollTrigger: { trigger: '.hero', start: 'top top', end: 'bottom top', scrub: 1 } });
      gsap.to('.hero__text', { yPercent: -16, opacity: .2, ease: 'none', scrollTrigger: { trigger: '.hero', start: '30% top', end: 'bottom top', scrub: 1 } });
    }
    if (reduce) return;

    /* ===== 2 · Naturalezza: the word comes into focus — like a natural result ===== */
    (function () {
      var word = q('.nat__word'), light = q('.nat__light'), never = qa('.nat__never li'), head = qa('.nat__label, .nat__lead'), sign = q('.nat__sign');
      gsap.set(word, { opacity: .18, filter: 'blur(26px)', scale: .9, letterSpacing: '.12em' });
      gsap.set(light, { scale: .55, opacity: .5 });
      var linen = q('.nat__photo img'); gsap.set(linen, { filter: 'blur(18px)', scale: 1.12 });
      gsap.set(never, { opacity: 0, y: 24, filter: 'blur(8px)' });
      gsap.set([head, sign], { opacity: 0, y: 16 });
      function build() {
        var tl = gsap.timeline({ defaults: { ease: 'none' } });
        tl.to(head, { opacity: 1, y: 0, duration: .5, stagger: .15 }, 0)
          .to(light, { scale: 1.1, opacity: 1, duration: 2.2 }, 0)
          .to(linen, { filter: 'blur(3px)', scale: 1, duration: 2.4 }, 0)
          .to(word, { opacity: 1, filter: 'blur(0px)', scale: 1, letterSpacing: '-.02em', duration: 1.8, ease: 'power2.out' }, .2)
          .to(never, { opacity: 1, y: 0, filter: 'blur(0px)', duration: .6, stagger: .45, ease: 'power2.out' }, 1.6)
          .to(sign, { opacity: 1, y: 0, duration: .5 }, 3.1)
          .to({}, { duration: .5 });
        return tl;
      }
      mm.add('(min-width: 901px)', function () { ST.create({ trigger: '.nat', start: 'top top', end: '+=150%', pin: '.nat__pin', scrub: 1, animation: build(), anticipatePin: 1 }); });
      mm.add('(max-width: 900px)', function () { ST.create({ trigger: '.nat', start: 'top 75%', end: 'bottom 70%', scrub: 1, animation: build() }); });
    })();

    /* ===== 7 · Lugano — a day on the lake: the arch opens, morning mist turns into dusk ===== */
    (function () {
      var win = q('[data-lake-window]'), mist = q('.lg__mist img'), duskL = q('.lg__dusk'), dusk = q('.lg__dusk img');
      var fog = q('.lg__fog'), glint = q('.lg__glint'), h = q('.lg__h'), txt = qa('.lg__text > :not(.lg__h)');
      var clock = q('[data-lg-time]'), am = q('[data-tod="am"]'), pm = q('[data-tod="pm"]'), o = { m: 7 * 60 };
      gsap.set(h, { opacity: 0, yPercent: 30, letterSpacing: '.1em' }); gsap.set(txt, { opacity: 0, y: 16 });
      function hhmm(v) { var hh = Math.floor(v / 60), mm2 = Math.round(v % 60 / 5) * 5; if (mm2 === 60) { hh++; mm2 = 0; } return (hh < 10 ? '0' : '') + hh + ':' + (mm2 < 10 ? '0' : '') + mm2; }
      function build() {
        return gsap.timeline({ defaults: { ease: 'none' } })
          .fromTo(win, { scale: .52, y: 40 }, { scale: 1, y: 0, duration: 2, ease: 'power2.out' }, 0)
          .fromTo(mist, { scale: 1.25 }, { scale: 1.06, duration: 3 }, 0)
          .to(h, { opacity: 1, yPercent: 0, letterSpacing: '-.02em', duration: 1.4, ease: 'power2.out' }, .7)
          .to(txt, { opacity: 1, y: 0, duration: .7, stagger: .2 }, 1.3)
          /* morning → evening */
          .to(o, { m: 19 * 60 + 30, duration: 3, onUpdate: function () { clock.textContent = hhmm(o.m); } }, 2.4)
          .to(duskL, { opacity: 1, duration: 2.2 }, 3)
          .fromTo(dusk, { scale: 1.14 }, { scale: 1, duration: 3 }, 2.6)
          .to(fog, { opacity: 0, duration: 1.6 }, 3.2)
          .to(glint, { opacity: .7, duration: 1.6 }, 3.6)
          .to(am, { opacity: 0, duration: .4 }, 3.9).to(pm, { opacity: 1, duration: .4 }, 4.1)
          .to({}, { duration: .6 });
      }
      mm.add('(min-width: 901px)', function () { ST.create({ trigger: '.lg', start: 'top top', end: '+=190%', pin: '.lg__pin', scrub: 1, animation: build(), anticipatePin: 1 }); });
      mm.add('(max-width: 900px)', function () { ST.create({ trigger: '.lg', start: 'top top', end: '+=120%', pin: '.lg__pin', scrub: 1, animation: build() }); });
    })();

    /* ===== 8 · Conversation: the arch monogram glows in ===== */
    (function () {
      var mono = q('.cv__mono');
      gsap.set(mono, { opacity: 0, scale: .85, filter: 'blur(10px)' });
      ST.create({ trigger: '.cv', start: 'top 70%', once: true, onEnter: function () { gsap.to(mono, { opacity: 1, scale: 1, filter: 'blur(0px)', duration: 1.6, ease: SOFT }); } });
    })();
  };
})();
