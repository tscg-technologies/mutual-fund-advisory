/**
 * MUTUAL FUND ADVISORY
 * Accessible Accordion Script
 */

document.addEventListener('DOMContentLoaded', () => {
  const accordionButtons = document.querySelectorAll('.accordion-button');

  accordionButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      const item = btn.closest('.accordion-item');
      const collapse = item.querySelector('.accordion-collapse');
      const isExpanded = btn.getAttribute('aria-expanded') === 'true';

      // Close sibling items in the same container
      const container = item.closest('.accordion-container');
      if (container) {
        const siblings = container.querySelectorAll('.accordion-item');
        siblings.forEach(sibling => {
          if (sibling !== item) {
            sibling.classList.remove('active');
            const siblingBtn = sibling.querySelector('.accordion-button');
            const siblingCollapse = sibling.querySelector('.accordion-collapse');
            if (siblingBtn) siblingBtn.setAttribute('aria-expanded', 'false');
            if (siblingCollapse) siblingCollapse.style.maxHeight = null;
          }
        });
      }

      if (!isExpanded) {
        item.classList.add('active');
        btn.setAttribute('aria-expanded', 'true');
        collapse.style.maxHeight = collapse.scrollHeight + 'px';
      } else {
        item.classList.remove('active');
        btn.setAttribute('aria-expanded', 'false');
        collapse.style.maxHeight = null;
      }
    });
  });
});
