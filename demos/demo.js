/* Demo booking widget: availability calendar + instant quote. Fictional data only. */
(function () {
  var el = document.getElementById('book');
  if (!el) return;
  var rate = +el.dataset.rate, clean = +el.dataset.clean, min = +el.dataset.min || 2;
  var today = new Date(); today.setHours(0, 0, 0, 0);
  var start = null, end = null, view = new Date(today.getFullYear(), today.getMonth(), 1);
  var cal = el.querySelector('.cal'), out = el.querySelector('.quote');
  var mn = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];

  // Pretend some 3-night blocks are already booked (deterministic, no real data)
  function booked(d) {
    if (d < today) return true;
    var k = Math.floor(Math.round(d.getTime() / 864e5) / 3);
    var s = Math.sin(k * 78.233) * 43758.5453;
    return (s - Math.floor(s)) > 0.7;
  }
  function fmt(d) { return d.toLocaleDateString('en-GB', { day: 'numeric', month: 'short', year: 'numeric' }); }
  function gbp(n) { return '£' + n.toLocaleString('en-GB'); }

  function draw() {
    var h = '';
    for (var m = 0; m < 2; m++) {
      var f = new Date(view.getFullYear(), view.getMonth() + m, 1);
      var days = new Date(f.getFullYear(), f.getMonth() + 1, 0).getDate();
      var off = (f.getDay() + 6) % 7;
      h += '<div class="month"><div class="mh">' + mn[f.getMonth()] + ' ' + f.getFullYear() + '</div>' +
        '<div class="dow"><i>M</i><i>T</i><i>W</i><i>T</i><i>F</i><i>S</i><i>S</i></div><div class="days">';
      for (var i = 0; i < off; i++) h += '<span></span>';
      for (var d = 1; d <= days; d++) {
        var dt = new Date(f.getFullYear(), f.getMonth(), d), b = booked(dt), c = 'd';
        if (b) c += ' b';
        if (start && +dt === +start) c += ' sel';
        if (end && +dt === +end) c += ' sel';
        if (start && end && dt > start && dt < end) c += ' rng';
        h += '<button type="button" class="' + c + '"' + (b ? ' disabled' : '') + ' data-t="' + dt.getTime() + '">' + d + '</button>';
      }
      h += '</div></div>';
    }
    cal.innerHTML = '<div class="nav"><button type="button" data-a="-1" aria-label="Previous month">&larr;</button>' +
      '<button type="button" data-a="1" aria-label="Next month">&rarr;</button></div><div class="months">' + h + '</div>';
  }

  function quote() {
    if (!start || !end) { out.innerHTML = '<p class="hint">Choose your arrival and departure dates.</p>'; return; }
    var n = Math.round((end - start) / 864e5);
    for (var t = new Date(start); t < end; t.setDate(t.getDate() + 1)) {
      if (booked(t)) { out.innerHTML = '<p class="hint">Those dates include a night that is already booked. Please pick another range.</p>'; return; }
    }
    if (n < min) { out.innerHTML = '<p class="hint">Minimum stay is ' + min + ' nights.</p>'; return; }
    var stay = n * rate, total = stay + clean, dep = Math.round(total * 0.25);
    out.innerHTML =
      '<div class="row"><span>' + fmt(start) + ' &rarr; ' + fmt(end) + '</span><span>' + n + ' nights</span></div>' +
      '<div class="row"><span>' + n + ' &times; ' + gbp(rate) + '</span><span>' + gbp(stay) + '</span></div>' +
      '<div class="row"><span>Cleaning fee</span><span>' + gbp(clean) + '</span></div>' +
      '<div class="row tot"><span>Total price</span><span>' + gbp(total) + '</span></div>' +
      '<div class="row sm"><span>Deposit today (25%)</span><span>' + gbp(dep) + '</span></div>' +
      '<button type="button" class="reserve">Reserve (demo)</button>';
    out.querySelector('.reserve').onclick = function () {
      alert('This is an example site for a fictional property, so no booking is made. On a real Stars & Stiles site, this button takes a secure card payment.');
    };
  }

  cal.addEventListener('click', function (e) {
    var b = e.target.closest('button'); if (!b) return;
    if (b.dataset.a) {
      view = new Date(view.getFullYear(), view.getMonth() + (+b.dataset.a), 1);
      var first = new Date(today.getFullYear(), today.getMonth(), 1);
      if (view < first) view = first;
      draw(); return;
    }
    var t = new Date(+b.dataset.t);
    if (!start || (start && end)) { start = t; end = null; }
    else if (t > start) { end = t; }
    else { start = t; }
    draw(); quote();
  });
  draw(); quote();
})();
