/**
 * MUTUAL FUND ADVISORY
 * Navigation & Mobile Drawer Script
 */

document.addEventListener('DOMContentLoaded', () => {
  const mobileToggle = document.querySelector('.mobile-toggle');
  const mainNav = document.querySelector('.main-nav');
  let backdrop = document.querySelector('.nav-backdrop');

  if (!backdrop) {
    backdrop = document.createElement('div');
    backdrop.className = 'nav-backdrop';
    document.body.appendChild(backdrop);
  }

  function toggleMobileNav() {
    const isOpen = mainNav.classList.contains('is-open');
    if (isOpen) {
      closeMobileNav();
    } else {
      openMobileNav();
    }
  }

  function openMobileNav() {
    mainNav.classList.add('is-open');
    backdrop.classList.add('is-open');
    document.body.style.overflow = 'hidden';
    mobileToggle.setAttribute('aria-expanded', 'true');
  }

  function closeMobileNav() {
    mainNav.classList.remove('is-open');
    backdrop.classList.remove('is-open');
    document.body.style.overflow = '';
    mobileToggle.setAttribute('aria-expanded', 'false');
  }

  if (mobileToggle) {
    mobileToggle.addEventListener('click', toggleMobileNav);
  }

  if (backdrop) {
    backdrop.addEventListener('click', closeMobileNav);
  }

  // Mobile Dropdown toggles
  const navItemsWithDropdown = document.querySelectorAll('.nav-item.has-dropdown');
  navItemsWithDropdown.forEach(item => {
    const link = item.querySelector('.nav-link');
    if (link) {
      link.addEventListener('click', (e) => {
        if (window.innerWidth <= 768) {
          e.preventDefault();
          const wasOpen = item.classList.contains('is-dropdown-open');
          navItemsWithDropdown.forEach(otherItem => {
            if (otherItem !== item) otherItem.classList.remove('is-dropdown-open');
          });
          if (!wasOpen) {
            item.classList.add('is-dropdown-open');
          } else {
            item.classList.remove('is-dropdown-open');
          }
        }
      });
    }
  });

  // Close menus on Escape key
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
      closeMobileNav();
      navItemsWithDropdown.forEach(item => item.classList.remove('is-dropdown-open'));
    }
  });
});
