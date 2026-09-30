/* Light-touch motion: scroll reveals + nav shadow. Skipped if the visitor prefers reduced motion. */
(function () {
  document.documentElement.classList.add('js');
  var els = document.querySelectorAll('.card, .step, .show, .tl, .section-head, .notice, table.cmp, .steps > *, .strip .cells > div, .band .cells > div, .s-in, .hh-photo');
  var nav = document.querySelector('header.topbar');
  function onScroll() { if (nav) nav.classList.toggle('scrolled', window.scrollY > 10); }
  window.addEventListener('scroll', onScroll, { passive: true }); onScroll();
  if (!('IntersectionObserver' in window) || window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    els.forEach(function (e) { e.classList.add('reveal', 'in'); }); return;
  }
  var io = new IntersectionObserver(function (ents) {
    ents.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); (function(t){setTimeout(function(){t.style.transitionDelay=''},1400)})(en.target); } });
  }, { threshold: .12, rootMargin: '0px 0px -40px 0px' });
  els.forEach(function (e, i) {
    e.classList.add('reveal');
    e.style.transitionDelay = ((i % 4) * 90) + 'ms';
    io.observe(e);
  });
})();
