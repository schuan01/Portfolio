<script lang="ts">
  const brands = [
    '/images/brand/brand-01.png',
    '/images/brand/brand-02.png',
    '/images/brand/brand-03.png',
    '/images/brand/brand-04.png',
    '/images/brand/brand-05.png',
    '/images/brand/brand-06.png'
  ]
</script>

<div class="rn-brand-area bg_color--1 rn-section-gapBottom">
  <div class="container">
    <div class="row">
      <div class="col-lg-12">
        <div class="section-title section-title--2 text-center mb--60">
          <h2 class="title">My Best Client</h2>
          <p>There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration.</p>
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
