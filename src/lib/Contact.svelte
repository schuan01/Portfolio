<script lang="ts">
  let formData = {
    name: '',
    email: '',
    subject: '',
    message: ''
  }

  const handleSubmit = (e: Event) => {
    e.preventDefault()
    console.log('Form submitted:', formData)
    // Reset form
    formData = { name: '', email: '', subject: '', message: '' }
  }
</script>

<div class="rn-contact-area rn-section-gapBottom bg_color--1">
  <div class="contact-form--1">
    <div class="container">
      <div class="row row--35 align-items-start">
        <div class="col-lg-6 order-2 order-lg-1">
          <div class="section-title text-start mb--50 mb_sm--30 mb_md--30">
            <h2 class="title">Hire Me.</h2>
            <p class="description">I am available for freelance work. Connect with me via phone:
              <a href="tel:+8801923088574">01923 088574</a> or email:
              <a href="mailto:admin@example.com"> admin@example.com</a>
            </p>
          </div>
          <div class="form-wrapper">
            <form method="POST" action="" onsubmit={handleSubmit}>
              <label for="item01">
                <input type="text" name="name" id="item01" placeholder="Your Name *" bind:value={formData.name}>
              </label>
              <label for="item02">
                <input type="text" name="email" id="item02" placeholder="Your email *" bind:value={formData.email}>
              </label>
              <label for="item03">
                <input type="text" name="subject" id="item03" placeholder="Write a Subject" bind:value={formData.subject}>
              </label>
              <label for="item04">
                <textarea id="item04" name="message" placeholder="Your Message" bind:value={formData.message}></textarea>
              </label>
              <button class="rn-button-style--2 btn_solid" type="submit" value="submit" name="submit" id="mc-embedded-subscribe">Submit</button>
            </form>
          </div>
        </div>
        <div class="col-lg-6 order-1 order-lg-2">
          <div class="thumbnail mb_md--30 mb_sm--30">
            <img src="/images/about/about-6.jpg" alt="trydo" />
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
