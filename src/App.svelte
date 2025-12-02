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

  // Scroll to top on route change
  $: if ($location) {
    window.scrollTo({ top: 0 })
  }

  onMount(() => {
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
