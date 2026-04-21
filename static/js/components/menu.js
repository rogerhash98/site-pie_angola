(function () {
  const root = document.querySelector('.pie-menu');
  if (!root) {
    return;
  }

  const mobileBreakpoint = window.matchMedia('(max-width: 900px)');
  const toggle = root.querySelector('#pie-menu-toggle');
  const accent = root.querySelector('#pie-menu-accent');
  const dropdowns = Array.from(root.querySelectorAll('.pie-menu__dropdown'));
  const megas = {
    produtos: root.querySelector('#mega-produtos'),
    sobre: root.querySelector('#mega-sobre'),
  };
  const mobileMenu = root.querySelector('#pie-mmenu');
  const mobileClose = root.querySelector('#pie-mmenu-close');
  const mobileGroups = Array.from(root.querySelectorAll('.pie-mmenu__nav > .pie-mmenu__group'));
  const mobileSubgroups = Array.from(root.querySelectorAll('.pie-mmenu__group--sub'));
  const mobileLinks = Array.from(root.querySelectorAll('.pie-mmenu a'));
  let openDesktopKey = null;
  let previousBodyOverflow = '';

  function isMobileViewport() {
    return mobileBreakpoint.matches;
  }

  function closeDesktopMenu() {
    Object.values(megas).forEach((menu) => {
      if (menu) {
        menu.hidden = true;
      }
    });

    dropdowns.forEach((dropdown) => {
      const button = dropdown.querySelector('button');
      if (button) {
        button.setAttribute('aria-expanded', 'false');
      }
      dropdown.classList.remove('is-open');
    });

    if (accent) {
      accent.style.opacity = '0';
    }

    openDesktopKey = null;
  }

  function positionAccent(button) {
    if (!accent || !button) {
      return;
    }

    const buttonRect = button.getBoundingClientRect();
    const header = root.querySelector('.pie-menu__bar');
    if (!header) {
      return;
    }

    const headerRect = header.getBoundingClientRect();
    accent.style.left = buttonRect.left + 'px';
    accent.style.width = buttonRect.width + 'px';
    accent.style.top = headerRect.bottom - 6 + 'px';
    accent.style.opacity = '1';
  }

  dropdowns.forEach((dropdown) => {
    const button = dropdown.querySelector('button');
    const key = dropdown.dataset.dropdown;
    if (!button || !key || !megas[key]) {
      return;
    }

    button.addEventListener('click', (event) => {
      if (isMobileViewport()) {
        return;
      }

      event.stopPropagation();
      if (openDesktopKey === key) {
        closeDesktopMenu();
        return;
      }

      closeDesktopMenu();
      openDesktopKey = key;
      megas[key].hidden = false;
      button.setAttribute('aria-expanded', 'true');
      dropdown.classList.add('is-open');
      positionAccent(button);
    });
  });

  document.addEventListener('click', (event) => {
    if (!openDesktopKey || isMobileViewport()) {
      return;
    }

    if (event.target.closest('.pie-mega') || event.target.closest('.pie-menu__dropdown')) {
      return;
    }

    closeDesktopMenu();
  });

  function syncDisclosureState(details) {
    const summary = details.querySelector(':scope > summary');
    if (summary) {
      summary.setAttribute('aria-expanded', details.open ? 'true' : 'false');
    }
  }

  function closeNestedGroups(parentGroup) {
    parentGroup.querySelectorAll('.pie-mmenu__group--sub').forEach((group) => {
      group.open = false;
      syncDisclosureState(group);
    });
  }

  function bindExclusiveAccordion(groups, onClose) {
    groups.forEach((group) => {
      syncDisclosureState(group);
      group.addEventListener('toggle', () => {
        syncDisclosureState(group);

        if (!group.open) {
          if (onClose) {
            onClose(group);
          }
          return;
        }

        groups.forEach((otherGroup) => {
          if (otherGroup !== group && otherGroup.open) {
            otherGroup.open = false;
            syncDisclosureState(otherGroup);
            if (onClose) {
              onClose(otherGroup);
            }
          }
        });
      });
    });
  }

  bindExclusiveAccordion(mobileGroups);
  bindExclusiveAccordion(mobileSubgroups);

  function openMobileMenu() {
    if (!mobileMenu || !isMobileViewport()) {
      return;
    }

    closeDesktopMenu();
    previousBodyOverflow = document.body.style.overflow;
    mobileMenu.hidden = false;
    mobileMenu.classList.add('is-open');
    mobileMenu.setAttribute('aria-hidden', 'false');
    if (toggle) {
      toggle.setAttribute('aria-expanded', 'true');
    }

    document.body.style.overflow = 'hidden';
  }

  function closeMobileMenu() {
    if (!mobileMenu || mobileMenu.hidden) {
      return;
    }

    mobileMenu.classList.remove('is-open');
    mobileMenu.hidden = true;
    mobileMenu.setAttribute('aria-hidden', 'true');
    if (toggle) {
      toggle.setAttribute('aria-expanded', 'false');
    }
    document.body.style.overflow = previousBodyOverflow;
  }

  if (toggle) {
    toggle.addEventListener('click', () => {
      if (mobileMenu && !mobileMenu.hidden) {
        closeMobileMenu();
        return;
      }

      openMobileMenu();
    });
  }

  if (mobileClose) {
    mobileClose.addEventListener('click', closeMobileMenu);
  }

  if (mobileMenu) {
    mobileMenu.addEventListener('click', (event) => {
      if (event.target === mobileMenu) {
        closeMobileMenu();
      }
    });
  }

  mobileLinks.forEach((link) => {
    link.addEventListener('click', closeMobileMenu);
  });

  document.addEventListener('keydown', (event) => {
    if (event.key !== 'Escape') {
      return;
    }

    closeDesktopMenu();
    closeMobileMenu();
  });

  window.addEventListener('resize', () => {
    if (openDesktopKey && !isMobileViewport()) {
      const activeDropdown = dropdowns.find((dropdown) => dropdown.dataset.dropdown === openDesktopKey);
      const activeButton = activeDropdown && activeDropdown.querySelector('button');
      if (activeButton) {
        positionAccent(activeButton);
      }
      return;
    }

    closeDesktopMenu();
  });

  mobileBreakpoint.addEventListener('change', () => {
    closeDesktopMenu();
    if (!isMobileViewport()) {
      closeMobileMenu();
    }
  });
})();
