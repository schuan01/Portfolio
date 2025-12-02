<script lang="ts">
  let activeTab = 'mainskill'
</script>

<div class="about-area about-position-top rn-section-gapBottom bg_color--1">
  <div class="about-wrapper">
    <div class="container">
      <div class="row row--35 align-items-center">
        <div class="col-lg-5">
          <div class="thumbnail">
            <img class="w-100" src="/images/about/about-5.jpg" alt="About Images" />
          </div>
        </div>
        <div class="col-lg-7">
          <div class="about-inner inner pt--100 pt_sm--40 pt_md--40">
            <div class="section-title">
              <h2 class="title">About Me</h2>
              <p class="description">There are many variations of passages of Lorem Ipsum available, but the majority have suffered <a href="https://juan.volpe.uy">alteration</a> in some form, by injected humour, or randomised words which dont look even slightly believable. If you are going to use a passage of Lorem Ipsum,</p>
            </div>
            <div class="tab-wrapper mt--30">
              <ul class="nav nav-tabs tab-style--1" id="myTab" role="tablist">
                <li class="nav-item">
                  <a class="nav-link" class:active={activeTab === 'mainskill'} id="mainskill" onclick={() => activeTab = 'mainskill'} role="tab" aria-controls="mainskill" aria-selected={activeTab === 'mainskill'}>Main skills</a>
                </li>
                <li class="nav-item">
                  <a class="nav-link" class:active={activeTab === 'awards'} id="awards" onclick={() => activeTab = 'awards'} role="tab" aria-controls="awards" aria-selected={activeTab === 'awards'}>Awards</a>
                </li>
                <li class="nav-item">
                  <a class="nav-link" class:active={activeTab === 'experience'} id="experience" onclick={() => activeTab = 'experience'} role="tab" aria-controls="experience" aria-selected={activeTab === 'experience'}>Experience</a>
                </li>
                <li class="nav-item">
                  <a class="nav-link" class:active={activeTab === 'education'} id="education" onclick={() => activeTab = 'education'} role="tab" aria-controls="education" aria-selected={activeTab === 'education'}>Education & Certification</a>
                </li>
              </ul>
              <div class="tab-content" id="myTabContent">
                <div class="tab-pane fade" class:show={activeTab === 'mainskill'} class:active={activeTab === 'mainskill'} id="rn-mainskill" role="tabpanel" aria-labelledby="mainskill">
                  <div class="single-tab-content">
                    <ul>
                      <li><a href="https://juan.volpe.uy">User experience design <span> - UI/UX</span></a>Delight the user and make it work.</li>
                      <li><a href="https://juan.volpe.uy">Web and user interface design<span> - Development</span></a>Websites, web experiences, ...</li>
                      <li><a href="https://juan.volpe.uy">Interaction design <span> - Animation</span></a>I like to move it move it.</li>
                    </ul>
                  </div>
                </div>
                <div class="tab-pane fade" class:show={activeTab === 'awards'} class:active={activeTab === 'awards'} id="rn-awards" role="tabpanel" aria-labelledby="awards">
                  <div class="single-tab-content">
                    <ul>
                      <li><a href="https://juan.volpe.uy">Awwwards.com <span>- Winner</span></a> 2019 - 2020</li>
                      <li><a href="https://juan.volpe.uy">CSS Design Awards <span>- Winner</span></a> 2017 - 2018</li>
                      <li><a href="https://juan.volpe.uy">Design nominees <span>- site of the day</span></a> 2013- 2014</li>
                    </ul>
                  </div>
                </div>
                <div class="tab-pane fade" class:show={activeTab === 'experience'} class:active={activeTab === 'experience'} id="rn-experience" role="tabpanel" aria-labelledby="experience">
                  <div class="single-tab-content">
                    <ul>
                      <li><a href="https://juan.volpe.uy">Sr. Front-end Engineer<span> - Google</span></a> 2018 - Current</li>
                      <li><a href="https://juan.volpe.uy">Front-end Engineer<span> - Microsoft</span></a> 2017 - 2018</li>
                      <li><a href="https://juan.volpe.uy">Software Engineer<span> - Alibaba </span></a> 2013- 2014</li>
                    </ul>
                  </div>
                </div>
                <div class="tab-pane fade" class:show={activeTab === 'education'} class:active={activeTab === 'education'} id="rn-education" role="tabpanel" aria-labelledby="education">
                  <div class="single-tab-content">
                    <ul>
                      <li><a href="https://juan.volpe.uy">BSc In CSE<span> - ABC University, Los Angeles, CA</span></a> 2010</li>
                      <li><a href="https://juan.volpe.uy">Diploma in Computer Science<span> - Gamma Technical Institute</span></a> 2009</li>
                      <li><a href="https://juan.volpe.uy">Graphic Designer<span> - ABC Institute, Los Angeles, CA</span></a> 2007</li>
                    </ul>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
