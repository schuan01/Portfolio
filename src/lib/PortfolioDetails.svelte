<script lang="ts">
  import { onMount } from 'svelte'
  import { getPortfolioById, type PortfolioItem } from './portfolioData'
  
  export let params: { id?: string } = {}
  
  let portfolio: PortfolioItem | undefined
  let relatedProjects: PortfolioItem[] = []
  
  onMount(() => {
    if (params.id) {
      portfolio = getPortfolioById(params.id)
    }
  })
  
  $: if (params.id) {
    portfolio = getPortfolioById(params.id)
    // Scroll to top when portfolio changes
    window.scrollTo({ top: 0, behavior: 'instant' })
    // Get 2 random related projects (excluding current)
    import('./portfolioData').then(({ portfolioData }) => {
      relatedProjects = portfolioData
        .filter(p => p.id !== params.id)
        .sort(() => Math.random() - 0.5)
        .slice(0, 2)
    })
  }
</script>

{#if portfolio}
<!-- Start breadcrumb Area -->
<div class="rn-page-title-area pt--120 pb--190 pb_md--100 pb_sm--100 bg_image {portfolio.headerBgClass}" data-black-overlay="5">
  <div class="container">
    <div class="row">
      <div class="col-lg-12">
        <div class="rn-page-title text-center pt--100">
          <h2 class="title theme-gradient">{portfolio.title}</h2>
          <p>{portfolio.subtitle}</p>
        </div>
      </div>
    </div>
  </div>
</div>
<!-- End breadcrumb Area -->

<!-- Start Page Wrapper -->
<main class="page-wrapper">
  <!-- Start Portfolio Details Area -->
  <div class="rn-portfolio-details ptb--120 bg_color--1">
    <div class="container">
      <div class="row">
        <div class="col-lg-12">
          <div class="portfolio-details">
            <div class="inner">
              <h2>{portfolio.title}</h2>
              <p class="subtitle">{portfolio.subtitle}</p>
              <p>{portfolio.description}</p>
              <div class="portfolio-view-list d-flex flex-wrap">
                <div class="port-view">
                  <span>Branch</span>
                  <h4>{portfolio.branch}</h4>
                </div>
                <div class="port-view">
                  <span>Project Types</span>
                  <h4>{portfolio.projectType}</h4>
                </div>
                <div class="port-view">
                  <span>Program</span>
                  <h4>{portfolio.program}</h4>
                </div>
              </div>
              <div class="portfolio-share-link mt--20 pb--70 pb_sm--40">
                <ul class="social-share rn-lg-size d-flex justify-content-start liststyle mt--15">
                  {#if portfolio.socialLinks.facebook}
                    <li><a href={portfolio.socialLinks.facebook}><i data-feather="facebook"></i></a></li>
                  {/if}
                  {#if portfolio.socialLinks.linkedin}
                    <li><a href={portfolio.socialLinks.linkedin}><i data-feather="linkedin"></i></a></li>
                  {/if}
                  {#if portfolio.socialLinks.instagram}
                    <li><a href={portfolio.socialLinks.instagram}><i data-feather="instagram"></i></a></li>
                  {/if}
                  {#if portfolio.socialLinks.twitter}
                    <li><a href={portfolio.socialLinks.twitter}><i data-feather="twitter"></i></a></li>
                  {/if}
                </ul>
              </div>
            </div>
            <div class="portfolio-thumb-inner">
              <div class="thumb position-relative mb--30">
                <img src={portfolio.mainImage} alt={portfolio.title} />
                {#if portfolio.videoUrl}
                  <a
                    class="video-popup position-top-center theme-color play__btn"
                    href={portfolio.videoUrl}
                  >
                    <span class="play-icon"></span>
                  </a>
                {/if}
              </div>
              {#each portfolio.additionalImages as image}
                <div class="thumb mb--30">
                  <img src={image} alt={portfolio.title} />
                </div>
              {/each}
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <!-- End Portfolio Details Area -->

  <!-- Start Related Work -->
  <div class="portfolio-related-work pb--120 bg_color--1">
    <div class="container">
      <div class="row">
        <div class="col-lg-12">
          <div class="section-title text-center">
            <span class="theme-color font--18 fontWeight600">Related Work</span>
            <h2>Other Projects</h2>
          </div>
        </div>
      </div>
      <div class="row mt--10">
        {#each relatedProjects as project}
          <div class="col-lg-6 col-md-6 col-12">
            <div class="related-work text-center mt--30">
              <div class="thumb">
                <a href="#/portfolio-details/{project.id}">
                  <img src={project.mainImage} alt={project.title} />
                </a>
              </div>
              <div class="inner">
                <h4><a href="#/portfolio-details/{project.id}">{project.title}</a></h4>
                <span class="category">{project.category}</span>
              </div>
            </div>
          </div>
        {/each}
      </div>
    </div>
  </div>
  <!-- End Related Work -->
</main>
<!-- End Page Wrapper -->
{:else}
<main class="page-wrapper">
  <div class="rn-portfolio-details ptb--120 bg_color--1">
    <div class="container">
      <div class="row">
        <div class="col-lg-12 text-center">
          <h2>Portfolio item not found</h2>
          <a href="#/" class="rn-button-style--2 btn_solid mt--30">Back to Home</a>
        </div>
      </div>
    </div>
  </div>
</main>
{/if}
