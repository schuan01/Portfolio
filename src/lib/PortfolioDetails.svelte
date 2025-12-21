<script lang="ts">
  import { onMount } from 'svelte'
  import { getPortfolioById, type PortfolioItem } from './portfolioData'
  
  export let params: { id?: string } = {}
  
  let portfolio: PortfolioItem | undefined
  let relatedProjects: PortfolioItem[] = []
  let previousId: string | undefined
  let customContent: string = ''
  const contentModules = import.meta.glob('../portfolio-content/*.html', { query: '?raw', import: 'default' })
  
  async function loadCustomContent(path: string) {
    try {
      const loader = contentModules[path]
      if (loader) {
        const content = await loader()
        customContent = content as string
        return
      }
      // Fallback: try fetching from public path if file was placed under public
      const publicPath = path.replace(/^\.\./, '')
      const response = await fetch(publicPath)
      if (response.ok) {
        customContent = await response.text()
      } else {
        customContent = ''
      }
    } catch (error) {
      console.error('Failed to load custom content:', error)
      customContent = ''
    }
  }
  
  onMount(() => {
    if (params.id) {
      portfolio = getPortfolioById(params.id)
      previousId = params.id
      if (portfolio?.customContentPath) {
        loadCustomContent(portfolio.customContentPath)
      }
    }
  })
  
  $: if (params.id) {
    portfolio = getPortfolioById(params.id)
    // Scroll to top when navigating to a different portfolio (including initial load)
    // Skip scrolling during hot reload when previousId === params.id
    if (previousId !== params.id) {
      window.scrollTo({ top: 0, behavior: 'instant' })
    }
    previousId = params.id
    // Load custom content if path exists
    if (portfolio?.customContentPath) {
      loadCustomContent(portfolio.customContentPath)
    } else {
      customContent = ''
    }
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
  <script src="https://player.vimeo.com/api/player.js"></script>
  <!-- Start Portfolio Details Area -->
  <div class="rn-portfolio-details ptb--120 bg_color--1">
    <div class="container">
      <div class="row">
        <div class="col-lg-12">
          <div class="portfolio-details">
            <div class="inner">
              <h2>{portfolio.title}</h2>
              <p class="subtitle">{portfolio.subtitle}</p>
              <blockquote class="rn-blog-quote">"{portfolio.description}"</blockquote>
              <div class="portfolio-view-list d-flex flex-wrap">
                <div class="port-view">
                  <span>Role</span>
                  <h4>{portfolio.area}</h4>
                </div>
                <div class="port-view">
                  <span>Platforms</span>
                  <h4>{portfolio.platform}</h4>
                </div>
                <div class="port-view">
                  <span>Company</span>
                  <h4>{portfolio.company}</h4>
                </div>
              </div>
              <div class="portfolio-share-link mt--20 pb--70 pb_sm--40">
                <ul class="social-share rn-lg-size d-flex justify-content-start liststyle mt--15">
                  {#if portfolio.socialLinks.steam}
                    <li>
                      <a href={portfolio.socialLinks.steam} aria-label="Steam">
                        <img src="/images/icons/steam-icon.svg" alt="Steam" class="icon-steam" />
                      </a>
                    </li>
                  {/if}
                  {#if portfolio.socialLinks.epic}
                    <li>
                      <a href={portfolio.socialLinks.epic} aria-label="Epic Games">
                        <img src="/images/icons/epic-icon.svg" alt="Epic Games" class="icon-epic" />
                      </a>
                    </li>
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
            
            <!-- Custom Content Section -->
            {#if customContent}
              {@html customContent}
            {:else}
              <!-- Default Content (when no custom content is provided) -->
              <div class="rn-blog-details pt--110 pb--70 bg_color--1">
                <div class="container">
                  <div class="row">
                    <div class="col-lg-12">
                      <div class="inner-wrapper">
                        <div class="inner">
                          <p class="mt--40">Project details coming soon.                                
                            There are many variations of passages of Lorem Ipsum available, but the majority
                                    have suffered alteration in some form, by injected humour, or randomised words
                                    which don't look even slightly believable. If you are going to use a passage of</p>
                                <p>Necessary, making this the first true generator on the Internet. It re are many
                                    variations of passages of Lo rem Ipsum available, but the majority have suffered
                                    alteration in some form, by injectedeed eedhumour, or randomised words which
                                    don't look even slightly believable.</p>
                                <blockquote class="rn-blog-quote">Lorem ipsum dolor sit amet, consectetuer
                                    adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis
                                    natoque penatibus et magnis dis parturient montes.</blockquote>
                                <p>There are many variations of passages of Lorem Ipsum available, but the majority
                                    have suffered alteration in some form, by injected humour, or randomised words
                                    which don't look even slightly believable. If you are going to use a passage of
                                    Lorem Ipsum. You need to be sure there isn't anything embarrassing hidden in the
                                    middle of text. All the Lorem Ipsum generators on the Internet tend toitrrepeat
                                    predefined chunks. Necessary, making this the first true generator on the
                                    Internet. It re are many variations of passages of Lorem Ipsum available, but
                                    the majority have suffered alteration in some form, by injectedeed eedhumour, or
                                    randomised words which don't look even slightly believable.</p>
                                <div class="blog-single-list-wrapper d-flex flex-wrap">
                                    <div class="thumbnail"><img class="w-100"
                                            src="/static/images/blog/blog-single-01.png"
                                            alt="BLog Images"><span>Lorem ipsum dolor sit amet, consectetur
                                            adipiscing elit, sed do</span></div>
                                    <div class="content">
                                        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
                                            tempor incididunt ut labore et dolore magna aliqua. Quis ipsum
                                            suspendisse ultrices gravida. Risus commodo .</p>
                                        <h4 class="title">Ordered &amp; Unordered Lists.</h4>
                                        <ul class="list-style">
                                            <li>Yet this above sewed flirted opened ouch</li>
                                            <li>Goldfinch realistic sporadic ingenuous</li>
                                            <li>Abominable this abidin far successfully then like piquan</li>
                                            <li>Risus commodo viverra</li>
                                            <li>Lorem ipsum dolor sit amet, consectetur adipiscing</li>
                                        </ul>
                                        <h4 class="title">Ordered &amp; Unordered Lists.</h4>
                                        <ul class="list-style">
                                            <li>Yet this above sewed flirted opened ouch</li>
                                            <li>Goldfinch realistic sporadic ingenuous</li>
                                            <li>Abominable this abidin far successfully then like piquan</li>
                                            <li>Risus commodo viverra</li>
                                        </ul>
                                    </div>
                                </div>
                                <p class="mt--25 mt_sm--5">There are many variations of passages of Lorem Ipsum
                                    available, but the majority have suffered alteration in some form, by injected
                                    humour, or randomised words which don't look even slightly believable. If you
                                    are going to use a passage of Lorem Ipsum. You need to be sure there isn't
                                    anything embarrassing hidden in the middle of text. All the Lorem Ipsum
                                    generators on the Internet tend toitrrepeat predefined chunks. Necessary, making
                                    this the first true generator on the Internet. It re are many variations of
                                    passages of Lorem Ipsum available, but the majority have suffered alteration in
                                    some form, by injectedeed eedhumour, or randomised words which don't look even
                                    slightly believable.</p>
                                <div class="video-wrapper position-relative mb--40">
                                    <div class="thumbnail">
                                        <img src="/static/images/blog/bl-big-01.jpg" alt="Blog Images">
                                    </div>
                                    <a class="video-popup position-top-center play__btn"
                                        href="https://www.youtube.com/watch?v=ZOoVOfieAF8"><span
                                            class="play-icon"></span></a>
                                </div>
                                <p class="mb--0">There are many variations of passages of Lorem Ipsum available, but
                                    the majority have suffered alteration in some form, by injected humour, or
                                    randomised words which don't look even slightly believable. If you are going to
                                    use a passage of Lorem Ipsum. You need to be sure there isn't anything
                                    embarrassing hidden in the middle of text. All the Lorem Ipsum generators on the
                                    Internet tend toitrrepeat predefined chunks. Necessary, making this the first
                                    true generator on the Internet. It re are many variations of passages of Lorem
                                    Ipsum available, but the majority have suffered alteration in some form, by
                                    injectedeed eedhumour, or randomised words which don't look even slightly
                                    believable.</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <!-- End Blog Details Area  -->
            {/if}
            <!-- End Custom Content Section -->
            
            <!-- <div class="portfolio-thumb-inner">
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
            </div> -->
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
