<script lang="ts">
  import Hero from './Hero.svelte'
  import About from './About.svelte'
  import Projects from './Projects.svelte'
  import Contact from './Contact.svelte'
    import Clients from './Clients.svelte';
</script>

<main class="page-wrapper">
  <section id="home"><Hero /></section>
  <section id="about"><About /></section>
  <section><Clients /></section>
  <section id="portfolio"><Projects /></section>
  <section id="contact"><Contact /></section>
</main>
