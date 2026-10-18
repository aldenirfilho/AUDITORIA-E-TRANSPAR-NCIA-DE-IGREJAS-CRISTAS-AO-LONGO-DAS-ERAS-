(function () {
  // Mobile nav
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.querySelector('.nav');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var open = nav.classList.toggle('is-open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  }

  // Reveal on scroll
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
      });
    }, { rootMargin: '0px 0px -8% 0px' });
    document.querySelectorAll('.reveal').forEach(function (el) { io.observe(el); });
  } else {
    document.querySelectorAll('.reveal').forEach(function (el) { el.classList.add('in'); });
  }

  // Filters (data-filter-group on container; chips with data-filter; items with data-tags)
  document.querySelectorAll('[data-filter-group]').forEach(function (group) {
    var chips = group.querySelectorAll('.chip');
    var targetSel = group.getAttribute('data-filter-group');
    var items = document.querySelectorAll(targetSel);
    var count = group.querySelector('.filters__count');
    function apply(tag) {
      var n = 0;
      items.forEach(function (it) {
        var tags = (it.getAttribute('data-tags') || '').split(/\s+/);
        var show = tag === 'all' || tags.indexOf(tag) !== -1;
        it.classList.toggle('is-hidden', !show);
        if (show) n++;
      });
      if (count) count.textContent = n + ' de ' + items.length;
    }
    chips.forEach(function (c) {
      c.addEventListener('click', function () {
        chips.forEach(function (x) { x.setAttribute('aria-pressed', 'false'); });
        c.setAttribute('aria-pressed', 'true');
        apply(c.getAttribute('data-filter'));
      });
    });
    apply('all');
  });

  // Calculator (impacto.html)
  var calc = document.querySelector('[data-calc]');
  if (calc) {
    var range = calc.querySelector('#calc-budget');
    var budgetOut = calc.querySelector('#calc-budget-out');
    var livesOut = calc.querySelector('#calc-lives');
    var haOut = calc.querySelector('#calc-ha');
    var splitOut = calc.querySelector('#calc-split');
    var mode = 'health';
    var fmtBRL = function (v) { return 'R$ ' + v.toLocaleString('pt-BR'); };
    var fmtInt = function (v) { return Math.round(v).toLocaleString('pt-BR'); };
    function update() {
      var steps = [1e6, 2e6, 5e6, 1e7, 2e7, 5e7, 1e8, 2e8, 5e8];
      var budget = steps[parseInt(range.value, 10)];
      budgetOut.textContent = fmtBRL(budget);
      // US$1 = R$5 hypothetical; cost per death averted US$3,500–5,500 => R$17,500–27,500
      var lo = budget / 27500, hi = budget / 17500;
      var ha = budget / 19000;
      if (mode === 'health') {
        livesOut.textContent = '≈ ' + fmtInt(lo) + '–' + fmtInt(hi);
        haOut.textContent = '—';
        splitOut.textContent = '100% saúde · 0% restauração';
      } else if (mode === 'env') {
        livesOut.textContent = '—';
        haOut.textContent = '≈ ' + fmtInt(ha);
        splitOut.textContent = '0% saúde · 100% restauração';
      } else {
        livesOut.textContent = '≈ ' + fmtInt(lo * 0.7) + '–' + fmtInt(hi * 0.7);
        haOut.textContent = '≈ ' + fmtInt(ha * 0.2);
        splitOut.textContent = '70% saúde · 20% restauração · 10% educação/assistência';
      }
    }
    range.addEventListener('input', update);
    calc.querySelectorAll('.seg button').forEach(function (b) {
      b.addEventListener('click', function () {
        calc.querySelectorAll('.seg button').forEach(function (x) { x.setAttribute('aria-pressed', 'false'); });
        b.setAttribute('aria-pressed', 'true');
        mode = b.getAttribute('data-mode');
        update();
      });
    });
    update();
  }

  // Copy helper for request model
  document.querySelectorAll('[data-copy]').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var src = document.querySelector(btn.getAttribute('data-copy'));
      if (!src) return;
      var txt = src.textContent;
      var done = function () { btn.textContent = 'Copiado'; setTimeout(function () { btn.textContent = 'Copiar texto'; }, 1800); };
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(txt).then(done, function () { selectText(src); });
      } else { selectText(src); }
    });
  });
  function selectText(el) {
    var r = document.createRange(); r.selectNodeContents(el);
    var s = window.getSelection(); s.removeAllRanges(); s.addRange(r);
  }
})();
