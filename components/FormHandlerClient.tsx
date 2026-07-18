'use client';

import { useEffect } from 'react';

export default function FormHandlerClient() {
  useEffect(() => {
    const handleFormSubmit = async (e: SubmitEvent) => {
      const form = e.target as HTMLFormElement;
      if (!form.classList.contains('elementor-form')) return;

      e.preventDefault();

      // Find or create the message container inside the form
      let messageContainer = form.querySelector('.elementor-message') as HTMLElement;
      if (!messageContainer) {
        messageContainer = document.createElement('div');
        messageContainer.className = 'elementor-message';
        messageContainer.setAttribute('role', 'alert');
        form.appendChild(messageContainer);
      }

      // Hide message container initially and reset state
      messageContainer.style.display = 'none';
      messageContainer.className = 'elementor-message';
      messageContainer.innerText = '';

      // Find submit button to show loading state
      const submitButton = form.querySelector('button[type="submit"]') as HTMLButtonElement;
      let originalButtonText = '';
      if (submitButton) {
        const textSpan = submitButton.querySelector('.elementor-button-text');
        originalButtonText = textSpan ? textSpan.textContent || '' : submitButton.innerText;
        if (textSpan) {
          textSpan.textContent = 'Sending...';
        } else {
          submitButton.innerText = 'Sending...';
        }
        submitButton.disabled = true;
      }

      // Collect form data
      const formData = new FormData(form);
      const data: Record<string, string> = {};
      formData.forEach((value, key) => {
        data[key] = value.toString();
      });

      try {
        const response = await fetch('/api/leads', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            formName: form.name || 'Generic Form',
            fields: data,
            url: window.location.href,
          }),
        });

        const result = await response.json();

        if (response.ok && result.success) {
          // Success state
          messageContainer.classList.add('elementor-message-success');
          messageContainer.innerText = 'Your submission was successful. Thank you!';
          messageContainer.style.display = 'block';
          form.reset();
        } else {
          // Failure state
          messageContainer.classList.add('elementor-message-danger');
          messageContainer.innerText = result.message || 'An error occurred. Please try again.';
          messageContainer.style.display = 'block';
        }
      } catch {
        // Error state
        messageContainer.classList.add('elementor-message-danger');
        messageContainer.innerText = 'Server error. Please check your internet connection and try again.';
        messageContainer.style.display = 'block';
      } finally {
        // Restore submit button state
        if (submitButton) {
          const textSpan = submitButton.querySelector('.elementor-button-text');
          if (textSpan) {
            textSpan.textContent = originalButtonText;
          } else {
            submitButton.innerText = originalButtonText;
          }
          submitButton.disabled = false;
        }
      }
    };

    document.addEventListener('submit', handleFormSubmit);
    return () => {
      document.removeEventListener('submit', handleFormSubmit);
    };
  }, []);

  return null;
}
