<script lang="ts">
  const currentYear = new Date().getFullYear()
  
  const socialLinks = [
    { icon: 'fab fa-facebook-f', url: '#' },
    { icon: 'fab fa-linkedin-in', url: '#' },
    { icon: 'fab fa-twitter', url: '#' },
    { icon: 'fab fa-instagram-square', url: '#' }
  ]
</script>

<footer class="footer-area footer-default">
  <div class="footer-wrapper">
    <div class="row align-items-end row--0">
      <div class="col-lg-6">
        <div class="footer-left">
          <div class="inner">
            <span>Ready To Do This</span>
            <h2>Let's get <br /> to work</h2>
            <a class="rn-button-style--2" href="#contact">
              <span>Contact Us</span>
            </a>
          </div>
        </div>
      </div>
      <div class="col-lg-6">
        <div class="footer-right" data-black-overlay="6">
          <div class="row">
            <!-- Start Single Widget -->
            <div class="col-lg-6 col-sm-6 col-12">
              <div class="footer-widget">
                <h4>Quick Link</h4>
                <ul class="ft-link">
                  <li><a href="#portfolio">Work</a></li>
                  <li><a href="#about">About</a></li>
                  <li><a href="#contact">Let's Talk</a></li>
                </ul>
              </div>
            </div>
            <!-- End Single Widget  -->
            <!-- Start Single Widget -->
            <div class="col-lg-6 col-sm-6 col-12 mt_mobile--30">
              <div class="footer-widget">
                <h4>Say Hello</h4>
                <ul class="ft-link">
                  <li><a href="mailto:admin@example.com">admin@example.com</a></li>
                  <li><a href="mailto:hr@example.com">hr@example.com</a></li>
                </ul>

                <div class="social-share-inner">
                  <ul class="social-share social-style--2 d-flex justify-content-start liststyle mt--15">
                    {#each socialLinks as social}
                      <li><a href={social.url}><i class="{social.icon}"></i></a></li>
                    {/each}
                  </ul>
                </div>
              </div>
            </div>
            <!-- End Single Widget  -->

            <div class="col-lg-12">
              <div class="copyright-text">
                <p>Copyright © {currentYear} Pixcels-Themes. All Rights Reserved.</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</footer>
