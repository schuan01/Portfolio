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
      <div class="row row--35 justify-content-center">
        <div class="col-lg-20">
          <div class="section-title text-center mb--50 mb_sm--30 mb_md--30">
            <h2 class="title">Contact Me</h2>
            <p class="description">If you would like to learn more about me or simply want to say hello, feel free to reach out via email:
              <a href="mailto:jcvolpe94@gmail.com"> jcvolpe94@gmail.com</a>
            </p>
          </div>
        </div>
        <div class="col-lg-5">
          <div class="thumbnail mb_md--30 mb_sm--30 text-center">
            <img src="/images/about/profile-about.jpeg" alt="trydo" />
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
