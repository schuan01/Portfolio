<script lang="ts">
  const brands = [
    '/images/brand/c-logo-black-and-white-2.png',
    '/images/brand/256px-UE_Logo_Black_Centered.png',
    '/images/brand/256px-Unity_2021.png',
    '/images/brand/c-sharp.png',
    '/images/brand/Perforce.png',
    '/images/brand/256px-Git-logo-black.png'
  ]
</script>

<div class="rn-brand-area bg_color--1 rn-section-gapBottom">
  <div class="container">
    <div class="row">
      <div class="col-lg-12">
        <div class="section-title section-title--2 text-center mb--60">
          <h2 class="title">Tech Stack</h2>
          <p>As a Game Developer, I have been working with different techologies, here are the main ones:</p>
        </div>
      </div>
    </div>
    <div class="row">
      <div class="col-lg-12">
        <ul class="brand-style">
          {#each brands as brand}
            <li>
              <img src={brand} alt="Logo Images" />
            </li>
          {/each}
        </ul>
      </div>
    </div>
  </div>
</div>
