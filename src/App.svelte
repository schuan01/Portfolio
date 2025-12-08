<script lang="ts">
  import { onMount } from 'svelte'
  import Router from 'svelte-spa-router'
  import { location } from 'svelte-spa-router'
  import Header from './lib/Header.svelte'
  import Footer from './lib/Footer.svelte'
  import Switcher from './lib/Switcher.svelte'
  import Home from './lib/Home.svelte'
  import PortfolioDetails from './lib/PortfolioDetails.svelte'

  const routes = {
    '/': Home,
    '/portfolio-details': PortfolioDetails,
    '/portfolio-details/:id': PortfolioDetails
  }

  // Smooth scroll to section or top on route/hash change
  $: if ($location) {
    const hash = window.location.hash.substring(1) // Remove '#'
    
    if (hash && hash !== '/') {
      // If there's a hash fragment (like #about), scroll to it smoothly
      setTimeout(() => {
        const element = document.getElementById(hash)
        if (element) {
          element.scrollIntoView({ behavior: 'smooth', block: 'start' })
        }
      }, 100)
    } else {
      // Otherwise scroll to top smoothly
      window.scrollTo({ top: 0 })
    }
  }

  onMount(() => {
    // Enable smooth scrolling in CSS
    document.documentElement.style.scrollBehavior = 'smooth'
    
    // Load main.js after Svelte components are mounted
    const script = document.createElement('script')
    script.src = '/js/main.js'
    script.async = false
    document.body.appendChild(script)
  })
</script>

<Switcher />
<Header />
<Router {routes} />
<Footer />
