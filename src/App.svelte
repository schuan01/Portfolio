<script lang="ts">
  import { onMount } from 'svelte'
  import Header from './lib/Header.svelte'
  import Hero from './lib/Hero.svelte'
  import About from './lib/About.svelte'
  import Clients from './lib/Clients.svelte'
  import Projects from './lib/Projects.svelte'
  import Contact from './lib/Contact.svelte'
  import Footer from './lib/Footer.svelte'
  import Switcher from './lib/Switcher.svelte'

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
<main class="page-wrapper">
  <Hero />
  <About />
  <Clients />
  <Projects />
  <Contact />
</main>
<Footer />
