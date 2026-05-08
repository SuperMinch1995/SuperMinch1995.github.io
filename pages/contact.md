---
layout: basic
title: Contact
permalink: "/contact/"
body_classes: page-contact
wide_content: true
---

<style>
  .contact-editorial {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 0;
    align-items: start;
    box-sizing: border-box;
  }

  .contact-editorial .contact-left {
    padding-right: 32px;
    padding-top: 0;
    margin-top: 0;
  }

  .contact-editorial .contact-left img {
    width: 100%;
    display: block;
    border-radius: 2px;
    vertical-align: top;
    margin-top: 0 !important;
    margin-bottom: 0 !important;
  }

  .contact-editorial .contact-right {
    display: flex;
    flex-direction: column;
    padding-left: 16px;
    padding-top: 0;
    margin-top: 0;
  }

  .contact-editorial {
    font-size: 13px;
    font-weight: 300;
    line-height: 1.7;
    color: var(--color-base-text, #111111);
    margin: 0 0 24px 0;
    font-style: italic;
  }

  .contact-editorial strong {
    font-style: normal;
    font-weight: 500;
  }

  .contact-editorial .form-box {
    border: 1.5px solid var(--color-base-text, #111111);
    padding: 24px 22px 22px;
    display: flex;
    flex-direction: column;
    background: transparent;
  }

  .contact-editorial .field-row {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 16px;
    margin-bottom: 18px;
  }

  .contact-editorial .field-group {
    display: flex;
    flex-direction: column;
    margin-bottom: 18px;
  }

  .contact-editorial .field-group:last-of-type {
    margin-bottom: 14px;
  }

  .contact-editorial .field-label {
    font-size: 11px;
    font-weight: 400;
    color: var(--color-base-text, #111111);
    margin-bottom: 10px;
    text-transform: uppercase;
    letter-spacing: 0.08em;
  }

  .contact-editorial .field-input,
  .contact-editorial .field-select {
    -webkit-appearance: none;
    appearance: none;
    background: transparent;
    border: none;
    border-bottom: 1.5px solid var(--color-base-text, #111111);
    border-radius: 0;
    box-shadow: none;
    padding: 0 0 6px 0;
    font-size: 13px;
    font-family: inherit;
    color: var(--color-base-text, #111111);
    outline: none;
    width: 100%;
  }

  .contact-editorial .field-select {
    background-image: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 12 8'><path fill='none' stroke='%23111' stroke-width='1.5' d='M1 1l5 5 5-5'/></svg>");
    background-repeat: no-repeat;
    background-position: right 4px center;
    background-size: 10px;
    padding-right: 18px;
    cursor: pointer;
  }

  .contact-editorial .field-input:focus,
  .contact-editorial .field-select:focus {
    border-bottom-color: var(--color-primary, #C2510A);
    box-shadow: none;
  }

  .contact-editorial textarea.field-input {
    resize: none;
    height: 64px;
    line-height: 1.5;
  }

  .contact-editorial textarea.field-bio {
    height: 44px;
  }

  .contact-editorial .radio-group {
    display: flex;
    gap: 22px;
    align-items: center;
    padding-top: 4px;
  }

  .contact-editorial .radio-option {
    display: flex;
    align-items: center;
    gap: 7px;
    font-size: 13px;
    cursor: pointer;
  }

  .contact-editorial .radio-option input[type="radio"] {
    -webkit-appearance: none;
    appearance: none;
    width: 13px;
    height: 13px;
    border: 1.5px solid var(--color-base-text, #111111);
    border-radius: 50%;
    margin: 0;
    cursor: pointer;
    background: transparent;
    flex-shrink: 0;
    position: relative;
  }

  .contact-editorial .radio-option input[type="radio"]:checked::after {
    content: "";
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 6px;
    height: 6px;
    border-radius: 50%;
    background: var(--color-primary, #C2510A);
  }

  .contact-editorial .thank-you {
    font-size: 13px;
    font-weight: 400;
    font-style: italic;
    color: var(--color-base-text, #111111);
    margin: 6px 0 12px 0;
    text-align: center;
  }

  .contact-editorial .submit-btn {
    margin-top: 8px;
    background: #4a4a4a;
    color: #EDE8DF;
    border: none;
    padding: 12px 0;
    font-size: 13px;
    font-family: inherit;
    font-weight: 400;
    cursor: pointer;
    border-radius: 50px;
    width: 100%;
    transition: background 0.2s ease;
  }

  .contact-editorial .submit-btn:hover {
    background: var(--color-primary, #C2510A);
  }

  .contact-editorial .submit-btn:disabled {
    opacity: 0.5;
    cursor: not-allowed;
  }

  /* Success / error status message */
  .contact-editorial .form-status {
    display: none;
    font-size: 12px;
    font-style: italic;
    margin-top: 10px;
    text-align: center;
    letter-spacing: 0.02em;
  }

  .contact-editorial .form-status.success {
    color: var(--color-primary, #C2510A);
  }

  .contact-editorial .form-status.error {
    color: #b00020;
  }

  @media (max-width: 768px) {
    .contact-editorial {
      grid-template-columns: 1fr;
    }

    .contact-editorial .contact-left {
      padding-right: 0;
      margin-bottom: 28px;
    }

    .contact-editorial .contact-right {
      padding-left: 0;
    }

    .contact-editorial .field-row {
      grid-template-columns: 1fr;
    }
  }
</style>

<div class="contact-editorial">
  <div class="contact-left">
    <img src="{{ '/assets/images/mayo.webp' | relative_url }}" alt="Mayo Clinic">
  </div>
  <div class="contact-right">

    <div class="form-box">

      <form id="contact-form">

        <div class="field-group">
          <label class="field-label" for="subject">Subject</label>
          <input class="field-input" type="text" id="subject" name="subject" placeholder="Be as specific as possible">
        </div>

        <div class="field-group">
          <label class="field-label" for="message">Message</label>
          <textarea class="field-input" id="message" name="message" placeholder="Go straight to the point"></textarea>
        </div>

        <div class="field-group">
            <label class="field-label" for="email">E-mail</label>
            <input class="field-input" type="email" id="email" name="email">
          </div>

        <div class="field-group">
            <label class="field-label" for="cell-phone">Cell phone</label>
            <input class="field-input" type="text" id="cell-phone" name="phone">
        </div>

        <div class="field-group">
          <label class="field-label" for="full-name">Full Name</label>
          <input class="field-input" type="text" id="full-name" name="name">
        </div>

        <p class="thank-you">Thank you 🕊️</p>

        <button class="submit-btn" type="submit" id="submit-btn">Submit</button>

        <p class="form-status" id="form-status"></p>

      </form>

    </div>
  </div>
</div>

<script>
  (function () {
    var form    = document.getElementById('contact-form');
    var btn     = document.getElementById('submit-btn');
    var status  = document.getElementById('form-status');

    form.addEventListener('submit', function (e) {
      e.preventDefault();

      btn.disabled    = true;
      btn.textContent = 'Sending…';
      status.className   = 'form-status';
      status.style.display = 'none';

      var data = new FormData(form);

      fetch('https://formspree.io/f/mzdoadww', {
        method:  'POST',
        body:    data,
        headers: { 'Accept': 'application/json' }
      })
      .then(function (response) {
        if (response.ok) {
          form.reset();
          btn.textContent      = 'Submit';
          btn.disabled         = false;
          status.textContent   = '✓ Sent — I\'ll be in touch soon.';
          status.className     = 'form-status success';
          status.style.display = 'block';
        } else {
          return response.json().then(function (json) {
            throw new Error(
              json.errors
                ? json.errors.map(function (err) { return err.message; }).join(', ')
                : 'Something went wrong.'
            );
          });
        }
      })
      .catch(function (err) {
        btn.textContent      = 'Submit';
        btn.disabled         = false;
        status.textContent   = '✗ ' + (err.message || 'Network error — please try again.');
        status.className     = 'form-status error';
        status.style.display = 'block';
      });
    });
  })();
</script>