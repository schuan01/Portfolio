<script lang="ts">
  const portfolioItems = [
    { imageClass: 'image-8', category: 'Development', title: 'Getting tickets to the big show' },
    { imageClass: 'image-7', category: 'Development', title: 'Getting tickets to the big show' },
    { imageClass: 'image-3', category: 'Development', title: 'Getting tickets to the big show' },
    { imageClass: 'image-4', category: 'Development', title: 'Getting tickets to the big show' },
    { imageClass: 'image-3', category: 'Development', title: 'Getting tickets to the big show' },
    { imageClass: 'image-2', category: 'Development', title: 'Getting tickets to the big show' }
  ]
</script>

<div class="rn-portfolio-area rn-section-gapBottom bg_color--1">
  <div class="container">
    <div class="row">
      <div class="col-lg-12">
        <div class="section-title section-title--2 text-center mb--30">
          <h2 class="title">My Latest Project</h2>
          <p>There are many variations of passages of Lorem Ipsum available, <br /> but the majority have suffered alteration.</p>
        </div>
      </div>
    </div>
    <div class="row">
      {#each portfolioItems as item}
        <div class="col-lg-4 col-md-6 col-sm-6 col-12 mt--30">
          <div class="portfolio text-center">
            <div class="thumbnail-inner">
              <div class="thumbnail {item.imageClass}"></div>
              <div class="bg-blr-image {item.imageClass}"></div>
            </div>
            <div class="content">
              <div class="inner">
                <p>{item.category}</p>
                <h4><a href="https://juan.volpe.uy">{item.title}</a></h4>
                <div class="portfolio-button">
                  <a class="rn-btn" href="https://juan.volpe.uy">Case Study</a>
                </div>
              </div>
            </div>
          </div>
        </div>
      {/each}
    </div>
    <div class="row">
      <div class="col-lg-12">
        <div class="view-more-btn mt--60 mt_sm--30 text-center">
          <a class="rn-button-style--2 btn_solid" href="https://juan.volpe.uy">View More</a>
        </div>
      </div>
    </div>
  </div>
</div>
