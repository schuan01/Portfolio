<script lang="ts">
  import { onMount } from 'svelte'

  onMount(() => {
    // Wait a bit for jQuery and Cookies to be available, then initialize switcher
    setTimeout(() => {
      if (typeof window.jQuery !== 'undefined' && typeof window.Cookies !== 'undefined') {
        const $ = window.jQuery
        const Cookies = window.Cookies

        function setStyleCookie() {
          const styleCookieVal = $('body').hasClass('active-dark-mode') ? 'dark' : 'light'
          Cookies.set('styleCookieName', styleCookieVal, { expires: 7 })
        }

        if (Cookies.get('styleCookieName') == 'dark') {
          $('body').addClass('active-dark-mode')
        } else if(Cookies.get('styleCookieName') == 'light') {
          $('body').removeClass('active-dark-mode')
        }

        // Check Cookie
        const activeStyle = Cookies.get('styleCookieName')
        if (activeStyle == "dark") {
          $('#my_switcher').find('.setColor.dark').addClass('active')
          $('body').removeClass('active-light-mode').addClass('active-dark-mode')
        } else if(activeStyle == "light") {
          $('#my_switcher').find('.setColor.light').addClass('active')
          $('body').removeClass('active-dark-mode').addClass('active-light-mode')
        } else {
          // Switcher Active Class Based on Body Class
          if($("body").hasClass("active-dark-mode")) {
            $('#my_switcher').find('.setColor.light').removeClass('active')
            $('#my_switcher').find('.setColor.dark').addClass('active')
          } else {
            $('#my_switcher').find('.setColor.dark').removeClass('active')
            $('#my_switcher').find('.setColor.light').addClass('active')
          }
        }

        // Set Click
        $('#my_switcher .setColor').on('click', function() {
          $(this).closest('ul').find('li').siblings().find('.active').removeClass('active')
          $(this).addClass('active')
          setStyleCookie()
        })

        // Add or Remove Class into body when click switcher
        $('#my_switcher .setColor.dark').on('click', function() {
          $('body').removeClass('active-light-mode').addClass('active-dark-mode')
          setStyleCookie()
        })
        $('#my_switcher .setColor.light').on('click', function() {
          $('body').removeClass('active-dark-mode').addClass('active-light-mode')
          setStyleCookie()
        })
      }
    }, 100)
  })
</script>

<div id="my_switcher" class="my_switcher">
  <ul>
    <li>
      <a href="#" data-theme="light" class="setColor light" on:click|preventDefault={() => {}}>
        <img src="/images/about/sun-01.svg" alt="Sun images" />
        <span title="Light Mode">Light</span>
      </a>
    </li>
    <li>
      <a href="#" data-theme="dark" class="setColor dark" on:click|preventDefault={() => {}}>
        <img src="/images/about/vector.svg" alt="Vector Images" />
        <span title="Dark Mode">Dark</span>
      </a>
    </li>
  </ul>
</div>
