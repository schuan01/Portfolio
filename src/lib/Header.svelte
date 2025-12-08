<script lang="ts">
  import { onMount } from 'svelte'
  import { location } from 'svelte-spa-router'
  import { getPortfolioById } from './portfolioData'
  
  const socialLinks = [
    { icon: 'fab fa-linkedin-in', url: 'https://www.linkedin.com/in/juan-volpe/' }
  ]

  let headerColorClass = 'color-black'

  // Update header color based on current route
  $: {
    const path = $location
    if (path.startsWith('/portfolio-details/')) {
      const id = path.replace('/portfolio-details/', '')
      const portfolio = getPortfolioById(id)
      headerColorClass = portfolio?.headerTextColor || 'color-black'
    } else {
      headerColorClass = 'color-black'
    }
  }

  onMount(() => {
    // Initialize feather icons
    if (typeof (window as any).feather !== 'undefined') {
      (window as any).feather.replace()
    }
  })
</script>

<header class="header-area header-style-two header--transparent {headerColorClass}">
  <div class="header-wrapper">
    <div class="header-left d-flex align-items-center">
      <div class="logo">
        <a href="#/">
          <img src="/images/logo/jv-logo-60x60.png" alt="Juan Volpe logo" />
        </a>
      </div>
      <div class="mainmenunav d-lg-block ml--50">
        <nav class="main-menu-navbar">
          <ul class="mainmenu">
            <li><a href="#home">Home</a></li>
            <li><a href="#about">About</a></li>
            <li><a href="#portfolio">Portfolio</a></li>
            <li><a href="#contact">Contact</a></li>
          </ul>
        </nav>
      </div>
    </div>
    <div class="header-right">
      <div class="social-share-inner">
        <ul class="social-share social-style--2 {headerColorClass} d-flex justify-content-start liststyle">
          {#each socialLinks as social}
            <li><a href={social.url}><i class="{social.icon}"></i></a></li>
          {/each}
        </ul>
      </div>
      <div class="humberger-menu d-block d-lg-none pl--20 pl_sm--10">
        <span class="menutrigger text-white">
          <i data-feather="menu"></i>
        </span>
      </div>
      <div class="close-menu d-block d-lg-none">
        <span class="closeTrigger">
          <i data-feather="x"></i>
        </span>
      </div>
    </div>
  </div>
</header>
