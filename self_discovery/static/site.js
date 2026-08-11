document.addEventListener('DOMContentLoaded', () => {
  document.body.classList.add('page-ready');

  const overlay = document.createElement('div');
  overlay.className = 'page-transition-overlay';
  document.body.appendChild(overlay);

  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add('show');
      }
    });
  }, { threshold: 0.12 });

  document.querySelectorAll('.reveal').forEach((el) => observer.observe(el));

  const goWithTransition = (url) => {
    if (!url) return;
    document.body.classList.add('page-exit');
    window.setTimeout(() => {
      window.location.href = url;
    }, 360);
  };

  document.querySelectorAll('a[data-transition]').forEach((link) => {
    link.addEventListener('click', (event) => {
      const href = link.getAttribute('href');
      if (!href || href.startsWith('#') || href.startsWith('mailto:') || href.startsWith('tel:')) {
        return;
      }

      const isInternal = href.startsWith('/') || href.startsWith(window.location.origin);
      if (!isInternal) return;

      event.preventDefault();
      goWithTransition(href);
    });
  });

  document.querySelectorAll('[data-go]').forEach((button) => {
    button.addEventListener('click', () => {
      goWithTransition(button.getAttribute('data-go'));
    });
  });
});
