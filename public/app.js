(() => {
  document.documentElement.classList.add('js');
  const menu = document.querySelector('.menu-toggle');
  const nav = document.querySelector('#site-nav');
  menu.hidden = false;
  function closeMenu() { nav.classList.remove('open'); menu.setAttribute('aria-expanded', 'false'); }
  menu.addEventListener('click', () => {
    const open = nav.classList.toggle('open');
    menu.setAttribute('aria-expanded', String(open));
  });
  nav.addEventListener('click', event => { if (event.target.closest('a')) closeMenu(); });
  document.addEventListener('keydown', event => {
    if (event.key === 'Escape' && nav.classList.contains('open')) { closeMenu(); menu.focus(); }
  });
  const buttons = [...document.querySelectorAll('[data-filter]')];
  const topics = [...document.querySelectorAll('[data-topic]')];
  const status = document.querySelector('.filter-status');
  document.querySelector('.filter-bar').hidden = false;
  function filter(key) {
    topics.forEach(topic => { topic.hidden = key !== 'all' && topic.dataset.topic !== key; });
    buttons.forEach(button => button.setAttribute('aria-pressed', String(button.dataset.filter === key)));
    const visible = topics.filter(topic => !topic.hidden);
    const count = visible.reduce((total, topic) => total + topic.querySelectorAll('blockquote').length, 0);
    status.textContent = (key === 'all' ? 'All 5 themes' : visible[0].querySelector('h3').textContent) + ' · ' + count + ' accounts';
  }
  buttons.forEach(button => button.addEventListener('click', () => { filter(button.dataset.filter); }));
  function revealHash() {
    const target = topics.find(topic => '#' + topic.id === window.location.hash);
    if (target) { filter(target.dataset.topic); requestAnimationFrame(() => target.scrollIntoView({block:'start'})); }
  }
  document.addEventListener('click', event => {
    const link = event.target.closest('a[href^="#"]');
    if (!link) return;
    const target = topics.find(topic => '#' + topic.id === link.getAttribute('href'));
    if (target) filter(target.dataset.topic);
  });
  window.addEventListener('hashchange', revealHash);
  revealHash();
})();
