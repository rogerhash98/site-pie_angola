const pieMenuToggle = document.getElementById('pie-menu-toggle');
const pieMenuNav = document.getElementById('pie-menu-nav');
const pieMenuSolutionsTrigger = document.getElementById('pie-menu-solutions-trigger');
const pieMegaMenu = document.getElementById('pie-menu-mega');
const pieMenuRoot = document.querySelector('.pie-menu');

if (pieMenuToggle && pieMenuNav) {
  pieMenuToggle.addEventListener('click', () => {
    pieMenuNav.classList.toggle('is-open');
  });
}

if (pieMenuSolutionsTrigger && pieMegaMenu) {
  const isMobile = () => window.matchMedia('(max-width: 900px)').matches;

  const setMegaMenuState = (isOpen) => {
    pieMegaMenu.classList.toggle('is-open', isOpen);
    pieMenuSolutionsTrigger.setAttribute('aria-expanded', String(isOpen));
  };

  const openMegaMenu = () => {
    if (!isMobile()) {
      setMegaMenuState(true);
    }
  };

  const closeMegaMenu = () => {
    if (!isMobile()) {
      setMegaMenuState(false);
    }
  };

  pieMenuSolutionsTrigger.addEventListener('click', (event) => {
    if (isMobile()) {
      event.preventDefault();
      const isOpen = !pieMegaMenu.classList.contains('is-open');
      setMegaMenuState(isOpen);
    }
  });

  pieMenuSolutionsTrigger.addEventListener('mouseenter', openMegaMenu);
  pieMenuSolutionsTrigger.addEventListener('focus', openMegaMenu);
  pieMegaMenu.addEventListener('mouseenter', openMegaMenu);

  if (pieMenuRoot) {
    pieMenuRoot.addEventListener('mouseleave', closeMegaMenu);
  }

  pieMenuRoot?.addEventListener('focusout', (event) => {
    const nextFocused = event.relatedTarget;
    if (!pieMenuRoot.contains(nextFocused)) {
      closeMegaMenu();
    }
  });

  window.addEventListener('resize', () => {
    if (isMobile()) {
      setMegaMenuState(false);
    }
  });
}
