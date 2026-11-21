/**
 * MUTUAL FUND ADVISORY
 * Form Validation & Client Consultation Enquiry (Vanilla JS)
 */

document.addEventListener('DOMContentLoaded', () => {
  const consultForm = document.getElementById('consultationForm');
  const consultSuccessAlert = document.getElementById('consultSuccessAlert');
  const contactForm = document.getElementById('contactForm');
  const contactSuccessAlert = document.getElementById('contactSuccessAlert');

  function validateEmail(email) {
    return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
  }

  function validatePhone(phone) {
    const cleaned = phone.replace(/[\s-]/g, '');
    return /^[0-9]{10}$/.test(cleaned);
  }

  // Consultation Form Handler
  if (consultForm) {
    // Multi-step tab navigation
    const stepTabs = document.querySelectorAll('.form-step-tab');
    const stepSections = document.querySelectorAll('.consult-step-section');
    const nextStepBtn = document.getElementById('nextStepBtn');
    const prevStepBtn = document.getElementById('prevStepBtn');
    let currentStep = 1;

    function goToStep(step) {
      currentStep = step;
      stepSections.forEach((sec, idx) => {
        sec.style.display = (idx + 1 === step) ? 'block' : 'none';
      });
      stepTabs.forEach((tab, idx) => {
        if (idx + 1 === step) {
          tab.classList.add('active');
        } else {
          tab.classList.remove('active');
        }
      });

      if (prevStepBtn) prevStepBtn.style.display = (step > 1) ? 'inline-flex' : 'none';
      if (nextStepBtn) {
        nextStepBtn.textContent = (step === 3) ? 'Submit Demo Enquiry' : 'Continue to Next Step';
      }
    }

    if (nextStepBtn) {
      nextStepBtn.addEventListener('click', () => {
        if (currentStep === 1) {
          const nameInput = document.getElementById('fullName');
          const emailInput = document.getElementById('emailAddress');
          const phoneInput = document.getElementById('phoneNumber');

          let hasError = false;

          if (!nameInput.value.trim()) {
            nameInput.closest('.form-group').classList.add('has-error');
            hasError = true;
          } else {
            nameInput.closest('.form-group').classList.remove('has-error');
          }

          if (!validateEmail(emailInput.value.trim())) {
            emailInput.closest('.form-group').classList.add('has-error');
            hasError = true;
          } else {
            emailInput.closest('.form-group').classList.remove('has-error');
          }

          if (!validatePhone(phoneInput.value.trim())) {
            phoneInput.closest('.form-group').classList.add('has-error');
            hasError = true;
          } else {
            phoneInput.closest('.form-group').classList.remove('has-error');
          }

          if (!hasError) goToStep(2);
        } else if (currentStep === 2) {
          goToStep(3);
        } else if (currentStep === 3) {
          // Final Submit
          if (consultSuccessAlert) {
            consultSuccessAlert.style.display = 'block';
            consultSuccessAlert.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
          }
          consultForm.reset();
          goToStep(1);
        }
      });
    }

    if (prevStepBtn) {
      prevStepBtn.addEventListener('click', () => {
        if (currentStep > 1) goToStep(currentStep - 1);
      });
    }

    consultForm.addEventListener('submit', (e) => {
      e.preventDefault();
    });
  }

  // Standard Contact Form Handler
  if (contactForm) {
    contactForm.addEventListener('submit', (e) => {
      e.preventDefault();

      const name = document.getElementById('contactName');
      const email = document.getElementById('contactEmail');
      const message = document.getElementById('contactMessage');
      let isValid = true;

      if (name && !name.value.trim()) {
        name.closest('.form-group').classList.add('has-error');
        isValid = false;
      } else if (name) {
        name.closest('.form-group').classList.remove('has-error');
      }

      if (email && !validateEmail(email.value.trim())) {
        email.closest('.form-group').classList.add('has-error');
        isValid = false;
      } else if (email) {
        email.closest('.form-group').classList.remove('has-error');
      }

      if (message && !message.value.trim()) {
        message.closest('.form-group').classList.add('has-error');
        isValid = false;
      } else if (message) {
        message.closest('.form-group').classList.remove('has-error');
      }

      if (isValid) {
        if (contactSuccessAlert) {
          contactSuccessAlert.style.display = 'block';
          contactSuccessAlert.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
        }
        contactForm.reset();
      }
    });
  }
});
