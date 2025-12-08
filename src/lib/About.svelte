<script lang="ts">
  let activeTab = 'mainskill'
</script>

<div class="about-area about-position-top rn-section-gapBottom bg_color--1">
  <div class="about-wrapper">
    <div class="container">
      <div class="row row--35 align-items-center">
        <div class="col-lg-5">
          <div class="thumbnail">
            <img class="w-100" src="/images/about/profile-495x780.jpg" alt="About Images" />
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
                  <a class="nav-link" class:active={activeTab === 'awards'} id="awards" onclick={() => activeTab = 'awards'} role="tab" aria-controls="awards" aria-selected={activeTab === 'awards'}>Certifications</a>
                </li>
                <li class="nav-item">
                  <a class="nav-link" class:active={activeTab === 'experience'} id="experience" onclick={() => activeTab = 'experience'} role="tab" aria-controls="experience" aria-selected={activeTab === 'experience'}>Experience</a>
                </li>
                <li class="nav-item">
                  <a class="nav-link" class:active={activeTab === 'education'} id="education" onclick={() => activeTab = 'education'} role="tab" aria-controls="education" aria-selected={activeTab === 'education'}>Education</a>
                </li>
              </ul>
              <div class="tab-content" id="myTabContent">
                <div class="tab-pane fade" class:show={activeTab === 'mainskill'} class:active={activeTab === 'mainskill'} id="rn-mainskill" role="tabpanel" aria-labelledby="mainskill">
                  <div class="single-tab-content">
                    <ul>
                      <li><p>Unreal Engine <span> - Game Developer</span></p>Generalist game development with C++ and Blueprint</li>
                      <li><p>C++ <span> - Development</span></p>Generalist game development with custom engines</li>
                      <li><p>UI Implementation <span> - Development</span></p>Implementation of UI in UE, Unity and Custom engines</li>
                      <li><p>Tech Lead <span> - Leadership</span></p>Leading teams and projects, tasks breakdown and mentoring</li>
                    </ul>
                  </div>
                </div>
                <div class="tab-pane fade" class:show={activeTab === 'awards'} class:active={activeTab === 'awards'} id="rn-awards" role="tabpanel" aria-labelledby="awards">
                  <div class="single-tab-content">
                    <ul>
                      <li>
                        <p>
                          Unreal Authorized Instructor Gold <span>- UAI</span>
                        </p> 
                        2024 - Current
                        <p><img src="/images/icons/badge-ue.png" alt="UAI" style="height: 64px; width: auto; vertical-align: middle; margin-right: 8px;" /></p>
                      </li>
                    </ul>
                  </div>
                </div>
                <div class="tab-pane fade" class:show={activeTab === 'experience'} class:active={activeTab === 'experience'} id="rn-experience" role="tabpanel" aria-labelledby="experience">
                  <div class="single-tab-content">
                    <ul>
                      <li><p>Lead Tech UI Designer <span> - Globant</span></p> 2023 - Current</li>
                      <li><p>Generalist Game Developer <span> - Globant</span></p> 2020 - 2023</li>
                      <li><p>Java Developer <span> - Globant </span></p> 2019 - 2020</li>
                    </ul>
                  </div>
                </div>
                <div class="tab-pane fade" class:show={activeTab === 'education'} class:active={activeTab === 'education'} id="rn-education" role="tabpanel" aria-labelledby="education">
                  <div class="single-tab-content">
                    <ul>
                      <li><p>Intro to Game Development with UE - Course <span> - Universidad ORT, Montevideo, Uruguay</span></p> 2017</li>
                      <li><p>Computer Systems Analyst <span> - Escuela de Sistemas BIOS, Montevideo, Uruguay</span></p> 2015</li>
                      <li><p>Bachelor of Information Technology <span> - UTU Pedro Blanes Viale Mercedes, Uruguay</span></p> 2011</li>
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
