<script lang="ts">
  import { onMount } from 'svelte'
  
  const socialLinks = [
    { icon: 'fab fa-facebook-f', url: '#' },
    { icon: 'fab fa-linkedin-in', url: '#' },
    { icon: 'fab fa-twitter', url: '#' },
    { icon: 'fab fa-instagram', url: '#' }
  ]

  onMount(() => {
    // Initialize feather icons
    if (typeof (window as any).feather !== 'undefined') {
      (window as any).feather.replace()
    }
  })
</script>

<header class="header-area header-style-two header--transparent color-black">
  <div class="header-wrapper">
    <div class="header-left d-flex align-items-center">
      <div class="logo">
        <a href="https://juan.volpe.uy">
          <img src="/images/logo/logo-symbol-dark.png" alt="Creative Agency" />
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
        <ul class="social-share social-style--2 color-black d-flex justify-content-start liststyle">
          {#each socialLinks as social}
            <li><a href={social.url}><i class="{social.icon}"></i></a></li>
          {/each}
        </ul>
      </div>
      <div class="header-btn ml_md--20 ml_sm--0"><a class="rn-btn" href="https://juan.volpe.uy"><span>buy now</span></a></div>
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
