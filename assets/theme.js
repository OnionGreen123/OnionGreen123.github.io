// Apply the preference before styles paint, then bind the accessible header control.
(() => {
  const root = document.documentElement;
  const key = 'shaoyang-theme';
  const system = window.matchMedia('(prefers-color-scheme: dark)');
  const locked = root.dataset.themeLocked;
  const valid = value => value === 'light' || value === 'dark';
  let preference = null;
  let button;
  try {
    const saved = localStorage.getItem(key);
    if (valid(saved)) preference = saved;
  } catch { /* Theme switching still works when storage is unavailable. */ }

  function apply() {
    const theme = locked || preference || (system.matches ? 'dark' : 'light');
    root.dataset.theme = theme;
    const meta = document.querySelector('meta[name="theme-color"]');
    if (meta) meta.content = locked ? '#101719' : theme === 'dark' ? '#171e1b' : '#f8f7f3';
    if (button) {
      const label = theme === 'dark' ? 'Switch to light mode' : 'Switch to dark mode';
      button.setAttribute('aria-label', label);
      button.title = label;
    }
  }
  apply();
  system.addEventListener('change', () => { if (!preference) apply(); });
  window.addEventListener('storage', event => {
    if (event.key === key || event.key === null) {
      preference = valid(event.newValue) ? event.newValue : null;
      apply();
    }
  });
  document.addEventListener('DOMContentLoaded', () => {
    button = document.querySelector('[data-theme-toggle]');
    if (!button || locked) return;
    button.addEventListener('click', () => {
      preference = root.dataset.theme === 'dark' ? 'light' : 'dark';
      try { localStorage.setItem(key, preference); } catch { /* Use in-memory preference. */ }
      apply();
    });
    apply();
    button.hidden = false;
  });
})();
