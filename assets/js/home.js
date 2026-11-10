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
      gsap.set(never, { opacity: 0, y: 24, filter: 'blur(8px)' });
      gsap.set([head, sign], { opacity: 0, y: 16 });
      function build() {
        var tl = gsap.timeline({ defaults: { ease: 'none' } });
        tl.to(head, { opacity: 1, y: 0, duration: .5, stagger: .15 }, 0)
          .to(light, { scale: 1.1, opacity: 1, duration: 2.2 }, 0)
          .to(word, { opacity: 1, filter: 'blur(0px)', scale: 1, letterSpacing: '-.02em', duration: 1.8, ease: 'power2.out' }, .2)
          .to(never, { opacity: 1, y: 0, filter: 'blur(0px)', duration: .6, stagger: .45, ease: 'power2.out' }, 1.6)
          .to(sign, { opacity: 1, y: 0, duration: .5 }, 3.1)
          .to({}, { duration: .5 });
        return tl;
      }
      mm.add('(min-width: 901px)', function () { ST.create({ trigger: '.nat', start: 'top top', end: '+=150%', pin: '.nat__pin', scrub: 1, animation: build(), anticipatePin: 1 }); });
      mm.add('(max-width: 900px)', function () { ST.create({ trigger: '.nat', start: 'top 75%', end: 'bottom 70%', scrub: 1, animation: build() }); });
    })();

    /* ===== 7 · A window on Lugano: the arch opens onto the lake ===== */
    (function () {
      var win = q('[data-lake-window]'), h = q('.lg__h'), txt = qa('.lg__text > :not(.lg__h)');
      gsap.set(h, { opacity: 0, yPercent: 30, letterSpacing: '.1em' }); gsap.set(txt, { opacity: 0, y: 16 });
      function build() {
        return gsap.timeline({ defaults: { ease: 'none' } })
          .fromTo(win, { scale: .52, y: 40 }, { scale: 1, y: 0, duration: 2, ease: 'power2.out' }, 0)
          .to(h, { opacity: 1, yPercent: 0, letterSpacing: '-.02em', duration: 1.4, ease: 'power2.out' }, .7)
          .to(txt, { opacity: 1, y: 0, duration: .7, stagger: .2 }, 1.3)
          .to({}, { duration: .5 });
      }
      mm.add('(min-width: 901px)', function () { ST.create({ trigger: '.lg', start: 'top top', end: '+=110%', pin: '.lg__pin', scrub: 1, animation: build(), anticipatePin: 1 }); });
      mm.add('(max-width: 900px)', function () { ST.create({ trigger: '.lg', start: 'top 80%', end: 'top 10%', scrub: 1, animation: build() }); });
    })();

    /* ===== 8 · Conversation: the arch monogram glows in ===== */
    (function () {
      var mono = q('.cv__mono');
      gsap.set(mono, { opacity: 0, scale: .85, filter: 'blur(10px)' });
      ST.create({ trigger: '.cv', start: 'top 70%', once: true, onEnter: function () { gsap.to(mono, { opacity: 1, scale: 1, filter: 'blur(0px)', duration: 1.6, ease: SOFT }); } });
    })();
  };
})();
