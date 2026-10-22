(function () {
  document.documentElement.classList.add('js');
  // Mobile nav
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.querySelector('.nav');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var open = nav.classList.toggle('is-open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
      toggle.setAttribute('aria-label', open ? 'Fechar menu' : 'Abrir menu');
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && nav.classList.contains('is-open')) {
        nav.classList.remove('is-open');
        toggle.setAttribute('aria-expanded', 'false');
        toggle.setAttribute('aria-label', 'Abrir menu');
        toggle.focus();
      }
    });
  }

  // Integração 360X: novas páginas em todos os HTML já publicados.
  function ensureNavLink(href, label, afterHref) {
    if (!nav || nav.querySelector('a[href="' + href + '"]')) return;
    var link = document.createElement('a');
    link.href = href;
    link.textContent = label;
    if (document.body.getAttribute('data-page') === href.replace('./', '').replace('.html', '')) {
      link.setAttribute('aria-current', 'page');
    }
    var anchor = nav.querySelector('a[href="' + afterHref + '"]');
    if (anchor && anchor.nextSibling) nav.insertBefore(link, anchor.nextSibling);
    else if (anchor) nav.appendChild(link);
    else nav.appendChild(link);
  }
  ensureNavLink('./cenario-atual.html', 'Cenário 2026', './index.html');
  ensureNavLink('./agentes.html', 'Agentes 360', './cenario-atual.html');

  document.querySelectorAll('.edition-number').forEach(function (el) {
    el.innerHTML = 'TURBO TEMI 360X<br>EDIÇÃO 22.10.2026';
  });
  document.querySelectorAll('.footer .xs').forEach(function (el) {
    if (el.textContent.indexOf('Edição de 18 de outubro de 2026') !== -1) {
      el.textContent = el.textContent.replace('Edição de 18 de outubro de 2026', 'Edição revisada em 22 de outubro de 2026');
    }
  });

  var footerLists = document.querySelectorAll('.footer ul');
  if (footerLists.length) {
    var footerAxis = footerLists[0];
    function footerLink(href, label) {
      if (footerAxis.querySelector('a[href="' + href + '"]')) return;
      var li = document.createElement('li');
      var a = document.createElement('a');
      a.href = href;
      a.textContent = label;
      li.appendChild(a);
      footerAxis.insertBefore(li, footerAxis.firstChild);
    }
    footerLink('./agentes.html', 'Arquitetura de agentes 360');
    footerLink('./cenario-atual.html', 'Cenário atual 2026');
  }

  if (document.body.getAttribute('data-page') === 'index' && !document.getElementById('cenario-2026-home')) {
    var focus = document.getElementById('em-foco');
    var section = document.createElement('section');
    section.className = 'section section--offset';
    section.id = 'cenario-2026-home';
    section.innerHTML = '<div class="wrap"><div class="section-heading"><div><span class="kicker">Atualização nacional · 22.10.2026</span><h2 class="title">47,4 milhões de evangélicos. Nenhuma licença para opacidade.</h2></div><a class="section-link" href="./cenario-atual.html">Abrir o cenário atual ↗</a></div><div class="route-grid"><a class="route" href="./cenario-atual.html"><span class="route__number">CENÁRIO 2026</span><h3>Dimensão, regras e lacunas.</h3><p>Demografia do IBGE, regime jurídico, imunidade tributária, riscos de governança e prioridades de auditoria.</p><span>Ler a síntese documental →</span></a><a class="route" href="./agentes.html"><span class="route__number">AGENTES 360</span><h3>Investigar sem perseguir.</h3><p>Quatorze agentes para catalogar entidades, seguir dinheiro, medir impacto, garantir contraditório e revisar evidências.</p><span>Conhecer a arquitetura →</span></a><div class="route"><span class="route__number">REGRA CENTRAL</span><h3>O setor não é uma pessoa jurídica única.</h3><p>Cada CNPJ, dirigente, processo, exercício, valor e resposta institucional precisa ser analisado separadamente.</p><span>Evidência antes da acusação.</span></div><div class="route"><span class="route__number">DADO OFICIAL</span><h3>47.418.024 pessoas.</h3><p>População evangélica de 10 anos ou mais no Panorama do Censo 2022. Demografia não é auditoria financeira.</p><span>Fonte: IBGE.</span></div></div></div>';
    if (focus && focus.parentNode) focus.parentNode.insertBefore(section, focus);
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
    var search = group.querySelector('[data-search]');
    var activeTag = 'all';
    var empty = document.createElement('p');
    empty.className = 'empty-result';
    empty.textContent = 'Nenhum resultado. Tente outro termo ou selecione Todos.';
    empty.hidden = true;
    group.insertAdjacentElement('afterend', empty);
    if (count) { count.setAttribute('role', 'status'); count.setAttribute('aria-live', 'polite'); }
    function normalize(value) {
      return value.normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase();
    }
    function apply(tag) {
      activeTag = tag;
      var query = normalize(search ? search.value.trim() : '');
      var n = 0;
      items.forEach(function (it) {
        var tags = (it.getAttribute('data-tags') || '').split(/\s+/);
        var show = (tag === 'all' || tags.indexOf(tag) !== -1) && normalize(it.textContent).indexOf(query) !== -1;
        it.classList.toggle('is-hidden', !show);
        it.hidden = !show;
        if (show) n++;
      });
      if (count) count.textContent = n + ' de ' + items.length;
      empty.hidden = n !== 0;
    }
    if (search) search.addEventListener('input', function () { apply(activeTag); });
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
      // US$1 = R$5 hipotético; custo por morte evitada US$3.500–5.500 => R$17.500–27.500
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
  // Progresso de leitura: sem animação ou coleta de dados.
  var progress = document.querySelector('.reading-progress span');
  if (progress) {
    var scheduled = false;
    function updateProgress() {
      var max = document.documentElement.scrollHeight - window.innerHeight;
      progress.style.width = (max > 0 ? Math.min(100, window.scrollY / max * 100) : 0) + '%';
      scheduled = false;
    }
    window.addEventListener('scroll', function () {
      if (!scheduled) { scheduled = true; window.requestAnimationFrame(updateProgress); }
    }, { passive: true });
    window.addEventListener('resize', updateProgress);
    updateProgress();
  }
})();
