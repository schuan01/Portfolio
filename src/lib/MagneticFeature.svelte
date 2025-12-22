<script lang="ts">
  import { onMount, onDestroy } from 'svelte'
  
  export let images: Array<{ src: string; alt?: string }> = [
    { src: '/images/portfolio/portfolio-3.jpg', alt: 'Portfolio 3' },
    { src: '/images/portfolio/portfolio-4.jpg', alt: 'Portfolio 4' },
    { src: '/images/portfolio/portfolio-6.jpg', alt: 'Portfolio 6' },
    { src: '/images/portfolio/portfolio-7.jpg', alt: 'Portfolio 7' }
  ]
  export let vertical: boolean = false
  export let intensity: number = 0.9
  export let damping: number = 0.14
  export let maxSpeed: number = 250
  
  let container: HTMLDivElement | null = null
  let frameId: number | null = null
  
  let globalMouseX = 0, globalMouseY = 0
  let prevGlobalMouseX = 0, prevGlobalMouseY = 0
  let globalVelocityX = 0, globalVelocityY = 0
  
  function updateMousePosition(clientX: number, clientY: number) {
    if (!container) return
    const rect = container.getBoundingClientRect()
    const centerX = rect.left + rect.width / 50
    const centerY = rect.top + rect.height / 50
    globalMouseX = clientX - centerX
    globalMouseY = clientY - centerY
  }
  
  function onMouseMove(e: MouseEvent) {
    updateMousePosition(e.clientX, e.clientY)
  }
  function onTouchMove(e: TouchEvent) {
    const t = e.touches?.[0] || e.changedTouches?.[0]
    if (!t) return
    updateMousePosition(t.clientX, t.clientY)
  }
  
  function animate() {
    const globalDeltaX = globalMouseX - prevGlobalMouseX
    const globalDeltaY = globalMouseY - prevGlobalMouseY
    
    globalVelocityX += globalDeltaX * intensity
    globalVelocityY += globalDeltaY * intensity
    
    globalVelocityX *= 1 - damping
    globalVelocityY *= 1 - damping
    
    prevGlobalMouseX = globalMouseX
    prevGlobalMouseY = globalMouseY
    
    if (container) {
      const heroRect = container.getBoundingClientRect()
      const items = container.querySelectorAll<HTMLElement>('.hero__image')
      items.forEach((imageEl) => {
        const rect = imageEl.getBoundingClientRect()
        const imageCenterX = rect.left + rect.width / 2
        const imageCenterY = rect.top + rect.height / 2
        
        const localMouseX = globalMouseX - (imageCenterX - heroRect.left)
        const localMouseY = globalMouseY - (imageCenterY - heroRect.top)
        
        const distance = Math.sqrt(localMouseX ** 2 + localMouseY ** 2)
        const effectRadius = Math.max(rect.width, rect.height)
        const influence = Math.max(0, Math.min(1, 1 - distance / effectRadius))
        
        let targetOffsetX = globalVelocityX * influence
        let targetOffsetY = globalVelocityY * influence
        
        targetOffsetX = Math.max(Math.min(targetOffsetX, maxSpeed), -maxSpeed)
        targetOffsetY = Math.max(Math.min(targetOffsetY, maxSpeed), -maxSpeed)
        
        imageEl.style.setProperty('--offsetX', (targetOffsetX * 2).toFixed(2))
        imageEl.style.setProperty('--offsetY', (targetOffsetY * 2).toFixed(2))
        imageEl.style.setProperty('--velocity', (((targetOffsetX - targetOffsetY) * -0.35)).toFixed(2))
      })
    }
    frameId = requestAnimationFrame(animate)
  }
  
  onMount(() => {
    if (!container) return
    container.addEventListener('mousemove', onMouseMove, { passive: true })
    container.addEventListener('touchmove', onTouchMove, { passive: true })
    frameId = requestAnimationFrame(animate)
  })
  
  onDestroy(() => {
    if (!container) return
    container.removeEventListener('mousemove', onMouseMove)
    container.removeEventListener('touchmove', onTouchMove)
    if (frameId) cancelAnimationFrame(frameId)
  })
</script>

<section class="magnetic_hero">
  <div class="hero__images {vertical ? 'vertical' : ''}" bind:this={container}>
    {#each images as img}
      <div class="hero__image">
        <img src={img.src} alt={img.alt || 'Image'} />
      </div>
    {/each}
  </div>
</section>
