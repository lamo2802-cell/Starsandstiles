/* Scroll reveal for demo sites. Skipped for visitors who prefer reduced motion. */
(function(){
  var els=document.querySelectorAll('.rv'); if(!els.length) return;
  if(!('IntersectionObserver' in window)||matchMedia('(prefers-reduced-motion: reduce)').matches){els.forEach(function(e){e.classList.add('in')});return}
  document.documentElement.classList.add('fx');
  var io=new IntersectionObserver(function(a){a.forEach(function(x){if(x.isIntersecting){x.target.classList.add('in');io.unobserve(x.target)}})},{threshold:.12});
  els.forEach(function(e,i){e.style.transitionDelay=((i%3)*90)+'ms';io.observe(e)});
})();
