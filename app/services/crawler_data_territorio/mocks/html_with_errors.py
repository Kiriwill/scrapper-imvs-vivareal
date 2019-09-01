html = '''
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    
    <script>
      (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
          (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
        m=s.getElementsByTagName(o)[0];a.src=g;m.parentNode.insertBefore(a,m)
      })(window,document,'script','https://www.google-analytics.com/analytics.js','ga');
      ga('create', 'UA-126375-31', 'auto');
      ga('require', 'GTM-PVK4X33');
    </script>
    <script>
      var pageCategory = 'CONDOMINIUM DETAIL PAGE';
    
      const clickstreamTracker = function (rawData) {
        const clickstreamTrackerEndpoint = 'https://tracking.vivareal.com/events/v2'
        const data = JSON.stringify(rawData)
    
        if (navigator.sendBeacon) {
          navigator.sendBeacon(clickstreamTrackerEndpoint, data)
        } else {
          const ajax = new XMLHttpRequest()
          ajax.open('POST', clickstreamTrackerEndpoint, true)
          ajax.send(data)
        }
      };
    
      (function () {
        const getCookie = function(name) {
          const value = `; ${document.cookie}`
          const parts = value.split(`; ${name}=`)
    
          if (parts.length == 2) return parts.pop().split(';').shift()
          return ''
        }
    
        const getExperimentId = function() {
          const gaExp = getCookie('_gaexp')
    
          if (gaExp) {
            return gaExp.split('!')
              .map(v => v.replace(/GAX([0-9]+\.){2}/, '').split('.')[0])
              .join('!') || ''
          }
    
          return ''
        }
    
        const getVariation = function() {
          const variationsOnUrl = window.location.search
            .split('&')
            .find(function (item) { return item.indexOf('__vt') >= 0 })
    
          return variationsOnUrl ? variationsOnUrl.split('=').pop() : ''
        }
    
        const cuid = function() {
          return ([1e7]+-1e3+-4e3+-8e3+-1e11).replace(/[018]/g, function(c) {
            return (c ^ crypto.getRandomValues(new Uint8Array(1))[0] & 15 >> c / 4)
              .toString(16)
          })
        }
    
        const loadAnonymousId = function() {
         const userAnonymousKey = 'new_vivareal_user_id'
    
         let id = getCookie(userAnonymousKey)
    
         if (!id) {
           id = cuid()
           document.cookie = [userAnonymousKey, id].join('=') + '; expires= Mon, 1 Jan 2099 00:00:00 UTC; path=/ '
         }
    
         return id
       }
    
        const loadSessionId = function() {
          const userSessionKey = 'V_USER_SESSION'
    
          let id = sessionStorage.getItem(userSessionKey)
    
          if (!id) {
            id = cuid()
            sessionStorage.setItem(userSessionKey, id)
          }
    
          return id
        }
    
        window.dataLayerClickstream = [{
          anonymous_id: loadAnonymousId(),
          device_sent_timestamp: Date.now(),
          experiment_id: getExperimentId(),
          page_category: pageCategory,
          platform: (window.outerWidth < 640) ? 'MOBILE' : 'DESKTOP',
          session_id: loadSessionId(),
          user_id: getCookie('vrSessionToken'),
          variation_name: getVariation(),
        }]
      })()
    </script>
    
      <noscript>
        <iframe src="//www.googletagmanager.com/ns.html?id=GTM-NP5VKCD"
          height="0" width="0" style="display:none;visibility:hidden">
        </iframe>
      </noscript>
    
      <script>
        (function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
          new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
          j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
          '//www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
        })(window, document, 'script', 'dataLayerClickstream', 'GTM-NP5VKCD');
      </script>

  <link rel="dns-prefetch" href="//cdn1.vivareal.com">
  <link rel="dns-prefetch" href="//resizedimgs.vivareal.com">
  <link rel="dns-prefetch" href="//tracking.vivareal.com">
  <link rel="dns-prefetch" href="//api.vivareal.com">
  
  <link rel="dns-prefetch" href="//www.googletagmanager.com">
  <link rel="dns-prefetch" href="//www.googletagservices.com">
  <link rel="dns-prefetch" href="//www.googleadservices.com﻿">
  <link rel="dns-prefetch" href="//www.google-analytics.com">
  <link rel="dns-prefetch" href="https://googleads.g.doubleclick.net">
  
  <link rel="dns-prefetch" href="//static.criteo.net">
  <link rel="dns-prefetch" href="//widget.criteo.com">
  <link rel="dns-prefetch" href="//dis.us.criteo.com">
  
  <link rel="dns-prefetch" href="//bam.nr-data.net">
  <link rel="dns-prefetch" href="//script.crazyegg.com">
  <link rel="dns-prefetch" href="https://analytics.twitter.com">
  <link rel="dns-prefetch" href="//platform.twitter.com">
    <style type="text/css">
      @-webkit-keyframes spinning{0%{-webkit-transform:rotate(0deg);transform:rotate(0deg)}to{-webkit-transform:rotate(1turn);transform:rotate(1turn)}}@font-face{font-family:Open Sans;font-style:normal;font-weight:400;font-display:swap;src:url(https://cdn1.vivareal.com/p/14483-4ce4541/v/static/app/fonts/Open_Sans_400.woff2) format("woff2"),url(https://cdn1.vivareal.com/p/14483-4ce4541/v/static/app/fonts/Open_Sans_400.woff) format("woff"),url(https://cdn1.vivareal.com/p/14483-4ce4541/v/static/app/fonts/Open_Sans_400.ttf) format("truetype")}@font-face{font-family:Open Sans;font-style:normal;font-weight:600;font-display:swap;src:url(https://cdn1.vivareal.com/p/14483-4ce4541/v/static/app/fonts/Open_Sans_600.woff2) format("woff2"),url(https://cdn1.vivareal.com/p/14483-4ce4541/v/static/app/fonts/Open_Sans_600.woff) format("woff"),url(https://cdn1.vivareal.com/p/14483-4ce4541/v/static/app/fonts/Open_Sans_600.ttf) format("truetype")}a,address,article,aside,b,blockquote,body,button,code,dd,div,dl,dt,em,fieldset,figure,footer,form,h1,h2,h3,h4,h5,h6,header,html,i,iframe,img,label,li,nav,object,ol,p,q,section,small,span,sub,sup,tt,ul,var{border:0;-webkit-box-sizing:border-box;box-sizing:border-box;font-size:100%;margin:0;padding:0;vertical-align:baseline}body,html{scroll-behavior:smooth}body{-moz-osx-font-smoothing:grayscale;-webkit-font-smoothing:antialiased;-webkit-tap-highlight-color:rgba(255,255,255,.001);color:rgba(0,0,0,.87);font-size:16px;font:normal normal 100% Open Sans,Helvetica,Sans-Serif;line-height:24px;font-weight:400}body input,body textarea{font-family:inherit}body[data-overlay]{overflow:hidden}body>img[width="0"][height="0"]{display:block}li{list-style:none}blockquote,q{quotes:none}blockquote:after,blockquote:before,q:after,q:before{content:"";content:none}table{border-collapse:collapse;border-spacing:0}@keyframes spinning{0%{-webkit-transform:rotate(0deg);transform:rotate(0deg)}to{-webkit-transform:rotate(1turn);transform:rotate(1turn)}}.site-header{background:#1190cd}.site-header[data-smart-banner]{margin-top:64px}.site-header__container{display:-webkit-box;display:-ms-flexbox;display:flex;height:56px;-webkit-box-pack:justify;-ms-flex-pack:justify;justify-content:space-between;position:relative}.site-header__login,.site-header__open-menu{-webkit-appearance:none;-moz-appearance:none;appearance:none;border-radius:4px;cursor:pointer;display:inline-block;text-align:center;text-decoration:none;font-size:13px;line-height:21px;font-weight:600;background:none;border:0;color:#fff;text-transform:uppercase}.site-header__login:focus,.site-header__open-menu:focus{outline:0}.site-header__login[disabled],.site-header__open-menu[disabled]{cursor:not-allowed;opacity:.5}.site-header__account{-webkit-box-align:center;-ms-flex-align:center;align-items:center;display:-webkit-box;display:-ms-flexbox;display:flex;position:relative;z-index:7}.site-header__account[data-active]{margin-right:-16px}.site-header__account[data-active] .site-header__login{display:none}.site-header__account[data-active] .account__menu{display:block}.site-header__account .account__menu{display:none;height:100%}.site-header__account .account__image{border-radius:50%;height:36px;-o-object-fit:cover;object-fit:cover;width:36px}.site-header__account .account__name{display:none}.site-header__account .account__open-options,.site-header__account .account__options a{font-size:13px;line-height:21px;font-weight:600;text-transform:uppercase;color:#fff}.site-header__account .account__options a{display:block;padding:16px;text-decoration:none;text-align:left}.site-header__account .account__options a:hover{background:#249ad1}.site-header__account .account__open-options{-webkit-box-align:center;-ms-flex-align:center;align-items:center;cursor:pointer;display:-webkit-box;display:-ms-flexbox;display:flex;height:100%;-webkit-box-pack:center;-ms-flex-pack:center;justify-content:center;position:relative;text-transform:uppercase;width:70px}.site-header__account .account__options{display:none}.site-header__account .account__menu:hover .account__options{background:#1190cd;border-radius:0 0 4px 4px;-webkit-box-shadow:0 4px 6px -2px rgba(0,0,0,.2);box-shadow:0 4px 6px -2px rgba(0,0,0,.2);display:block;position:absolute;right:0;width:100vw}.site-header__account .account__menu:hover .account__open-options{background:#249ad1}.site-header__account .account__avatar{background:#0a5a80;border-radius:100%;height:36px;line-height:36px;text-align:center;width:36px}.site-header__account .account__user{padding:16px;background:#249ad1;color:#fff}.site-header__account .account__email{font-size:13px;font-weight:400;line-height:21px}@media screen and (min-width:720px){.site-header__account .account__menu:hover .account__options{width:320px}}@media screen and (min-width:1050px){.site-header__account .account__name{display:none}}.site-header__brand{overflow:hidden;text-indent:100vw;white-space:nowrap;background:url(https://cdn1.vivareal.com/p/14483-4ce4541/v/static/app/svg/styleguide/logo/vivareal-5bcdffca.svg) no-repeat 0 44%;background-size:initial;bottom:0;display:inline-block;height:24px;left:0;margin:auto;position:absolute;right:0;top:0;width:110px}.site-header__landing-page-links,.site-header__publishers{display:none}@media screen and (min-width:720px){.site-header[data-smart-banner]{margin-top:0}}@media screen and (min-width:1050px){.site-header__container{height:56px}.site-header__brand{margin-right:24px;position:relative;width:148px}.site-header__account a,.site-header__landing-page-links a{font-size:13px;line-height:21px;text-transform:uppercase;-webkit-appearance:none;-moz-appearance:none;appearance:none;border-radius:4px;cursor:pointer;display:inline-block;text-align:center;text-decoration:none;background:transparent;color:#fff;border:0;border-radius:0;font-weight:600;height:100%;line-height:56px;padding:0 16px}.site-header__account a:focus,.site-header__landing-page-links a:focus{outline:0}.site-header__account a[disabled],.site-header__landing-page-links a[disabled]{cursor:not-allowed;opacity:.5}.site-header__account a:active,.site-header__landing-page-links a:active{background:rgba(17,144,205,.1)}.site-header__account a:hover,.site-header__landing-page-links a:hover{background:#249ad1}.site-header__landing-page-links{-webkit-box-flex:1;-ms-flex:1 100%;flex:1 100%}.site-header__landing-page-links li{float:left;height:100%}.site-header__landing-page-links .landing-page-link--mktcampaign,.site-header__landing-page-links .landing-page-link--publisher{float:right}.site-header__landing-page-links .landing-page-link--mktcampaign{background:#414141;font-size:24px}.site-header__landing-page-links .landing-page-link--mktcampaign:hover a{background:#5d5c5c}.site-header__landing-page-links{display:block}.site-header__open-menu{display:none}}.site-header .site-header__container{padding-left:16px;padding-right:16px}@media screen and (min-width:720px){.site-header .site-header__container{padding-left:48px;padding-right:48px}}@media screen and (min-width:1050px){.site-header .site-header__container{max-width:none}}.site-menu{background:#fff;color:rgba(0,0,0,.54);width:240px;-webkit-transform:translate3d(-100%,0,0);transform:translate3d(-100%,0,0);-webkit-transition:-webkit-transform .2s ease-out;transition:-webkit-transform .2s ease-out;transition:transform .2s ease-out;transition:transform .2s ease-out,-webkit-transform .2s ease-out;bottom:0;position:absolute;top:0}.site-menu,.site-menu a{font-size:13px;line-height:21px;font-weight:600;text-transform:uppercase}.site-menu a{color:#1190cd;text-decoration:none;display:block;padding:16px}.site-menu header{-webkit-box-align:center;-ms-flex-align:center;align-items:center;background:#1190cd;display:-webkit-box;display:-ms-flexbox;display:flex;height:56px;padding:0 16px;width:240px}.site-menu__wrapper{position:fixed;top:0;left:0;bottom:0;right:0;visibility:hidden;z-index:9}.site-menu__wrapper:before{position:fixed;top:0;left:0;bottom:0;right:0;background:rgba(0,0,0,.4);content:"";z-index:6}.site-menu__close{font-size:13px;font-weight:600;height:36px;line-height:31px;padding:0 12px;vertical-align:middle;-webkit-appearance:none;-moz-appearance:none;appearance:none;border-radius:4px;cursor:pointer;display:inline-block;text-align:center;text-decoration:none;background:transparent;border:2px solid #fff;color:#fff;text-transform:uppercase}.site-menu__close:focus{outline:0}.site-menu__close[disabled]{cursor:not-allowed;opacity:.5}.site-menu__close:active{background:rgba(17,144,205,.1)}.site-menu .landing-page-link--mktcampaign{background:#414141}.site-menu .landing-page-link--mktcampaign a{color:#fff}@media screen and (min-width:1050px){.site-menu,.site-menu__wrapper{display:none}}.site-menu__wrapper[data-active] .site-menu{-webkit-transform:translateZ(0);transform:translateZ(0);z-index:7}.site-menu__wrapper:before{opacity:0;-webkit-transition:opacity .2s ease-out;transition:opacity .2s ease-out}.site-menu__wrapper[data-active]{visibility:visible}.site-menu__wrapper[data-active]:before{opacity:1}.title:after{background-color:#1190cd;border-radius:4px;content:"";display:block;height:4px;left:50%;width:32px;left:0;margin:12px auto 32px 0}.title__title{font-size:32px;font-weight:400;line-height:40px;color:#212121;margin-bottom:16px}.title__see-on-map{font-size:13px;line-height:21px;font-weight:600;text-transform:uppercase;-webkit-appearance:none;-moz-appearance:none;appearance:none;border-radius:4px;cursor:pointer;display:inline-block;text-align:center;text-decoration:none;background:transparent;border:2px solid transparent;color:#1190cd}.title__see-on-map:focus{outline:0}.title__see-on-map[disabled]{cursor:not-allowed;opacity:.5}.title__see-on-map:active{background:rgba(17,144,205,.1)}.title__address{font-size:13px;font-weight:400;line-height:21px;color:#757575;display:inline;margin-right:8px}@media screen and (min-width:1050px){.title__title{font-size:48px;font-weight:400;line-height:56px}}.price{margin-bottom:44px}.price__title{font-size:13px;line-height:21px;font-weight:600;color:#757575;text-transform:uppercase}.price__price-info{font-size:32px;font-weight:400;line-height:40px;font-weight:600}.price__month-label{font-size:16px;font-weight:400;line-height:24px;text-transform:lowercase}@media screen and (max-width:719px){.price__wrapper+.price__wrapper{margin-top:24px}}@media screen and (min-width:720px){.price{display:-webkit-box;display:-ms-flexbox;display:flex}.price__wrapper+.price__wrapper{margin-left:56px}}@media screen and (min-width:1050px){.price{margin-bottom:0}}.features{-webkit-box-align:start;-ms-flex-align:start;align-items:flex-start;display:-webkit-box;display:-ms-flexbox;display:flex;-ms-flex-wrap:wrap;flex-wrap:wrap;min-height:44px}.features__item{font-size:13px;line-height:21px;font-weight:600;color:#757575;margin-bottom:32px;width:50%}.features__item--area:before,.features__item--bathroom:before,.features__item--bedroom:before,.features__item--parking:before,.features__item--real-state:before{margin-right:12px}.features__item--real-state:before{background:url(https://cdn1.vivareal.com/p/14483-4ce4541/v/static/app/svg/styleguide/icons/ic-real-state.svg) no-repeat 50%}.features__item--area:before,.features__item--real-state:before{content:"";display:inline-block;height:100%;min-height:24px;vertical-align:middle;width:24px}.features__item--area:before{background:url(https://cdn1.vivareal.com/p/14483-4ce4541/v/static/app/svg/styleguide/icons/ic-area.svg) no-repeat 50%}.features__item--bedroom:before{background:url(https://cdn1.vivareal.com/p/14483-4ce4541/v/static/app/svg/styleguide/icons/ic-bedroom.svg) no-repeat 50%}.features__item--bathroom:before,.features__item--bedroom:before{content:"";display:inline-block;height:100%;min-height:24px;vertical-align:middle;width:24px}.features__item--bathroom:before{background:url(https://cdn1.vivareal.com/p/14483-4ce4541/v/static/app/svg/styleguide/icons/ic-bathroom.svg) no-repeat 50%}.features__item--parking:before{background:url(https://cdn1.vivareal.com/p/14483-4ce4541/v/static/app/svg/styleguide/icons/ic-parking.svg) no-repeat 50%;content:"";display:inline-block;height:100%;min-height:24px;vertical-align:middle;width:24px}.features__item--bathrooms.detail:before,.features__item--parking-spots.detail:before,.features__item--rooms.detail:before{top:12px}.features__item--bathrooms.detail .detail__value,.features__item--parking-spots.detail .detail__value,.features__item--rooms.detail .detail__value{padding-top:12px;margin-right:4px}.features .request-information__button{margin-left:40px}.feature__extra-info{display:block;margin-left:40px}@media screen and (min-width:720px){hr{margin:24px 0 48px}}@media screen and (min-width:1050px){.features{margin:56px 0 8px}.features__item{margin-bottom:0;width:25%}}.amenities__lightbox{-webkit-box-align:baseline;-ms-flex-align:baseline;align-items:baseline;bottom:0;display:none;-webkit-box-pack:center;-ms-flex-pack:center;justify-content:center;left:0;overflow-y:auto;position:fixed;right:0;top:0;z-index:10}.amenities__lightbox[data-active]{display:-webkit-box;display:-ms-flexbox;display:flex}.amenities__lightbox:before{background:rgba(0,0,0,.4);content:"";cursor:pointer;height:100%;position:fixed;width:100%}.amenities__container{background:#fff;position:relative;z-index:9;padding:24px;overflow:auto;width:100vw}.amenities__button-close{right:24px;top:32px;background:hsla(0,0%,100%,.001);cursor:pointer;outline:none;position:absolute;z-index:10}.amenities__button-close:after{background:url(https://cdn1.vivareal.com/p/14483-4ce4541/v/static/app/svg/styleguide/icons/ic-close-blue.svg) no-repeat 50%;background-size:14px;content:"";display:inline-block;height:100%;min-height:14px;vertical-align:middle;width:14px}@media screen and (max-width:719px){.amenities__container{height:100vh}}@media screen and (min-width:720px){.amenities__lightbox{-webkit-box-align:center;-ms-flex-align:center;align-items:center}.amenities__container{max-width:640px;min-width:300px;width:640px}}.amenities__container{padding:32px}.amenities__lightbox{-webkit-box-align:center;-ms-flex-align:center;align-items:center}.amenities__list{-ms-flex-line-pack:stretch;align-content:stretch;display:-webkit-box;display:-ms-flexbox;display:flex;-ms-flex-wrap:wrap;flex-wrap:wrap;max-height:80%;overflow-y:auto}.amenities__list li{font-size:16px;font-weight:400;line-height:24px;-webkit-box-sizing:border-box;box-sizing:border-box;margin-bottom:12px;padding-right:24px;width:100%}.amenities__title{font-size:20px;font-weight:400;line-height:28px;margin-bottom:32px}.more-amenities{font-size:13px;line-height:21px;font-weight:600;text-transform:uppercase;-webkit-appearance:none;-moz-appearance:none;appearance:none;border-radius:4px;cursor:pointer;display:inline-block;text-align:center;text-decoration:none;background:transparent;border:2px solid transparent;color:#1190cd}.more-amenities:focus{outline:0}.more-amenities[disabled]{cursor:not-allowed;opacity:.5}.more-amenities:active{background:rgba(17,144,205,.1)}@media screen and (max-width:719px){.more-amenities{margin:0 16px;position:relative;top:-16px}}@media screen and (min-width:720px){.amenities__list li{overflow:hidden;text-overflow:ellipsis;white-space:nowrap;font-size:13px;font-weight:400;line-height:21px;width:33.33%}}.hero{background:#fafafa;padding:44px 0}.hero .address-container{margin-bottom:44px}.hero .features{margin:16px 0 0}@media screen and (max-width:719px){.hero .condominium-amenities__container{border-top:1px solid #d8d8d8;margin-top:40px;padding-top:40px}}@media screen and (min-width:720px){.hero{padding:74px 0}.hero .features__item{width:25%}}@media screen and (min-width:1050px){.hero .detail-container{display:-webkit-box;display:-ms-flexbox;display:flex}.hero .condominium-amenities__container{border-left:1px solid #d8d8d8;-webkit-box-flex:1;-ms-flex:1;flex:1;margin-left:56px;padding-left:56px}}.hero{margin-bottom:74px}.hero__container{padding-left:16px;padding-right:16px}@media screen and (min-width:720px){.hero__container{padding-left:48px;padding-right:48px}}@media screen and (min-width:1050px){.hero__container{-webkit-box-sizing:content-box;box-sizing:content-box;margin-left:auto;margin-right:auto;max-width:1024px}}.udp-section__title{font-size:20px;font-weight:400;line-height:28px;text-align:center}.udp-section__title:after{background-color:#1190cd;border-radius:4px;content:"";display:block;height:4px;left:50%;margin:12px auto 32px;width:32px}@media screen and (min-width:1050px){.udp-section__title{font-size:32px;font-weight:400;line-height:40px}.udp-section__title:after{background-color:#1190cd;border-radius:4px;content:"";display:block;height:4px;left:50%;margin:24px auto 64px;width:32px}.udp-section__title[data-left]{font-size:28px;font-weight:400;line-height:36px;text-align:left}.udp-section__title[data-left]:after{left:0;margin-left:0}}.catalog .pills-tabs__wrapper{background:#fff;border-radius:32px;border:2px solid rgba(0,0,0,.12);display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-pack:justify;-ms-flex-pack:justify;justify-content:space-between}.catalog .pills-tabs__button{font-size:13px;line-height:21px;font-weight:600;background:none;border-radius:32px;color:#1190cd;cursor:pointer;display:block;height:auto;line-height:32px;margin:0;outline:none;padding:2px 16px;text-decoration:none;text-transform:uppercase;-webkit-transition:background .3s ease-in-out;transition:background .3s ease-in-out;will-change:background}.catalog .pills-tabs__button:focus,.catalog .pills-tabs__button[data-active]{background:#1190cd;-webkit-box-shadow:0 0 0 2px #1190cd;box-shadow:0 0 0 2px #1190cd;color:#fff}.catalog .condo-unities__container[data-business=RENTAL] [data-business=SALE],.catalog .condo-unities__container[data-business=SALE] [data-business=RENTAL]{display:none}.catalog .condo-unities__title{font-size:13px;line-height:21px;font-weight:600;color:#757575;padding:24px 16px 16px;text-transform:uppercase}.catalog .condo-unity{border-bottom:1px solid rgba(0,0,0,.12);padding:16px;position:relative}.catalog .condo-unity__thumbnail{display:none}.catalog .condo-unity__title{margin-bottom:8px}.catalog .condo-unity__price{font-size:16px;font-weight:400;line-height:24px;display:block}.catalog .condo-unity__price--secondary{font-size:13px;line-height:21px;font-weight:600;color:#757575}.catalog .condo-unity__link{color:#1190cd;text-decoration:none;font-size:13px;line-height:21px;font-weight:600;display:block;text-transform:uppercase}.catalog .condo-unity__link:before{bottom:0;content:"";left:0;position:absolute;right:0;top:0}.catalog .condo-unity__features .features__item{display:inline;margin-right:24px}.catalog .condo-unity__features .features__item:before{display:none}.catalog .condo-unity-features__feature-value{font-weight:600}.catalog .catalog__tabs{margin:24px 16px}.catalog .catalog__tabs .pills-tabs__wrapper{background:#fff;border-radius:32px;border:2px solid rgba(0,0,0,.12);display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-pack:justify;-ms-flex-pack:justify;justify-content:space-between}.catalog .catalog__tabs .pills-tabs__button{font-size:13px;line-height:21px;font-weight:600;background:none;border-radius:32px;color:#1190cd;cursor:pointer;display:block;height:auto;line-height:32px;margin:0;outline:none;padding:2px 16px;text-decoration:none;text-transform:uppercase;-webkit-transition:background .3s ease-in-out;transition:background .3s ease-in-out;will-change:background}.catalog .catalog__tabs .pills-tabs__button:focus,.catalog .catalog__tabs .pills-tabs__button[data-active]{background:#1190cd;-webkit-box-shadow:0 0 0 2px #1190cd;box-shadow:0 0 0 2px #1190cd;color:#fff}@media screen and (max-width:719px){.catalog .condo-unity__features{margin-bottom:16px}}@media screen and (min-width:1050px){.catalog .condo-unity{-webkit-box-align:center;-ms-flex-align:center;align-items:center;border-radius:4px;border:1px solid hsla(0,0%,100%,.001);display:-webkit-box;display:-ms-flexbox;display:flex;margin-bottom:12px;padding:12px;-webkit-transition:-webkit-box-shadow .3s ease-in-out;transition:-webkit-box-shadow .3s ease-in-out;transition:box-shadow .3s ease-in-out;transition:box-shadow .3s ease-in-out,-webkit-box-shadow .3s ease-in-out;will-change:box-shadow}.catalog .condo-unity__thumbnail{display:block;height:56px;position:absolute;width:72px}.catalog .condo-unity__features{-webkit-box-flex:1;-ms-flex:1;flex:1}.catalog .condo-unity__title{margin:0 0 0 88px;min-width:185px;width:20vw}.catalog .condo-unity__title small{font-size:13px;text-transform:lowercase}.catalog .condo-unity__link{font-weight:600;height:48px;line-height:43px;padding:0 16px;vertical-align:middle;-webkit-appearance:none;-moz-appearance:none;appearance:none;border-radius:4px;cursor:pointer;display:inline-block;text-align:center;text-decoration:none;background:transparent;border:2px solid #ff3f00;color:#ff3f00;font-size:16px;text-transform:none}.catalog .condo-unity__link:focus{outline:0}.catalog .condo-unity__link[disabled]{cursor:not-allowed;opacity:.5}.catalog .condo-unity__link:active{background:rgba(17,144,205,.1)}.catalog .condo-unity:hover{border:1px solid #f8f8f8;-webkit-box-shadow:0 4px 8px 0 rgba(0,0,0,.12);box-shadow:0 4px 8px 0 rgba(0,0,0,.12)}.catalog .condo-unity:hover .condo-unity__link{background-color:#ff3f00;color:#fff}.catalog .condo-unity__features .features__item:before{display:inline-block;margin-right:4px}.catalog .condo-features__feature-label{display:none}.catalog .catalog__title{display:block;margin-top:64px}.catalog .catalog__tabs{display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-pack:center;-ms-flex-pack:center;justify-content:center}}@media screen and (min-width:720px){.catalog{padding-left:48px;padding-right:48px}}@media screen and (min-width:1050px){.catalog{-webkit-box-sizing:content-box;box-sizing:content-box;margin-left:auto;margin-right:auto;max-width:1024px}}
    </style>

    <script>!function(a){a.loadCSS=function(b,c,d){var e,f=a.document,g=f.createElement("link");c?e=c:(e=(f.body||f.getElementsByTagName("head")[0]).childNodes,e=e[e.length-1]);var h=f.styleSheets;g.rel="stylesheet",g.href=b,g.media="only x",e.parentNode.insertBefore(g,c?e:e.nextSibling);var i=function(a){for(var b=g.href,c=h.length;c--;)if(h[c].href===b)return a();setTimeout(function(){i(a)})};return g.onloadcssdefined=i,i(function(){g.media=d||"all"}),g};}(window);</script>
    <link rel="preload" as="style" href="https://cdn1.vivareal.com/p/14483-4ce4541/v/static/app/css/condominium-detail.css" onload="this.rel='stylesheet'" onerror="loadCSS(this.href)">
    
    <script>!function(e){if(e.loadCSS){var t=loadCSS.relpreload={};if(t.support=function(){try{return e.document.createElement("link").relList.supports("preload")}catch(t){return!1}},t.poly=function(){for(var t=e.document.getElementsByTagName("link"),r=0;r<t.length;r++){var n=t[r];"preload"===n.rel&&"style"===n.getAttribute("as")&&(e.loadCSS(n.href,n,n.getAttribute("media")),n.rel=null)}},!t.support()){t.poly();var r=e.setInterval(t.poly,300);e.addEventListener&&e.addEventListener("load",function(){t.poly(),e.clearInterval(r)}),e.attachEvent&&e.attachEvent("onload",function(){e.clearInterval(r)})}}}(this);</script>
    
      <script src="https://cdn.ravenjs.com/3.22.1/raven.min.js" defer="defer" crossorigin="anonymous"> </script>
    
      <script src="https://cdn1.vivareal.com/nps/latest/nps.js" defer="defer" crossorigin=""> </script>
    
    <script src="https://cdn1.vivareal.com/p/14483-4ce4541/v/static/app/js/shared.js" defer="defer" crossorigin=""> </script>
    <script src="https://cdn1.vivareal.com/p/14483-4ce4541/v/static/app/js/condominium-detail.js" defer="defer" crossorigin=""> </script>
    <script src="https://cdn1.vivareal.com/p/14483-4ce4541/v/static/app/js/start.js" defer="defer" crossorigin=""> </script>

  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="theme-color" content="#1190cd">
  <meta name="google" content="nositelinkssearchbox">
  
  <link rel="search" type="application/opensearchdescription+xml" href="/opensearchdescription.xml" title="Buscar no Viva Real">
  <link rel="apple-touch-icon" sizes="180x180" href="https://cdn1.vivareal.com/p/14483-4ce4541/v/static/app/img/favicon/apple-touch-icon.png">
  <link rel="icon" type="image/png" href="https://cdn1.vivareal.com/p/14483-4ce4541/v/static/app/img/favicon/favicon-32x32.png" sizes="32x32">
  <link rel="icon" type="image/png" href="https://cdn1.vivareal.com/p/14483-4ce4541/v/static/app/img/favicon/favicon-16x16.png" sizes="16x16">
  <link rel="manifest" href="https://cdn1.vivareal.com/p/14483-4ce4541/v/static/app/img/favicon/manifest.json">
  <meta name="msvalidate.01" content="5DB2670D7BB1D1D3E36C46F7C3D59380">
  <meta name="omniverify" content="omni2c019e0">
  
  <meta property="og:url" content="https://www.vivareal.com.br/condominio/present-alphaville-alphaville-id-6ad8eb6a-e5a8/">
  <meta property="og:type" content="">
  <meta property="og:image" content="">
  
    <meta property="og:title" content="Avenida Ômega, 171 - PRESENT ALPHAVILLE - Viva Real">
    <meta property="og:description" content="Imóveis à venda ou para alugar em PRESENT ALPHAVILLE em Avenida Ômega, 171 no bairro Alphaville.">
    <meta name="description" content="Imóveis à venda ou para alugar em PRESENT ALPHAVILLE em Avenida Ômega, 171 no bairro Alphaville.">
    <title> Avenida Ômega, 171 - PRESENT ALPHAVILLE - Viva Real </title>
  
  
  
  
  
  
  	<link rel="canonical" href="https://www.vivareal.com.br/condominio/present-alphaville-alphaville-id-6ad8eb6a-e5a8/" >
  
  
  
</head>

<body>
  <nav id="js-site-menu" class="js-site-menu">
      <div class="site-menu__wrapper js-site-menu-wrapper">
        <div class="site-menu js-site-menu-panel">
          <header>
            <button class="site-menu__close js-site-menu-close">
              Fechar
            </button>
          </header>
    
          <ul class="site-menu__list">
            <li>
              <a href="/venda/" class="js-track">
                Comprar
              </a>
            </li>
            
            <li>
              <a href="/aluguel/" class="js-track">
                Alugar
              </a>
            </li>
            
            <li>
              <a href="/imoveis-lancamento/"
                class="js-track"> Imóveis Novos </a>
            </li>
            
            <li class="landing-page-link--publisher">
              <a href="/anunciar-imoveis/" class="js-track"> Anunciar imóveis </a>
            </li>
            
          </ul>
        </div>
      </div>
  </nav>

  <header id="js-site-header" class="site-header js-site-header">
    <div class="site-header__container">
      <button class="site-header__open-menu js-open-site-menu">
        Menu
      </button>
    
      <a href="/" class="site-header__brand"
        title="Viva Real - Conecta você ao imóvel de seus sonhos">
        Viva Real - Conecta você ao imóvel de seus sonhos
      </a>
    
      <ul class="site-header__landing-page-links">
        <li>
          <a href="/venda/" class="js-track">
            Comprar
          </a>
        </li>
        
        <li>
          <a href="/aluguel/" class="js-track">
            Alugar
          </a>
        </li>
        
        <li>
          <a href="/imoveis-lancamento/"
            class="js-track"> Imóveis Novos </a>
        </li>
        
        <li class="landing-page-link--publisher">
          <a href="/anunciar-imoveis/" class="js-track"> Anunciar imóveis </a>
        </li>
        
      </ul>
    
      <div class="site-header__account" >
        <a title="Entrar" class="site-header__login js-login"> Entrar </a>
        <div class="account__menu">
          <div class="account__open-options js-loggedButton">
              <div class="account__avatar"></div>
          </div>
    
          <ul class="account__options">
    
            <li class="account__option">
              <a href="/minha-conta/" class="js-track">
                Minha Conta
              </a>
            </li>
    
            <li class="account__option">
              <a href="/minha-conta/?aba=favoritos" class="js-track">
                Imóveis Favoritos
              </a>
            </li>
    
            <li class="account__option">
              <a href="/" title="Sair" class="js-logout">
                Sair
              </a>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </header>

  <main id="js-site-main" class="site-main">
      <aside class="app-smart-banner js-app-smart-banner"></aside>
  
  <div class="hero js-hero">
    <div class="hero__container">
      <div class="address-container">
          <section class="js-condominium-title title">
            <div class="title__content-wrapper">
              <h1 class="title__title js-title-view">
                PRESENT ALPHAVILLE
              </h1>
              <div class="title__address-wrapper">
                <p class="title__address js-address">Avenida Ômega, 171 - Alphaville, Barueri - SP</p>
                <a class="title__see-on-map js-see-on-map" href="#">Ver no mapa</a>
              </div>
            </div>
          </section>
      </div>
  
      <div class="detail-container">
        <div class="price js-price">
            <div class="price__wrapper">
              <p class="price__title">Preço a partir de</p>
              <h3 class="price__price-info js-price-sale">
                R$ 593.681
              </h3>
            </div>
        
            <div class="price__wrapper">
              <p class="price__title">Aluguel a partir de</p>
              <h3 class="price__price-info js-price-rent">
                R$ 4.000
                  <span class="price__month-label">/mês</span>
              </h3>
            </div>
        </div>
  
        <div class="condominium-amenities__container">
          <ul class="features">
            <li class="features__item features__item--area js-area" title="Área">
                <span>85</span> a <span>112</span>m²
            </li>
          
            <li class="features__item features__item--bedroom js-bedrooms" title="Quartos">
                <span>2</span>-<span>3</span>
                quartos
            </li>
          
            <li class="features__item features__item--bathroom js-bathrooms" title="Banheiros">
                <span>2</span>
                banheiros
            </li>
          
            <li class="features__item features__item--parking js-parking" title="Vagas">
                <span>2</span>
                vagas
            </li>
          </ul>
  
            <div class="js-more-amenities">
              <button class="more-amenities js-amenities-button">Ver mais características (7)</button>
          
              <div class="amenities__lightbox js-amenities-modal">
                <div class="amenities__container">
                  <h3 class="amenities__title">Características</h3>
                  <button class="amenities__button-close js-close"></button>
          
                  <ul class="amenities__list">
                        <li title="Salão de festas"> Salão de festas </li>
                        <li title="Piscina para adulto"> Piscina para adulto </li>
                        <li title="Churrasqueira"> Churrasqueira </li>
                        <li title="Sauna"> Sauna </li>
                        <li title="Salão de jogos"> Salão de jogos </li>
                        <li title="Playground"> Playground </li>
                  </ul>
                </div>
              </div>
            </div>
        </div>
      </div>
    </div>
  </div>
  
  <div class="catalog" id="js-catalog">
      <section class="condo-detail__catalog">
        <h2 class="udp-section__title">
          Unidades do condomínio
        </h2>
        
          <section class="catalog__tabs">
            <nav class="pills-tabs__wrapper">
              <button
                data-active
                class="pills-tabs__button js-tab-units js-tab-menu-item">
                Todos
              </button>
        
              <button
                data-business="RENTAL"
                class="pills-tabs__button js-tab-units js-tab-menu-item">
                Aluguel
              </button>
        
              <button
                data-business="SALE"
                class="pills-tabs__button js-tab-units js-tab-menu-item">
                Venda
              </button>
            </nav>
          </section>
    
        <section class="tab__content">
          <div id="all-units" class="tab__content-item condo-unities__container js-content-item js-content-units" data-active>
              <section class="condo-unities js-condo-list js-filters js-filters--2" data-active>
                <h4 class="condo-unities__title" data-business="RENTAL_SALE">
                  2 Quartos (24 unidades)
                </h4>
              
                <ul class="condo-unities__list">
                    <li class="condo-unity" data-business="RENTAL">
                          <img src="https://resizedimgs.vivareal.com/fit-in/72x56/vr.images.sp/c409d3140666558503f916cf4d4eb787.jpg"
                            alt="Unidade do condomínio  - Avenida Ômega, 171 - Alphaville 18 Forte, Barueri - SP" class="condo-unity__thumbnail js-gallery-fullscreen-toggle">
              
                        <h5 class="condo-unity__title">
                                <span class="condo-unity__price ">
                                  Aluguel R$ 4.000<small>/Mês</small>
                                </span>
                        </h5>
              
                        <ul class="condo-unity__features">
                              <li class="features__item features__item--area" title="Área ">
                                <span class="condo-features__feature-value">
                                   112<span>m²</span> 
                                </span>
                            
                              </li>
              
                              <li class="features__item features__item--bedroom" title="Quartos">
                                <span class="condo-features__feature-value">
                                   2 
                                </span>
                            
                                  <span class="condo-features__feature-label">
                                    Quartos
                                  </span>
                              </li>
              
                              <li class="features__item features__item--bathroom" title="Banheiros">
                                <span class="condo-features__feature-value">
                                   3 
                                </span>
                            
                                  <span class="condo-features__feature-label">
                                    Banheiros
                                  </span>
                              </li>
              
                              <li class="features__item features__item--parking" title="Vagas">
                                <span class="condo-features__feature-value">
                                   2 
                                </span>
                            
                                  <span class="condo-features__feature-label">
                                    Vagas
                                  </span>
                              </li>
                        </ul>
              
                      <a class="condo-unity__link js-property-link"
                        data-id="2436011588"
                        data-position="1"
                        href="/imovel/apartamento-2-quartos-alphaville-18-forte-bairros-barueri-com-garagem-112m2-aluguel-RS4000-id-2436011588/">Ver detalhes</a>
                    </li>
                    <li class="condo-unity" data-business="RENTAL_SALE">
                          <img src="https://resizedimgs.vivareal.com/fit-in/72x56/vr.images.sp/caecf904027ac7c5773579ff0bcdc81e.jpg"
                            alt="Unidade do condomínio  - Avenida Ômega - Empresarial 18 do Forte, Barueri - SP" class="condo-unity__thumbnail js-gallery-fullscreen-toggle">
              
                        <h5 class="condo-unity__title">
                                <span class="condo-unity__price  condo-unity__price--secondary ">
                                  Aluguel R$ 5.877<small>/Mês</small>
                                </span>
                              <span class="condo-unity__price">
                                Venda R$ 705.268
                              </span>
                        </h5>
              
                        <ul class="condo-unity__features">
                              <li class="features__item features__item--area" title="Área ">
                                <span class="condo-features__feature-value">
                                   85<span>m²</span> 
                                </span>
                            
                              </li>
              
                              <li class="features__item features__item--bedroom" title="Quartos">
                                <span class="condo-features__feature-value">
                                   2 
                                </span>
                            
                                  <span class="condo-features__feature-label">
                                    Quartos
                                  </span>
                              </li>
              
                              <li class="features__item features__item--bathroom" title="Banheiros">
                                <span class="condo-features__feature-value">
                                   2 
                                </span>
                            
                                  <span class="condo-features__feature-label">
                                    Banheiros
                                  </span>
                              </li>
              
                              <li class="features__item features__item--parking" title="Vagas">
                                <span class="condo-features__feature-value">
                                   2 
                                </span>
                            
                                  <span class="condo-features__feature-label">
                                    Vagas
                                  </span>
                              </li>
                        </ul>
              
                      <a class="condo-unity__link js-property-link"
                        data-id="1037532575"
                        data-position="2"
                        href="/imovel/apartamento-2-quartos-empresarial-18-do-forte-bairros-barueri-com-garagem-85m2-venda-RS705268-id-1037532575/">Ver detalhes</a>
                    </li>
                    <li class="condo-unity" data-business="RENTAL_SALE">
                          <img src="https://resizedimgs.vivareal.com/fit-in/72x56/vr.images.sp/1c863a9aedaaad5abfd431b2c538d19c.jpg"
                            alt="Unidade do condomínio  - Avenida Ômega - Empresarial 18 do Forte, Barueri - SP" class="condo-unity__thumbnail js-gallery-fullscreen-toggle">
              
                        <h5 class="condo-unity__title">
                                <span class="condo-unity__price  condo-unity__price--secondary ">
                                  Aluguel R$ 6.030<small>/Mês</small>
                                </span>
                              <span class="condo-unity__price">
                                Venda R$ 723.569
                              </span>
                        </h5>
              
                        <ul class="condo-unity__features">
                              <li class="features__item features__item--area" title="Área ">
                                <span class="condo-features__feature-value">
                                   85<span>m²</span> 
                                </span>
                            
                              </li>
              
                              <li class="features__item features__item--bedroom" title="Quartos">
                                <span class="condo-features__feature-value">
                                   2 
                                </span>
                            
                                  <span class="condo-features__feature-label">
                                    Quartos
                                  </span>
                              </li>
              
                              <li class="features__item features__item--bathroom" title="Banheiros">
                                <span class="condo-features__feature-value">
                                   2 
                                </span>
                            
                                  <span class="condo-features__feature-label">
                                    Banheiros
                                  </span>
                              </li>
              
                              <li class="features__item features__item--parking" title="Vagas">
                                <span class="condo-features__feature-value">
                                   2 
                                </span>
                            
                                  <span class="condo-features__feature-label">
                                    Vagas
                                  </span>
                              </li>
                        </ul>
              
                      <a class="condo-unity__link js-property-link"
                        data-id="1037532394"
                        data-position="3"
                        href="/imovel/apartamento-2-quartos-empresarial-18-do-forte-bairros-barueri-com-garagem-85m2-venda-RS723569-id-1037532394/">Ver detalhes</a>
                    </li>
                    <li class="condo-unity" data-business="SALE">
                          <img src="https://resizedimgs.vivareal.com/fit-in/72x56/vr.images.sp/61266525c383243f55c66b2fa3440141.jpg"
                            alt="Unidade do condomínio  - Avenida Ômega, 171 - Alphaville 18 Forte, Barueri - SP" class="condo-unity__thumbnail js-gallery-fullscreen-toggle">
              
                        <h5 class="condo-unity__title">
                              <span class="condo-unity__price">
                                Venda R$ 593.681
                              </span>
                        </h5>
              
                        <ul class="condo-unity__features">
                              <li class="features__item features__item--area" title="Área ">
                                <span class="condo-features__feature-value">
                                   85<span>m²</span> 
                                </span>
                            
                              </li>
              
                              <li class="features__item features__item--bedroom" title="Quartos">
                                <span class="condo-features__feature-value">
                                   2 
                                </span>
                            
                                  <span class="condo-features__feature-label">
                                    Quartos
                                  </span>
                              </li>
              
                              <li class="features__item features__item--bathroom" title="Banheiros">
                                <span class="condo-features__feature-value">
                                   3 
                                </span>
                            
                                  <span class="condo-features__feature-label">
                                    Banheiros
                                  </span>
                              </li>
              
                              <li class="features__item features__item--parking" title="Vagas">
                                <span class="condo-features__feature-value">
                                   2 
                                </span>
                            
                                  <span class="condo-features__feature-label">
                                    Vagas
                                  </span>
                              </li>
                        </ul>
              
                      <a class="condo-unity__link js-property-link"
                        data-id="94794243"
                        data-position="4"
                        href="/imovel/apartamento-2-quartos-alphaville-18-forte-bairros-barueri-com-garagem-85m2-venda-RS593681-id-94794243/">Ver detalhes</a>
                    </li>
                    <li class="condo-unity" data-business="SALE">
                          <img src="https://resizedimgs.vivareal.com/fit-in/72x56/vr.images.sp/98876f82dc5cf8065ba96d5978e3d40b.jpg"
                            alt="Unidade do condomínio  - Avenida Ômega, 171 - Melville Empresarial Ii, Barueri - SP" class="condo-unity__thumbnail js-gallery-fullscreen-toggle">
              
                        <h5 class="condo-unity__title">
                              <span class="condo-unity__price">
                                Venda R$ 617.000
                              </span>
                        </h5>
              
                        <ul class="condo-unity__features">
                              <li class="features__item features__item--area" title="Área ">
                                <span class="condo-features__feature-value">
                                   85<span>m²</span> 
                                </span>
                            
                              </li>
              
                              <li class="features__item features__item--bedroom" title="Quartos">
                                <span class="condo-features__feature-value">
                                   2 
                                </span>
                            
                                  <span class="condo-features__feature-label">
                                    Quartos
                                  </span>
                              </li>
              
                              <li class="features__item features__item--bathroom" title="Banheiros">
                                <span class="condo-features__feature-value">
                                   3 
                                </span>
                            
                                  <span class="condo-features__feature-label">
                                    Banheiros
                                  </span>
                              </li>
              
                              <li class="features__item features__item--parking" title="Vagas">
                                <span class="condo-features__feature-value">
                                   2 
                                </span>
                            
                                  <span class="condo-features__feature-label">
                                    Vagas
                                  </span>
                              </li>
                        </ul>
              
                      <a class="condo-unity__link js-property-link"
                        data-id="2444438277"
                        data-position="5"
                        href="/imovel/apartamento-2-quartos-melville-empresarial-ii-bairros-barueri-com-garagem-85m2-venda-RS617000-id-2444438277/">Ver detalhes</a>
                    </li>
                    <li class="condo-unity" data-business="SALE">
                          <img src="https://resizedimgs.vivareal.com/fit-in/72x56/vr.images.sp/ecfbd8977a49e7ba993b2070b5c84764.jpg"
                            alt="Unidade do condomínio  - Avenida Ômega, 171 - Alphaville 18 Forte, Barueri - SP" class="condo-unity__thumbnail js-gallery-fullscreen-toggle">
              
                        <h5 class="condo-unity__title">
                              <span class="condo-unity__price">
                                Venda R$ 627.800
                              </span>
                        </h5>
              
                        <ul class="condo-unity__features">
                              <li class="features__item features__item--area" title="Área ">
                                <span class="condo-features__feature-value">
                                   85<span>m²</span> 
                                </span>
                            
                              </li>
              
                              <li class="features__item features__item--bedroom" title="Quartos">
                                <span class="condo-features__feature-value">
                                   2 
                                </span>
                            
                                  <span class="condo-features__feature-label">
                                    Quartos
                                  </span>
                              </li>
              
                              <li class="features__item features__item--bathroom" title="Banheiros">
                                <span class="condo-features__feature-value">
                                   2 
                                </span>
                            
                                  <span class="condo-features__feature-label">
                                    Banheiros
                                  </span>
                              </li>
              
                              <li class="features__item features__item--parking" title="Vagas">
                                <span class="condo-features__feature-value">
                                   2 
                                </span>
                            
                                  <span class="condo-features__feature-label">
                                    Vagas
                                  </span>
                              </li>
                        </ul>
              
                      <a class="condo-unity__link js-property-link"
                        data-id="1039335185"
                        data-position="6"
                        href="/imovel/apartamento-2-quartos-alphaville-18-forte-bairros-barueri-com-garagem-85m2-venda-RS627800-id-1039335185/">Ver detalhes</a>
                    </li>
                    <li class="condo-unity" data-business="SALE">
                          <img src="https://resizedimgs.vivareal.com/fit-in/72x56/vr.images.sp/5e88780f87e77e567915ac64eb97d43d.jpg"
                            alt="Unidade do condomínio  - Empresarial 18 do Forte, Barueri - SP" class="condo-unity__thumbnail js-gallery-fullscreen-toggle">
              
                        <h5 class="condo-unity__title">
                              <span class="condo-unity__price">
                                Venda R$ 627.800
                              </span>
                        </h5>
              
                        <ul class="condo-unity__features">
                              <li class="features__item features__item--area" title="Área ">
                                <span class="condo-features__feature-value">
                                   85<span>m²</span> 
                                </span>
                            
                              </li>
              
                              <li class="features__item features__item--bedroom" title="Quartos">
                                <span class="condo-features__feature-value">
                                   2 
                                </span>
                            
                                  <span class="condo-features__feature-label">
                                    Quartos
                                  </span>
                              </li>
              
                              <li class="features__item features__item--bathroom" title="Banheiros">
                                <span class="condo-features__feature-value">
                                   2 
                                </span>
                            
                                  <span class="condo-features__feature-label">
                                    Banheiros
                                  </span>
                              </li>
              
                              <li class="features__item features__item--parking" title="Vagas">
                                <span class="condo-features__feature-value">
                                   2 
                                </span>
                            
                                  <span class="condo-features__feature-label">
                                    Vagas
                                  </span>
                              </li>
                        </ul>
              
                      <a class="condo-unity__link js-property-link"
                        data-id="2427889480"
                        data-position="7"
                        href="/imovel/apartamento-2-quartos-empresarial-18-do-forte-bairros-barueri-com-garagem-85m2-venda-RS627800-id-2427889480/">Ver detalhes</a>
                    </li>
                    <li class="condo-unity" data-business="SALE">
                          <img src="https://resizedimgs.vivareal.com/fit-in/72x56/vr.images.sp/f2dd53e89055b8b349d0421671f992b1.jpg"
                            alt="Unidade do condomínio  - Avenida Ômega, 171 - Empresarial 18 do Forte, Barueri - SP" class="condo-unity__thumbnail js-gallery-fullscreen-toggle">
              
                        <h5 class="condo-unity__title">
                              <span class="condo-unity__price">
                                Venda R$ 631.270
                              </span>
                        </h5>
              
                        <ul class="condo-unity__features">
                              <li class="features__item features__item--area" title="Área ">
                                <span class="condo-features__feature-value">
                                   85<span>m²</span> 
                                </span>
                            
                              </li>
              
                              <li class="features__item features__item--bedroom" title="Quartos">
                                <span class="condo-features__feature-value">
                                   2 
                                </span>
                            
                                  <span class="condo-features__feature-label">
                                    Quartos
                                  </span>
                              </li>
              
                              <li class="features__item features__item--bathroom" title="Banheiros">
                                <span class="condo-features__feature-value">
                                   2 
                                </span>
                            
                                  <span class="condo-features__feature-label">
                                    Banheiros
                                  </span>
                              </li>
              
                              <li class="features__item features__item--parking" title="Vagas">
                                <span class="condo-features__feature-value">
                                   2 
                                </span>
                            
                                  <span class="condo-features__feature-label">
                                    Vagas
                                  </span>
                              </li>
                        </ul>
              
                      <a class="condo-unity__link js-property-link"
                        data-id="95308375"
                        data-position="8"
                        href="/imovel/apartamento-2-quartos-empresarial-18-do-forte-bairros-barueri-com-garagem-85m2-venda-RS631270-id-95308375/">Ver detalhes</a>
                    </li>
                    <li class="condo-unity" data-business="SALE">
                          <img src="https://resizedimgs.vivareal.com/fit-in/72x56/vr.images.sp/2cf7b7892466113f52f289e2d96f144f.jpg"
                            alt="Unidade do condomínio  - Avenida Ômega - Alphaville, Barueri - SP" class="condo-unity__thumbnail js-gallery-fullscreen-toggle">
              
                        <h5 class="condo-unity__title">
                              <span class="condo-unity__price">
                                Venda R$ 650.000
                              </span>
                        </h5>
              
                        <ul class="condo-unity__features">
                              <li class="features__item features__item--area" title="Área ">
                                <span class="condo-features__feature-value">
                                   85<span>m²</span> 
                                </span>
                            
                              </li>
              
                              <li class="features__item features__item--bedroom" title="Quartos">
                                <span class="condo-features__feature-value">
                                   2 
                                </span>
                            
                                  <span class="condo-features__feature-label">
                                    Quartos
                                  </span>
                              </li>
              
                              <li class="features__item features__item--bathroom" title="Banheiros">
                                <span class="condo-features__feature-value">
                                   3 
                                </span>
                            
                                  <span class="condo-features__feature-label">
                                    Banheiros
                                  </span>
                              </li>
              
                              <li class="features__item features__item--parking" title="Vagas">
                                <span class="condo-features__feature-value">
                                   2 
                                </span>
                            
                                  <span class="condo-features__feature-label">
                                    Vagas
                                  </span>
                              </li>
                        </ul>
              
                      <a class="condo-unity__link js-property-link"
                        data-id="2123195473"
                        data-position="9"
                        href="/imovel/apartamento-2-quartos-alphaville-bairros-barueri-com-garagem-85m2-venda-RS650000-id-2123195473/">Ver detalhes</a>
                    </li>
                    <li class="condo-unity" data-business="SALE">
                          <img src="https://resizedimgs.vivareal.com/fit-in/72x56/vr.images.sp/d04b73e43c1c1b74b9a7aae3ea4fb48b.jpg"
                            alt="Unidade do condomínio  - Avenida Ômega, 171 - Empresarial 18 do Forte, Barueri - SP" class="condo-unity__thumbnail js-gallery-fullscreen-toggle">
              
                        <h5 class="condo-unity__title">
                              <span class="condo-unity__price">
                                Venda R$ 651.000
                              </span>
                        </h5>
              
                        <ul class="condo-unity__features">
                              <li class="features__item features__item--area" title="Área ">
                                <span class="condo-features__feature-value">
                                   85<span>m²</span> 
                                </span>
                            
                              </li>
              
                              <li class="features__item features__item--bedroom" title="Quartos">
                                <span class="condo-features__feature-value">
                                   2 
                                </span>
                            
                                  <span class="condo-features__feature-label">
                                    Quartos
                                  </span>
                              </li>
              
                              <li class="features__item features__item--bathroom" title="Banheiros">
                                <span class="condo-features__feature-value">
                                   3 
                                </span>
                            
                                  <span class="condo-features__feature-label">
                                    Banheiros
                                  </span>
                              </li>
              
                              <li class="features__item features__item--parking" title="Vagas">
                                <span class="condo-features__feature-value">
                                   2 
                                </span>
                            
                                  <span class="condo-features__feature-label">
                                    Vagas
                                  </span>
                              </li>
                        </ul>
              
                      <a class="condo-unity__link js-property-link"
                        data-id="1037386790"
                        data-position="10"
                        href="/imovel/apartamento-2-quartos-empresarial-18-do-forte-bairros-barueri-com-garagem-85m2-venda-RS651000-id-1037386790/">Ver detalhes</a>
                    </li>
                    <li class="condo-unity" data-business="SALE">
                          <img src="https://resizedimgs.vivareal.com/fit-in/72x56/vr.images.sp/97c54eca7410a63265add519c2b6283d.jpg"
                            alt="Unidade do condomínio  - Avenida Ômega - Empresarial 18 do Forte, Barueri - SP" class="condo-unity__thumbnail js-gallery-fullscreen-toggle">
              
                        <h5 class="condo-unity__title">
                              <span class="condo-unity__price">
                                Venda R$ 665.000
                              </span>
                        </h5>
              
                        <ul class="condo-unity__features">
                              <li class="features__item features__item--area" title="Área ">
                                <span class="condo-features__feature-value">
                                   85<span>m²</span> 
                                </span>
                            
                              </li>
              
                              <li class="features__item features__item--bedroom" title="Quartos">
                                <span class="condo-features__feature-value">
                                   2 
                                </span>
                            
                                  <span class="condo-features__feature-label">
                                    Quartos
                                  </span>
                              </li>
              
                              <li class="features__item features__item--bathroom" title="Banheiros">
                                <span class="condo-features__feature-value">
                                   2 
                                </span>
                            
                                  <span class="condo-features__feature-label">
                                    Banheiros
                                  </span>
                              </li>
              
                              <li class="features__item features__item--parking" title="Vagas">
                                <span class="condo-features__feature-value">
                                   2 
                                </span>
                            
                                  <span class="condo-features__feature-label">
                                    Vagas
                                  </span>
                              </li>
                        </ul>
              
                      <a class="condo-unity__link js-property-link"
                        data-id="95060085"
                        data-position="11"
                        href="/imovel/apartamento-2-quartos-empresarial-18-do-forte-bairros-barueri-com-garagem-85m2-venda-RS665000-id-95060085/">Ver detalhes</a>
                    </li>
                    <li class="condo-unity" data-business="SALE">
                          <img src="https://resizedimgs.vivareal.com/fit-in/72x56/vr.images.sp/35e4badb51ab3efbbe6d2107292937f8.jpg"
                            alt="Unidade do condomínio  - Avenida Ômega - Empresarial 18 do Forte, Barueri - SP" class="condo-unity__thumbnail js-gallery-fullscreen-toggle">
              
                        <h5 class="condo-unity__title">
                              <span class="condo-unity__price">
                                Venda R$ 700.000
                              </span>
                        </h5>
              
                        <ul class="condo-unity__features">
                              <li class="features__item features__item--area" title="Área ">
                                <span class="condo-features__feature-value">
                                   85<span>m²</span> 
                                </span>
                            
                              </li>
              
                              <li class="features__item features__item--bedroom" title="Quartos">
                                <span class="condo-features__feature-value">
                                   2 
                                </span>
                            
                                  <span class="condo-features__feature-label">
                                    Quartos
                                  </span>
                              </li>
              
                              <li class="features__item features__item--bathroom" title="Banheiros">
                                <span class="condo-features__feature-value">
                                   3 
                                </span>
                            
                                  <span class="condo-features__feature-label">
                                    Banheiros
                                  </span>
                              </li>
              
                              <li class="features__item features__item--parking" title="Vagas">
                                <span class="condo-features__feature-value">
                                   2 
                                </span>
                            
                                  <span class="condo-features__feature-label">
                                    Vagas
                                  </span>
                              </li>
                        </ul>
              
                      <a class="condo-unity__link js-property-link"
                        data-id="93821081"
                        data-position="12"
                        href="/imovel/apartamento-2-quartos-empresarial-18-do-forte-bairros-barueri-com-garagem-85m2-venda-RS700000-id-93821081/">Ver detalhes</a>
                    </li>
                    <li class="condo-unity" data-business="SALE">
                          <img src="https://resizedimgs.vivareal.com/fit-in/72x56/vr.images.sp/c880eb2e4475dd9badc3ced2b9ff1c59.jpg"
                            alt="Unidade do condomínio  - Melville Empresarial Ii, Barueri - SP" class="condo-unity__thumbnail js-gallery-fullscreen-toggle">
              
                        <h5 class="condo-unity__title">
                              <span class="condo-unity__price">
                                Venda R$ 749.999
                              </span>
                        </h5>
              
                        <ul class="condo-unity__features">
                              <li class="features__item features__item--area" title="Área ">
                                <span class="condo-features__feature-value">
                                   85<span>m²</span> 
                                </span>
                            
                              </li>
              
                              <li class="features__item features__item--bedroom" title="Quartos">
                                <span class="condo-features__feature-value">
                                   2 
                                </span>
                            
                                  <span class="condo-features__feature-label">
                                    Quartos
                                  </span>
                              </li>
              
                              <li class="features__item features__item--bathroom" title="Banheiros">
                                <span class="condo-features__feature-value">
                                   3 
                                </span>
                            
                                  <span class="condo-features__feature-label">
                                    Banheiros
                                  </span>
                              </li>
              
                              <li class="features__item features__item--parking" title="Vagas">
                                <span class="condo-features__feature-value">
                                   2 
                                </span>
                            
                                  <span class="condo-features__feature-label">
                                    Vagas
                                  </span>
                              </li>
                        </ul>
              
                      <a class="condo-unity__link js-property-link"
                        data-id="2447512592"
                        data-position="13"
                        href="/imovel/apartamento-2-quartos-melville-empresarial-ii-bairros-barueri-com-garagem-85m2-venda-RS749999-id-2447512592/">Ver detalhes</a>
                    </li>
                    <li class="condo-unity" data-business="SALE">
                          <img src="https://resizedimgs.vivareal.com/fit-in/72x56/vr.images.sp/3fc3a3d2f568e64d3c721ddb03dac3f6.jpg"
                            alt="Unidade do condomínio  - Alphaville, Barueri - SP" class="condo-unity__thumbnail js-gallery-fullscreen-toggle">
              
                        <h5 class="condo-unity__title">
                              <span class="condo-unity__price">
                                Venda R$ 750.000
                              </span>
                        </h5>
              
                        <ul class="condo-unity__features">
                              <li class="features__item features__item--area" title="Área ">
                                <span class="condo-features__feature-value">
                                   112<span>m²</span> 
                                </span>
                            
                              </li>
              
                              <li class="features__item features__item--bedroom" title="Quartos">
                                <span class="condo-features__feature-value">
                                   2 
                                </span>
                            
                                  <span class="condo-features__feature-label">
                                    Quartos
                                  </span>
                              </li>
              
                              <li class="features__item features__item--bathroom" title="Banheiros">
                                <span class="condo-features__feature-value">
                                   2 
                                </span>
                            
                                  <span class="condo-features__feature-label">
                                    Banheiros
                                  </span>
                              </li>
              
                              <li class="features__item features__item--parking" title="Vagas">
                                <span class="condo-features__feature-value">
                                   2 
                                </span>
                            
                                  <span class="condo-features__feature-label">
                                    Vagas
                                  </span>
                              </li>
                        </ul>
              
                      <a class="condo-unity__link js-property-link"
                        data-id="2445099699"
                        data-position="14"
                        href="/imovel/apartamento-2-quartos-alphaville-bairros-barueri-com-garagem-112m2-venda-RS750000-id-2445099699/">Ver detalhes</a>
                    </li>
                    <li class="condo-unity" data-business="SALE">
                          <img src="https://resizedimgs.vivareal.com/fit-in/72x56/vr.images.sp/302c247860b8febf409daadd0200c3b3.jpg"
                            alt="Unidade do condomínio  - Avenida Ômega, 171 - Empresarial 18 do Forte, Barueri - SP" class="condo-unity__thumbnail js-gallery-fullscreen-toggle">
              
                        <h5 class="condo-unity__title">
                              <span class="condo-unity__price">
                                Venda R$ 770.000
                              </span>
                        </h5>
              
                        <ul class="condo-unity__features">
                              <li class="features__item features__item--area" title="Área ">
                                <span class="condo-features__feature-value">
                                   112<span>m²</span> 
                                </span>
                            
                              </li>
              
                              <li class="features__item features__item--bedroom" title="Quartos">
                                <span class="condo-features__feature-value">
                                   2 
                                </span>
                            
                                  <span class="condo-features__feature-label">
                                    Quartos
                                  </span>
                              </li>
              
                              <li class="features__item features__item--bathroom" title="Banheiros">
                                <span class="condo-features__feature-value">
                                   3 
                                </span>
                            
                                  <span class="condo-features__feature-label">
                                    Banheiros
                                  </span>
                              </li>
              
                              <li class="features__item features__item--parking" title="Vagas">
                                <span class="condo-features__feature-value">
                                   2 
                                </span>
                            
                                  <span class="condo-features__feature-label">
                                    Vagas
                                  </span>
                              </li>
                        </ul>
              
                      <a class="condo-unity__link js-property-link"
                        data-id="2443122691"
                        data-position="15"
                        href="/imovel/apartamento-2-quartos-empresarial-18-do-forte-bairros-barueri-com-garagem-112m2-venda-RS770000-id-2443122691/">Ver detalhes</a>
                    </li>
                    <li class="condo-unity" data-business="SALE">
                          <img src="https://resizedimgs.vivareal.com/fit-in/72x56/vr.images.sp/2b0ca191818f2dd752d96c08b34de843.jpg"
                            alt="Unidade do condomínio  - Empresarial 18 do Forte, Barueri - SP" class="condo-unity__thumbnail js-gallery-fullscreen-toggle">
              
                        <h5 class="condo-unity__title">
                              <span class="condo-unity__price">
                                Venda R$ 770.000
                              </span>
                        </h5>
              
                        <ul class="condo-unity__features">
                              <li class="features__item features__item--area" title="Área ">
                                <span class="condo-features__feature-value">
                                   112<span>m²</span> 
                                </span>
                            
                              </li>
              
                              <li class="features__item features__item--bedroom" title="Quartos">
                                <span class="condo-features__feature-value">
                                   2 
                                </span>
                            
                                  <span class="condo-features__feature-label">
                                    Quartos
                                  </span>
                              </li>
              
                              <li class="features__item features__item--bathroom" title="Banheiros">
                                <span class="condo-features__feature-value">
                                   3 
                                </span>
                            
                                  <span class="condo-features__feature-label">
                                    Banheiros
                                  </span>
                              </li>
              
                              <li class="features__item features__item--parking" title="Vagas">
                                <span class="condo-features__feature-value">
                                   2 
                                </span>
                            
                                  <span class="condo-features__feature-label">
                                    Vagas
                                  </span>
                              </li>
                        </ul>
              
                      <a class="condo-unity__link js-property-link"
                        data-id="2444095382"
                        data-position="16"
                        href="/imovel/apartamento-2-quartos-empresarial-18-do-forte-bairros-barueri-com-garagem-112m2-venda-RS770000-id-2444095382/">Ver detalhes</a>
                    </li>
                    <li class="condo-unity" data-business="SALE">
                          <img src="https://resizedimgs.vivareal.com/fit-in/72x56/vr.images.sp/ce248efe03b3e3aa2a1a58d5552b227a.jpg"
                            alt="Unidade do condomínio  - Alphaville, Barueri - SP" class="condo-unity__thumbnail js-gallery-fullscreen-toggle">
              
                        <h5 class="condo-unity__title">
                              <span class="condo-unity__price">
                                Venda R$ 799.999
                              </span>
                        </h5>
              
                        <ul class="condo-unity__features">
                              <li class="features__item features__item--area" title="Área ">
                                <span class="condo-features__feature-value">
                                   112<span>m²</span> 
                                </span>
                            
                              </li>
              
                              <li class="features__item features__item--bedroom" title="Quartos">
                                <span class="condo-features__feature-value">
                                   2 
                                </span>
                            
                                  <span class="condo-features__feature-label">
                                    Quartos
                                  </span>
                              </li>
              
                              <li class="features__item features__item--bathroom" title="Banheiros">
                                <span class="condo-features__feature-value">
                                   4 
                                </span>
                            
                                  <span class="condo-features__feature-label">
                                    Banheiros
                                  </span>
                              </li>
              
                              <li class="features__item features__item--parking" title="Vagas">
                                <span class="condo-features__feature-value">
                                   2 
                                </span>
                            
                                  <span class="condo-features__feature-label">
                                    Vagas
                                  </span>
                              </li>
                        </ul>
              
                      <a class="condo-unity__link js-property-link"
                        data-id="1177095478"
                        data-position="17"
                        href="/imovel/apartamento-2-quartos-alphaville-bairros-barueri-com-garagem-112m2-venda-RS799999-id-1177095478/">Ver detalhes</a>
                    </li>
                    <li class="condo-unity" data-business="SALE">
                          <img src="https://resizedimgs.vivareal.com/fit-in/72x56/vr.images.sp/b3cdaa9cd56457a1c69cef778fc874d6.jpg"
                            alt="Unidade do condomínio  - Avenida Ômega - Empresarial 18 do Forte, Barueri - SP" class="condo-unity__thumbnail js-gallery-fullscreen-toggle">
              
                        <h5 class="condo-unity__title">
                              <span class="condo-unity__price">
                                Venda R$ 800.000
                              </span>
                        </h5>
              
                        <ul class="condo-unity__features">
                              <li class="features__item features__item--area" title="Área ">
                                <span class="condo-features__feature-value">
                                   112<span>m²</span> 
                                </span>
                            
                              </li>
              
                              <li class="features__item features__item--bedroom" title="Quartos">
                                <span class="condo-features__feature-value">
                                   2 
                                </span>
                            
                                  <span class="condo-features__feature-label">
                                    Quartos
                                  </span>
                              </li>
              
                              <li class="features__item features__item--bathroom" title="Banheiros">
                                <span class="condo-features__feature-value">
                                   3 
                                </span>
                            
                                  <span class="condo-features__feature-label">
                                    Banheiros
                                  </span>
                              </li>
              
                              <li class="features__item features__item--parking" title="Vagas">
                                <span class="condo-features__feature-value">
                                   2 
                                </span>
                            
                                  <span class="condo-features__feature-label">
                                    Vagas
                                  </span>
                              </li>
                        </ul>
              
                      <a class="condo-unity__link js-property-link"
                        data-id="94583186"
                        data-position="18"
                        href="/imovel/apartamento-2-quartos-empresarial-18-do-forte-bairros-barueri-com-garagem-112m2-venda-RS800000-id-94583186/">Ver detalhes</a>
                    </li>
                    <li class="condo-unity" data-business="SALE">
                          <img src="https://resizedimgs.vivareal.com/fit-in/72x56/vr.images.sp/129d2fde3173672a96ccb371357c66d2.jpg"
                            alt="Unidade do condomínio  - Avenida Ômega - Empresarial 18 do Forte, Barueri - SP" class="condo-unity__thumbnail js-gallery-fullscreen-toggle">
              
                        <h5 class="condo-unity__title">
                              <span class="condo-unity__price">
                                Venda R$ 850.000
                              </span>
                        </h5>
              
                        <ul class="condo-unity__features">
                              <li class="features__item features__item--area" title="Área ">
                                <span class="condo-features__feature-value">
                                   85<span>m²</span> 
                                </span>
                            
                              </li>
              
                              <li class="features__item features__item--bedroom" title="Quartos">
                                <span class="condo-features__feature-value">
                                   2 
                                </span>
                            
                                  <span class="condo-features__feature-label">
                                    Quartos
                                  </span>
                              </li>
              
                              <li class="features__item features__item--bathroom" title="Banheiros">
                                <span class="condo-features__feature-value">
                                   3 
                                </span>
                            
                                  <span class="condo-features__feature-label">
                                    Banheiros
                                  </span>
                              </li>
              
                        </ul>
              
                      <a class="condo-unity__link js-property-link"
                        data-id="2434049882"
                        data-position="19"
                        href="/imovel/apartamento-2-quartos-empresarial-18-do-forte-bairros-barueri-85m2-venda-RS850000-id-2434049882/">Ver detalhes</a>
                    </li>
                    <li class="condo-unity" data-business="SALE">
                          <img src="https://resizedimgs.vivareal.com/fit-in/72x56/vr.images.sp/664dd13336efa138561df1aa887177a8.jpg"
                            alt="Unidade do condomínio  - Avenida Ômega, 171 - Alphaville, Barueri - SP" class="condo-unity__thumbnail js-gallery-fullscreen-toggle">
              
                        <h5 class="condo-unity__title">
                              <span class="condo-unity__price">
                                Venda R$ 850.000
                              </span>
                        </h5>
              
                        <ul class="condo-unity__features">
                              <li class="features__item features__item--area" title="Área ">
                                <span class="condo-features__feature-value">
                                   112<span>m²</span> 
                                </span>
                            
                              </li>
              
                              <li class="features__item features__item--bedroom" title="Quartos">
                                <span class="condo-features__feature-value">
                                   2 
                                </span>
                            
                                  <span class="condo-features__feature-label">
                                    Quartos
                                  </span>
                              </li>
              
                              <li class="features__item features__item--bathroom" title="Banheiros">
                                <span class="condo-features__feature-value">
                                   3 
                                </span>
                            
                                  <span class="condo-features__feature-label">
                                    Banheiros
                                  </span>
                              </li>
              
                              <li class="features__item features__item--parking" title="Vagas">
                                <span class="condo-features__feature-value">
                                   2 
                                </span>
                            
                                  <span class="condo-features__feature-label">
                                    Vagas
                                  </span>
                              </li>
                        </ul>
              
                      <a class="condo-unity__link js-property-link"
                        data-id="85770957"
                        data-position="20"
                        href="/imovel/apartamento-2-quartos-alphaville-bairros-barueri-com-garagem-112m2-venda-RS850000-id-85770957/">Ver detalhes</a>
                    </li>
                    <li class="condo-unity" data-business="SALE">
                          <img src="https://resizedimgs.vivareal.com/fit-in/72x56/vr.images.sp/870ca60633bed428283269daf2f0fabe.jpg"
                            alt="Unidade do condomínio  - Avenida Ômega, 171 - Melville Empresarial Ii, Barueri - SP" class="condo-unity__thumbnail js-gallery-fullscreen-toggle">
              
                        <h5 class="condo-unity__title">
                              <span class="condo-unity__price">
                                Venda R$ 869.000
                              </span>
                        </h5>
              
                        <ul class="condo-unity__features">
                              <li class="features__item features__item--area" title="Área ">
                                <span class="condo-features__feature-value">
                                   85<span>m²</span> 
                                </span>
                            
                              </li>
              
                              <li class="features__item features__item--bedroom" title="Quartos">
                                <span class="condo-features__feature-value">
                                   2 
                                </span>
                            
                                  <span class="condo-features__feature-label">
                                    Quartos
                                  </span>
                              </li>
              
                              <li class="features__item features__item--bathroom" title="Banheiros">
                                <span class="condo-features__feature-value">
                                   2 
                                </span>
                            
                                  <span class="condo-features__feature-label">
                                    Banheiros
                                  </span>
                              </li>
              
                              <li class="features__item features__item--parking" title="Vagas">
                                <span class="condo-features__feature-value">
                                   2 
                                </span>
                            
                                  <span class="condo-features__feature-label">
                                    Vagas
                                  </span>
                              </li>
                        </ul>
              
                      <a class="condo-unity__link js-property-link"
                        data-id="2446982338"
                        data-position="21"
                        href="/imovel/apartamento-2-quartos-melville-empresarial-ii-bairros-barueri-com-garagem-85m2-venda-RS869000-id-2446982338/">Ver detalhes</a>
                    </li>
                    <li class="condo-unity" data-business="SALE">
                          <img src="https://resizedimgs.vivareal.com/fit-in/72x56/vr.images.sp/276f37470e09feb9c74e6dec256f30f3.jpg"
                            alt="Unidade do condomínio  - Melville Empresarial Ii, Barueri - SP" class="condo-unity__thumbnail js-gallery-fullscreen-toggle">
              
                        <h5 class="condo-unity__title">
                              <span class="condo-unity__price">
                                Venda R$ 870.000
                              </span>
                        </h5>
              
                        <ul class="condo-unity__features">
                              <li class="features__item features__item--area" title="Área ">
                                <span class="condo-features__feature-value">
                                   85<span>m²</span> 
                                </span>
                            
                              </li>
              
                              <li class="features__item features__item--bedroom" title="Quartos">
                                <span class="condo-features__feature-value">
                                   2 
                                </span>
                            
                                  <span class="condo-features__feature-label">
                                    Quartos
                                  </span>
                              </li>
              
                              <li class="features__item features__item--bathroom" title="Banheiros">
                                <span class="condo-features__feature-value">
                                   3 
                                </span>
                            
                                  <span class="condo-features__feature-label">
                                    Banheiros
                                  </span>
                              </li>
              
                              <li class="features__item features__item--parking" title="Vagas">
                                <span class="condo-features__feature-value">
                                   2 
                                </span>
                            
                                  <span class="condo-features__feature-label">
                                    Vagas
                                  </span>
                              </li>
                        </ul>
              
                      <a class="condo-unity__link js-property-link"
                        data-id="2447759268"
                        data-position="22"
                        href="/imovel/apartamento-2-quartos-melville-empresarial-ii-bairros-barueri-com-garagem-85m2-venda-RS870000-id-2447759268/">Ver detalhes</a>
                    </li>
                    <li class="condo-unity" data-business="SALE">
                          <img src="https://resizedimgs.vivareal.com/fit-in/72x56/vr.images.sp/742d61efebd4036cde2da07e5de99ad2.jpg"
                            alt="Unidade do condomínio  - Alphaville, Barueri - SP" class="condo-unity__thumbnail js-gallery-fullscreen-toggle">
              
                        <h5 class="condo-unity__title">
                              <span class="condo-unity__price">
                                Venda R$ 927.547
                              </span>
                        </h5>
              
                        <ul class="condo-unity__features">
                              <li class="features__item features__item--area" title="Área ">
                                <span class="condo-features__feature-value">
                                   112<span>m²</span> 
                                </span>
                            
                              </li>
              
                              <li class="features__item features__item--bedroom" title="Quartos">
                                <span class="condo-features__feature-value">
                                   2 
                                </span>
                            
                                  <span class="condo-features__feature-label">
                                    Quartos
                                  </span>
                              </li>
              
                              <li class="features__item features__item--bathroom" title="Banheiros">
                                <span class="condo-features__feature-value">
                                   2 
                                </span>
                            
                                  <span class="condo-features__feature-label">
                                    Banheiros
                                  </span>
                              </li>
              
                              <li class="features__item features__item--parking" title="Vagas">
                                <span class="condo-features__feature-value">
                                   2 
                                </span>
                            
                                  <span class="condo-features__feature-label">
                                    Vagas
                                  </span>
                              </li>
                        </ul>
              
                      <a class="condo-unity__link js-property-link"
                        data-id="81444510"
                        data-position="23"
                        href="/imovel/apartamento-2-quartos-alphaville-bairros-barueri-com-garagem-112m2-venda-RS927547-id-81444510/">Ver detalhes</a>
                    </li>
                    <li class="condo-unity" data-business="SALE">
                          <img src="https://resizedimgs.vivareal.com/fit-in/72x56/vr.images.sp/191f717fa8e560474d41cc23e64838b2.jpg"
                            alt="Unidade do condomínio  - Melville Empresarial Ii, Barueri - SP" class="condo-unity__thumbnail js-gallery-fullscreen-toggle">
              
                        <h5 class="condo-unity__title">
                              <span class="condo-unity__price">
                                Venda R$ 950.000
                              </span>
                        </h5>
              
                        <ul class="condo-unity__features">
                              <li class="features__item features__item--area" title="Área ">
                                <span class="condo-features__feature-value">
                                   112<span>m²</span> 
                                </span>
                            
                              </li>
              
                              <li class="features__item features__item--bedroom" title="Quartos">
                                <span class="condo-features__feature-value">
                                   2 
                                </span>
                            
                                  <span class="condo-features__feature-label">
                                    Quartos
                                  </span>
                              </li>
              
                              <li class="features__item features__item--bathroom" title="Banheiros">
                                <span class="condo-features__feature-value">
                                   3 
                                </span>
                            
                                  <span class="condo-features__feature-label">
                                    Banheiros
                                  </span>
                              </li>
              
                        </ul>
              
                      <a class="condo-unity__link js-property-link"
                        data-id="2444265377"
                        data-position="24"
                        href="/imovel/apartamento-2-quartos-melville-empresarial-ii-bairros-barueri-112m2-venda-RS950000-id-2444265377/">Ver detalhes</a>
                    </li>
                </ul>
              </section>
              <section class="condo-unities js-condo-list js-filters js-filters--3" data-active>
                <h4 class="condo-unities__title" data-business="RENTAL_SALE">
                  3 Quartos (15 unidades)
                </h4>
              
                <ul class="condo-unities__list">
                    <li class="condo-unity" data-business="RENTAL">
                          <img src="https://resizedimgs.vivareal.com/fit-in/72x56/vr.images.sp/a93954a658891b9ab85658eb04945e2a.jpg"
                            alt="Unidade do condomínio  - Avenida Ômega - Empresarial 18 do Forte, Barueri - SP" class="condo-unity__thumbnail js-gallery-fullscreen-toggle">
              
                        <h5 class="condo-unity__title">
                                <span class="condo-unity__price ">
                                  Aluguel R$ 4.500<small>/Mês</small>
                                </span>
                        </h5>
              
                        <ul class="condo-unity__features">
                              <li class="features__item features__item--area" title="Área ">
                                <span class="condo-features__feature-value">
                                   112<span>m²</span> 
                                </span>
                            
                              </li>
              
                              <li class="features__item features__item--bedroom" title="Quartos">
                                <span class="condo-features__feature-value">
                                   3 
                                </span>
                            
                                  <span class="condo-features__feature-label">
                                    Quartos
                                  </span>
                              </li>
              
                              <li class="features__item features__item--bathroom" title="Banheiros">
                                <span class="condo-features__feature-value">
                                   4 
                                </span>
                            
                                  <span class="condo-features__feature-label">
                                    Banheiros
                                  </span>
                              </li>
              
                              <li class="features__item features__item--parking" title="Vagas">
                                <span class="condo-features__feature-value">
                                   2 
                                </span>
                            
                                  <span class="condo-features__feature-label">
                                    Vagas
                                  </span>
                              </li>
                        </ul>
              
                      <a class="condo-unity__link js-property-link"
                        data-id="2447537087"
                        data-position="1"
                        href="/imovel/apartamento-3-quartos-empresarial-18-do-forte-bairros-barueri-com-garagem-112m2-aluguel-RS4500-id-2447537087/">Ver detalhes</a>
                    </li>
                    <li class="condo-unity" data-business="RENTAL_SALE">
                          <img src="https://resizedimgs.vivareal.com/fit-in/72x56/vr.images.sp/a2a8a439aea91d644b0508febe3cfa99.jpg"
                            alt="Unidade do condomínio  - Avenida Ômega - Empresarial 18 do Forte, Barueri - SP" class="condo-unity__thumbnail js-gallery-fullscreen-toggle">
              
                        <h5 class="condo-unity__title">
                                <span class="condo-unity__price  condo-unity__price--secondary ">
                                  Aluguel R$ 7.550<small>/Mês</small>
                                </span>
                              <span class="condo-unity__price">
                                Venda R$ 905.956
                              </span>
                        </h5>
              
                        <ul class="condo-unity__features">
                              <li class="features__item features__item--area" title="Área ">
                                <span class="condo-features__feature-value">
                                   112<span>m²</span> 
                                </span>
                            
                              </li>
              
                              <li class="features__item features__item--bedroom" title="Quartos">
                                <span class="condo-features__feature-value">
                                   3 
                                </span>
                            
                                  <span class="condo-features__feature-label">
                                    Quartos
                                  </span>
                              </li>
              
                              <li class="features__item features__item--bathroom" title="Banheiros">
                                <span class="condo-features__feature-value">
                                   3 
                                </span>
                            
                                  <span class="condo-features__feature-label">
                                    Banheiros
                                  </span>
                              </li>
              
                              <li class="features__item features__item--parking" title="Vagas">
                                <span class="condo-features__feature-value">
                                   2 
                                </span>
                            
                                  <span class="condo-features__feature-label">
                                    Vagas
                                  </span>
                              </li>
                        </ul>
              
                      <a class="condo-unity__link js-property-link"
                        data-id="1037532391"
                        data-position="2"
                        href="/imovel/apartamento-3-quartos-empresarial-18-do-forte-bairros-barueri-com-garagem-112m2-venda-RS905956-id-1037532391/">Ver detalhes</a>
                    </li>
                    <li class="condo-unity" data-business="RENTAL_SALE">
                          <img src="https://resizedimgs.vivareal.com/fit-in/72x56/vr.images.sp/7bd601e695866398cd7af75aec8c35c7.jpg"
                            alt="Unidade do condomínio  - Avenida Ômega - Empresarial 18 do Forte, Barueri - SP" class="condo-unity__thumbnail js-gallery-fullscreen-toggle">
              
                        <h5 class="condo-unity__title">
                                <span class="condo-unity__price  condo-unity__price--secondary ">
                                  Aluguel R$ 7.827<small>/Mês</small>
                                </span>
                              <span class="condo-unity__price">
                                Venda R$ 939.901
                              </span>
                        </h5>
              
                        <ul class="condo-unity__features">
                              <li class="features__item features__item--area" title="Área ">
                                <span class="condo-features__feature-value">
                                   112<span>m²</span> 
                                </span>
                            
                              </li>
              
                              <li class="features__item features__item--bedroom" title="Quartos">
                                <span class="condo-features__feature-value">
                                   3 
                                </span>
                            
                                  <span class="condo-features__feature-label">
                                    Quartos
                                  </span>
                              </li>
              
                              <li class="features__item features__item--bathroom" title="Banheiros">
                                <span class="condo-features__feature-value">
                                   3 
                                </span>
                            
                                  <span class="condo-features__feature-label">
                                    Banheiros
                                  </span>
                              </li>
              
                              <li class="features__item features__item--parking" title="Vagas">
                                <span class="condo-features__feature-value">
                                   2 
                                </span>
                            
                                  <span class="condo-features__feature-label">
                                    Vagas
                                  </span>
                              </li>
                        </ul>
              
                      <a class="condo-unity__link js-property-link"
                        data-id="1037532390"
                        data-position="3"
                        href="/imovel/apartamento-3-quartos-empresarial-18-do-forte-bairros-barueri-com-garagem-112m2-venda-RS939901-id-1037532390/">Ver detalhes</a>
                    </li>
                    <li class="condo-unity" data-business="SALE">
                          <img src="https://resizedimgs.vivareal.com/fit-in/72x56/vr.images.sp/a3f3f8920e25d07f85c8fc644063fbd1.jpg"
                            alt="Unidade do condomínio  - Avenida Ômega - Melville Empresarial Ii, Barueri - SP" class="condo-unity__thumbnail js-gallery-fullscreen-toggle">
              
                        <h5 class="condo-unity__title">
                              <span class="condo-unity__price">
                                Venda R$ 750.320
                              </span>
                        </h5>
              
                        <ul class="condo-unity__features">
                              <li class="features__item features__item--area" title="Área ">
                                <span class="condo-features__feature-value">
                                   85<span>m²</span> 
                                </span>
                            
                              </li>
              
                              <li class="features__item features__item--bedroom" title="Quartos">
                                <span class="condo-features__feature-value">
                                   3 
                                </span>
                            
                                  <span class="condo-features__feature-label">
                                    Quartos
                                  </span>
                              </li>
              
                              <li class="features__item features__item--bathroom" title="Banheiro">
                                <span class="condo-features__feature-value">
                                   1 
                                </span>
                            
                                  <span class="condo-features__feature-label">
                                    Banheiro
                                  </span>
                              </li>
              
                              <li class="features__item features__item--parking" title="Vagas">
                                <span class="condo-features__feature-value">
                                   2 
                                </span>
                            
                                  <span class="condo-features__feature-label">
                                    Vagas
                                  </span>
                              </li>
                        </ul>
              
                      <a class="condo-unity__link js-property-link"
                        data-id="2446439133"
                        data-position="4"
                        href="/imovel/apartamento-3-quartos-melville-empresarial-ii-bairros-barueri-com-garagem-85m2-venda-RS750320-id-2446439133/">Ver detalhes</a>
                    </li>
                    <li class="condo-unity" data-business="SALE">
                          <img src="https://resizedimgs.vivareal.com/fit-in/72x56/vr.images.sp/b2b9ff58593bcd834b1e6fe0197a9aec.jpg"
                            alt="Unidade do condomínio  - Avenida Ômega, 171 - Empresarial 18 do Forte, Barueri - SP" class="condo-unity__thumbnail js-gallery-fullscreen-toggle">
              
                        <h5 class="condo-unity__title">
                              <span class="condo-unity__price">
                                Venda R$ 783.700
                              </span>
                        </h5>
              
                        <ul class="condo-unity__features">
                              <li class="features__item features__item--area" title="Área ">
                                <span class="condo-features__feature-value">
                                   112<span>m²</span> 
                                </span>
                            
                              </li>
              
                              <li class="features__item features__item--bedroom" title="Quartos">
                                <span class="condo-features__feature-value">
                                   3 
                                </span>
                            
                                  <span class="condo-features__feature-label">
                                    Quartos
                                  </span>
                              </li>
              
                              <li class="features__item features__item--bathroom" title="Banheiros">
                                <span class="condo-features__feature-value">
                                   2 
                                </span>
                            
                                  <span class="condo-features__feature-label">
                                    Banheiros
                                  </span>
                              </li>
              
                              <li class="features__item features__item--parking" title="Vagas">
                                <span class="condo-features__feature-value">
                                   2 
                                </span>
                            
                                  <span class="condo-features__feature-label">
                                    Vagas
                                  </span>
                              </li>
                        </ul>
              
                      <a class="condo-unity__link js-property-link"
                        data-id="95308248"
                        data-position="5"
                        href="/imovel/apartamento-3-quartos-empresarial-18-do-forte-bairros-barueri-com-garagem-112m2-venda-RS783700-id-95308248/">Ver detalhes</a>
                    </li>
                    <li class="condo-unity" data-business="SALE">
                          <img src="https://resizedimgs.vivareal.com/fit-in/72x56/vr.images.sp/29fb765f804d2323b475ebe5424d7774.jpg"
                            alt="Unidade do condomínio  - Avenida Ômega, 171 - Empresarial 18 do Forte, Barueri - SP" class="condo-unity__thumbnail js-gallery-fullscreen-toggle">
              
                        <h5 class="condo-unity__title">
                              <span class="condo-unity__price">
                                Venda R$ 790.000
                              </span>
                        </h5>
              
                        <ul class="condo-unity__features">
                              <li class="features__item features__item--area" title="Área ">
                                <span class="condo-features__feature-value">
                                   112<span>m²</span> 
                                </span>
                            
                              </li>
              
                              <li class="features__item features__item--bedroom" title="Quartos">
                                <span class="condo-features__feature-value">
                                   3 
                                </span>
                            
                                  <span class="condo-features__feature-label">
                                    Quartos
                                  </span>
                              </li>
              
                              <li class="features__item features__item--bathroom" title="Banheiros">
                                <span class="condo-features__feature-value">
                                   3 
                                </span>
                            
                                  <span class="condo-features__feature-label">
                                    Banheiros
                                  </span>
                              </li>
              
                              <li class="features__item features__item--parking" title="Vagas">
                                <span class="condo-features__feature-value">
                                   2 
                                </span>
                            
                                  <span class="condo-features__feature-label">
                                    Vagas
                                  </span>
                              </li>
                        </ul>
              
                      <a class="condo-unity__link js-property-link"
                        data-id="1037386888"
                        data-position="6"
                        href="/imovel/apartamento-3-quartos-empresarial-18-do-forte-bairros-barueri-com-garagem-112m2-venda-RS790000-id-1037386888/">Ver detalhes</a>
                    </li>
                    <li class="condo-unity" data-business="SALE">
                          <img src="https://resizedimgs.vivareal.com/fit-in/72x56/vr.images.sp/00e724f1da9c0666193b7b6dd4a57b97.jpg"
                            alt="Unidade do condomínio  - Avenida Ômega, 171 - Melville Empresarial Ii, Barueri - SP" class="condo-unity__thumbnail js-gallery-fullscreen-toggle">
              
                        <h5 class="condo-unity__title">
                              <span class="condo-unity__price">
                                Venda R$ 800.000
                              </span>
                        </h5>
              
                        <ul class="condo-unity__features">
                              <li class="features__item features__item--area" title="Área ">
                                <span class="condo-features__feature-value">
                                   112<span>m²</span> 
                                </span>
                            
                              </li>
              
                              <li class="features__item features__item--bedroom" title="Quartos">
                                <span class="condo-features__feature-value">
                                   3 
                                </span>
                            
                                  <span class="condo-features__feature-label">
                                    Quartos
                                  </span>
                              </li>
              
                              <li class="features__item features__item--bathroom" title="Banheiros">
                                <span class="condo-features__feature-value">
                                   4 
                                </span>
                            
                                  <span class="condo-features__feature-label">
                                    Banheiros
                                  </span>
                              </li>
              
                              <li class="features__item features__item--parking" title="Vagas">
                                <span class="condo-features__feature-value">
                                   2 
                                </span>
                            
                                  <span class="condo-features__feature-label">
                                    Vagas
                                  </span>
                              </li>
                        </ul>
              
                      <a class="condo-unity__link js-property-link"
                        data-id="2444437381"
                        data-position="7"
                        href="/imovel/apartamento-3-quartos-melville-empresarial-ii-bairros-barueri-com-garagem-112m2-venda-RS800000-id-2444437381/">Ver detalhes</a>
                    </li>
                    <li class="condo-unity" data-business="SALE">
                          <img src="https://resizedimgs.vivareal.com/fit-in/72x56/vr.images.sp/d40ca8c7665f61b691679af9561a0a24.jpg"
                            alt="Unidade do condomínio  - Avenida Ômega, 171 - Melville Empresarial Ii, Barueri - SP" class="condo-unity__thumbnail js-gallery-fullscreen-toggle">
              
                        <h5 class="condo-unity__title">
                              <span class="condo-unity__price">
                                Venda R$ 849.900
                              </span>
                        </h5>
              
                        <ul class="condo-unity__features">
                              <li class="features__item features__item--area" title="Área ">
                                <span class="condo-features__feature-value">
                                   112<span>m²</span> 
                                </span>
                            
                              </li>
              
                              <li class="features__item features__item--bedroom" title="Quartos">
                                <span class="condo-features__feature-value">
                                   3 
                                </span>
                            
                                  <span class="condo-features__feature-label">
                                    Quartos
                                  </span>
                              </li>
              
                              <li class="features__item features__item--bathroom" title="Banheiros">
                                <span class="condo-features__feature-value">
                                   3 
                                </span>
                            
                                  <span class="condo-features__feature-label">
                                    Banheiros
                                  </span>
                              </li>
              
                              <li class="features__item features__item--parking" title="Vagas">
                                <span class="condo-features__feature-value">
                                   2 
                                </span>
                            
                                  <span class="condo-features__feature-label">
                                    Vagas
                                  </span>
                              </li>
                        </ul>
              
                      <a class="condo-unity__link js-property-link"
                        data-id="1041221596"
                        data-position="8"
                        href="/imovel/apartamento-3-quartos-melville-empresarial-ii-bairros-barueri-com-garagem-112m2-venda-RS849900-id-1041221596/">Ver detalhes</a>
                    </li>
                    <li class="condo-unity" data-business="SALE">
                          <img src="https://resizedimgs.vivareal.com/fit-in/72x56/vr.images.sp/86bb8a80997071b23fd8302915015b8c.jpg"
                            alt="Unidade do condomínio  - Alphaville, Barueri - SP" class="condo-unity__thumbnail js-gallery-fullscreen-toggle">
              
                        <h5 class="condo-unity__title">
                              <span class="condo-unity__price">
                                Venda R$ 855.000
                              </span>
                        </h5>
              
                        <ul class="condo-unity__features">
                              <li class="features__item features__item--area" title="Área ">
                                <span class="condo-features__feature-value">
                                   112<span>m²</span> 
                                </span>
                            
                              </li>
              
                              <li class="features__item features__item--bedroom" title="Quartos">
                                <span class="condo-features__feature-value">
                                   3 
                                </span>
                            
                                  <span class="condo-features__feature-label">
                                    Quartos
                                  </span>
                              </li>
              
                              <li class="features__item features__item--bathroom" title="Banheiros">
                                <span class="condo-features__feature-value">
                                   3 
                                </span>
                            
                                  <span class="condo-features__feature-label">
                                    Banheiros
                                  </span>
                              </li>
              
                              <li class="features__item features__item--parking" title="Vagas">
                                <span class="condo-features__feature-value">
                                   2 
                                </span>
                            
                                  <span class="condo-features__feature-label">
                                    Vagas
                                  </span>
                              </li>
                        </ul>
              
                      <a class="condo-unity__link js-property-link"
                        data-id="2445096429"
                        data-position="9"
                        href="/imovel/apartamento-3-quartos-alphaville-bairros-barueri-com-garagem-112m2-venda-RS855000-id-2445096429/">Ver detalhes</a>
                    </li>
                    <li class="condo-unity" data-business="SALE">
                          <img src="https://resizedimgs.vivareal.com/fit-in/72x56/vr.images.sp/804a61833eed0a6b24ee094979d3002b.jpg"
                            alt="Unidade do condomínio  - Avenida Ômega - Empresarial 18 do Forte, Barueri - SP" class="condo-unity__thumbnail js-gallery-fullscreen-toggle">
              
                        <h5 class="condo-unity__title">
                              <span class="condo-unity__price">
                                Venda R$ 870.000
                              </span>
                        </h5>
              
                        <ul class="condo-unity__features">
                              <li class="features__item features__item--area" title="Área ">
                                <span class="condo-features__feature-value">
                                   112<span>m²</span> 
                                </span>
                            
                              </li>
              
                              <li class="features__item features__item--bedroom" title="Quartos">
                                <span class="condo-features__feature-value">
                                   3 
                                </span>
                            
                                  <span class="condo-features__feature-label">
                                    Quartos
                                  </span>
                              </li>
              
                              <li class="features__item features__item--bathroom" title="Banheiros">
                                <span class="condo-features__feature-value">
                                   4 
                                </span>
                            
                                  <span class="condo-features__feature-label">
                                    Banheiros
                                  </span>
                              </li>
              
                              <li class="features__item features__item--parking" title="Vagas">
                                <span class="condo-features__feature-value">
                                   2 
                                </span>
                            
                                  <span class="condo-features__feature-label">
                                    Vagas
                                  </span>
                              </li>
                        </ul>
              
                      <a class="condo-unity__link js-property-link"
                        data-id="1042003545"
                        data-position="10"
                        href="/imovel/apartamento-3-quartos-empresarial-18-do-forte-bairros-barueri-com-garagem-112m2-venda-RS870000-id-1042003545/">Ver detalhes</a>
                    </li>
                    <li class="condo-unity" data-business="SALE">
                          <img src="https://resizedimgs.vivareal.com/fit-in/72x56/vr.images.sp/d50d69bcb19113fb02bae4661e6f620e.jpg"
                            alt="Unidade do condomínio  - Avenida Ômega, 171 - Melville Empresarial Ii, Barueri - SP" class="condo-unity__thumbnail js-gallery-fullscreen-toggle">
              
                        <h5 class="condo-unity__title">
                              <span class="condo-unity__price">
                                Venda R$ 872.000
                              </span>
                        </h5>
              
                        <ul class="condo-unity__features">
                              <li class="features__item features__item--area" title="Área ">
                                <span class="condo-features__feature-value">
                                   112<span>m²</span> 
                                </span>
                            
                              </li>
              
                              <li class="features__item features__item--bedroom" title="Quartos">
                                <span class="condo-features__feature-value">
                                   3 
                                </span>
                            
                                  <span class="condo-features__feature-label">
                                    Quartos
                                  </span>
                              </li>
              
                              <li class="features__item features__item--bathroom" title="Banheiros">
                                <span class="condo-features__feature-value">
                                   4 
                                </span>
                            
                                  <span class="condo-features__feature-label">
                                    Banheiros
                                  </span>
                              </li>
              
                              <li class="features__item features__item--parking" title="Vagas">
                                <span class="condo-features__feature-value">
                                   2 
                                </span>
                            
                                  <span class="condo-features__feature-label">
                                    Vagas
                                  </span>
                              </li>
                        </ul>
              
                      <a class="condo-unity__link js-property-link"
                        data-id="80980340"
                        data-position="11"
                        href="/imovel/apartamento-3-quartos-melville-empresarial-ii-bairros-barueri-com-garagem-112m2-venda-RS872000-id-80980340/">Ver detalhes</a>
                    </li>
                    <li class="condo-unity" data-business="SALE">
                          <img src="https://resizedimgs.vivareal.com/fit-in/72x56/vr.images.sp/1bf75bff42741735da8c59d2f7af88c5.jpg"
                            alt="Unidade do condomínio  - Avenida Ômega, 171 - Alphaville, Barueri - SP" class="condo-unity__thumbnail js-gallery-fullscreen-toggle">
              
                        <h5 class="condo-unity__title">
                              <span class="condo-unity__price">
                                Venda R$ 875.000
                              </span>
                        </h5>
              
                        <ul class="condo-unity__features">
                              <li class="features__item features__item--area" title="Área ">
                                <span class="condo-features__feature-value">
                                   112<span>m²</span> 
                                </span>
                            
                              </li>
              
                              <li class="features__item features__item--bedroom" title="Quartos">
                                <span class="condo-features__feature-value">
                                   3 
                                </span>
                            
                                  <span class="condo-features__feature-label">
                                    Quartos
                                  </span>
                              </li>
              
                              <li class="features__item features__item--bathroom" title="Banheiros">
                                <span class="condo-features__feature-value">
                                   4 
                                </span>
                            
                                  <span class="condo-features__feature-label">
                                    Banheiros
                                  </span>
                              </li>
              
                              <li class="features__item features__item--parking" title="Vagas">
                                <span class="condo-features__feature-value">
                                   2 
                                </span>
                            
                                  <span class="condo-features__feature-label">
                                    Vagas
                                  </span>
                              </li>
                        </ul>
              
                      <a class="condo-unity__link js-property-link"
                        data-id="1042032728"
                        data-position="12"
                        href="/imovel/apartamento-3-quartos-alphaville-bairros-barueri-com-garagem-112m2-venda-RS875000-id-1042032728/">Ver detalhes</a>
                    </li>
                    <li class="condo-unity" data-business="SALE">
                          <img src="https://resizedimgs.vivareal.com/fit-in/72x56/vr.images.sp/fe1ee86994cac743d84a60082e820970.jpg"
                            alt="Unidade do condomínio  - Empresarial 18 do Forte, Barueri - SP" class="condo-unity__thumbnail js-gallery-fullscreen-toggle">
              
                        <h5 class="condo-unity__title">
                              <span class="condo-unity__price">
                                Venda R$ 895.000
                              </span>
                        </h5>
              
                        <ul class="condo-unity__features">
                              <li class="features__item features__item--area" title="Área ">
                                <span class="condo-features__feature-value">
                                   112<span>m²</span> 
                                </span>
                            
                              </li>
              
                              <li class="features__item features__item--bedroom" title="Quartos">
                                <span class="condo-features__feature-value">
                                   3 
                                </span>
                            
                                  <span class="condo-features__feature-label">
                                    Quartos
                                  </span>
                              </li>
              
                              <li class="features__item features__item--bathroom" title="Banheiros">
                                <span class="condo-features__feature-value">
                                   2 
                                </span>
                            
                                  <span class="condo-features__feature-label">
                                    Banheiros
                                  </span>
                              </li>
              
                              <li class="features__item features__item--parking" title="Vagas">
                                <span class="condo-features__feature-value">
                                   2 
                                </span>
                            
                                  <span class="condo-features__feature-label">
                                    Vagas
                                  </span>
                              </li>
                        </ul>
              
                      <a class="condo-unity__link js-property-link"
                        data-id="2443850442"
                        data-position="13"
                        href="/imovel/apartamento-3-quartos-empresarial-18-do-forte-bairros-barueri-com-garagem-112m2-venda-RS895000-id-2443850442/">Ver detalhes</a>
                    </li>
                    <li class="condo-unity" data-business="SALE">
                          <img src="https://resizedimgs.vivareal.com/fit-in/72x56/vr.images.sp/0259b644c24a9890c509af41d54c4aa1.jpg"
                            alt="Unidade do condomínio  - Avenida Ômega, 171 - Empresarial 18 do Forte, Barueri - SP" class="condo-unity__thumbnail js-gallery-fullscreen-toggle">
              
                        <h5 class="condo-unity__title">
                              <span class="condo-unity__price">
                                Venda R$ 895.000
                              </span>
                        </h5>
              
                        <ul class="condo-unity__features">
                              <li class="features__item features__item--area" title="Área ">
                                <span class="condo-features__feature-value">
                                   112<span>m²</span> 
                                </span>
                            
                              </li>
              
                              <li class="features__item features__item--bedroom" title="Quartos">
                                <span class="condo-features__feature-value">
                                   3 
                                </span>
                            
                                  <span class="condo-features__feature-label">
                                    Quartos
                                  </span>
                              </li>
              
                              <li class="features__item features__item--bathroom" title="Banheiros">
                                <span class="condo-features__feature-value">
                                   4 
                                </span>
                            
                                  <span class="condo-features__feature-label">
                                    Banheiros
                                  </span>
                              </li>
              
                              <li class="features__item features__item--parking" title="Vagas">
                                <span class="condo-features__feature-value">
                                   2 
                                </span>
                            
                                  <span class="condo-features__feature-label">
                                    Vagas
                                  </span>
                              </li>
                        </ul>
              
                      <a class="condo-unity__link js-property-link"
                        data-id="1042224679"
                        data-position="14"
                        href="/imovel/apartamento-3-quartos-empresarial-18-do-forte-bairros-barueri-com-garagem-112m2-venda-RS895000-id-1042224679/">Ver detalhes</a>
                    </li>
                    <li class="condo-unity" data-business="SALE">
                          <img src="https://resizedimgs.vivareal.com/fit-in/72x56/vr.images.sp/510f105e8ec614142f94b54ce9026215.jpg"
                            alt="Unidade do condomínio  - Avenida Ômega - Empresarial 18 do Forte, Barueri - SP" class="condo-unity__thumbnail js-gallery-fullscreen-toggle">
              
                        <h5 class="condo-unity__title">
                              <span class="condo-unity__price">
                                Venda R$ 950.000
                              </span>
                        </h5>
              
                        <ul class="condo-unity__features">
                              <li class="features__item features__item--area" title="Área ">
                                <span class="condo-features__feature-value">
                                   112<span>m²</span> 
                                </span>
                            
                              </li>
              
                              <li class="features__item features__item--bedroom" title="Quartos">
                                <span class="condo-features__feature-value">
                                   3 
                                </span>
                            
                                  <span class="condo-features__feature-label">
                                    Quartos
                                  </span>
                              </li>
              
                              <li class="features__item features__item--bathroom" title="Banheiros">
                                <span class="condo-features__feature-value">
                                   4 
                                </span>
                            
                                  <span class="condo-features__feature-label">
                                    Banheiros
                                  </span>
                              </li>
              
                              <li class="features__item features__item--parking" title="Vagas">
                                <span class="condo-features__feature-value">
                                   2 
                                </span>
                            
                                  <span class="condo-features__feature-label">
                                    Vagas
                                  </span>
                              </li>
                        </ul>
              
                      <a class="condo-unity__link js-property-link"
                        data-id="1041050325"
                        data-position="15"
                        href="/imovel/apartamento-3-quartos-empresarial-18-do-forte-bairros-barueri-com-garagem-112m2-venda-RS950000-id-1041050325/">Ver detalhes</a>
                    </li>
                </ul>
              </section>
          </div>
        </section>
      </section>
  </div>
  
      <div class="price-history" id="js-price-history"></div>
  
  <div class="js-fullsized-map">
    <section class="map">
      <h2 class="udp-section__title"> Explore a vizinhança </h2>
      <p class="map__address"> Avenida Ômega, 171 - Alphaville, Barueri - SP </p>
    
      <div class="map__container js-map-container">
        <div class="map__object">
          <div class="js-map"> </div>
        </div>
    
        <button class="map__navigate js-navigate"> Navegue pela região </button>
    
        <span class="map__close js-close"></span>
      </div>
    </section>
  </div>

  </main>

  <div class="research-component js-research-component">
  	<div class="research-component__container js-container">
  	  <button class="research-component__button-close js-close"></button>
  	  <p class="research-component__text">
  	    Quer participar de <strong>pesquisas</strong> para melhorar nossos produtos?
  	  </p>
  	  <a href="https://www.getfeedback.com/r/YKnMqXf1/" title="Quero participar!" target="_blank" class="research-component__button-open js-open">
  	    Quero participar!
  	  </a>
  	</div>
  </div>

  <footer id="js-site-footer" class="site-footer js-site-footer">
      <div class="site-footer__container">
        <div class="site-footer__section--pages">
          <span class="section__title">Encontre imóveis</span>
    
          <ul class="site-footer__menu">
            <li class="menu__item">
              <a href="/venda/" class="js-track">Comprar</a>
            </li>
    
            <li class="menu__item">
              <a href="/aluguel/" class="js-track">Alugar</a>
            </li>
    
            <li class="menu__item">
              <a href="/imoveis-lancamento/" class="js-track">Imóveis Novos</a>
            </li>
    
            <li class="menu__item">
              <a href="/ajuda/#ajuda-para-quem-procura" rel="nofollow" target="_blank"
                class="js-track">Dúvidas sobre como usar o Viva Real</a>
            </li>
          </ul>
        </div>
    
        <div class="site-footer__section--institutional">
          <span class="section__title">Institucional</span>
    
          <ul class="site-footer__menu">
            <li class="menu__item">
              <a href="/empresa/" class="js-track">Sobre nós</a>
            </li>
    
            <li class="menu__item">
              <a href="/empresa/carreira/vagas/"
                class="js-track">Quer trabalhar conosco?</a>
            </li>
          </ul>
        </div>
    
        <div class="site-footer__section--other-products">
          <span class="section__title">Mais produtos</span>
          <ul class="site-footer__menu">
            <li class="menu__item">
              <a href="/blog/" class="js-track">Blog</a>
            </li>
    
            <li class="menu__item">
              <a href="/vivacorretor/" class="js-track">Viva Corretor</a>
            </li>
          </ul>
        </div>
    
        <div class="site-footer__section--publisher-and-social">
          <div class="site-footer__section--publisher">
            <span class="section__title">Anunciante</span>
    
            <ul class="site-footer__menu">
              <li class="menu__item">
                <a href="/anunciar-imoveis/" class="js-track">Anunciar imóveis</a>
              </li>
    
              <li class="menu__item">
                <a href="/ajuda-anunciante/#ajuda-para-quem-anuncia" rel="nofollow" target="_blank"
                  class="js-track">Dúvidas frequentes dos Anunciantes</a>
              </li>
            </ul>
          </div>
    
          <span class="section__title">Social</span>
    
          <ul class="site-footer__social">
            <li class="social__item social__item--facebook">
              <a href="https://www.facebook.com/VivaReal" rel="nofollow" target="_blank"
                class="js-track">facebook</a>
            </li>
    
            <li class="social__item social__item--twitter">
              <a href="https://twitter.com/vivareal" rel="nofollow" target="_blank"
                class="js-track">twitter</a>
            </li>
    
            <li class="social__item social__item--youtube">
              <a href="https://www.youtube.com/user/VivaRealBrasil" rel="nofollow" target="_blank"
                class="js-track">youtube</a>
            </li>
    
            <li class="social__item social__item--instagram">
              <a href="https://instagram.com/vivareal" rel="nofollow" target="_blank"
                class="js-track">instagram</a>
            </li>
          </ul>
    
          <span class="section__title">Aplicativos</span>
    
          <ul class="site-footer__mobile">
            <li class="mobile__item mobile__item--playstore">
              <a href="http://vr.vivareal.com/android"
                rel="nofollow" class="js-track">play store</a>
            </li>
    
            <li class="mobile__item mobile__item--applestore">
              <a href="http://vr.vivareal.com/ios"
                rel="nofollow" class="js-track">apple store</a>
            </li>
          </ul>
        </div>
      </div>
    </div>
    
    <div class="site-footer__about">
      <div class="site-footer__container">
        <div class="site-footer__brand">
          Uma empresa do grupo zap
        </div>
    
        <p class="about__legal">
          Copyright &copy; 2019 Grupo ZAP. Todos os direitos reservados.
        </p>
    
        <ul class="about__terms-policy">
          <li class="terms-policy__item js-terms-policy__item">
            <a href="/legal/termos/" rel="nofollow" title="Termos de Uso"
              class="js-track">Termos de Uso</a>
          </li>
    
          <li class="terms-policy__item js-terms-policy__item">
            <a href="/legal/privacidade/" rel="nofollow" title="Política de Privacidade"
              class="js-track">Política de Privacidade</a>
          </li>
        </ul>
      </div>
    </div>
  </footer>

  <script>
    function setupApp () {
      if (window.performance && window.performance.mark) {
        window.performance.mark('script_start')
      }
  
      var settings = getSettings()
      var App = window.App
  
        configureSentry(settings.portalContext)
  
      var app = new App(settings)
      app.start()
    }
  
    function getSettings () {
      return _.assign(
        // Template rendering data
        {
          baseUrl: '',
          pageName: 'condominium-detail',
          nps: window.VivaNPS,
          tracking: getGoogleAnalyticsSettings(),
          // Remove this after migration to listing v3
          dataModel: 'v3',
        },
        // Initialization Data
        _.assign({}, ([])[0] || {}),
        // Ranking Manager data
        {
          // We use sectionName because on config module we check if seccion has "IDX_" as prefix
          sectionName: '' || 'condominium-detail',
        },
        //Publisher data
        // Feature Toogle data
          {
            featureToggle: JSON.parse('[{"enabled":true,"groups":["site"],"id":7,"feature":"dfp"},{"enabled":true,"groups":["site"],"id":62,"feature":"condo_map"},{"enabled":true,"groups":["site"],"id":54,"feature":"tmpNewScriptLoad"},{"enabled":true,"groups":["site"],"id":3001,"feature":"login_url_encode"},{"enabled":false,"groups":["vivapro"],"id":1002,"feature":"vivapro_maintenance"},{"enabled":true,"groups":["site"],"id":135,"feature":"results_map"},{"enabled":true,"groups":["site"],"id":139,"feature":"split_test_google_like"},{"enabled":true,"groups":["site"],"id":10,"feature":"frontend_sentry"},{"enabled":true,"groups":["site"],"id":31,"feature":"newrelic"},{"enabled":true,"groups":["site"],"id":58,"feature":"verified_publisher"},{"enabled":true,"groups":["site"],"id":720,"feature":"phone_leads"},{"enabled":true,"groups":["site"],"id":65,"feature":"condo_price_history"},{"enabled":false,"groups":["site"],"id":123,"feature":"aldo"},{"enabled":true,"groups":["site"],"id":2,"feature":"googleTagManager"},{"enabled":true,"groups":["site"],"id":21,"feature":"phone_postlead"},{"enabled":false,"groups":["site"],"id":14,"feature":"mktcampaign_teaser"},{"enabled":false,"groups":["login","zap"],"id":2003,"feature":"HistNavWrite"},{"enabled":false,"groups":["site"],"id":138,"feature":"split_test_grid_visualization"},{"enabled":true,"groups":["site"],"id":142,"feature":"streets_suggestions"},{"enabled":true,"groups":["site"],"id":25,"feature":"pdpTopRecommendation"},{"enabled":true,"groups":["site"],"id":53,"feature":"nps"},{"enabled":false,"groups":["vivapro"],"id":1001,"feature":"vivapro_online_subscription"},{"enabled":false,"groups":["zap_api"],"id":2000,"feature":"avm_pagamento"},{"enabled":false,"groups":["site"],"id":16,"feature":"mktcampaign_pdp"},{"enabled":false,"groups":["site"],"id":143,"feature":"pdp_new_layout"},{"enabled":false,"groups":["site"],"id":17,"feature":"mktcampaign_menu"},{"enabled":true,"groups":["site"],"id":133,"feature":"aldo_spin"},{"enabled":false,"groups":["site"],"id":6,"feature":"crazyegg"},{"enabled":true,"groups":["site"],"id":66,"feature":"decision_tree_lead_form"},{"enabled":true,"groups":["site"],"id":63,"feature":"pois_school_data"},{"enabled":true,"groups":["login","zap"],"id":999,"feature":"capitaoLogin"},{"enabled":true,"groups":["site"],"id":59,"feature":"google_optimize"},{"enabled":true,"groups":["site"],"id":137,"feature":"development_highlight"},{"enabled":true,"groups":["anuncie"],"id":3000,"feature":"login_capitao"},{"enabled":true,"groups":["site"],"id":61,"feature":"map_with_pois"},{"enabled":false,"groups":["site"],"id":134,"feature":"branch_lead_sms"},{"enabled":true,"groups":["login","zap"],"id":2002,"feature":"capitaoZapWa"},{"enabled":true,"groups":["site"],"id":42,"feature":"new_find_by_id"},{"enabled":true,"groups":["login"],"id":998,"feature":"capitaoIntranet"},{"enabled":false,"groups":["site"],"id":1,"feature":"bacon"},{"enabled":true,"groups":["site"],"id":144,"feature":"rp_see_phone"},{"enabled":true,"groups":["site"],"id":64,"feature":"condo_new_catalog_list"},{"enabled":true,"groups":["site"],"id":2005,"feature":"minha_casa_minha_vida"},{"enabled":true,"groups":["site"],"id":5,"feature":"googleAnalytics"},{"enabled":true,"groups":["vivapro"],"id":1003,"feature":"vivapro_hide_hotlead"},{"enabled":false,"groups":["internal"],"id":24,"feature":"styleguide"},{"enabled":false,"groups":["site"],"id":30,"feature":"amplitude"},{"enabled":false,"groups":["site"],"id":15,"feature":"mktcampaign_rp"},{"enabled":true,"groups":["login","zap"],"id":2001,"feature":"capitaoApi"},{"enabled":true,"groups":["site"],"id":67,"feature":"user_recommendations"},{"enabled":false,"groups":["site"],"id":11,"feature":"go_page_hiding"},{"enabled":false,"groups":["login","zap"],"id":2004,"feature":"HistNavRead"},{"enabled":true,"groups":["site"],"id":3003,"feature":"favoriteNewStack"}]'),
          },
        // Other data
        {"portalContext":"prod","glueApiEndpoint":"https://glue-api.vivareal.com","aldoApiEndpoint":"https://api-aldo.vivareal.com.br","accountApiEndpoint":"https://account-api.grupozap.com","percivalApiEndpoint":"https://growth.percival.vivareal.io","myAccountApiEndpoint":"https://my-account-api.vivareal.com.br","accountLoginUrl":"https://account-api.grupozap.com/oauth/authorize?response_type=code&source=vivareal&client_id=site&redirect_uri=https://my-account-api.vivareal.com.br/user/login?state=","loginUrl":"https://account-api.grupozap.com/oauth/authorize?response_type=code&source=vivareal&client_id=site&redirect_uri=https%3A%2F%2Fmy-account-api.vivareal.com.br%2Fuser%2Flogin%3Fstate%3D","cdnPath":"https://cdn1.vivareal.com/p/14483-4ce4541/v/static","detail":{"seo":{"metaContent":{"metaTitle":"Avenida Ômega, 171 - PRESENT ALPHAVILLE - Viva Real","metaDescription":"Imóveis à venda ou para alugar em PRESENT ALPHAVILLE em Avenida Ômega, 171 no bairro Alphaville.","heading":"PRESENT ALPHAVILLE, Alphaville - Barueri - Viva Real"}},"condominium":{"uuid":"6ad8eb6a-41d8-4703-929c-3c5b3898e5a8","name":"PRESENT ALPHAVILLE","description":"","totalUnits":120,"media":[],"amenities":["PARTY_HALL","ADULT_POOL","BARBECUE_GRILL","SAUNA","ADULT_GAME_ROOM","PLAYGROUND","CHILDREN_POOL"],"address":{"street":"Avenida Ômega","streetNumber":"171","neighborhood":"Alphaville","city":"Barueri","state":"São Paulo","zipCode":"06472005","geoLocation":{"latitude":-23.484779,"longitude":-46.851354,"precision":"RANGE_INTERPOLATED"}},"buildings":[],"provider":-1,"constructionStatus":"UNDER_CONSTRUCTION","createdAt":"2017-05-12T19:45:07.145Z","updatedAt":"2017-05-12T19:45:07.145Z","yearDelivered":2014,"externalId":"33517514","shortUuid":"6ad8eb6a-e5a8","unitTypes":[{"amenities":[],"condominiumUuid":"6ad8eb6a-41d8-4703-929c-3c5b3898e5a8","address":{"zipCode":"06472005","streetNumber":"171","city":"Barueri","geoLocation":{"latitude":-23.484779,"precision":"RANGE_INTERPOLATED","longitude":-46.851354},"street":"Avenida Ômega","neighborhood":"Alphaville","state":"São Paulo"},"suites":3,"description":"","media":[],"type":"APARTMENT","bathrooms":2,"uuid":"8f467744-994a-4439-92c6-4460ddfcded8","bedrooms":3,"createdAt":"2017-05-12T19:45:07.146Z","floors":0,"iptu":0,"buildingUuid":"","parkingSpaces":2,"dimensions":{"grossInternalArea":0,"netInternalArea":112,"grossExternalArea":168},"updatedAt":"2017-05-12T19:45:07.146Z"},{"amenities":[],"condominiumUuid":"6ad8eb6a-41d8-4703-929c-3c5b3898e5a8","address":{"zipCode":"06472005","streetNumber":"171","city":"Barueri","geoLocation":{"latitude":-23.484779,"precision":"RANGE_INTERPOLATED","longitude":-46.851354},"street":"Avenida Ômega","neighborhood":"Alphaville","state":"São Paulo"},"suites":2,"description":"","media":[],"type":"APARTMENT","bathrooms":2,"uuid":"984e57b4-d826-460a-ac46-31cc7da237ba","bedrooms":2,"createdAt":"2017-05-12T19:45:07.146Z","floors":0,"iptu":0,"buildingUuid":"","parkingSpaces":2,"dimensions":{"grossInternalArea":0,"netInternalArea":85,"grossExternalArea":127},"updatedAt":"2017-05-12T19:45:07.146Z"}]},"listings":{"time":33,"totalCount":39,"result":{"listings":[{"listing":{"amenities":["NEAR_ACCESS_ROADS","NEAR_SHOPPING_CENTER","NEAR_PUBLIC_TRANSPORT","NEAR_SCHOOL","NEAR_HOSPITAL","BALCONY","FULL_CABLING","GARAGE","LAUNDRY","KITCHEN","SERVICE_AREA","ELEVATOR","GARDEN","GOURMET_SPACE","GYM","PARTY_HALL","PLAYGROUND","POOL","GREEN_SPACE","ADULT_POOL","CHILDRENS_POOL","ADULT_GAME_ROOM","YOUTH_GAME_ROOM","HEATING","ALARM_SYSTEM","GATED_COMMUNITY","INTERCOM","SECURITY_24_HOURS","SAFETY_CIRCUIT","WATCHMAN","ELECTRIC_GENERATOR","NUMBER_OF_FLOORS","REFLECTING_POOL","SAUNA"],"feedsId":"","usableAreas":[112],"description":"OPORTUNIDADE DE LOCAÇÃO NO 18 DO FORTE .<br><br>APARTAMENTO NOVO COM <br>METRAGEM: 112 m² <br>2 SUÍTES<br>2 VAGAS<br><br>PROPRIETÁRIO VAI COLOCAR OS MOVEIS PLANEJADOS NO APARTAMENTO <br><br>CASO NECESSITAR DA LOCAÇÃO MOBILIADO O VALOR SERA R$ 6.000,00/MÊS + DESPESAS DE CONDOMÍNIO.","listingType":"USED","title":"APARTAMENTO NOVO 2 SUÍTES NO 18 DO FORTE","createdAt":"2019-03-10T17:13:08.058Z","publisherId":126112,"unitTypes":["APARTMENT"],"providerId":"VIVAREAL","condominiumName":"","propertyType":"UNIT","contact":{"chat":"","phones":["1147506168"],"emails":[]},"listingStatus":"ACTIVE","id":"2436011588","parkingSpaces":[2],"updatedAt":"2019-06-08T20:53:50.535Z","owner":false,"address":{"country":"Brasil","state":"São Paulo","city":"Barueri","neighborhood":"Alphaville 18 Forte","street":"Avenida Ômega","streetNumber":"171","unitNumber":"","zipCode":"06472005","locationId":"BR>Sao Paulo>NULL>Barueri>Barrios>Alphaville 18 Forte","zone":"Bairros","district":"","geoLocation":{"location":{"lat":-23.484829,"lon":-46.851078},"precision":"ROOFTOP","optionalPrecision":"precision"}},"suites":[2],"publicationType":"STANDARD","externalId":"PRESENT_LUCAS_112","bathrooms":[3],"totalAreas":[112],"logoUrl":"","bedrooms":[2],"promotions":[],"highlights":"","pricingInfos":[{"period":"MONTHLY","yearlyIptu":"400","price":"4000","rentalTotalPrice":"4880","businessType":"RENTAL","monthlyCondoFee":"880"}],"showPrice":true,"displayAddress":"ALL","images":["https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/c409d3140666558503f916cf4d4eb787.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/3fdb0ec867a5435756c75c6ba772a87a.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/7774154cf8ccd49fd1d2e0f5f8446efd.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/c1329c351ec2f7beb7f291e37df11c28.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/ae5ce2c69c925b57929f3186e404c040.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/dfc8fd00a5acabf79215b0dd05ba87c7.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/99f33f73d3cb837041be076bee1ce8eb.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/66bdbe511d5414116191367dd9d2357e.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/5260f174bdf75845634c421538f04a87.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/12ca8ca98758ab63a48fa508f8bf5168.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/68e08dba46a9dc32f6e4336ad7bf8411.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/bd7805bdc7204877a42ac96b6571287f.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/9c94cca478c7528525a55bdf27c9e314.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/30eb45de525f8eff750744996084ca82.jpg"],"videos":[]},"publisher":{"id":"126112","name":"MADONA","phone":{"leadsPhone":"1147506168","mobile":null,"alternative":"","primary":"1147506168"},"logoUrl":"https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/2dd578fb2da4624d48a17128c647cf54.jpg","licenseNumber":"69073-F-SP","websiteUrl":"","leadEmails":[],"createdDate":"2018-03-27T17:19:08Z","showAddress":false},"url":{"id":"2436011588","link":{"name":"Apartamento com 2 Quartos para alugar, 112m²","href":"/imovel/apartamento-2-quartos-alphaville-18-forte-bairros-barueri-com-garagem-112m2-aluguel-RS4000-id-2436011588/","rel":""}},"properAddress":null,"publisherUrl":{"link":{"name":"","href":"/126112/madona/","rel":""}}},{"listing":{"amenities":["AIR_CONDITIONING","BARBECUE_GRILL","KITCHEN","ELEVATOR","GOURMET_BALCONY","POOL","BALCONY","SAUNA","SERVICE_AREA"],"feedsId":"AP1767","usableAreas":[112],"description":"Lindo apartamento no Ed. Present Alphaviile.<br>Vista previlegiada! Moveis com excelente acabamento e ampla opção de armários. Já com alguns eletrodomésticos.<br>sacada Gourmet já com churrasqueira.<br>Condomínio moderno e bem localizado.<br>Ótima oportunidade para morar bem! -","listingType":"USED","title":"Edifício Present Alphaville","createdAt":"2019-06-09T01:36:10.578Z","publisherId":251211,"unitTypes":["APARTMENT"],"providerId":"23014","condominiumName":"","propertyType":"UNIT","contact":{"chat":"","phones":["1141950195","11991076161"],"emails":[]},"listingStatus":"ACTIVE","id":"2447537087","parkingSpaces":[2],"owner":false,"address":{"country":"Brasil","state":"São Paulo","city":"Barueri","neighborhood":"Empresarial 18 do Forte","street":"Avenida Ômega","unitNumber":"","zipCode":"06472005","locationId":"BR>Sao Paulo>NULL>Barueri>Barrios>Empresarial 18 do Forte","zone":"Bairros","district":"","geoLocation":{"location":{"lat":-23.484829,"lon":-46.851078},"precision":"ROOFTOP","optionalPrecision":"precision"}},"suites":[3],"publicationType":"STANDARD","externalId":"AP1767","bathrooms":[4],"totalAreas":[112],"logoUrl":"","bedrooms":[3],"promotions":[],"highlights":"","pricingInfos":[{"period":"MONTHLY","yearlyIptu":"0","price":"4500","rentalTotalPrice":"5100","businessType":"RENTAL","monthlyCondoFee":"600"}],"showPrice":true,"displayAddress":"STREET","buildings":0,"images":["https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/a93954a658891b9ab85658eb04945e2a.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/0b1612e664bda7459d810d3c13c98892.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/b9d25b008a5c16d97e3c732d61502e1f.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/e049c3881ed3ee79ac082fef4ffc1ed6.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/f72b3bfa472f9bc07a06ebdd28bcfa40.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/473a65d07fd19703041f4c27526454ef.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/075dcbb0134a99cdedda1ac641f20bb6.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/94ed68bc33c5beda1922052182d7f005.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/9c43d467d4b563d20aae90699d04cc39.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/c4492b61fd73ab853be83a47a14988bb.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/49ce56d7f2ea7689a7a50b8e112fccc7.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/ab2ac182fd52c2d82eaac3d6ab04d980.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/1e034a2a486bce6c8749c02930df702b.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/8a7feed1abc7abd895558b41f87bd6a0.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/41a827c22f243be8dc0d23bcd56acb64.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/94086c0fe9b23351bef10b9f63946f34.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/f948eb09de5cdce50df3bbd424995b8c.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/c21e9b6d2950d96401e65126a739f33a.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/8f5d46824086a7fb980af42aecbc7bb5.jpg"],"videos":[]},"publisher":{"id":"251211","name":"ALPHA IMÓVEL","address":{"country":"Brasil","zipCode":"06543-001","city":"Santana de Parnaíba","streetNumber":"4000","zone":"","street":"Avenida Marcos Penteado de Ulhôa Rodrigues","locationId":"","district":"","unitNumber":"","state":"SP","neighborhood":"Tamboré"},"phone":{"leadsPhone":"","mobile":"11991076161","alternative":"","primary":"1141950195"},"logoUrl":"https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/46c3a76e0d71a18194a319ab626b4cc5.jpg","licenseNumber":"18786-J-SP","websiteUrl":"http://www.alphaimovel.com.br/","leadEmails":[],"createdDate":"2018-03-28T10:42:55Z","showAddress":true},"url":{"id":"2447537087","link":{"name":"Apartamento com 3 Quartos para alugar, 112m²","href":"/imovel/apartamento-3-quartos-empresarial-18-do-forte-bairros-barueri-com-garagem-112m2-aluguel-RS4500-id-2447537087/","rel":""}},"properAddress":null,"publisherUrl":{"link":{"name":"","href":"/251211/alpha-imovel/","rel":""}}},{"listing":{"amenities":["ELEVATOR"],"feedsId":"AP0945","usableAreas":[85],"description":"Sua vida acaba de ganhar um novo endereço, um lugar repleto de verde e muita tranquilidade. Chegou a hora de você aproveitar o tempo de outra maneira.<br>Aluguel<br>Entrada parcelada em 30 meses, já morando. Financiamento direto com a construtora em até 120 meses. -","listingType":"USED","title":"Present Alphaville 18 do Forte","createdAt":"2018-06-06T04:43:17.587Z","publisherId":251211,"unitTypes":["APARTMENT"],"providerId":"23014","condominiumName":"","propertyType":"UNIT","contact":{"chat":"","phones":["1141950195","11991076161"],"emails":[]},"listingStatus":"ACTIVE","id":"1037532575","parkingSpaces":[2],"updatedAt":"2019-05-20T23:28:18.472Z","owner":false,"address":{"country":"Brasil","state":"São Paulo","city":"Barueri","neighborhood":"Empresarial 18 do Forte","street":"Avenida Ômega","unitNumber":"","zipCode":"06472005","locationId":"BR>Sao Paulo>NULL>Barueri>Barrios>Empresarial 18 do Forte","zone":"Bairros","district":"","geoLocation":{"location":{"lat":-23.484829,"lon":-46.851078},"precision":"ROOFTOP","optionalPrecision":"precision"}},"suites":[2],"publicationType":"STANDARD","externalId":"AP0945","bathrooms":[2],"totalAreas":[85],"logoUrl":"","bedrooms":[2],"promotions":[],"highlights":"","pricingInfos":[{"period":"MONTHLY","yearlyIptu":"0","price":"5877","rentalTotalPrice":"5877","businessType":"RENTAL","monthlyCondoFee":"0"},{"yearlyIptu":"0","price":"705268","businessType":"SALE","monthlyCondoFee":"0"}],"showPrice":true,"displayAddress":"STREET","buildings":0,"images":["https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/caecf904027ac7c5773579ff0bcdc81e.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/7f399d18f7f55f037171c41552cd29b1.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/f7a14ca2ddf7460b2ec886fa64feb618.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/9944669e936ff5e0b880daacd77db532.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/bae699df43d36dab313e04aaa83feae7.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/458c0bead03edc617eec410e730831f3.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/574b2d0e813857787fe079a25ef40362.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/a4c6debca1ade1de0d7c070cf112a800.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/5ac68f860eea80fab392202536910a14.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/9c370df514403813687132ca0004312c.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/d88b795a5bfdbe256756ada1f2636af8.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/2ef67746c5f5e743f84d17249b1c32ec.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/875e4459727d81f221e87c20c43b85a3.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/2886ebaaadfbec23439cb191d8441cd5.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/3fac5017278869d0a6b900a1089e055a.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/91e08a90a59390274b8c94cf0fd24b42.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/e1d6e72dcc40e0b2f1e6dfcf5b5f9753.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/d681dac04951993d25991254cb1d4929.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/24d89317094bea72e096c102c0754c23.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/856345768aa4c8218456d516d39dc272.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/ea95b12101d36f8d292066ea48403409.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/866ac6cca0717b0ff667eac0d90ba91d.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/194aaa78b585aa6559665991ad912539.jpg"],"videos":["http://www.youtube.com/embed/Qu1Crj0P3kw"]},"publisher":{"id":"251211","name":"ALPHA IMÓVEL","address":{"country":"Brasil","zipCode":"06543-001","city":"Santana de Parnaíba","streetNumber":"4000","zone":"","street":"Avenida Marcos Penteado de Ulhôa Rodrigues","locationId":"","district":"","unitNumber":"","state":"SP","neighborhood":"Tamboré"},"phone":{"leadsPhone":"","mobile":"11991076161","alternative":"","primary":"1141950195"},"logoUrl":"https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/46c3a76e0d71a18194a319ab626b4cc5.jpg","licenseNumber":"18786-J-SP","websiteUrl":"http://www.alphaimovel.com.br/","leadEmails":[],"createdDate":"2018-03-28T10:42:55Z","showAddress":true},"url":{"id":"1037532575","link":{"name":"Apartamento com 2 Quartos para venda ou aluguel, 85m²","href":"/imovel/apartamento-2-quartos-empresarial-18-do-forte-bairros-barueri-com-garagem-85m2-venda-RS705268-id-1037532575/","rel":""}},"properAddress":null,"publisherUrl":{"link":{"name":"","href":"/251211/alpha-imovel/","rel":""}}},{"listing":{"amenities":["BARBECUE_GRILL","ELEVATOR","GOURMET_BALCONY","POOL","SAUNA"],"feedsId":"AP0946","usableAreas":[85],"description":"Aluguel<br>Entrada parcelada em 30 meses, já morando. Financiamento direto com a construtora em até 120 meses. -","listingType":"USED","title":"Present Alphaville 18 do Forte","createdAt":"2018-06-06T04:40:17.713Z","publisherId":251211,"unitTypes":["APARTMENT"],"providerId":"23014","condominiumName":"","propertyType":"UNIT","contact":{"chat":"","phones":["1141950195","11991076161"],"emails":[]},"listingStatus":"ACTIVE","id":"1037532394","parkingSpaces":[2],"updatedAt":"2019-05-20T23:28:17.224Z","owner":false,"address":{"country":"Brasil","state":"São Paulo","city":"Barueri","neighborhood":"Empresarial 18 do Forte","street":"Avenida Ômega","unitNumber":"","zipCode":"06472005","locationId":"BR>Sao Paulo>NULL>Barueri>Barrios>Empresarial 18 do Forte","zone":"Bairros","district":"","geoLocation":{"location":{"lat":-23.484829,"lon":-46.851078},"precision":"ROOFTOP","optionalPrecision":"precision"}},"suites":[2],"publicationType":"STANDARD","externalId":"AP0946","bathrooms":[2],"totalAreas":[85],"logoUrl":"","bedrooms":[2],"promotions":[],"highlights":"","pricingInfos":[{"period":"MONTHLY","yearlyIptu":"0","price":"6030","rentalTotalPrice":"6030","businessType":"RENTAL","monthlyCondoFee":"0"},{"yearlyIptu":"0","price":"723569","businessType":"SALE","monthlyCondoFee":"0"}],"showPrice":true,"displayAddress":"STREET","buildings":0,"images":["https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/1c863a9aedaaad5abfd431b2c538d19c.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/edfa01e26a1991bbde11a15e576d3968.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/0152a5c5318f042d92d0d923f7ddf80e.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/fa97273b2587493fc6f13ff5863ab984.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/c5af72de86530b578dfa7e01443c98f7.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/92d870f7b99da0107d1337afd52dd714.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/8577340b5f3c35d727beb4fe7596a9a1.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/a660703798daa4cab398f5fbcf27b6a0.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/54065e7c085c1ddf7a6302ee8696b969.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/525dd50c262b7d701bb47de24fab4113.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/64a5773cb9c73d45e5b8afe2e0838b2d.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/9d5ccd728efd30d34a39d077d7d8f8f1.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/edc2f47704fc6b40e537819e3a852571.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/4dc50e38cba8abdfad3c2c7f60f28d12.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/6cf0c0485a0ae4129b26b2d551872bb8.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/35bf54c1afb853b4067f90c39df191a5.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/402be383eca1db39ecafb1a2516fde8f.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/0749359090b2aff2575263ceb0f491dc.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/22cf43989522f25cd04e130c63a1a4c2.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/328d4efa280192f724c963646e42b432.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/a696eecd833772afdae8354267a4d59c.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/855fc67ea077aad550a1c19d3bc1fb36.jpg"],"videos":["http://www.youtube.com/embed/Qu1Crj0P3kw"]},"publisher":{"id":"251211","name":"ALPHA IMÓVEL","address":{"country":"Brasil","zipCode":"06543-001","city":"Santana de Parnaíba","streetNumber":"4000","zone":"","street":"Avenida Marcos Penteado de Ulhôa Rodrigues","locationId":"","district":"","unitNumber":"","state":"SP","neighborhood":"Tamboré"},"phone":{"leadsPhone":"","mobile":"11991076161","alternative":"","primary":"1141950195"},"logoUrl":"https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/46c3a76e0d71a18194a319ab626b4cc5.jpg","licenseNumber":"18786-J-SP","websiteUrl":"http://www.alphaimovel.com.br/","leadEmails":[],"createdDate":"2018-03-28T10:42:55Z","showAddress":true},"url":{"id":"1037532394","link":{"name":"Apartamento com 2 Quartos para venda ou aluguel, 85m²","href":"/imovel/apartamento-2-quartos-empresarial-18-do-forte-bairros-barueri-com-garagem-85m2-venda-RS723569-id-1037532394/","rel":""}},"properAddress":null,"publisherUrl":{"link":{"name":"","href":"/251211/alpha-imovel/","rel":""}}},{"listing":{"amenities":["BARBECUE_GRILL","ELEVATOR","GOURMET_BALCONY","POOL","SAUNA"],"feedsId":"AP0947","usableAreas":[112],"description":"Sua vida acaba de ganhar um novo endereço, um lugar repleto de verde e muita tranquilidade. Chegou a hora de você aproveitar o tempo de outra maneira.<br>ALUGUEL INVESTIDO<br>Entrada parcelada em 30 meses, já morando. Financiamento direto com a construtora em até 120 meses. -","listingType":"USED","title":"Edifício Present Alphaville","createdAt":"2018-06-06T04:40:17.017Z","publisherId":251211,"unitTypes":["APARTMENT"],"providerId":"23014","condominiumName":"","propertyType":"UNIT","contact":{"chat":"","phones":["1141950195","11991076161"],"emails":[]},"listingStatus":"ACTIVE","id":"1037532391","parkingSpaces":[2],"updatedAt":"2019-05-20T23:28:17.191Z","owner":false,"address":{"country":"Brasil","state":"São Paulo","city":"Barueri","neighborhood":"Empresarial 18 do Forte","street":"Avenida Ômega","unitNumber":"","zipCode":"06472005","locationId":"BR>Sao Paulo>NULL>Barueri>Barrios>Empresarial 18 do Forte","zone":"Bairros","district":"","geoLocation":{"location":{"lat":-23.484829,"lon":-46.851078},"precision":"ROOFTOP","optionalPrecision":"precision"}},"suites":[3],"publicationType":"STANDARD","externalId":"AP0947","bathrooms":[3],"totalAreas":[112],"logoUrl":"","bedrooms":[3],"promotions":[],"highlights":"","pricingInfos":[{"period":"MONTHLY","yearlyIptu":"0","price":"7550","rentalTotalPrice":"7550","businessType":"RENTAL","monthlyCondoFee":"0"},{"yearlyIptu":"0","price":"905956","businessType":"SALE","monthlyCondoFee":"0"}],"showPrice":true,"displayAddress":"STREET","buildings":0,"images":["https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/a2a8a439aea91d644b0508febe3cfa99.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/0e32833efb8248a770f394a8cb331385.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/91b3070c89339d98251f17649d919f82.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/cc2fe71606618df0ea1b6b01f6de160d.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/8211841e7104b3931b7c9fb5c71db98d.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/48923cbc5a162ea58edbcabfcb1738dc.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/0b4ac13f795622432382c0682e65b7ed.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/71f34334091e6c15d48ce11d69ead7b4.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/d09adc1e1c0fb33b5a174e24e679c637.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/a7f48c45df87538eb52445b239ac1635.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/668b11d9c90e75b74ed24c2152712bb6.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/64fabc2ebaedde7fee8544bc6d0adb33.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/3dd5028062e11fc8d11ce2440bafbe7e.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/271afbc53c1de958b2cba27fdfa5c52f.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/6072b7da6648508d17545c887359e153.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/29cb9894bf402e3bd659fe3767acceb6.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/c83895e2284233f47931afe159663b90.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/d35bdea9bb9309fcf29cb585854fb488.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/9272bccf4de105b88406ed2297efe5ba.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/c139e2592cdc73d0effa89cbc1974edf.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/f5c49769323863f99ec9487e82246594.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/64aa8f7e1ccc9f01c791aa10794a82d9.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/b660d2a3740f33aa604ffa62f3363d69.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/1ea387d73ef897e71d46f036ec43196b.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/2a441562155345e6dfbfa579ef9b3c6d.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/a63999193d1d5317f0d4f6d006e957ed.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/2adc1e9aca7d0bbccc1685f5f0586c70.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/8c870739f73dddbc0bd09d4477fd4d3a.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/eae9a8a01f5e1786684b74a4e0604f0d.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/0dddc337b50a182997e7c89653f25c21.jpg"],"videos":["http://www.youtube.com/embed/Qu1Crj0P3kw"]},"publisher":{"id":"251211","name":"ALPHA IMÓVEL","address":{"country":"Brasil","zipCode":"06543-001","city":"Santana de Parnaíba","streetNumber":"4000","zone":"","street":"Avenida Marcos Penteado de Ulhôa Rodrigues","locationId":"","district":"","unitNumber":"","state":"SP","neighborhood":"Tamboré"},"phone":{"leadsPhone":"","mobile":"11991076161","alternative":"","primary":"1141950195"},"logoUrl":"https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/46c3a76e0d71a18194a319ab626b4cc5.jpg","licenseNumber":"18786-J-SP","websiteUrl":"http://www.alphaimovel.com.br/","leadEmails":[],"createdDate":"2018-03-28T10:42:55Z","showAddress":true},"url":{"id":"1037532391","link":{"name":"Apartamento com 3 Quartos para venda ou aluguel, 112m²","href":"/imovel/apartamento-3-quartos-empresarial-18-do-forte-bairros-barueri-com-garagem-112m2-venda-RS905956-id-1037532391/","rel":""}},"properAddress":null,"publisherUrl":{"link":{"name":"","href":"/251211/alpha-imovel/","rel":""}}},{"listing":{"amenities":["BARBECUE_GRILL","ELEVATOR","GOURMET_BALCONY","POOL","BALCONY","SAUNA"],"feedsId":"AP0948","usableAreas":[112],"description":"Sua vida acaba de ganhar um novo endereço, um lugar repleto de verde e muita tranquilidade. Chegou a hora de você aproveitar o tempo de outra maneira<br>ALUGUEL INVESTIDO<br>Entrada parcelada em 30 meses, já morando. Financiamento direto com a construtora em até 120 meses. -","listingType":"USED","title":"Present Alphaville 18 do Forte","createdAt":"2018-06-06T04:40:16.741Z","publisherId":251211,"unitTypes":["APARTMENT"],"providerId":"23014","condominiumName":"","propertyType":"UNIT","contact":{"chat":"","phones":["1141950195","11991076161"],"emails":[]},"listingStatus":"ACTIVE","id":"1037532390","parkingSpaces":[2],"updatedAt":"2019-05-20T23:28:17.223Z","owner":false,"address":{"country":"Brasil","state":"São Paulo","city":"Barueri","neighborhood":"Empresarial 18 do Forte","street":"Avenida Ômega","unitNumber":"","zipCode":"06472005","locationId":"BR>Sao Paulo>NULL>Barueri>Barrios>Empresarial 18 do Forte","zone":"Bairros","district":"","geoLocation":{"location":{"lat":-23.484829,"lon":-46.851078},"precision":"ROOFTOP","optionalPrecision":"precision"}},"suites":[3],"publicationType":"STANDARD","externalId":"AP0948","bathrooms":[3],"totalAreas":[112],"logoUrl":"","bedrooms":[3],"promotions":[],"highlights":"","pricingInfos":[{"period":"MONTHLY","yearlyIptu":"0","price":"7827","rentalTotalPrice":"7827","businessType":"RENTAL","monthlyCondoFee":"0"},{"yearlyIptu":"0","price":"939901","businessType":"SALE","monthlyCondoFee":"0"}],"showPrice":true,"displayAddress":"STREET","buildings":0,"images":["https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/7bd601e695866398cd7af75aec8c35c7.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/3f6e59d523e05f41d80461f6e8e1a0f5.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/ad1ce2a49a5ceb505aae6bf27044bec9.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/f2a72b53d06d48cc57a62b2390175e19.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/66520a5068225763b0579a4b843c6417.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/f4a745ff32569cfe54f230feb3f1326f.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/299ff376c252d37dc9d38abdadf12e4c.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/e50d659219ea53dfc225a2073c7b1efa.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/2bc22a091d2ad15461424912f7adb375.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/16542556ac7eeede99760f609942d17f.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/1fb42f535019deed794747f537aef9e8.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/e7cfd8c3aa5dfdf3f532d330e3d51de5.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/196a450070e97e46e411f0dac8080216.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/674026d57eccfeb2d15200715e8d05e7.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/091090692af8a6198d8fb85df2550275.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/cc32a568c1ad9dd0030e77636b3637ef.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/49d8b711529924eba36a3a19fcad605a.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/d2710aaddeb1b533666d40efc2488cac.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/9ab6241240562c40d5a546c6d844cd15.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/e79b2953fd793d86fb0c1f8ae48c0c0b.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/c7840ea303a45233ef189ac56aee2508.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/4b085108a6071e046d9e711fc1f60b8c.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/e65a8e51269479004656fa35c744d229.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/0c34c4bbcfa80013718109fd6e6e5626.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/85aac72a56c23bfffb675d587ad05550.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/9f75398f516158eabf090a8e065699a7.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/52d923bfb9a8987f13911e8fbbc01af6.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/03ad450277278593006a40e16f829fd1.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/46b70bb3a152db7c38e2220a23f46515.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/128164befd438f9e4ab3f18cfacf5400.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/ff52c9d7f126b0ca8e096a13853e4b50.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/6c730f906c47a1fe41044c91a832c077.jpg"],"videos":["http://www.youtube.com/embed/Qu1Crj0P3kw"]},"publisher":{"id":"251211","name":"ALPHA IMÓVEL","address":{"country":"Brasil","zipCode":"06543-001","city":"Santana de Parnaíba","streetNumber":"4000","zone":"","street":"Avenida Marcos Penteado de Ulhôa Rodrigues","locationId":"","district":"","unitNumber":"","state":"SP","neighborhood":"Tamboré"},"phone":{"leadsPhone":"","mobile":"11991076161","alternative":"","primary":"1141950195"},"logoUrl":"https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/46c3a76e0d71a18194a319ab626b4cc5.jpg","licenseNumber":"18786-J-SP","websiteUrl":"http://www.alphaimovel.com.br/","leadEmails":[],"createdDate":"2018-03-28T10:42:55Z","showAddress":true},"url":{"id":"1037532390","link":{"name":"Apartamento com 3 Quartos para venda ou aluguel, 112m²","href":"/imovel/apartamento-3-quartos-empresarial-18-do-forte-bairros-barueri-com-garagem-112m2-venda-RS939901-id-1037532390/","rel":""}},"properAddress":null,"publisherUrl":{"link":{"name":"","href":"/251211/alpha-imovel/","rel":""}}},{"listing":{"amenities":["NEAR_ACCESS_ROADS","NEAR_SHOPPING_CENTER","NEAR_PUBLIC_TRANSPORT","NEAR_SCHOOL","NEAR_HOSPITAL","BARBECUE_GRILL","ELEVATOR","GOURMET_SPACE","GYM","PARTY_HALL","PLAYGROUND","POOL","ADULT_POOL","CHILDRENS_POOL","AIR_CONDITIONING","BALCONY","FULL_CABLING","GARAGE","LAUNDRY","KITCHEN","SERVICE_AREA","EXTERIOR_VIEW","HEATING","ALARM_SYSTEM","GATED_COMMUNITY","INTERCOM","SECURITY_24_HOURS","SAFETY_CIRCUIT","WATCHMAN","ADULT_GAME_ROOM","YOUTH_GAME_ROOM","RECEPTION","MASSAGE","SAUNA","ESSENTIAL_PUBLIC_SERVICES","SPA","GOURMET_BALCONY","NUMBER_OF_FLOORS","ELECTRIC_GENERATOR"],"feedsId":"","usableAreas":[85],"description":"Campanha Invest Bem MPD,..Várias oportunidades de negócio em diversos empreendimentos,...Aproveite!!<br>Present Residencial Alphaville <br>Apartamentos de 2 e 3 dormitórios + Lavabo e 2 vagas.<br>Pronto para morar,<br>Avenida Ômega,. Alphaville, Barueri/SP<br>Present Alphaville é um projeto exclusivo que alia natureza e contemporaneidade numa localização privilegiada,...<br>Lazer panorâmico na cobertura,.Um dos grandes diferenciais do empreendimento,.Com linda vista para uma área de preservação e um lago: O Sky Space. Um conceito inédito de lazer com salão de jogos, churrasqueira com forno de pizza, espaço gourmet, espaço de convivência e terraço panorâmico. Já no térreo, a área de lazer é composta por duas piscinas (adulto e infantil), solarium, salão de festas, pet place, brinquedoteca, fitness, sala de ginástica, playground, deck molhado, espaço de convivência e sauna seca com descanso.<br>Perto de escola, parques, pista de caminhada, restaurantes, Shoppings, Supermercados, farmácias, hospitais, bancos, e principais vias de acesso para São Paulo e interior,.<br>Além disso,......A Construtora acabou de baixar os preços,.Confira nossas oportunidades,.Valores a partir de:<br>85 m² com 2 suítes + lavabo - R$ 593,6 mil<br>112 m² com 3 suítes + lavabo - R$ 729 mil<br>Financiamento bancário ou direto com a construtora.<br>Além das duas modalidades de financiamento, temos também a opção de aluguel investido, onde o valor pago de aluguel, será revertido como crédito para compra do apartamento,...Show!!<br>Aproveite!<br>Ligue agora mesmo tire sua dúvida e agende uma visita!<br>11 9 8 0 7 4 0 2 6 7<br>11 4 2 3 7 5 6 6 2<br>Att,<br>Roberto<br>Corretor de imóveis, CRECI - 151452/SPF","listingType":"USED","title":"Apartamentos de 2 e 3 dormitórios Alphaville","createdAt":"2018-04-25T18:02:12.467Z","publisherId":101150,"unitTypes":["APARTMENT"],"providerId":"VIVAREAL","condominiumName":"","propertyType":"UNIT","contact":{"chat":"","phones":["1148610958"],"emails":[]},"listingStatus":"ACTIVE","id":"94794243","parkingSpaces":[2],"updatedAt":"2019-05-03T16:50:03.800Z","owner":false,"address":{"country":"Brasil","state":"São Paulo","city":"Barueri","neighborhood":"Alphaville 18 Forte","street":"Avenida Ômega","streetNumber":"171","unitNumber":"","zipCode":"06472005","locationId":"BR>Sao Paulo>NULL>Barueri>Barrios>Alphaville 18 Forte","zone":"Bairros","district":"","geoLocation":{"location":{"lat":-23.483886,"lon":-46.849025},"precision":"ROOFTOP","optionalPrecision":"precision"}},"suites":[2],"publicationType":"STANDARD","externalId":"PRESENT","bathrooms":[3],"totalAreas":[85],"logoUrl":"","bedrooms":[2],"promotions":[],"highlights":"","pricingInfos":[{"yearlyIptu":"0","price":"593681","businessType":"SALE","monthlyCondoFee":"0"}],"showPrice":true,"displayAddress":"ALL","images":["https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/61266525c383243f55c66b2fa3440141.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/041bcf5d6f3726f98df46635f48fc0b8.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/8ea7a744987697b7ffa3e3655044f01d.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/9472914bcaedcb5278aca2a4b246395d.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/4d94ba83fb8a9cd07a33ba609bfdfcff.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/53bd16cced938c161bdbd4eade2bde17.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/5b7fcca96975bd61964e1961d06d96ac.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/6d12255084ba32f315c6082aedd1aa5e.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/b2c6e07cdc79d81ec6f9eadbafce60f1.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/23cdc5d7171545e4aeafb66dd065aa04.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/ed8732b167ef1b01a9209ab74a8793d3.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/db129c9c2911c8c7d57fe220a8eb6840.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/0b2bea281f7a5f092987fb5be8488f0b.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/e1a143c5c726f07aeab6f5695f4cea2d.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/5bd223ff4f28ffe640caebcc5163be69.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/c57923d7bbc72fc8059111dd49f78767.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/72572cedabd9e6d2a85d4ce082f4ce9d.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/2e9965107ed67bce8bcce84e51f68f66.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/05a52a8f7d0a103942d4359dbc909c0d.jpg"],"videos":[]},"publisher":{"id":"101150","name":"José Roberto Santos de Carvalho","address":{"country":"Brasil","zipCode":"06253-020","city":"Osasco","streetNumber":"530","zone":"","street":"Rua Nelson Rodrigues","locationId":"","district":"","unitNumber":"","state":"SP","neighborhood":"Helena Maria"},"phone":{"leadsPhone":"1148610958","mobile":null,"alternative":"","primary":"1148610958"},"logoUrl":"","licenseNumber":"151452-F-SP","websiteUrl":"","leadEmails":[],"createdDate":"2018-03-27T21:25:58Z","showAddress":true},"url":{"id":"94794243","link":{"name":"Apartamento com 2 Quartos à venda, 85m²","href":"/imovel/apartamento-2-quartos-alphaville-18-forte-bairros-barueri-com-garagem-85m2-venda-RS593681-id-94794243/","rel":""}},"properAddress":null,"publisherUrl":{"link":{"name":"","href":"/101150/jose-roberto-santos-de-carvalho/","rel":""}}},{"listing":{"amenities":["ELECTRIC_GENERATOR","RECEPTION","SAFETY_CIRCUIT","GATED_COMMUNITY","GYM","BARBECUE_GRILL","GOURMET_SPACE","GARDEN","POOL","PLAYGROUND","SQUASH","TENNIS_COURT","SPORTS_COURT","PARTY_HALL","ADULT_GAME_ROOM","ELEVATOR","LAUNDRY","SAUNA","SPA","AIR_CONDITIONING","GOURMET_BALCONY"],"feedsId":"","usableAreas":[85],"description":"O apartamento está localizado no bairro Melville Empresarial I e II possui 85 metros quadrados com 2 quartos sendo 2 suites e 3 banheiros. A alguns minutos de restaurantes, hospitais, farmácias, estacionamentos, universidades, shoppings, padarias, hospitais, transporte coletivo, escolas.<br>Possui academia, espaço gourmet, jardim, parquinho com diferentes brinquedos, espaço para festas.<br>Vai lhe possibilitar curtir os dias mais quentes na piscina, praticar diversos esportes na quadra poliesportiva, todo o conforto do ar condicionado nos dias mais quentes.Fica em um condomínio fechado.<br>Espaço reservado para preparar o seu churrasco.<br>Elevador para mais praticidade no dia-a-dia.<br><br>Este valor refere se a unidade 16, pronto para morar","listingType":"USED","title":"Apartamento para venda possui 85 metros com 2 quartos em Melville I e II - Barueri - SP","createdAt":"2019-05-11T16:48:33.952Z","publisherId":536971,"unitTypes":["APARTMENT"],"providerId":"VIVAREAL","condominiumName":"PRESENT ALPHAVILLE","propertyType":"UNIT","contact":{"chat":"","phones":["11992803316","11992930597"],"emails":[]},"listingStatus":"ACTIVE","id":"2444438277","parkingSpaces":[2],"updatedAt":"2019-06-03T14:03:11.936Z","owner":false,"address":{"country":"Brasil","state":"São Paulo","city":"Barueri","neighborhood":"Melville Empresarial Ii","street":"Avenida Ômega","streetNumber":"171","unitNumber":"","zipCode":"06472005","locationId":"BR>Sao Paulo>NULL>Barueri>Barrios>Melville Empresarial Ii","zone":"Bairros","district":"","geoLocation":{"location":{"lat":-23.484829,"lon":-46.851078},"precision":"ROOFTOP","optionalPrecision":"precision"}},"suites":[2],"publicationType":"PREMIUM","externalId":"present85","bathrooms":[3],"totalAreas":[],"logoUrl":"","bedrooms":[2],"promotions":[],"highlights":"","pricingInfos":[{"period":"MONTHLY","yearlyIptu":"0","price":"617000","businessType":"SALE","monthlyCondoFee":"468"}],"showPrice":true,"displayAddress":"ALL","buildings":1,"images":["https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/98876f82dc5cf8065ba96d5978e3d40b.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/b6a88bb3b8bd78ee9744acab2e842285.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/2c27a4e676b2d7c73b6fc42535997653.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/a858177f5ac11a7d4a66e9b5e3e82c14.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/be96064cb7f48b8dc93689d91fb51474.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/1d04339be05f495ecb721a6dd3fe40f6.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/6b566206afe99f1f40207e3606bbe173.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/bf9a6276281cd3b5f3f5b990aabac181.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/081c9e4d6a1d4128ca00e8510e1b72bf.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/c9abdaa0f7d6d3939c8018a8d2df6a35.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/3ee73a84995bc076ffebddf770bea910.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/b4c71f8b0a246fbc76cc670ab7ab2ce3.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/13c028d0cee4274f102981467dbea11d.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/3aa92cf3af828a237936f0161189ab53.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/fbe3d6e23174dea66425ac606ec24d1d.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/6e16d805bccd88e3a5df9e5c0d3474de.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/6f1b626140ad4cea1b3b75b81dbf4cb8.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/f76e9ef2eb833412aedcb7e9cf72ebd2.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/3144ba318e66a25d7a1011954f6129d1.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/bc05261e3b4a723d8b2820acb3c2e61b.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/819e0b5ed9d9c129c248791d7ed2059c.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/86a2e795ec01c32ccfaeb037b340c010.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/024a7b2b3d992c3ceae7989ccf0fa15f.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/88d74e44936adbb327974da5bfe0fc18.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/5d1c3e847e27e7c0d20b8aef0b570c41.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/bba0159f3b3a1fe36e04454225fd41f5.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/0f414210104b5508a1495ff0629af6c8.jpg"],"videos":["https://www.youtube.com/watch?v=xndW58OAy-0&t=3s"]},"publisher":{"id":"536971","name":"Joao Lucas Minuncio  - Corretor","phone":{"leadsPhone":"","mobile":"11992930597","alternative":"","primary":"11992803316"},"logoUrl":"","licenseNumber":"177047-F-SP","websiteUrl":"","leadEmails":[],"createdDate":"2019-04-26T18:38:21Z","showAddress":false},"url":{"id":"2444438277","link":{"name":"Apartamento com 2 Quartos à venda, 85m²","href":"/imovel/apartamento-2-quartos-melville-empresarial-ii-bairros-barueri-com-garagem-85m2-venda-RS617000-id-2444438277/","rel":""}},"properAddress":null,"publisherUrl":{"link":{"name":"","href":"/536971/joao-lucas-minuncio-corretor/","rel":""}}},{"listing":{"amenities":["NEAR_PUBLIC_TRANSPORT","NEAR_SCHOOL","BALCONY","FULL_CABLING","GARAGE","LAUNDRY","SERVICE_AREA","KITCHEN","EXTERIOR_VIEW","HEATING","AIR_CONDITIONING","GATED_COMMUNITY","INTERCOM","SECURITY_24_HOURS","SAFETY_CIRCUIT","ELECTRIC_GENERATOR","LAKE_VIEW","SPA","SAUNA","YOUTH_GAME_ROOM","ADULT_GAME_ROOM","ADULT_POOL","CHILDRENS_POOL","PARTY_HALL","GYM","GOURMET_SPACE","GARDEN","BARBECUE_GRILL","ELEVATOR","PLAYGROUND","POOL"],"feedsId":"","usableAreas":[85],"description":"O apartamento de 85 metros quadrados está localizado no bairro Melville Empresarial I e II com 2 quartos sendo 2 suítes e 2 banheiros. A apenas alguns instantes de estacionamentos, padarias, escolas, restaurantes, shoppings, universidades, hospitais e transporte coletivo.<br>Tem sacada, academia, jardim, espaço gourmet e salão para festas e eventos.<br>O apartamento vai lhe possibilitar todo o conforto do ar condicionado nos dias mais quentes.<br>Além disso, segurança 24 horas e piscina para lazer e prática de exercícios para você e sua família.<br>Churrasqueira para você aproveitar nos momentos de descontração.<br>Elevador que garante o transporte das suas malas e compras.<br>Fica em um condomínio fechado.","listingType":"USED","title":"Apartamento para venda com 85 metros quadrados e 2 quartos em 18 do forte alphaville","createdAt":"2018-08-03T19:37:55.888Z","publisherId":376928,"unitTypes":["APARTMENT"],"providerId":"VIVAREAL","condominiumName":"","propertyType":"UNIT","contact":{"chat":"","phones":["1134192437","11959117003"],"emails":[]},"listingStatus":"ACTIVE","id":"1039335185","parkingSpaces":[2],"updatedAt":"2019-04-02T20:05:32.436Z","owner":false,"address":{"country":"Brasil","state":"São Paulo","city":"Barueri","neighborhood":"Alphaville 18 Forte","street":"Avenida Ômega","streetNumber":"171","unitNumber":"","zipCode":"06472005","locationId":"BR>Sao Paulo>NULL>Barueri>Barrios>Alphaville 18 Forte","zone":"Bairros","district":"","geoLocation":{"location":{"lat":-23.483886,"lon":-46.849025},"precision":"ROOFTOP","optionalPrecision":"precision"}},"suites":[2],"publicationType":"STANDARD","externalId":"d02bdc","bathrooms":[2],"totalAreas":[85],"logoUrl":"","bedrooms":[2],"promotions":[],"highlights":"","pricingInfos":[{"yearlyIptu":"0","price":"627800","businessType":"SALE","monthlyCondoFee":"0"}],"showPrice":true,"displayAddress":"ALL","images":["https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/ecfbd8977a49e7ba993b2070b5c84764.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/0cdd63dafc05b9635e5f0ebbdb8be73d.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/85a03df8991aedfe14b3087abf5d65c1.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/64c4ed629d94edac6d66e98d4c299bb2.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/2ccb913342aaa4d15c4bc455d6328391.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/1a95110e05bf4aaabf6a2ec569c6c14a.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/5f0cdd4ef82ec3da0a1f8ae2355486a0.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/0191aa630e9c6c9bdf521dddcfabc26a.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/59b407fd2fee349e0e3bc8673b12bedb.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/5c5d86524980e41ff282b0ff0d57e751.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/18bed11dc9afa539927ebcf8d498b323.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/25891a9b63e82c3ef7720d3d031b6b20.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/7dbbb24d15884c801cc8a045241f80f1.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/00b916fc2ac11b932232de6771fdab24.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/c76c1bcb2b007c81d9d7e1c07b8e47d7.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/974906e876863f0921cea38ac4223cef.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/5870dd10f34446f937eb45eca7ed03dd.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/d90f80b433db20f5c7e4bb8a225943bb.jpg"],"videos":[]},"publisher":{"id":"376928","name":"Aliança Plus Consultoria Imobiliária","address":{"country":"Brasil","zipCode":"06414-070","city":"Barueri","streetNumber":"263","zone":"","street":"Rua Sol","locationId":"","district":"","unitNumber":"","state":"SP","neighborhood":"Jardim Tupanci"},"phone":{"leadsPhone":"","mobile":"11959117003","alternative":"","primary":"1134192437"},"logoUrl":"https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/a8feeb62f043ab23caa68efa053b4bc3.jpg","licenseNumber":"","websiteUrl":"","leadEmails":[],"createdDate":"2018-07-25T14:28:18Z","showAddress":true},"url":{"id":"1039335185","link":{"name":"Apartamento com 2 Quartos à venda, 85m²","href":"/imovel/apartamento-2-quartos-alphaville-18-forte-bairros-barueri-com-garagem-85m2-venda-RS627800-id-1039335185/","rel":""}},"properAddress":null,"publisherUrl":{"link":{"name":"","href":"/376928/alianca-plus-consultoria-imobiliaria/","rel":""}}},{"listing":{"amenities":["BARBECUE_GRILL","PLAYGROUND","GYM","ADULT_GAME_ROOM","INTERCOM","GARAGE","GARDEN","SERVICE_AREA"],"feedsId":"IMO2","usableAreas":[85],"description":"Present Alphaville é um projeto exclusivo que alia natureza e contemporaneidade numa localização privilegiada,...<br>Lazer panorâmico na cobertura,.Um dos grandes diferenciais do empreendimento,.Com linda vista para uma área de preservação e um lago: O Sky Space. Um conceito inédito de lazer com salão de jogos, churrasqueira com forno de pizza, espaço gourmet, espaço de convivência e terraço panorâmico. Já no térreo, a área de lazer é composta por duas piscinas (adulto e infantil), solarium, salão de festas, pet place, brinquedoteca, fitness, sala de ginástica, playground, deck molhado, espaço de convivência e sauna seca com descanso.<br>Perto de escola, parques, pista de caminhada, restaurantes, Shoppings, Supermercados, farmácias, hospitais, bancos, e principais vias de acesso para São Paulo e interior.","listingType":"USED","title":"BARUERI - Padrão - EMPRESARIAL 18 DO FORTE","createdAt":"2019-01-04T12:48:59.309Z","publisherId":376928,"unitTypes":["APARTMENT"],"providerId":"329","condominiumName":"","propertyType":"UNIT","contact":{"chat":"","phones":["1134192437","11959117003"],"emails":[]},"listingStatus":"ACTIVE","id":"2427889480","parkingSpaces":[2],"updatedAt":"2019-06-08T08:33:45.205Z","owner":false,"address":{"country":"Brasil","state":"São Paulo","city":"Barueri","neighborhood":"Empresarial 18 do Forte","unitNumber":"","zipCode":"06471001","locationId":"BR>Sao Paulo>NULL>Barueri>Barrios>Empresarial 18 do Forte","zone":"Bairros","district":"","geoLocation":{"location":{"lat":-23.484829,"lon":-46.851078},"precision":"ROOFTOP","optionalPrecision":"precision"}},"suites":[2],"publicationType":"STANDARD","externalId":"IMO2","bathrooms":[2],"totalAreas":[],"logoUrl":"","bedrooms":[2],"promotions":[],"highlights":"","pricingInfos":[{"price":"627800","businessType":"SALE"}],"showPrice":true,"displayAddress":"NEIGHBORHOOD","buildings":0,"images":["https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/5e88780f87e77e567915ac64eb97d43d.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/c0e7dd26392dd63c791cbffee857db54.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/55207206335f6d55f8369f72cece112e.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/a7f6c1fbd031000c347127e47cf3086b.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/b97dfdee26ae257a55850ac4e711a4f8.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/c1f2ee8431fbfaa3ca567aa5c9eb450d.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/3711ea76c304a84df9e4cf0025a0bada.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/b53a5b8e7bffa0563d02245cb1a424cd.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/ec685cb467881b5d6d859b75adcf3ef9.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/7e3fecdc31d57a96c169a555dac42b1f.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/ac4de16af41b9005d6baddb2093102cd.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/d1a560411229dd4b5ff424cb9e58d5f1.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/37bc9dafad6ebbcd6f59e8adecf477aa.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/4244f281783c771e628f44e8d0222bdf.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/cf18564669f0fbe9a3dcdf7df669bcdf.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/073a06a2663aaed93830c3b6acb7a1a8.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/e29ec8490be36a3d76c703cef595b8c2.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/53d753d2e3398ced37cf7156688d77d2.jpg"],"videos":[]},"publisher":{"id":"376928","name":"Aliança Plus Consultoria Imobiliária","address":{"country":"Brasil","zipCode":"06414-070","city":"Barueri","streetNumber":"263","zone":"","street":"Rua Sol","locationId":"","district":"","unitNumber":"","state":"SP","neighborhood":"Jardim Tupanci"},"phone":{"leadsPhone":"","mobile":"11959117003","alternative":"","primary":"1134192437"},"logoUrl":"https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/a8feeb62f043ab23caa68efa053b4bc3.jpg","licenseNumber":"","websiteUrl":"","leadEmails":[],"createdDate":"2018-07-25T14:28:18Z","showAddress":true},"url":{"id":"2427889480","link":{"name":"Apartamento com 2 Quartos à venda, 85m²","href":"/imovel/apartamento-2-quartos-empresarial-18-do-forte-bairros-barueri-com-garagem-85m2-venda-RS627800-id-2427889480/","rel":""}},"properAddress":null,"publisherUrl":{"link":{"name":"","href":"/376928/alianca-plus-consultoria-imobiliaria/","rel":""}}},{"listing":{"amenities":["NEAR_ACCESS_ROADS","NEAR_SHOPPING_CENTER","NEAR_PUBLIC_TRANSPORT","NEAR_SCHOOL","NEAR_HOSPITAL","BARBECUE_GRILL","ELEVATOR","GARDEN","GOURMET_SPACE","GYM","PARTY_HALL","PLAYGROUND","POOL","SAUNA","ALARM_SYSTEM","GATED_COMMUNITY","INTERCOM","SECURITY_24_HOURS","SAFETY_CIRCUIT","SPA"],"feedsId":"","usableAreas":[85],"description":"Apartamento amplo no condomínio Present em Alphaville, PRONTO PARA MORAR com 85m², varanda gourmet, 2 suítes e 2 vagas de garagem.<br><br>Condomínio com lazer completo localizado em uma das regiões mais privilegiadas de Alphaville, o 18 do Forte. Próximo a Hospitais, Colégios, restaurantes e centros empresariais. <br><br>Últimas Unidades Direto com a Construtora. <br>Agende uma visita e conheça!","listingType":"USED","title":"Apartamento em Alphaville","createdAt":"2018-05-15T21:59:31.792Z","publisherId":140041,"unitTypes":["APARTMENT"],"providerId":"VIVAREAL","condominiumName":"","propertyType":"UNIT","contact":{"chat":"","phones":["11972162424","11972162424"],"emails":[]},"listingStatus":"ACTIVE","id":"95308375","parkingSpaces":[2],"updatedAt":"2019-04-29T18:25:03.339Z","owner":false,"address":{"country":"Brasil","state":"São Paulo","city":"Barueri","neighborhood":"Empresarial 18 do Forte","street":"Avenida Ômega","streetNumber":"171","unitNumber":"","zipCode":"06472005","locationId":"BR>Sao Paulo>NULL>Barueri>Barrios>Empresarial 18 do Forte","zone":"Bairros","district":"","geoLocation":{"location":{"lat":-23.483886,"lon":-46.849025},"precision":"ROOFTOP","optionalPrecision":"precision"}},"suites":[2],"publicationType":"STANDARD","externalId":"PRES123085","bathrooms":[2],"totalAreas":[85],"logoUrl":"","bedrooms":[2],"promotions":[],"highlights":"","pricingInfos":[{"yearlyIptu":"0","price":"631270","businessType":"SALE","monthlyCondoFee":"0"}],"showPrice":true,"displayAddress":"ALL","images":["https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/f2dd53e89055b8b349d0421671f992b1.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/89aac85a559e772bcbcba4e07a390635.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/ddd91b39c163d715d9149b500c89e6cc.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/fc1285fc72defa00f762a63a598c2cb6.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/e4c0b29829daaa8041ab6c0101ac9b8f.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/a30a0f414d14ee945165fe4a2625fd55.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/bda37bd2b3319b51b9f95dc6460b0f2b.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/a873318d05ec36a6b0e028447e862ffb.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/b42754483ec0695263d45f9bd43fb95f.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/a63bbc6c3e7d7e57618a72e4f6e322c4.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/794a8f48183a31894dada84786f4d050.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/cd10dab8143fd898066ba84abccca531.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/d9e352ae71b3677741beaac3d526fe8d.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/fcc63cca12340fa3efe685f29eee7522.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/0f03f4167e067a2a7fc1d6bef61b7f59.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/6a697187ff1a3d1e0b292f2a3ace612a.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/8718f8aa509ba400eadf1be7e437f28b.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/9e549816ca970a1a4d981f928b78a196.jpg"],"videos":[]},"publisher":{"id":"140041","name":"Adalberson Silva Lino","phone":{"leadsPhone":"","mobile":"11972162424","alternative":"","primary":"11972162424"},"logoUrl":"","licenseNumber":"","websiteUrl":"","leadEmails":[],"createdDate":"2018-03-27T19:02:06Z","showAddress":false},"url":{"id":"95308375","link":{"name":"Apartamento com 2 Quartos à venda, 85m²","href":"/imovel/apartamento-2-quartos-empresarial-18-do-forte-bairros-barueri-com-garagem-85m2-venda-RS631270-id-95308375/","rel":""}},"properAddress":null,"publisherUrl":{"link":{"name":"","href":"/140041/adalberson-silva-lino/","rel":""}}},{"listing":{"amenities":["SAFETY_CIRCUIT","AIR_CONDITIONING","BARBECUE_GRILL","ELEVATOR","GYM","POOL","CINEMA","ADULT_GAME_ROOM","BALCONY","INTERCOM","GOURMET_SPACE","SPORTS_COURT","PLAYGROUND","SPA","PARTY_HALL","MASSAGE","SAUNA","SECURITY_24_HOURS"],"feedsId":"16185","usableAreas":[85],"description":"Apartamento 18 do Forte 85 Metros 2 Suítes 2 Vagas<br><br>Torre Única com Varanda Gourmet e Cobertura Panorâmica<br><br>Apartamento com 2 suítes maravilhosas, porcelanato nas áreas frias, metais Deca, terraço gourmet amplo e espaçoso com churrasqueira, sala 2 ambientes, 2 vagas de garagem cobertas. Única Torre. Lazer no último pavimento, uma linda vista panorâmica dos residenciais de altíssimo padrão ! Próximo a Alameda Rio Negro, completa infraestrutura de comércio e serviços , ao lado da Escola Internacional, ótimos restaurantes e academias. Lugar repleto de verde e muita tranquilidade . - Anúncio do corretor de imóveis Caroline Masi - CRECI: 183260","listingType":"USED","title":"Apartamento para venda Melville Empresarial I e II 2 dormitórios","createdAt":"2018-12-21T03:49:11.950Z","publisherId":234940,"unitTypes":["APARTMENT"],"providerId":"17973","condominiumName":"","propertyType":"UNIT","contact":{"chat":"","phones":["11989251160","11971074412"],"emails":[]},"listingStatus":"ACTIVE","id":"2123195473","parkingSpaces":[2],"updatedAt":"2019-06-13T04:55:05.303Z","owner":false,"address":{"country":"Brasil","state":"São Paulo","city":"Barueri","neighborhood":"Alphaville","street":"Avenida Ômega","unitNumber":"","zipCode":"06472005","locationId":"BR>Sao Paulo>NULL>Barueri>Barrios>Alphaville","zone":"Bairros","district":"","geoLocation":{"location":{"lat":-23.484829,"lon":-46.851078},"precision":"ROOFTOP","optionalPrecision":"precision"}},"suites":[2],"publicationType":"STANDARD","externalId":"16185","bathrooms":[3],"totalAreas":[85],"logoUrl":"","bedrooms":[2],"promotions":[],"highlights":"","pricingInfos":[{"yearlyIptu":"600","price":"650000","businessType":"SALE","monthlyCondoFee":"500"}],"showPrice":true,"displayAddress":"STREET","buildings":0,"images":["https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/2cf7b7892466113f52f289e2d96f144f.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/ad0b2442fee566eba7697fd29fcad9c4.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/265b4f8822f35a4e88e355cc9bbf1736.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/8bd768ee41858585f6608b81e6938366.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/55a7e1eb85315e750c646830b8a62aef.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/8314fee51999d000f9bc5c274d465a39.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/b9a8a10bf98c5ad04ea1f4162bdf0b44.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/02e37b1f8f523073115eb008d11b85d2.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/00e8c20d380c7399bc772df5542ac284.jpg"],"videos":[]},"publisher":{"id":"234940","name":"USUÁRIO NEWCORE","address":{"country":"Brasil","zipCode":"04501-000","city":"São Paulo","streetNumber":"331","zone":"","street":"Avenida República do Líbano","locationId":"","district":"","unitNumber":"","state":"SP","neighborhood":"Ibirapuera"},"phone":{"leadsPhone":"","mobile":"11971074412","alternative":"","primary":"11989251160"},"logoUrl":"https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/3ac8702f4b33fb33b07a90112755ee96.jpg","licenseNumber":"160778-J-SP","websiteUrl":"","leadEmails":[],"createdDate":"2018-03-27T23:24:33Z","showAddress":true},"url":{"id":"2123195473","link":{"name":"Apartamento com 2 Quartos à venda, 85m²","href":"/imovel/apartamento-2-quartos-alphaville-bairros-barueri-com-garagem-85m2-venda-RS650000-id-2123195473/","rel":""}},"properAddress":null,"publisherUrl":{"link":{"name":"","href":"/234940/usuario-newcore/","rel":""}}},{"listing":{"amenities":["AIR_CONDITIONING","BARBECUE_GRILL","KITCHEN","ELEVATOR","GOURMET_BALCONY","INTERCOM","POOL","BALCONY","ALARM_SYSTEM","CABLE_TV","SAUNA","SERVICE_AREA"],"feedsId":"AP0485","usableAreas":[85],"description":"Amplo Apartamento com 2 Suítes, sendo 1 Master com Varanda lavado, Sala de Estar, Sala de Jantar, Varanda com Churrasqueira, Cozinha, Área de Serviço, 2 Vagas de Garagem !!<br>Total Infraestrutura de Lazer e segurança com :<br>Churrasqueira, Espaço Gourmet, Fitness, Lazer Infantil, Piscina Adulto, Piscina Infantil, Sauna, Pet Place, Salão de festas, Espaço convivência, Espaço de descanço com sauna seca, Home Office<br>Maravilhosa Vista na Cobertura com Espaço Convivência !!<br>Agende sua Visita -","listingType":"USED","title":"Alphaville -18 do Forte - 2 Suítes - Alto Padrão - 85 m² de Área Útil !!","createdAt":"2018-05-30T17:35:44.030Z","publisherId":225320,"unitTypes":["APARTMENT"],"providerId":"7739","condominiumName":"","propertyType":"UNIT","contact":{"chat":"","phones":["1141182388","11968982828"],"emails":[]},"listingStatus":"ACTIVE","id":"1037386790","parkingSpaces":[2],"updatedAt":"2019-06-04T00:03:19.435Z","owner":false,"address":{"country":"Brasil","state":"São Paulo","city":"Barueri","neighborhood":"Empresarial 18 do Forte","street":"Avenida Ômega","streetNumber":"171","unitNumber":"","zipCode":"06472005","locationId":"BR>Sao Paulo>NULL>Barueri>Barrios>Empresarial 18 do Forte","zone":"Bairros","district":"","geoLocation":{"location":{"lat":-23.484829,"lon":-46.851078},"precision":"ROOFTOP","optionalPrecision":"precision"}},"suites":[2],"publicationType":"PREMIUM","externalId":"AP0485","bathrooms":[3],"totalAreas":[],"logoUrl":"","bedrooms":[2],"promotions":[],"highlights":"","pricingInfos":[{"yearlyIptu":"160","price":"651000","businessType":"SALE","monthlyCondoFee":"790"}],"showPrice":true,"displayAddress":"ALL","buildings":0,"images":["https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/d04b73e43c1c1b74b9a7aae3ea4fb48b.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/f0bd7be005191346ebeedb2e413db0b5.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/98d62800a29f9afdf765597fffb4f074.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/e4564f59ad89763c7ffed290fd31ace8.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/0a53966737ccc1d38f6a8ffe20cf129b.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/2a0323811b66b43c8f82793114e2e0c9.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/78b0fbc98f180e00c7e7fbe18a487a24.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/0499d846f5d082a68a1206c4eff13872.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/cd7d28208db290ca6c367671a65b5efb.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/9289d38e10e651e45aaa57d2d5496324.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/e4f85fdb33cd6d7dcb1ce41c3a3fc3cc.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/0f054d50115f49f2706dd228f467a8e2.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/9def69efe9f673e6bb23321516c75fc1.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/3692c1ee42f674c62d46e260bae7b206.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/00f6523da7aeb410246b52fd2dbc573f.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/ea43b22882a59e485da342057d26c603.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/08196cf88c8fd4724af1685246998cbb.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/ba3181554a44ccf44c765135713dfac1.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/ca7a3e2b20d6d2081c13cd116e181615.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/2a5ee08e0c803400bdaa08922081a8b3.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/944bdd46717bbc79cd112cc041a4c82e.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/4e7d19634af8fa3599f6c3a479f4072c.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/3257731e9248647f9588ec2288f7ae3c.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/6c86e7e623fd6227bd28588ea94d7c0d.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/035b1a1c29faf4a64048d13629010050.jpg"],"videos":[]},"publisher":{"id":"225320","name":"OTTO DESENVOLVIMENTO IMOBILIARIO LTDA","address":{"country":"Brasil","zipCode":"02036-011","city":"SAO PAULO","streetNumber":"577","zone":"","street":"R. Dr. Gabriel Piza, 577","locationId":"","district":"","unitNumber":"","state":"SP","neighborhood":"Santana"},"phone":{"leadsPhone":"","mobile":"11968982828","alternative":"","primary":"1141182388"},"logoUrl":"https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/60e663554b143c607112ba8eebc031a8.jpg","licenseNumber":"79955-J-SP","websiteUrl":"http://www.ottoimob.com.br","leadEmails":[],"createdDate":"2018-03-28T09:45:45Z","showAddress":true},"url":{"id":"1037386790","link":{"name":"Apartamento com 2 Quartos à venda, 85m²","href":"/imovel/apartamento-2-quartos-empresarial-18-do-forte-bairros-barueri-com-garagem-85m2-venda-RS651000-id-1037386790/","rel":""}},"properAddress":null,"publisherUrl":{"link":{"name":"","href":"/225320/otto-desenvolvimento-imobiliario-ltda/","rel":""}}},{"listing":{"amenities":["BARBECUE_GRILL","ELEVATOR","GOURMET_BALCONY","POOL","PLAYGROUND","PARTY_HALL","SECURITY_24_HOURS","GOURMET_SPACE","ADULT_GAME_ROOM","MASSAGE","SAUNA"],"feedsId":"AP0843","usableAreas":[85],"description":"Terraço gourmet, previsão para churrasqueira, preparado para ar condicionado nos dormitórios e sala (infraestrutura - ponto de energia no terraço técnico e passagens nas alvenarias para futura instalação de tubulação frigorígena e equipamentos pelo cliente, lavabo em todos os apartamentos, 2 vagas indeterminadas, caixilho tipo persiana de enrolar, misturador de água quente e água fria nas torneiras da cozinha e banheiros, pé-direito de 2,80m (sala e dormitórios). O Empreendimento será construído em estrutura de concreto convencional, com as divisões internas entre as unidades em alvenaria de vedação, vagas para visitantes na frente do condomínio, vaga de carga e descarga dentro da garagem, vestiários e fereitório para funcionários do condomínio, gerador para resgate de todos os elevadores e atendimento de um elevador, bacias sanitárias com duplo acionamento, espaço reservado para coleta seletiva de lixo reciclável, portaria com Delivery, Acesso Social e Serviço isolados, medição individualizada de água, previsão para medição individualizada de gás, cobertura de lazer, áreas sociais entregues decoradas e equipadas. Aptos com 85,00 / 112,00 m2 / 2 e 3 dormitórios. -","listingType":"USED","title":"Present Alphaville NOVO!!","createdAt":"2018-05-05T01:23:10.994Z","publisherId":251211,"unitTypes":["APARTMENT"],"providerId":"23014","condominiumName":"","propertyType":"UNIT","contact":{"chat":"","phones":["1141950195","11991076161"],"emails":[]},"listingStatus":"ACTIVE","id":"95060085","parkingSpaces":[2],"updatedAt":"2019-05-20T23:28:18.478Z","owner":false,"address":{"country":"Brasil","state":"São Paulo","city":"Barueri","neighborhood":"Empresarial 18 do Forte","street":"Avenida Ômega","unitNumber":"","zipCode":"06472005","locationId":"BR>Sao Paulo>NULL>Barueri>Barrios>Empresarial 18 do Forte","zone":"Bairros","district":"","geoLocation":{"location":{"lat":-23.484829,"lon":-46.851078},"precision":"ROOFTOP","optionalPrecision":"precision"}},"suites":[1],"publicationType":"STANDARD","externalId":"AP0843","bathrooms":[2],"totalAreas":[85],"logoUrl":"","bedrooms":[2],"promotions":[],"highlights":"","pricingInfos":[{"yearlyIptu":"0","price":"665000","businessType":"SALE","monthlyCondoFee":"600"}],"showPrice":true,"displayAddress":"STREET","buildings":0,"images":["https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/97c54eca7410a63265add519c2b6283d.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/b2c520c742df7d08c725f6c62d5f7c0e.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/31397bb3d5feec648a29450557d6f767.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/7f76eedf35253d09ab9f73f745e3e891.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/93ac5e078530a558f061dc8f0d3e632e.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/87c3001b42e6b8f8d45742453353117c.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/d7e7173030ebb83c21725f1491b3947e.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/777978871f4a6693b06b7f445f61b0bc.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/b711e0414c10807ba75a4996c5b84b99.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/b4100a830f03867ddc71d67ca3e3077e.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/46727c69dd133a670ec34ee982d2d134.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/58f3757f44938e52e829176ffd14cdd5.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/45ad7fbf6b79783af33124d74c097880.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/0deba25a833e7e1fc9903e02bcc39646.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/f186af66b4ca46652e93433954be1c69.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/0b04cbd9934a19c216b4cc8137ca2f93.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/fc399218ae40ba6b10b3729b178b70f0.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/c1276656fa839cf5e17a4cf16e743c27.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/c26fdb59b8efddc58d678af77ff0e424.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/6383ed8e81dfa7d28c17288f45082e00.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/6dac288f7bca36b2b5d6e0b5bfbba609.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/ecb707d78ed27493bcddc9ff1ba134ae.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/5c4f0a0cf5ef039f077ffa5f4333d432.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/787522e943dcfac360f91674f86317c6.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/b45e557778cf5fa76de86edb9a7bed32.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/c4dc4209b21511a46ab15ccebd5d6757.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/e7c4afc1c3ed8b4bf120862fa9cf2dbe.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/a49c05066098bf603d583f778c372a5a.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/3b10458503d85b2dd0d489317e7b1efe.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/616c571dcdbd07202ec57796e42543a6.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/c4c1ea77a6b444a430c442a123b44946.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/91c571b9a13caac9db907516054d472f.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/fb2a3dcf041748049965df6127256614.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/216dc4d4c9ea76caa6fb0ef7191f45f8.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/a11dfdb4db3c73ef67782b8feff997e6.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/1823c2a7c445b1caad86e81d3172a851.jpg"],"videos":["http://www.youtube.com/embed/Qu1Crj0P3kw"]},"publisher":{"id":"251211","name":"ALPHA IMÓVEL","address":{"country":"Brasil","zipCode":"06543-001","city":"Santana de Parnaíba","streetNumber":"4000","zone":"","street":"Avenida Marcos Penteado de Ulhôa Rodrigues","locationId":"","district":"","unitNumber":"","state":"SP","neighborhood":"Tamboré"},"phone":{"leadsPhone":"","mobile":"11991076161","alternative":"","primary":"1141950195"},"logoUrl":"https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/46c3a76e0d71a18194a319ab626b4cc5.jpg","licenseNumber":"18786-J-SP","websiteUrl":"http://www.alphaimovel.com.br/","leadEmails":[],"createdDate":"2018-03-28T10:42:55Z","showAddress":true},"url":{"id":"95060085","link":{"name":"Apartamento com 2 Quartos à venda, 85m²","href":"/imovel/apartamento-2-quartos-empresarial-18-do-forte-bairros-barueri-com-garagem-85m2-venda-RS665000-id-95060085/","rel":""}},"properAddress":null,"publisherUrl":{"link":{"name":"","href":"/251211/alpha-imovel/","rel":""}}},{"listing":{"amenities":["BARBECUE_GRILL","ELEVATOR","GOURMET_BALCONY","INTERCOM","POOL","CABLE_TV","SAUNA"],"feedsId":"AP0700","usableAreas":[85],"description":"- Apartamento disponível para venda, conforme a construtora entregou! Com 2 suítes, porem pode ser modificado. Sacada gourmet. Belíssimo condomínio, lindo e moderno. Área de lazer fantástica para adultos e crianças. Espaço gourmet na cobertura. Salão de festas e sala de jogos. -","listingType":"USED","title":"Edifício Present Alphaville","createdAt":"2018-03-26T03:50:48.960Z","publisherId":251211,"unitTypes":["APARTMENT"],"providerId":"23014","condominiumName":"","propertyType":"UNIT","contact":{"chat":"","phones":["1141950195","11991076161"],"emails":[]},"listingStatus":"ACTIVE","id":"93821081","parkingSpaces":[2],"updatedAt":"2019-05-20T23:28:17.187Z","owner":false,"address":{"country":"Brasil","state":"São Paulo","city":"Barueri","neighborhood":"Empresarial 18 do Forte","street":"Avenida Ômega","unitNumber":"","zipCode":"06472005","locationId":"BR>Sao Paulo>NULL>Barueri>Barrios>Empresarial 18 do Forte","zone":"Bairros","district":"","geoLocation":{"location":{"lat":-23.484829,"lon":-46.851078},"precision":"ROOFTOP","optionalPrecision":"precision"}},"suites":[2],"publicationType":"STANDARD","externalId":"AP0700","bathrooms":[3],"totalAreas":[85],"logoUrl":"","bedrooms":[2],"promotions":[],"highlights":"","pricingInfos":[{"yearlyIptu":"0","price":"700000","businessType":"SALE","monthlyCondoFee":"420"}],"showPrice":true,"displayAddress":"STREET","buildings":0,"images":["https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/35e4badb51ab3efbbe6d2107292937f8.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/78cee2c03e8fd97b3baceae7d46d3e87.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/2aa12b3e26e729255ef6f22389acae46.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/a601d7871cd1a5a6a8c24ca085dc40af.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/709ef5b5b69563c44cafcfd38a7e9932.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/8f1eebd0e5c6ae670a2b223fb97a60a3.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/fd39211ad10b488caf8eee22589e89cf.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/0b4f6b2d49e6ef1267dc0fd914b2a7f3.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/f0373e83b402f2a1f9c5f8023a12d846.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/4634e9e8859dc041fb10a5a9389c235c.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/38923d1028cc4b546ff7459544aada9b.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/8409b6886b8810c54c4d5b8da5a7db1e.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/c0dca0b0ee46cea7c9a797cecc513b30.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/c6e13afe254a715d16d878d0184a8644.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/9a3e418db06de52c8085e5c76b78a6c4.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/a7aa8e5fdd9d4a8fef1f305a2b4e4609.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/07b110beb53ee263efe4dbe0f8e4706c.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/25706de988099cc309e322edd6364571.jpg"],"videos":["http://www.youtube.com/embed/Qu1Crj0P3kw"]},"publisher":{"id":"251211","name":"ALPHA IMÓVEL","address":{"country":"Brasil","zipCode":"06543-001","city":"Santana de Parnaíba","streetNumber":"4000","zone":"","street":"Avenida Marcos Penteado de Ulhôa Rodrigues","locationId":"","district":"","unitNumber":"","state":"SP","neighborhood":"Tamboré"},"phone":{"leadsPhone":"","mobile":"11991076161","alternative":"","primary":"1141950195"},"logoUrl":"https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/46c3a76e0d71a18194a319ab626b4cc5.jpg","licenseNumber":"18786-J-SP","websiteUrl":"http://www.alphaimovel.com.br/","leadEmails":[],"createdDate":"2018-03-28T10:42:55Z","showAddress":true},"url":{"id":"93821081","link":{"name":"Apartamento com 2 Quartos à venda, 85m²","href":"/imovel/apartamento-2-quartos-empresarial-18-do-forte-bairros-barueri-com-garagem-85m2-venda-RS700000-id-93821081/","rel":""}},"properAddress":null,"publisherUrl":{"link":{"name":"","href":"/251211/alpha-imovel/","rel":""}}},{"listing":{"amenities":[],"feedsId":"","usableAreas":[85],"description":"Informações básicas<br>2 vaga(s) / 2 dorm(s) / 2 suíte(s) / 85,00 área útil <br>Cond/Ed.: Present Alphaville <br>Ponto de referência: escola internacional <br><br>Valores<br>$ Venda: 750.000,00 <br><br>Descrição<br>Belíssimo apartamento Present Alphaville, totalmente acabado, localização privilegiada , pronto para morar","listingType":"USED","title":"Apartamento Residencial Present Alphaville","createdAt":"2019-06-08T14:37:34.695Z","publisherId":330965,"unitTypes":["APARTMENT"],"providerId":"VIVAREAL","condominiumName":"PRESENT ALPHAVILLE","propertyType":"UNIT","contact":{"chat":"","phones":["11954211416","11954211416"],"emails":[]},"listingStatus":"ACTIVE","id":"2447512592","parkingSpaces":[2],"updatedAt":"2019-06-08T14:38:24.160Z","owner":false,"address":{"country":"Brasil","state":"São Paulo","city":"Barueri","neighborhood":"Melville Empresarial Ii","unitNumber":"","zipCode":"06472005","locationId":"BR>Sao Paulo>NULL>Barueri>Barrios>Melville Empresarial Ii","zone":"Bairros","district":"","geoLocation":{"location":{"lat":-23.484829,"lon":-46.851078},"precision":"ROOFTOP","optionalPrecision":"precision"}},"suites":[2],"publicationType":"PREMIUM","externalId":"RH0715","bathrooms":[3],"totalAreas":[85],"logoUrl":"","bedrooms":[2],"promotions":[],"highlights":"","pricingInfos":[{"period":"MONTHLY","yearlyIptu":"0","price":"749999","businessType":"SALE","monthlyCondoFee":"0"}],"showPrice":true,"displayAddress":"NEIGHBORHOOD","buildings":0,"images":["https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/c880eb2e4475dd9badc3ced2b9ff1c59.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/1a550e7c60033d9f82cc0f41919ca532.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/b6afc2645403afbff5ce7b208cfd78b7.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/7809cfa5b1d6f31bc8573419b6e3edf8.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/a43259a84b3ce26c0874c7a1b8796f9a.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/2d2f5a65679dd9a6a84b8e16b781e58e.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/2647aed5dac4b79f67b89243ce0f40a7.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/8dbee19e9e0fe4ce1dd3db373055f01c.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/1e6a99ba802a0f47eacbaee15f65f40a.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/9a7ed71554e45cf3eb7bb29907166e47.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/580443cfa1db32379b801b015e2789d6.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/acaf122653a57664500bfb2cf9f6bf5f.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/3ce3a9e660811db3ced85f04b476be3d.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/5bd2c8196e5c559076d1a6fcd063c157.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/6cf1edb99d4467cfc9913a2372ad98e0.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/2fe6b3b0387759db0fd0b7ddd1569e87.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/5d3d7becf0e9b80fdc82cc7a38968eeb.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/3ca6f7ee215821a4ebc408cf7cbd5d7d.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/dfc0462fa3447930d07eed6525b2e46a.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/5bce360e7a417bb4ea887a00929a60e6.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/7b67a87220684841620794cde388f65d.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/0e539866f13f74eae69633f603b3c8ee.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/03a75e4834f162980aec67b4fbbfc8a0.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/51f87794b6479ab0f3b16e34bd43a7b0.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/169be79bd2dd291963879a60ff2cdf9b.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/7c3fd087b3ed3b1f0c92c5c8a087dfd4.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/68741e895ead9227db4a556a4088a9b5.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/ea3d035a2c7a54ad27d0b0aa8d2c3b23.jpg"],"videos":[]},"publisher":{"id":"330965","name":"RICARDO HASEGAWA","address":{"country":"Brasil","zipCode":"06410-010","city":"Barueri","streetNumber":"575","zone":"","street":"Avenida Café do Ponto","locationId":"","district":"","unitNumber":"","state":"SP","neighborhood":"Jardim dos Camargos"},"phone":{"leadsPhone":"","mobile":"11954211416","alternative":"","primary":"11954211416"},"logoUrl":"","licenseNumber":"77968-F-SP","websiteUrl":"","leadEmails":[],"createdDate":"2018-04-05T14:11:29Z","showAddress":true},"url":{"id":"2447512592","link":{"name":"Apartamento com 2 Quartos à venda, 85m²","href":"/imovel/apartamento-2-quartos-melville-empresarial-ii-bairros-barueri-com-garagem-85m2-venda-RS749999-id-2447512592/","rel":""}},"properAddress":null,"publisherUrl":{"link":{"name":"","href":"/330965/ricardo-hasegawa/","rel":""}}},{"listing":{"amenities":["PLAYGROUND","GYM","ADULT_GAME_ROOM","GARDEN"],"feedsId":"65563","usableAreas":[112],"description":"Excelente oportunidade apartamento novo com 112 m², 3 suítes como foi entregue pela construtora. Condomínio com toda infraestrutura com lazer e segurança. Localização próxima à colégios, faculdades, restaurantes, academia e centro comercial","listingType":"USED","title":"BARUERI - Padrão - Alphaville","createdAt":"2019-05-17T12:47:07.929Z","publisherId":421100,"unitTypes":["APARTMENT"],"providerId":"41735","condominiumName":"","propertyType":"UNIT","contact":{"chat":"","phones":["1138296109","1138296109"],"emails":[]},"listingStatus":"ACTIVE","id":"2445099699","parkingSpaces":[2],"owner":false,"address":{"country":"Brasil","state":"São Paulo","city":"Barueri","neighborhood":"Alphaville","unitNumber":"","zipCode":"06472005","locationId":"BR>Sao Paulo>NULL>Barueri>Barrios>Alphaville","zone":"Bairros","district":"","geoLocation":{"location":{"lat":-23.484829,"lon":-46.851078},"precision":"ROOFTOP","optionalPrecision":"precision"}},"suites":[2],"publicationType":"STANDARD","externalId":"65563","bathrooms":[2],"totalAreas":[112],"logoUrl":"","bedrooms":[2],"promotions":[],"highlights":"","pricingInfos":[{"yearlyIptu":"400","price":"750000","businessType":"SALE","monthlyCondoFee":"780"}],"showPrice":true,"displayAddress":"NEIGHBORHOOD","buildings":0,"images":["https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/3fc3a3d2f568e64d3c721ddb03dac3f6.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/913a5fb5ddff19487bb9214a3ba86b8c.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/bdefb1b506cf96af0c67407472dcdfb1.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/2daefde7710227dea38c499d469152e1.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/484a1d1fd3907cb7ef52a8278ae8d992.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/fdb00f54685abac265f9352e47d8ae23.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/bcf7c367ac88c42e83368a795a4cbf2a.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/d0a5083868a6e81656d8be61db2a095a.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/0a84a7c5a645015e13803f3e63667053.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/fc232d81edf3f3ac3e92943548b46e78.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/7adc433ad6936c897f10541091decdc2.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/b6da1a1ef676c0097b3129c251149de5.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/196ac22b8d21ef9fb5ee30df3a0c0182.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/c920522cceca5be46ffe58ecdbb305d6.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/1a38697b090e30d12476f93cf96b24d8.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/a9201620790a2b666ecc67db66375770.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/c443196ac95c638d759b790c8e615ceb.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/dad6381e05212b33f350b273961568d6.jpg"],"videos":[]},"publisher":{"id":"421100","name":"Apoena","address":{"country":"Brasil","zipCode":"06454-020","city":"Barueri","streetNumber":"350","zone":"","street":"Avenida Cauaxi","locationId":"","district":"","unitNumber":"","state":"SP","neighborhood":"Alphaville Centro Industrial e Empresarial/Alphaville."},"phone":{"leadsPhone":"","mobile":"1138296109","alternative":"","primary":"1138296109"},"logoUrl":"https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/e6a95e6b651765412ac046655eb03a18.jpg","licenseNumber":"","websiteUrl":"http://apoenaimoveis.com.br/","leadEmails":[],"createdDate":"2018-10-26T16:37:28Z","showAddress":true},"url":{"id":"2445099699","link":{"name":"Apartamento com 2 Quartos à venda, 112m²","href":"/imovel/apartamento-2-quartos-alphaville-bairros-barueri-com-garagem-112m2-venda-RS750000-id-2445099699/","rel":""}},"properAddress":null,"publisherUrl":{"link":{"name":"","href":"/421100/apoena/","rel":""}}},{"listing":{"amenities":["GYM","BARBECUE_GRILL","GOURMET_SPACE","GARDEN","POOL","PLAYGROUND","PARTY_HALL","ADULT_GAME_ROOM","GATED_COMMUNITY","ELEVATOR"],"feedsId":"","usableAreas":[85],"description":"Present<br>Apartamentos de 85 m² e 112 m² | 2 e 3 suítes <br>Alphaville<br><br>Lazer completo:<br>Principais características<br>Churrasqueira<br>Espaço Gourmet<br>Espaço de descanço com sauna seca<br>Espaço convivência<br>Fitness<br>Lazer Infantil<br>Piscina Adulto<br>Piscina Infantil<br>Pet Place<br>Sauna<br>Salão de festas...<br><br>Sua vida acaba de ganhar um novo endereço, um lugar repleto de verde e muita tranquilidade.<br>Chegou a hora de você aproveitar o tempo de outra maneira!!!<br>Sua familia merece!<br><br>Preço sujeito a alteração.","listingType":"USED","title":"Apartamento novo em Alphaville 2 e 3 suítes/ Present Alphaville","createdAt":"2019-05-29T18:52:38.648Z","publisherId":541510,"unitTypes":["APARTMENT"],"providerId":"VIVAREAL","condominiumName":"PRESENT ALPHAVILLE","propertyType":"UNIT","contact":{"chat":"","phones":["11988858200","11988858200"],"emails":[]},"listingStatus":"ACTIVE","id":"2446439133","parkingSpaces":[2],"updatedAt":"2019-05-29T19:03:16.538Z","owner":false,"address":{"country":"Brasil","state":"São Paulo","city":"Barueri","neighborhood":"Melville Empresarial Ii","street":"Avenida Ômega","unitNumber":"","zipCode":"06472005","locationId":"BR>Sao Paulo>NULL>Barueri>Barrios>Melville Empresarial Ii","zone":"Bairros","district":"","geoLocation":{"location":{"lat":-23.484829,"lon":-46.851078},"precision":"ROOFTOP","optionalPrecision":"precision"}},"suites":[3],"publicationType":"STANDARD","externalId":"1QFGGQ6","bathrooms":[1],"totalAreas":[85],"logoUrl":"","deliveredAt":"2017-01-01T02:00:00Z","bedrooms":[3],"promotions":[],"highlights":"","pricingInfos":[{"period":"MONTHLY","yearlyIptu":"0","price":"750320","businessType":"SALE","monthlyCondoFee":"0"}],"showPrice":true,"displayAddress":"STREET","buildings":1,"images":["https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/a3f3f8920e25d07f85c8fc644063fbd1.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/e3738c96ee7da2acdedf147904a72421.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/b4df65b997d33b46205d398498b80dc8.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/2487a27fc9bd3ac7c544df8512e0355b.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/c3239bc359e3695ec69006334b215e1b.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/24a8bf02577e489403c0f0e9b5e76f86.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/2a4f3678c9b349c72ca3057e5fb00ea4.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/66ee67e2cca496b9553ff54314c65805.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/57035ccc1b425358d2f4c1560db41c2d.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/beacf33867b33b47e87ca0c85d0d5a5f.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/a3ca13843db4a6e4549ddbe06df0f0d7.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/25507e9f19bf3de4aaae051a2bf750f8.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/09f8620c6de72464381de1b13b920dea.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/eee3fa9e94ae98d1970e31b04fd1fb70.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/2a0b402aa7c1b6a6e5035bacf2a020b8.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/e05b0249e00948883ebaca7e1fba9d65.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/901764ba46bf51087cd57cc6addac851.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/5067f0ece126a61e491ce190a01d7f57.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/772c9bf7f2570263bb029cdae277ae9b.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/da86fa716eb955f1b2b292ac22dc6e28.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/a0dd057481e7f7b37adf38c928b1d73d.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/ed1b1eb3868fcd6885550842370df633.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/b318cfe50bcfd4b088bbd834f9d291cf.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/b1f357ce7cb611b4d8863cb151c63e5c.jpg"],"videos":[]},"publisher":{"id":"541510","name":"RIVKA SANTOS","phone":{"leadsPhone":"","mobile":"11988858200","alternative":"","primary":"11988858200"},"logoUrl":"","licenseNumber":"194961-F-SP","websiteUrl":"","leadEmails":[],"createdDate":"2019-05-20T13:36:03Z","showAddress":false},"url":{"id":"2446439133","link":{"name":"Apartamento com 3 Quartos à venda, 85m²","href":"/imovel/apartamento-3-quartos-melville-empresarial-ii-bairros-barueri-com-garagem-85m2-venda-RS750320-id-2446439133/","rel":""}},"properAddress":null,"publisherUrl":{"link":{"name":"","href":"/541510/rivka-santos/","rel":""}}},{"listing":{"amenities":["PLAYGROUND","ADULT_POOL","BALCONY","BARBECUE_GRILL","LAUNDRY","POOL"],"feedsId":"AP267242","usableAreas":[112],"description":"Para quem quer estudar ou trabalhar em São Paulo, não há opção melhor e mais vantajosa financeiramente e com relação ao transito. Sem falar na segurança e tranquilidade. 112 m² de área útil, planta de 3 dormitórios, porem foi alterado para uma sala estendida, lavado, 2 suítes, varanda gourmet, 2 garagens. Lazer na cobertura maravilhosa, tem piscina adulto e infantil, churrasqueira, espaço gourmet, espaço de descanso e sauna seca, lazer infantil, Pet Place e salão de festas. -","listingType":"USED","title":"apartamento - Empresarial 18 do Forte - Barueri","createdAt":"2019-05-01T05:20:41.902Z","publisherId":50702,"unitTypes":["APARTMENT"],"providerId":"19425","condominiumName":"","propertyType":"UNIT","contact":{"chat":"","phones":["1931121511","1931121511"],"emails":[]},"listingStatus":"ACTIVE","id":"2443122691","parkingSpaces":[2],"updatedAt":"2019-06-13T18:30:05.089Z","owner":false,"address":{"country":"Brasil","state":"São Paulo","city":"Barueri","neighborhood":"Empresarial 18 do Forte","street":"Avenida Ômega","streetNumber":"171","unitNumber":"","zipCode":"06472005","locationId":"BR>Sao Paulo>NULL>Barueri>Barrios>Empresarial 18 do Forte","zone":"Bairros","district":"","geoLocation":{"location":{"lat":-23.484829,"lon":-46.851078},"precision":"ROOFTOP","optionalPrecision":"precision"}},"suites":[2],"publicationType":"STANDARD","externalId":"AP267242","bathrooms":[3],"totalAreas":[],"logoUrl":"","bedrooms":[2],"promotions":[],"highlights":"","pricingInfos":[{"yearlyIptu":"240","price":"770000","businessType":"SALE","monthlyCondoFee":"780"}],"showPrice":true,"displayAddress":"ALL","buildings":0,"images":["https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/302c247860b8febf409daadd0200c3b3.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/54a650fb1dcfe83a979c136ae604bd96.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/469373aac1f355aaa7f613f85ef959cc.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/0a887c4cdea36f517cabdf23aa2c6bdc.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/cb72454c2cf586eab2498d438abc278f.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/0a95569527c44f96e479d117e7b1c3a0.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/f233b580de7b07812a1637f96e2adac0.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/ae3ca56a8a91e436a141dcb1dc7bf795.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/36c09194019f27c6b7ecfd9813ba956b.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/59efcbbabfffc58d050814ca834a1428.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/22f647ec824b57d31d9d14f442be3946.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/0a4ced26597c51b8b91ff11100322296.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/d48a497ffb94eb088c9e7eae4ad0df0c.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/7a9b3d6855d308ebfbe1c2fe2e901151.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/5774c80850de2c8323766c854a63465a.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/bc247d1177c5664d5ef11058dd210ad2.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/d45d62db82745a2c027e8192aa48326f.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/1038be4bc7cab6c3c3dcd031ea1ab9c2.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/27d1a036475263d2589d549383a7726b.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/2b1c3da1062cebe4f9c7d3bfc813ac9c.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/7040793747a26fe25a26e5c370c9b2fc.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/04e824dcc3dd0fcc76311cfb5db2a448.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/b9f57fb4a1c8310fbb8d5a537a30981f.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/5e6e1d17231c64f0328bfddd8243454f.jpg"],"videos":[]},"publisher":{"id":"50702","name":"PROVECTUM IMÓVEIS","address":{"country":"Brasil","zipCode":"13076-110","city":"Campinas","streetNumber":"347","zone":"","street":"Rua Ary Barroso","locationId":"","district":"","unitNumber":"","state":"SP","neighborhood":"Taquaral"},"phone":{"leadsPhone":"","mobile":"1931121511","alternative":"","primary":"1931121511"},"logoUrl":"https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/2aebbad9046df6952f61262cfc543759.jpg","licenseNumber":"10179-J-SP","websiteUrl":"http://www.provectumimoveis.com.br","leadEmails":[],"createdDate":"2018-03-27T15:44:00Z","showAddress":true},"url":{"id":"2443122691","link":{"name":"Apartamento com 2 Quartos à venda, 112m²","href":"/imovel/apartamento-2-quartos-empresarial-18-do-forte-bairros-barueri-com-garagem-112m2-venda-RS770000-id-2443122691/","rel":""}},"properAddress":null,"publisherUrl":{"link":{"name":"","href":"/50702/provectum-imoveis/","rel":""}}},{"listing":{"amenities":["BARBECUE_GRILL","POOL","PLAYGROUND","GYM","WATCHMAN","BALCONY","SAUNA"],"feedsId":"10488","usableAreas":[112],"description":"LINDO APARTAMENTO NOVO, CONFORME ENTREGUE PELA CONSTRUTORA! ANDAR ALTO COM LINDA VISTA, 112 M2, SALA AMPLIADA, 02 SUÍTES SENDO A PRINCIPAL COM VARANDA E CUBA DUPLA NO BANHEIRO, VARANDA GOURMET COM PASSAGEM DE PRATOS PARA COZINHA, LAVABO, COZINHA, LAVANDERIA, 02 VAGAS E LAZER COM PISCINA ADULTO E INFANTIL, ACADEMIA, CHURRASQUEIRA, SAUNA, ESPAÇO DE DESCANSO, PLAYGORUND E PET PLACE. DOCUMENTAÇÃO EM ORDEM!","listingType":"USED","title":"LINDO APARTAMENTO NOVO, ANDAR ALTO E LINDA VISTA!","createdAt":"2019-05-10T01:17:51.387Z","publisherId":57997,"unitTypes":["APARTMENT"],"providerId":"6645","condominiumName":"","propertyType":"UNIT","contact":{"chat":"","phones":["1141955600","11985059755"],"emails":[]},"listingStatus":"ACTIVE","id":"2444095382","parkingSpaces":[2],"owner":false,"address":{"country":"Brasil","state":"São Paulo","city":"Barueri","neighborhood":"Empresarial 18 do Forte","unitNumber":"","zipCode":"06472005","locationId":"BR>Sao Paulo>NULL>Barueri>Barrios>Empresarial 18 do Forte","zone":"Bairros","district":"","geoLocation":{"location":{"lat":-23.484829,"lon":-46.851078},"precision":"ROOFTOP","optionalPrecision":"precision"}},"suites":[2],"publicationType":"STANDARD","externalId":"10488","bathrooms":[3],"totalAreas":[112],"logoUrl":"","bedrooms":[2],"promotions":[],"highlights":"","pricingInfos":[{"yearlyIptu":"200","price":"770000","businessType":"SALE","monthlyCondoFee":"760"}],"showPrice":true,"displayAddress":"NEIGHBORHOOD","buildings":0,"images":["https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/2b0ca191818f2dd752d96c08b34de843.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/dca8662d7cfa4fa9c16d1927b2d2fb7d.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/474e0873b8f882e27f970c2b69f65499.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/90a9ce48fbb772eb20a797d5611f102e.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/541136886dd1acf72d44f97f9c79a4f0.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/befac7d502474ee211dec936c0b9fe6d.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/882ba87430c50a49c2f98e41b003a6b0.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/14cd5546c18be1ec5f1f5fa7d123fb53.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/e7b22b743f6dff4f7b81422ab9f90d0a.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/e63a4126f7f0fec8a989572ad66d990c.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/78727689199a5b8bbe2745ced46f80ed.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/44ebd1fd73e8b89e39aac8c6fc14dcaa.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/f2def680f7b4e2f375f3346e3418c166.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/e3eeb5be4ad7c4e0ee1fa147af2333a5.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/46aa8fed9a744ecabf1e9d6d2c1a3230.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/53b7d51c1150af3124f83125243fdb26.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/3d49da9daf06009c7fc25b4d8356f1b2.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/a41a71d6483401070a1c325a9dd96f28.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/434a7c17248fe0196412476ca0dcdc1a.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/da4ec1a5814021f3638f7ae7ada2ad5b.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/49aa7c91a54b2f8de863bfc12806b0a9.jpg"],"videos":[]},"publisher":{"id":"57997","name":"Alpha Master Imóveis","address":{"country":"Brasil","zipCode":"06453-062","city":"Barueri","streetNumber":"s/n","zone":"","street":"Calçada Flor de Lis, 14 - 2º andar - Centro Comercial Alphaville - Barueri/SP","locationId":"","district":"","unitNumber":"","state":"SP","neighborhood":""},"phone":{"leadsPhone":"","mobile":"11985059755","alternative":"","primary":"1141955600"},"logoUrl":"https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/d313459ac188a518a14eb3fbff532f82.jpg","licenseNumber":"99088-F-SP","websiteUrl":"http://www.alphamasterimoveis.com.br/","leadEmails":[],"createdDate":"2018-03-27T18:47:11Z","showAddress":true},"url":{"id":"2444095382","link":{"name":"Apartamento com 2 Quartos à venda, 112m²","href":"/imovel/apartamento-2-quartos-empresarial-18-do-forte-bairros-barueri-com-garagem-112m2-venda-RS770000-id-2444095382/","rel":""}},"properAddress":null,"publisherUrl":{"link":{"name":"","href":"/57997/alpha-master-imoveis/","rel":""}}},{"listing":{"amenities":["NEAR_ACCESS_ROADS","NEAR_SHOPPING_CENTER","NEAR_PUBLIC_TRANSPORT","NEAR_SCHOOL","NEAR_HOSPITAL","BARBECUE_GRILL","ELEVATOR","GARDEN","GOURMET_SPACE","GYM","PARTY_HALL","PLAYGROUND","POOL","SAUNA","ALARM_SYSTEM","GATED_COMMUNITY","INTERCOM","SECURITY_24_HOURS","SAFETY_CIRCUIT"],"feedsId":"","usableAreas":[112],"description":"Apartamento amplo em Alphaville, PRONTO PARA MORAR com 112m², varanda gourmet, 3 suítes e 2 vagas de garagem.<br><br>Condomínio com lazer completo localizado em uma das regiões mais privilegiadas de Alphaville, o 18 do Forte. Próximo a Hospitais, Colégios, restaurantes e centros empresariais. <br><br>Últimas Unidades Direto com a Construtora. <br>Agende uma visita e conheça!","listingType":"USED","title":"Apartamento em Alphaville","createdAt":"2018-05-15T21:47:25.848Z","publisherId":140041,"unitTypes":["APARTMENT"],"providerId":"VIVAREAL","condominiumName":"","propertyType":"UNIT","contact":{"chat":"","phones":["11972162424","11972162424"],"emails":[]},"listingStatus":"ACTIVE","id":"95308248","parkingSpaces":[2],"updatedAt":"2019-04-29T18:25:03.339Z","owner":false,"address":{"country":"Brasil","state":"São Paulo","city":"Barueri","neighborhood":"Empresarial 18 do Forte","street":"Avenida Ômega","streetNumber":"171","unitNumber":"","zipCode":"06472005","locationId":"BR>Sao Paulo>NULL>Barueri>Barrios>Empresarial 18 do Forte","zone":"Bairros","district":"","geoLocation":{"location":{"lat":-23.483886,"lon":-46.849025},"precision":"ROOFTOP","optionalPrecision":"precision"}},"suites":[3],"publicationType":"STANDARD","externalId":"PRES123112","bathrooms":[2],"totalAreas":[112],"logoUrl":"","bedrooms":[3],"promotions":[],"highlights":"","pricingInfos":[{"yearlyIptu":"0","price":"783700","businessType":"SALE","monthlyCondoFee":"0"}],"showPrice":true,"displayAddress":"ALL","images":["https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/b2b9ff58593bcd834b1e6fe0197a9aec.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/6e1e3bb02d93e9c4f61e2bfaf4744804.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/0977b3016692869a8d19138006588523.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/490d15fb3aed5fddc73de281583df36f.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/799c9f966d68d72e7e569a37688c4cf8.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/d141646a6b9049a599f5d4e1032e794f.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/19786503ee170d117448c54ca422dde9.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/1c087206fd12ce7e7b52b4a76ec99613.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/e27e17e9f83093c04369c93bbf619796.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/e8f8f235655570b9004a7befc8432d00.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/53f631c2e06724cb96aa49e3b38ba997.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/d922a2e31bcdf2bc1e0f15b3e82857b0.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/9e70700085532571b3ea5f50d758e88e.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/e4c058bcf86e053784eb95ea25c8d10f.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/50a402377b4fb39f274cd089ba7d2981.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/392a5f50fb1d98fa9136478702cf60d8.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/3765cc8024114d6e1a31309c4a151903.jpg"],"videos":[]},"publisher":{"id":"140041","name":"Adalberson Silva Lino","phone":{"leadsPhone":"","mobile":"11972162424","alternative":"","primary":"11972162424"},"logoUrl":"","licenseNumber":"","websiteUrl":"","leadEmails":[],"createdDate":"2018-03-27T19:02:06Z","showAddress":false},"url":{"id":"95308248","link":{"name":"Apartamento com 3 Quartos à venda, 112m²","href":"/imovel/apartamento-3-quartos-empresarial-18-do-forte-bairros-barueri-com-garagem-112m2-venda-RS783700-id-95308248/","rel":""}},"properAddress":null,"publisherUrl":{"link":{"name":"","href":"/140041/adalberson-silva-lino/","rel":""}}},{"listing":{"amenities":["AIR_CONDITIONING","BARBECUE_GRILL","KITCHEN","ELEVATOR","GOURMET_BALCONY","INTERCOM","POOL","BALCONY","ALARM_SYSTEM","CABLE_TV","HOME_OFFICE","SAUNA","SERVICE_AREA"],"feedsId":"AP0486","usableAreas":[112],"description":"Amplo Apartamento com 3 Suítes, 112 m² de Área Útil, sendo 1 Master com Varanda lavado, Sala de Estar, Sala de Jantar, Varanda com Churrasqueira, Cozinha, Área de Serviço, 2 Vagas de Garagem !!<br>Total Infraestrutura de Lazer e segurança com :<br>Churrasqueira, Espaço Gourmet, Fitness, Lazer Infantil, Piscina Adulto, Piscina Infantil, Sauna, Pet Place, Salão de festas, Espaço convivência, Espaço de descanço com sauna seca, Home Office<br>Maravilhosa Vista na Cobertura com Espaço Convivência !!<br>Agende sua Visita -","listingType":"USED","title":"Alpahville 18 do Forte - 3 Suítes Alto Padrão - Total Infraestrutura de Lazer e Segurança !!","createdAt":"2018-05-30T17:35:51.416Z","publisherId":225320,"unitTypes":["APARTMENT"],"providerId":"7739","condominiumName":"","propertyType":"UNIT","contact":{"chat":"","phones":["1141182388","11968982828"],"emails":[]},"listingStatus":"ACTIVE","id":"1037386888","parkingSpaces":[2],"updatedAt":"2019-05-22T23:30:39.216Z","owner":false,"address":{"country":"Brasil","state":"São Paulo","city":"Barueri","neighborhood":"Empresarial 18 do Forte","street":"Avenida Ômega","streetNumber":"171","unitNumber":"","zipCode":"06472005","locationId":"BR>Sao Paulo>NULL>Barueri>Barrios>Empresarial 18 do Forte","zone":"Bairros","district":"","geoLocation":{"location":{"lat":-23.484829,"lon":-46.851078},"precision":"ROOFTOP","optionalPrecision":"precision"}},"suites":[3],"publicationType":"STANDARD","externalId":"AP0486","bathrooms":[3],"totalAreas":[],"logoUrl":"","bedrooms":[3],"promotions":[],"highlights":"","pricingInfos":[{"yearlyIptu":"200","price":"790000","businessType":"SALE","monthlyCondoFee":"880"}],"showPrice":true,"displayAddress":"ALL","buildings":0,"images":["https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/29fb765f804d2323b475ebe5424d7774.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/83dd60d9d1313d8c429b130780b1e2b1.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/d6c5abca0f87129deabee83d7470bd89.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/1e3101b9297a5cb1a412693146101ac6.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/739b2b09f5c19bf3f746f8139e45d12e.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/4160185d3a1b855bb37188317916a9b8.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/60919b46c1d8602ec71a6ac86ada7689.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/ad0fbe8082feafdae7b96c0680384459.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/9b952f309d469e0ecb59bc82d602cf8e.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/b874f1e95a5e82d613ee55f9e9d6fab9.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/da93e005e2ff0ac97faa3b2dbe2acd72.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/126c93589f62b0825f57a4b7350320c4.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/3a8915e55d8ed469c4364aa668bfc63b.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/80ddeb874eb0b96078104d7d5160970c.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/a08a18bba77b6a79c7f836e7efb7eca4.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/59f04ba1d0942f98f7a5c846fd3f35a5.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/06062ef5f695cf64db9afd5ac79ae1bc.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/07bbf5c8e97d5221757e8300156f6084.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/2fe84fa03de6df36eeddf253bf5218c8.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/201a624b346be23a75d5633a231a9699.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/a0d830d60f3b36c991f59ec062a0cca7.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/4dd1bed7d4d84341cfe54f5d09e23560.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/3282c21f7dbb4fa894b51a62fff80866.jpg"],"videos":[]},"publisher":{"id":"225320","name":"OTTO DESENVOLVIMENTO IMOBILIARIO LTDA","address":{"country":"Brasil","zipCode":"02036-011","city":"SAO PAULO","streetNumber":"577","zone":"","street":"R. Dr. Gabriel Piza, 577","locationId":"","district":"","unitNumber":"","state":"SP","neighborhood":"Santana"},"phone":{"leadsPhone":"","mobile":"11968982828","alternative":"","primary":"1141182388"},"logoUrl":"https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/60e663554b143c607112ba8eebc031a8.jpg","licenseNumber":"79955-J-SP","websiteUrl":"http://www.ottoimob.com.br","leadEmails":[],"createdDate":"2018-03-28T09:45:45Z","showAddress":true},"url":{"id":"1037386888","link":{"name":"Apartamento com 3 Quartos à venda, 112m²","href":"/imovel/apartamento-3-quartos-empresarial-18-do-forte-bairros-barueri-com-garagem-112m2-venda-RS790000-id-1037386888/","rel":""}},"properAddress":null,"publisherUrl":{"link":{"name":"","href":"/225320/otto-desenvolvimento-imobiliario-ltda/","rel":""}}},{"listing":{"amenities":[],"feedsId":"","usableAreas":[112],"description":"Informações básicas<br>2 dorm(s) / 2 suíte(s) / 112,00 área útil<br>Cond/Ed.: Cond. Present Alphaville<br><br>Valores<br>$ Venda: 800.000,00<br><br>Descrição<br>Ótima oportunidade, proprietário aceita permuta em apartamento em Campinas, entre em contato para receber maiores informações","listingType":"USED","title":"Apartamento Residencial / Edifício Present","createdAt":"2018-11-06T12:00:26.502Z","publisherId":330965,"unitTypes":["APARTMENT"],"providerId":"VIVAREAL","condominiumName":"","propertyType":"UNIT","contact":{"chat":"","phones":["11954211416","11954211416"],"emails":[]},"listingStatus":"ACTIVE","id":"1177095478","parkingSpaces":[2],"updatedAt":"2019-03-13T21:25:14.139Z","owner":false,"address":{"country":"Brasil","state":"São Paulo","city":"Barueri","neighborhood":"Alphaville","unitNumber":"","zipCode":"06472005","locationId":"BR>Sao Paulo>NULL>Barueri>Barrios>Alphaville","zone":"Bairros","district":"","geoLocation":{"location":{"lat":-23.48458,"lon":-46.850891},"precision":"ROOFTOP","optionalPrecision":"precision"}},"suites":[2],"publicationType":"STANDARD","externalId":"RH0482 - AP0148","bathrooms":[4],"totalAreas":[112],"logoUrl":"","bedrooms":[2],"promotions":[],"highlights":"","pricingInfos":[{"yearlyIptu":"0","price":"799999","businessType":"SALE","monthlyCondoFee":"0"}],"showPrice":true,"displayAddress":"NEIGHBORHOOD","images":["https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/ce248efe03b3e3aa2a1a58d5552b227a.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/3f041607c417866cc0445145dc8282cb.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/ff6169389878bbff08f86f68505e86b5.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/c7c4da1c090230afd220a8a2c0a5330e.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/d4c62c604dbd017cad8d1bb4864086d9.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/3f8cda1c955c2a1943d86a0584f567ba.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/5f05768d3565c737d3fa01e4a8a46f74.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/fb845a2ad081b7c215ed8b22f8be33e5.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/b74a0117b15065994032ec8d0b4b73c5.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/86b7a2dbac3888079dd30454d68754a0.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/09af064ad63dc90d53ea2ac4f39285e2.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/1819633aad87d1503ec6fc72c10d05ae.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/0fad77ed59b946d3564613e506b3a837.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/6a2ca98cbe548cdd2519c28223a68644.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/62bcf51da1b470c7c564ba72cc2c6c3a.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/950852cbba94bf0b467501eb2b543a6f.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/dbe0a4569251d7d44167831b61772ae3.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/db3fee44699810b76b2a8bafee73222b.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/b56dbc60fd03f816ad84b0ab423c9e05.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/f315448ab1f0488a061a63494f097367.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/686d269cbd537b01ec9c7a9ca8702aa4.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/70a8db21f60a25abf58bbcf64a72a78f.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/4711a18f8287731dd66034470b80e79c.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/a159deb2d668b2bac0e13542bc55f780.jpg"],"videos":[]},"publisher":{"id":"330965","name":"RICARDO HASEGAWA","address":{"country":"Brasil","zipCode":"06410-010","city":"Barueri","streetNumber":"575","zone":"","street":"Avenida Café do Ponto","locationId":"","district":"","unitNumber":"","state":"SP","neighborhood":"Jardim dos Camargos"},"phone":{"leadsPhone":"","mobile":"11954211416","alternative":"","primary":"11954211416"},"logoUrl":"","licenseNumber":"77968-F-SP","websiteUrl":"","leadEmails":[],"createdDate":"2018-04-05T14:11:29Z","showAddress":true},"url":{"id":"1177095478","link":{"name":"Apartamento com 2 Quartos à venda, 112m²","href":"/imovel/apartamento-2-quartos-alphaville-bairros-barueri-com-garagem-112m2-venda-RS799999-id-1177095478/","rel":""}},"properAddress":null,"publisherUrl":{"link":{"name":"","href":"/330965/ricardo-hasegawa/","rel":""}}},{"listing":{"amenities":["ELEVATOR"],"feedsId":"AP0769","usableAreas":[112],"description":"Apartamento em um lindo, novo e moderno condomínio!<br>Entregue recentemente pela construtora, o apartamento está a venda estado original da construtora. Ótima oportunidade! -","listingType":"USED","title":"Edifício Present Alphaville","createdAt":"2018-04-18T04:52:07.275Z","publisherId":251211,"unitTypes":["APARTMENT"],"providerId":"23014","condominiumName":"","propertyType":"UNIT","contact":{"chat":"","phones":["1141950195","11991076161"],"emails":[]},"listingStatus":"ACTIVE","id":"94583186","parkingSpaces":[2],"updatedAt":"2019-05-30T00:30:00.349Z","owner":false,"address":{"country":"Brasil","state":"São Paulo","city":"Barueri","neighborhood":"Empresarial 18 do Forte","street":"Avenida Ômega","unitNumber":"","zipCode":"06472005","locationId":"BR>Sao Paulo>NULL>Barueri>Barrios>Empresarial 18 do Forte","zone":"Bairros","district":"","geoLocation":{"location":{"lat":-23.484829,"lon":-46.851078},"precision":"ROOFTOP","optionalPrecision":"precision"}},"suites":[2],"publicationType":"STANDARD","externalId":"AP0769","bathrooms":[3],"totalAreas":[112],"logoUrl":"","bedrooms":[2],"promotions":[],"highlights":"","pricingInfos":[{"yearlyIptu":"0","price":"800000","businessType":"SALE","monthlyCondoFee":"504"}],"showPrice":true,"displayAddress":"STREET","buildings":0,"images":["https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/b3cdaa9cd56457a1c69cef778fc874d6.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/c8623facb4e6052d66093e749adb89a8.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/94998922b816a241d466700d7a21969b.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/44abacb5eb017cf54a055fc65f373eb2.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/d1513bf6e5a231df59331de9d0fd9989.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/c4fa42cc231559e58a9abd098948ff41.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/4eb7f6e191e043f4eb1aec7218b491a0.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/6a680f8ffaaf671b77473119f4c88f59.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/844d03450cc8fa3dcb4ddaf3cff5595f.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/5159e33c95403f41879391c412bdb370.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/f46c1e4af7e5c1da20bff0c6b3d6dd96.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/f3d045f436d8f23f8c730b28dcd300c4.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/bb713d4363fc3192e3d73395f1417886.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/7f4c3c0256956a106826de31a45f29a5.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/0f763f7ad69f0f26aee83f886982ed41.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/2db86e0a0afeb54d45092ea8e9244f31.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/3e27ed7e97bc1f9deeaf41891cba7a17.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/37d228e75d5889a1a0aab7539762f279.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/568d8e5a7854bf545e0fe8e9593ab016.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/0782f0221ed2761e984b0a06f1c92f77.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/080dffcaf018cf5525bd3366ab4b7c14.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/d6908ff383acff998b2634bd3446e53c.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/8f0df95fbd65837c2d35f3f0fd9b172c.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/9f9aa5abf141f983d9b81100656d6449.jpg"],"videos":["http://www.youtube.com/embed/Qu1Crj0P3kw"]},"publisher":{"id":"251211","name":"ALPHA IMÓVEL","address":{"country":"Brasil","zipCode":"06543-001","city":"Santana de Parnaíba","streetNumber":"4000","zone":"","street":"Avenida Marcos Penteado de Ulhôa Rodrigues","locationId":"","district":"","unitNumber":"","state":"SP","neighborhood":"Tamboré"},"phone":{"leadsPhone":"","mobile":"11991076161","alternative":"","primary":"1141950195"},"logoUrl":"https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/46c3a76e0d71a18194a319ab626b4cc5.jpg","licenseNumber":"18786-J-SP","websiteUrl":"http://www.alphaimovel.com.br/","leadEmails":[],"createdDate":"2018-03-28T10:42:55Z","showAddress":true},"url":{"id":"94583186","link":{"name":"Apartamento com 2 Quartos à venda, 112m²","href":"/imovel/apartamento-2-quartos-empresarial-18-do-forte-bairros-barueri-com-garagem-112m2-venda-RS800000-id-94583186/","rel":""}},"properAddress":null,"publisherUrl":{"link":{"name":"","href":"/251211/alpha-imovel/","rel":""}}},{"listing":{"amenities":["ELECTRIC_GENERATOR","SAFETY_CIRCUIT","RECEPTION","GATED_COMMUNITY","GYM","BARBECUE_GRILL","GOURMET_SPACE","GARDEN","POOL","PLAYGROUND","SQUASH","TENNIS_COURT","SPORTS_COURT","PARTY_HALL","ADULT_GAME_ROOM","ELEVATOR","LAUNDRY","SAUNA","SPA","AIR_CONDITIONING","GOURMET_BALCONY"],"feedsId":"","usableAreas":[112],"description":"O apartamento no bairro Melville Empresarial I e II tem 112 metros quadrados com 3 quartos sendo 3 suites e 4 banheiros. Fica próximo a restaurantes, hospitais, farmácias, estacionamentos, universidades, shoppings, padarias, hospitais, transporte coletivo, escolas.<br>Possui academia, espaço gourmet, jardim, área de recreação infantil, salão para festas e eventos.<br>Vai lhe possibilitar curtir os dias mais quentes na piscina, praticar diversos esportes na quadra poliesportiva, todo o conforto do ar condicionado nos dias mais quentes.Encontra-se na privacidade de um condomínio fechado.<br>Churrasqueira para você aproveitar nos momentos de descontração.<br>Elevador para mais praticidade no dia-a-dia.<br><br>Este valor refere se a unidade 11, pronto para morar","listingType":"USED","title":"Apartamento para venda tem 112 metros com 3 quartos em Melville Empresarial I e II - Barueri - SP","createdAt":"2019-05-11T16:14:31.355Z","publisherId":536971,"unitTypes":["APARTMENT"],"providerId":"VIVAREAL","condominiumName":"PRESENT ALPHAVILLE","propertyType":"UNIT","contact":{"chat":"","phones":["11992803316","11992930597"],"emails":[]},"listingStatus":"ACTIVE","id":"2444437381","parkingSpaces":[2],"updatedAt":"2019-05-20T20:43:17.269Z","owner":false,"address":{"country":"Brasil","state":"São Paulo","city":"Barueri","neighborhood":"Melville Empresarial Ii","street":"Avenida Ômega","streetNumber":"171","unitNumber":"","zipCode":"06472005","locationId":"BR>Sao Paulo>NULL>Barueri>Barrios>Melville Empresarial Ii","zone":"Bairros","district":"","geoLocation":{"location":{"lat":-23.484829,"lon":-46.851078},"precision":"ROOFTOP","optionalPrecision":"precision"}},"suites":[3],"publicationType":"PREMIUM","externalId":"present112","bathrooms":[4],"totalAreas":[112],"logoUrl":"","bedrooms":[3],"promotions":[],"highlights":"","pricingInfos":[{"period":"MONTHLY","yearlyIptu":"0","price":"800000","businessType":"SALE","monthlyCondoFee":"587"}],"showPrice":true,"displayAddress":"ALL","buildings":1,"images":["https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/00e724f1da9c0666193b7b6dd4a57b97.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/91370d42bb840e6bf7f2f73b25a6f8dd.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/df581a158b45da203c271dda61f42c4b.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/7093567e5b359d38d1af87d42293eb2f.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/451d8357063dd8c7447c11832fab4167.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/862b9980b2b7b0b2b3e5edbf2337cd91.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/ca874df78e4641ca1f547c912768aa11.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/d75366816862254cb170b887d1c71015.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/e8c3364d33e13072380e8848ea1c756e.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/b04f2cb495a184932ecef5d8cceb040d.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/6c7704bb936f9055d0f94c2fb9568241.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/6ed0cd598e17a2b05c8da5fd708d8ec0.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/6f17b255ce0891874e9e4ac176f821cc.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/066872eef90313ffbe36ad52d95f7ed4.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/8c8eceff18d87a98b9986f416f5711b9.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/57fb1ddf01612b61453a6381971a0732.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/5d4d5fde50bfde9d13da6769a0703eda.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/fabefdbd3c118db6e7b71b339161551c.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/d75d03fa24a073dd512fa9466619af2a.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/c1ede1f6917064440ae2c0b3b58356fd.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/ad08efffaad20f597a6fea99ad2478d0.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/b136cdf85b0787d5d6e8d6771eb34978.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/121e4860e166559d98e4d532d54def7e.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/32d81563be3e58d1fd1a1d999fd0fe2f.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/14aae4ca6abdca70189ff3801b3a7cb8.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/7ea145fb3f348ddda879f4ed442f8c2e.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/eb867b72d5dc9a43dc81ebd854dc055b.jpg"],"videos":["https://www.youtube.com/watch?v=xndW58OAy-0&t=3s"]},"publisher":{"id":"536971","name":"Joao Lucas Minuncio  - Corretor","phone":{"leadsPhone":"","mobile":"11992930597","alternative":"","primary":"11992803316"},"logoUrl":"","licenseNumber":"177047-F-SP","websiteUrl":"","leadEmails":[],"createdDate":"2019-04-26T18:38:21Z","showAddress":false},"url":{"id":"2444437381","link":{"name":"Apartamento com 3 Quartos à venda, 112m²","href":"/imovel/apartamento-3-quartos-melville-empresarial-ii-bairros-barueri-com-garagem-112m2-venda-RS800000-id-2444437381/","rel":""}},"properAddress":null,"publisherUrl":{"link":{"name":"","href":"/536971/joao-lucas-minuncio-corretor/","rel":""}}},{"listing":{"amenities":["AIR_CONDITIONING","BARBECUE_GRILL","KITCHEN","GOURMET_BALCONY","INTERCOM","POOL","BALCONY","CABLE_TV","SERVICE_AREA"],"feedsId":"AP0568","usableAreas":[112],"description":"Lindo apartamento com 112m², sendo três suítes, rico em armários, varanda gourmet e vaga para 2 carros<br><br>Verificar disponibilidade<br><br>Corretor Sergio Queiroz<br>CRECI 137094-F -","listingType":"USED","title":"Present Alphaville - Apartamento novo!!","createdAt":"2018-09-16T00:58:43.451Z","publisherId":94173,"unitTypes":["APARTMENT"],"providerId":"17623","condominiumName":"","propertyType":"UNIT","contact":{"chat":"","phones":["11995987835","11999459264"],"emails":[]},"listingStatus":"ACTIVE","id":"1041221596","parkingSpaces":[2],"updatedAt":"2019-05-21T02:41:54.502Z","owner":false,"address":{"country":"Brasil","state":"São Paulo","city":"Barueri","neighborhood":"Melville Empresarial Ii","street":"Avenida Ômega","streetNumber":"171","unitNumber":"","zipCode":"06472005","locationId":"BR>Sao Paulo>NULL>Barueri>Barrios>Melville Empresarial Ii","zone":"Bairros","district":"","geoLocation":{"location":{"lat":-23.484829,"lon":-46.851078},"precision":"ROOFTOP","optionalPrecision":"precision"}},"suites":[3],"publicationType":"STANDARD","externalId":"AP0568","bathrooms":[3],"totalAreas":[112],"logoUrl":"","bedrooms":[3],"promotions":[],"highlights":"","pricingInfos":[{"yearlyIptu":"40","price":"849900","businessType":"SALE","monthlyCondoFee":"600"}],"showPrice":true,"displayAddress":"ALL","buildings":0,"images":["https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/d40ca8c7665f61b691679af9561a0a24.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/13660e96cbec33ef882bd2aaf48d7289.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/014044c8399140202f64545c0e6e5593.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/ecf4f9e2827c8c7a0c83526ca0b9af45.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/f65fd61dee4cdf79a8d53a4d18d08d6d.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/e277fec945a8f40fcdb320ec518a0a2f.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/0f31582c407e099e4afaa8713b945e32.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/fe60fab965938585f2ac39930612dd92.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/99918b5991d30a0602618b3b2de4cd60.jpg"],"videos":[]},"publisher":{"id":"94173","name":"Ricardo Borelli Ferreira","phone":{"leadsPhone":"","mobile":"11999459264","alternative":"","primary":"11995987835"},"logoUrl":"https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/d54efc4ffc43ec22bdcf26b063f4e2bb.jpg","licenseNumber":"153165-F-SP","websiteUrl":"","leadEmails":[],"createdDate":"2018-03-28T09:14:48Z","showAddress":false},"url":{"id":"1041221596","link":{"name":"Apartamento com 3 Quartos à venda, 112m²","href":"/imovel/apartamento-3-quartos-melville-empresarial-ii-bairros-barueri-com-garagem-112m2-venda-RS849900-id-1041221596/","rel":""}},"properAddress":null,"publisherUrl":{"link":{"name":"","href":"/94173/ricardo-borelli-ferreira/","rel":""}}},{"listing":{"amenities":["GYM","GOURMET_SPACE","BARBECUE_GRILL","ELEVATOR","PLAYGROUND","PARTY_HALL","POOL","TEEN_SPACE","GREEN_SPACE","CHILDRENS_POOL","ADULT_POOL","ADULT_GAME_ROOM","YOUTH_GAME_ROOM","RECEPTION","SAUNA","ELECTRIC_GENERATOR","NEAR_SCHOOL","GATED_COMMUNITY","SECURITY_24_HOURS","INTERCOM","WATCHMAN","SAFETY_CIRCUIT"],"feedsId":"","usableAreas":[85],"description":"Apartamento de 85m² com móveis planejados e completamente mobiliado com 2 dormitórios com piso de madeira, sendo 1 suíte com closet e uma varanda privativa com um jardim de inverno, lavabo, piso de porcelanato, pia com triturador, torneira com filtro de água junto, varanda gourmet integrada, ar condicionado, sistema de automação de iluminação em todos os ambientes, em andar alto com vista para o lago.<br>E duas vagas na garagem.","listingType":"USED","title":"Apartamento de 85m² completamente Mobiliado!","createdAt":"2019-02-24T22:19:52.890Z","publisherId":239874,"unitTypes":["APARTMENT"],"providerId":"VIVAREAL","condominiumName":"","propertyType":"UNIT","contact":{"chat":"","phones":["11955710022","11955710022"],"emails":[]},"listingStatus":"ACTIVE","id":"2434049882","parkingSpaces":[0],"updatedAt":"2019-05-16T17:38:01.520Z","owner":false,"address":{"country":"Brasil","state":"São Paulo","city":"Barueri","neighborhood":"Empresarial 18 do Forte","street":"Avenida Ômega","unitNumber":"","zipCode":"06472005","locationId":"BR>Sao Paulo>NULL>Barueri>Barrios>Empresarial 18 do Forte","zone":"Bairros","district":"","geoLocation":{"location":{"lat":-23.484829,"lon":-46.851078},"precision":"ROOFTOP","optionalPrecision":"precision"}},"suites":[1],"publicationType":"PREMIUM","externalId":"AP01RC","bathrooms":[3],"totalAreas":[],"logoUrl":"","bedrooms":[2],"promotions":[],"highlights":"","pricingInfos":[{"period":"MONTHLY","yearlyIptu":"0","price":"850000","businessType":"SALE","monthlyCondoFee":"550"}],"showPrice":true,"displayAddress":"STREET","buildings":0,"images":["https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/129d2fde3173672a96ccb371357c66d2.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/870bd0a0669da36d6cb172fdadf4716b.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/f05770ac83091357a041bb611e79a12e.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/b19abdbac25bde343a8ef91c85d1bbe8.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/5de7fec84c522d62a950c095d9794cec.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/8d28dd264da16c072926fa5c310ea1f6.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/75cc3d546e0dbc75c42ab2a0656e6a74.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/92274bcc0d89ca49db9917242e4204e9.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/4f0ab60b3b041ff16bad03a6d19d6653.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/c601f118d39d5e3f16ff196959d4f779.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/a23f7ad8854a83eb927051b432b39c1d.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/89db2275923909c071c311d18f893f8d.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/2c1cacb04a186e8056d9a0d27caf50f0.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/1009f6ddd38d81c66791418b772661af.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/bc127579528cff594030a0a2d5440200.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/cf8519cb5c16d45beb4e831b8a6f81e3.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/7b947ff7623fa32be5c09c65fef0c448.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/f68811613c7a076db7e9d9bc07c30524.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/07f341a226bbb6d49710eea31b5a27d5.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/35e505b790246dc77cb51aca5652a7fb.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/8958296770f41f30053470c7fb2d100b.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/67326725dc9968eb5a07d76a1439ec32.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/528491e28a657ac90f17f6b0484bd361.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/81e39cfcb7767a99d889df5a6b572728.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/7b5f38bf7082eeb3bfecacd153cd2ded.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/c2e32481d62442715d6c75da72a9da09.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/5927d0826fe53da37dc71b64de45c84a.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/0fbd293aa8223b813156b60d6376276c.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/2f96581f339c9cc867dc2c9acc6af613.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/9c43b7fa0ea80889555cdea3affd7d33.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/3c8888c0b122b606ba3a1ca067845780.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/85455bd09b3242e93c9675e60cad719f.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/9fdb7379de6fabd297dde9790e7c24aa.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/4578eed52e903e382b1834f226f37110.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/8accf78235fa4e47fd7165df81cc7c4c.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/048586c92230446723ada00f158a3199.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/523afe5bae3782248414b249dffbd2c6.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/e1639df8dba6c91f0ca0afadbbd04204.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/9defb2bee33c86fd630518f2a9fd0d9d.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/a25c4fefa401ce9e5d8b6a6938744581.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/a1bafdae40380924cffdc2a1817b72de.jpg"],"videos":[]},"publisher":{"id":"239874","name":"Mattioli","address":{"country":"Brasil","zipCode":"06660-120","city":"Itapevi","streetNumber":"90","zone":"","street":"Rua Olímpia Marques de Oliveira","locationId":"","district":"","unitNumber":"","state":"SP","neighborhood":"Jardim Santa Rita"},"phone":{"leadsPhone":"","mobile":"11955710022","alternative":"","primary":"11955710022"},"logoUrl":"","licenseNumber":"75472-F-SP","websiteUrl":"","leadEmails":[],"createdDate":"2018-03-28T10:27:41Z","showAddress":true},"url":{"id":"2434049882","link":{"name":"Apartamento com 2 Quartos à venda, 85m²","href":"/imovel/apartamento-2-quartos-empresarial-18-do-forte-bairros-barueri-85m2-venda-RS850000-id-2434049882/","rel":""}},"properAddress":null,"publisherUrl":{"link":{"name":"","href":"/239874/mattioli/","rel":""}}},{"listing":{"amenities":["POOL","SPORTS_COURT","BARBECUE_GRILL","GARDEN","SECURITY_24_HOURS","NEAR_ACCESS_ROADS","GYM","ALARM_SYSTEM","GATED_COMMUNITY","ELEVATOR","INTERCOM","PARTY_HALL"],"feedsId":"","usableAreas":[112],"description":"Excelente apto, conforme a construtora entregou, boa localização, lazer, sala ampliada! Estuda- se proposta!condominio com llazer completo,segurança e muita qualidade de vida.<br>Agende ja uma visita","listingType":"USED","title":"Apartamento a venda em Alphaville Barueri com 3 quartos","createdAt":"2017-09-11T19:51:38.400Z","publisherId":69008,"unitTypes":["APARTMENT"],"providerId":"VIVAREAL","condominiumName":"","propertyType":"UNIT","contact":{"chat":"","phones":["11998873257","11940164251"],"emails":[]},"listingStatus":"ACTIVE","id":"85770957","parkingSpaces":[2],"updatedAt":"2019-03-19T09:35:11.402Z","owner":false,"address":{"country":"Brasil","state":"São Paulo","city":"Barueri","neighborhood":"Alphaville","street":"Avenida Ômega","streetNumber":"171","unitNumber":"","zipCode":"06472005","locationId":"BR>Sao Paulo>NULL>Barueri>Barrios>Alphaville","zone":"Bairros","district":"","geoLocation":{"location":{"lat":-23.483886,"lon":-46.849025},"precision":"ROOFTOP","optionalPrecision":"precision"}},"suites":[2],"publicationType":"STANDARD","externalId":"106455","bathrooms":[3],"totalAreas":[112],"logoUrl":"","bedrooms":[2],"promotions":[],"highlights":"","pricingInfos":[{"yearlyIptu":"300","price":"850000","businessType":"SALE","monthlyCondoFee":"800"}],"showPrice":true,"displayAddress":"ALL","images":["https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/664dd13336efa138561df1aa887177a8.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/afdd6d2c76b46e0ea95bf722c0aecf67.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/5281430f8920417206c33da3e0eca117.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/77205277bb20dc5a891c8777905ea6c0.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/99bb55a3b5505c5086bd16853bf91933.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/5b5a8a3e79d99c0e694ba010af588959.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/5032e4be00fd0e15d8460660f374001a.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/d181526afc2845932dd0283f23443c17.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/cd630db06eb3c9e10a7d94c1bc84d867.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/f2a421181cb2a71be6bfe2558b43e296.jpg"],"videos":[]},"publisher":{"id":"69008","name":"Flavio Barone Corretor de Imóveis","address":{"country":"Brasil","zipCode":"06454-010","city":"Barueri","streetNumber":"503","zone":"","street":"Alameda Rio Negro, 503. Conj. 2218","locationId":"","district":"","unitNumber":"","state":"SP","neighborhood":""},"phone":{"leadsPhone":"","mobile":"11940164251","alternative":"","primary":"11998873257"},"logoUrl":"https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/6b8e118d903e8fd5a5ca50537d6f91a9.jpg","licenseNumber":"72973-F-SP","websiteUrl":"","leadEmails":[],"createdDate":"2018-03-27T19:11:09Z","showAddress":true},"url":{"id":"85770957","link":{"name":"Apartamento com 2 Quartos à venda, 112m²","href":"/imovel/apartamento-2-quartos-alphaville-bairros-barueri-com-garagem-112m2-venda-RS850000-id-85770957/","rel":""}},"properAddress":null,"publisherUrl":{"link":{"name":"","href":"/69008/flavio-barone-corretor-de-imoveis/","rel":""}}},{"listing":{"amenities":["BARBECUE_GRILL","PLAYGROUND","GYM","ADULT_GAME_ROOM","GARDEN","SERVICE_AREA"],"feedsId":"67317","usableAreas":[112],"description":"Confira essa ótima opção de apartamento com 3 suítes, 2 vagas de garagem, completo de armários,<br>novíssimo, pronto para mudar.<br>Lazer completo com piscina, salão de festas, playground, academia.<br>Localizado próximo a entrada de Alphaville, perto de colégios, shoppings, padarias e pista de corrida.<br>Oportunidade unica.<br><br>Agende uma visita!! Cod. 67317.","listingType":"USED","title":"BARUERI - Padrão - Alphaville","createdAt":"2019-05-17T12:47:06.317Z","publisherId":421100,"unitTypes":["APARTMENT"],"providerId":"41735","condominiumName":"","propertyType":"UNIT","contact":{"chat":"","phones":["1138296109","1138296109"],"emails":[]},"listingStatus":"ACTIVE","id":"2445096429","parkingSpaces":[2],"owner":false,"address":{"country":"Brasil","state":"São Paulo","city":"Barueri","neighborhood":"Alphaville","unitNumber":"","zipCode":"06472005","locationId":"BR>Sao Paulo>NULL>Barueri>Barrios>Alphaville","zone":"Bairros","district":"","geoLocation":{"location":{"lat":-23.484829,"lon":-46.851078},"precision":"ROOFTOP","optionalPrecision":"precision"}},"suites":[3],"publicationType":"STANDARD","externalId":"67317","bathrooms":[3],"totalAreas":[112],"logoUrl":"","bedrooms":[3],"promotions":[],"highlights":"","pricingInfos":[{"yearlyIptu":"400","price":"855000","businessType":"SALE","monthlyCondoFee":"676"}],"showPrice":true,"displayAddress":"NEIGHBORHOOD","buildings":0,"images":["https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/86bb8a80997071b23fd8302915015b8c.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/9b07308c8ef6bcbe4026e4c658176a1e.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/d732f98b7a55d11e9dabad248460fa42.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/f418d31487d87f193e1f65b48389c0b5.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/f152749c2ec740d65042d80b8e308524.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/f6be151847d0d6177d8a6008c4e59c40.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/18b9e7cc8dc1538a2b818325c7921c7d.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/c3b4f92c088b9623ea26081f17c34f4b.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/adf79f3d0565db47a6ee4b9840f4e25e.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/51e5021658ba3550683d825ce3d77cc6.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/cec2eac0cc9be212e8451ac66fbea9e1.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/689e7835d9b8027a797d13a7715aac25.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/b1d043a773bc94435580f27a698b02bc.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/6a37c3ee115192285d7b966441ce1bff.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/35a08ae414d2e95f27a772eb7ec61b77.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/c0aeb8bd9a5fb477847a7e51c2da4f16.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/d6e60753f2a3a1483bf8eee84f68953d.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/1b168f76aabf33aa66787e2a7423f70d.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/c53fdb597d057c4a39562c4492c2bd34.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/93af9e0fea8856a1e455a5af4deed1e7.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/441b3c7f697fb912ec2f57f0daddc836.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/b0002cbc3270a9687e6e2059836d8a6b.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/7000744e6a9d54ef1878c70961c37939.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/f6ee211fbc0085b480d1927227801099.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/b46f85cd9aad35b1397404408e29fe48.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/00d4b455cbb41823aa7aaa0fcbb4f298.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/76d2fc7f4756585aa4ece3acc1ac14cc.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/6b471649deeadd4dd483ab921c6bdff5.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/a43a27d9bad266ef76c1e720d2e89933.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/ae46a04891fa23e8a24a62bd560caf13.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/39921e4be61753d5eafcc1fcd6719bc1.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/62b665c4445d8546c6ff59c18e29295e.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/f8ce24fcd70059710e5b2b12ae517507.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/a4a0c83ffdcd512e5150ed8e7f9489d9.jpg"],"videos":[]},"publisher":{"id":"421100","name":"Apoena","address":{"country":"Brasil","zipCode":"06454-020","city":"Barueri","streetNumber":"350","zone":"","street":"Avenida Cauaxi","locationId":"","district":"","unitNumber":"","state":"SP","neighborhood":"Alphaville Centro Industrial e Empresarial/Alphaville."},"phone":{"leadsPhone":"","mobile":"1138296109","alternative":"","primary":"1138296109"},"logoUrl":"https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/e6a95e6b651765412ac046655eb03a18.jpg","licenseNumber":"","websiteUrl":"http://apoenaimoveis.com.br/","leadEmails":[],"createdDate":"2018-10-26T16:37:28Z","showAddress":true},"url":{"id":"2445096429","link":{"name":"Apartamento com 3 Quartos à venda, 112m²","href":"/imovel/apartamento-3-quartos-alphaville-bairros-barueri-com-garagem-112m2-venda-RS855000-id-2445096429/","rel":""}},"properAddress":null,"publisherUrl":{"link":{"name":"","href":"/421100/apoena/","rel":""}}},{"listing":{"amenities":["GATED_COMMUNITY","GYM","BARBECUE_GRILL","GOURMET_SPACE","GARDEN","POOL","PLAYGROUND","SQUASH","TENNIS_COURT","SPORTS_COURT","PARTY_HALL","ADULT_GAME_ROOM","ELEVATOR","LAUNDRY","AIR_CONDITIONING","FURNISHED","GOURMET_BALCONY"],"feedsId":"","usableAreas":[85],"description":"O apartamento no bairro Melville Empresarial I e II possui 85 metros quadrados com 2 quartos sendo 2 suites e 2 banheiros e um lavabo, varanda gourmet com churrasqueira, todo Mobiliado, Linda e completa cozinha com Cooktop e espaço para coifa, Piso em porcelanato no piso Portinari 90x90, Box em Vidro temperado, Pia Sobreposta com bancada Rustica, iluminação industrial, planejados em todos os ambientes, Próximo a restaurantes, hospitais, farmácias, estacionamentos, universidades, shoppings, padarias, hospitais, transporte coletivo, escolas. Piscina aquecida e duas vagas cobertas. Condições especiais de parcelamento - Direto + Entrada. Edifício Present","listingType":"USED","title":"APARTAMENTO ALTO PADRÃO ALPHAVILLE - BARUERI - DUAS SUÍTES - DUAS VAGAS","createdAt":"2019-06-03T21:26:30.827Z","publisherId":420668,"unitTypes":["APARTMENT"],"providerId":"VIVAREAL","condominiumName":"","propertyType":"UNIT","contact":{"chat":"","phones":["11995624544",""],"emails":[]},"listingStatus":"ACTIVE","id":"2446982338","parkingSpaces":[2],"updatedAt":"2019-06-03T21:53:00.797Z","owner":false,"address":{"country":"Brasil","state":"São Paulo","city":"Barueri","neighborhood":"Melville Empresarial Ii","street":"Avenida Ômega","streetNumber":"171","unitNumber":"","zipCode":"06472005","locationId":"BR>Sao Paulo>NULL>Barueri>Barrios>Melville Empresarial Ii","zone":"Bairros","district":"","geoLocation":{"location":{"lat":-46.851078,"lon":-23.484829},"precision":"ROOFTOP","optionalPrecision":"precision"}},"suites":[2],"publicationType":"STANDARD","externalId":"1F4AQPS","bathrooms":[2],"totalAreas":[85],"logoUrl":"","deliveredAt":"2017-01-01T02:00:00Z","bedrooms":[2],"promotions":[],"highlights":"","pricingInfos":[{"yearlyIptu":"500","price":"869000","businessType":"SALE","monthlyCondoFee":"500"}],"showPrice":true,"displayAddress":"ALL","buildings":0,"images":["https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/870ca60633bed428283269daf2f0fabe.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/f2c6fedaf47d739ac45e8fd254076204.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/849746f1f83ddd67332f830b30b1aec8.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/7cc0b9cf4426bec0e2cb20b4360e0a20.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/b5afce68f82463fc35fe812d5990eea9.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/cfef2e6778e907cd6f0cb5b06935704f.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/7d99fa27053dd9cbfa8aae42f9b707a4.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/6c6ba0c1a92a926df075559000917792.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/e7586d51837e8c8ca0db1a3e16130251.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/5064f63330ef9d68de059e18152651a5.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/8e5a9c48dddecc409fda0449f7709316.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/2274fd860225afefa5264a76b641473c.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/7a8409d9b3e27128e87c384e706b8bee.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/321041f0a8917f5dd853e4cf3e107cfa.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/e6bd8e0af27dc79bc3c752b9d8d2e8b8.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/2b737da6a62e91b7bba16f9d285f6055.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/026bcfdc4420b9a8bc058ab6497b4513.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/8c3a2243636909f92cd771d66fe6b7c1.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/249e5dfaa2c8298980ab445b1210551a.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/479a7a6964351ca3e25fd2cdd7a536ea.jpg"],"videos":[]},"publisher":{"id":"420668","name":"ALEXANDRE FACCHINI","address":{"country":"Brasil","zipCode":"18035-370","city":"Sorocaba","streetNumber":"1810","zone":"","street":"Avenida Doutor Afonso Vergueiro Ap. 112 Bloco A","locationId":"","district":"","unitNumber":"","state":"SP","neighborhood":"Centro"},"phone":{"leadsPhone":"","mobile":"","alternative":"","primary":"11995624544"},"logoUrl":"https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/98aeb6a29d770f9dc165e235c500a4ff.jpg","licenseNumber":"193474-F-SP","websiteUrl":"","leadEmails":[],"createdDate":"2018-10-23T19:09:22Z","showAddress":true},"url":{"id":"2446982338","link":{"name":"Apartamento com 2 Quartos à venda, 85m²","href":"/imovel/apartamento-2-quartos-melville-empresarial-ii-bairros-barueri-com-garagem-85m2-venda-RS869000-id-2446982338/","rel":""}},"properAddress":null,"publisherUrl":{"link":{"name":"","href":"/420668/alexandre-facchini/","rel":""}}},{"listing":{"amenities":["BARBECUE_GRILL","KITCHEN","ELEVATOR","GOURMET_BALCONY","POOL","SAUNA","SERVICE_AREA"],"feedsId":"AP1270","usableAreas":[112],"description":"NOVO APARTAMENTO 03 SUITES, VISTA PANORÂMICA PARA LAGO.. Repleto de armários, condomínio com Churrasqueira e Forno de Pizza; Espaço Gourmet; Espaço de descanso com sauna seca; Espaço convivência; Excelente espaço Fitness; Lazer Infantil; Piscina Adulto; Piscina Infantil; Sauna; Salão de festas entre outros. -","listingType":"USED","title":"Apartamento residencial para locação, Alphaville, Barueri.","createdAt":"2018-10-04T05:41:40.410Z","publisherId":251211,"unitTypes":["APARTMENT"],"providerId":"23014","condominiumName":"","propertyType":"UNIT","contact":{"chat":"","phones":["1141950195","11991076161"],"emails":[]},"listingStatus":"ACTIVE","id":"1042003545","parkingSpaces":[2],"updatedAt":"2019-05-20T23:28:17.265Z","owner":false,"address":{"country":"Brasil","state":"São Paulo","city":"Barueri","neighborhood":"Empresarial 18 do Forte","street":"Avenida Ômega","unitNumber":"","zipCode":"06472005","locationId":"BR>Sao Paulo>NULL>Barueri>Barrios>Empresarial 18 do Forte","zone":"Bairros","district":"","geoLocation":{"location":{"lat":-23.484829,"lon":-46.851078},"precision":"ROOFTOP","optionalPrecision":"precision"}},"suites":[3],"publicationType":"STANDARD","externalId":"AP1270","bathrooms":[4],"totalAreas":[112],"logoUrl":"","bedrooms":[3],"promotions":[],"highlights":"","pricingInfos":[{"yearlyIptu":"0","price":"870000","businessType":"SALE","monthlyCondoFee":"676"}],"showPrice":true,"displayAddress":"STREET","buildings":0,"images":["https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/804a61833eed0a6b24ee094979d3002b.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/5539000aca53396cdc3094c9acf9604e.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/46934db444c76dfe89e698884e0b1579.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/3bae4777e14d11809c0fafc46b99ddf1.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/3e6908eac6d890b2a77f45b0a0b94923.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/726d9c8cb4f017075fef3ac46f98e203.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/f08335e175ec7237518815f95792f61b.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/2451677875ca01b6a9d1e0355d0fe783.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/a6d6c8f57ee464b861780961328233cb.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/8c099b918d079e46964a24d45b0c7368.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/c28229b49eaa5cfd9b847f93c07d05ad.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/ded3fbcf9f929559ed815b67b18dc6dd.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/c3f919698c829d94f9d4af064b4f6658.jpg"],"videos":[]},"publisher":{"id":"251211","name":"ALPHA IMÓVEL","address":{"country":"Brasil","zipCode":"06543-001","city":"Santana de Parnaíba","streetNumber":"4000","zone":"","street":"Avenida Marcos Penteado de Ulhôa Rodrigues","locationId":"","district":"","unitNumber":"","state":"SP","neighborhood":"Tamboré"},"phone":{"leadsPhone":"","mobile":"11991076161","alternative":"","primary":"1141950195"},"logoUrl":"https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/46c3a76e0d71a18194a319ab626b4cc5.jpg","licenseNumber":"18786-J-SP","websiteUrl":"http://www.alphaimovel.com.br/","leadEmails":[],"createdDate":"2018-03-28T10:42:55Z","showAddress":true},"url":{"id":"1042003545","link":{"name":"Apartamento com 3 Quartos à venda, 112m²","href":"/imovel/apartamento-3-quartos-empresarial-18-do-forte-bairros-barueri-com-garagem-112m2-venda-RS870000-id-1042003545/","rel":""}},"properAddress":null,"publisherUrl":{"link":{"name":"","href":"/251211/alpha-imovel/","rel":""}}},{"listing":{"amenities":["GYM","BARBECUE_GRILL","GOURMET_SPACE","POOL","PLAYGROUND","PARTY_HALL","ADULT_GAME_ROOM","GATED_COMMUNITY","ELEVATOR","SPA","SAUNA","GARDEN","AIR_CONDITIONING","FURNISHED","GOURMET_BALCONY"],"feedsId":"","usableAreas":[85],"description":"Lindo apartamento mobiliado e decorado com excelente bom gosto. Imóvel com menos de 1 ano de uso. Armários planejados em todos os cômodos, ar condicionado, eletros de primeira linha, acabamentos impecáveis, automação residencial (iluminação, som, persinas, ar condicionado). Tudo de excelente qualidade e muito bom gosto. Apartamento composto por 2 suítes, sendo a suíte master com closet e sacada, lavabo, sala de estar e jantar, espaço gourmet, cozinha e área de serviço. Imóvel em andar alto com sol da manhã ótima iluminação e ventilação natural. Edifício com uma completa estrutura de lazer tendo salão de festas, espaço pet, brinquedoteca, playground, ampla academia, sauna, piscina, vestiários, espaço gourmet com churrasqueira e sala de jogos.","listingType":"USED","title":"Lindo Apartamento Mobiliado!","createdAt":"2019-06-11T22:21:05.441Z","publisherId":370390,"unitTypes":["APARTMENT"],"providerId":"VIVAREAL","condominiumName":"PRESENT ALPHAVILLE","propertyType":"UNIT","contact":{"chat":"","phones":["11993090983","11993090983"],"emails":[]},"listingStatus":"ACTIVE","id":"2447759268","parkingSpaces":[2],"updatedAt":"2019-06-11T22:21:15.800Z","owner":false,"address":{"country":"Brasil","state":"São Paulo","city":"Barueri","neighborhood":"Melville Empresarial Ii","unitNumber":"","zipCode":"06472005","locationId":"BR>Sao Paulo>NULL>Barueri>Barrios>Melville Empresarial Ii","zone":"Bairros","district":"","geoLocation":{"location":{"lat":-23.484829,"lon":-46.851078},"precision":"ROOFTOP","optionalPrecision":"precision"}},"suites":[2],"publicationType":"PREMIUM","externalId":"AP0950","bathrooms":[3],"totalAreas":[],"logoUrl":"","bedrooms":[2],"promotions":[],"highlights":"","pricingInfos":[{"period":"MONTHLY","yearlyIptu":"0","price":"870000","businessType":"SALE","monthlyCondoFee":"750"}],"showPrice":true,"displayAddress":"NEIGHBORHOOD","buildings":1,"images":["https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/276f37470e09feb9c74e6dec256f30f3.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/91a345063044788a9a9d8d3059bd1261.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/6e169f139b667f9af50caded0e61a191.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/d5eb754407f1869ddad57dc3a33709fa.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/8822ea8758b3e09fcfc3a1c43fbc1db6.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/9d7f57deffaf44d8c1821e9bd0c6eb66.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/6d2b284585720e33cc86dc89588f0eb1.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/700f143b78692850a178764dc072d227.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/5c9ec54328741a9baeeb2071ae7d971c.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/30370c4940ea3fb5a5e1f9799439e3a7.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/843f88cfa66df4462a7a8fc4dc965747.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/9490f94a74e832727a049283d42acfa8.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/08de29845fd85c3e0731283a5b714949.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/22ddf4b0ee8d0dfab46895ba578af31c.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/e4046ef6a930e19e64c502a74cc80cd4.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/107322ed835cb1b7ce2b404f80707559.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/e8b67c7b29a9b62f7c1d1af53906b326.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/ad4f1fc1a981dd6b18682912f1a8036f.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/4e6ee9015fbe3cf52a6a1adfd237a4eb.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/10c19672667725e1efe32e3b1caf9cc5.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/912fc9d1519a43702d0a7dea51e47b25.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/3bdf6f7ca791d22b17fc141ea22837ad.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/565163f8ecb6df528b60c079d431e200.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/ec3b049272b78641953a120716ae747d.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/4bf2c831cc4733512837ff5803ae128d.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/becf19adf78506a638f6577988d2ff8d.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/f173c1a384c21833de7467882d8cf665.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/48cdc405b5992377cfbd518a1fb026ac.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/714996efbff712ecb6aa098e5dd7c2e2.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/0481bec4f0c4c5aceec7f52ba94e1534.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/7204b3eccbe77019ff11b0f1c909105f.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/8492a705d12a43ddc49e8c5724546997.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/7d42cb816c2700ebe0f98485df4a7cc7.jpg"],"videos":[]},"publisher":{"id":"370390","name":"Fabiana Martello","address":{"country":"Brasil","zipCode":"06454-050","city":"Barueri","streetNumber":"218","zone":"","street":"Alameda Grajaú","locationId":"","district":"","unitNumber":"","state":"SP","neighborhood":"Alphaville Centro Industrial e Empresarial/Alphaville."},"phone":{"leadsPhone":"","mobile":"11993090983","alternative":"","primary":"11993090983"},"logoUrl":"","licenseNumber":"52358-F-RS","websiteUrl":"","leadEmails":[],"createdDate":"2018-07-10T13:00:10Z","showAddress":true},"url":{"id":"2447759268","link":{"name":"Apartamento com 2 Quartos à venda, 85m²","href":"/imovel/apartamento-2-quartos-melville-empresarial-ii-bairros-barueri-com-garagem-85m2-venda-RS870000-id-2447759268/","rel":""}},"properAddress":null,"publisherUrl":{"link":{"name":"","href":"/370390/fabiana-martello/","rel":""}}},{"listing":{"amenities":["SECURITY_24_HOURS","PLAYGROUND","GOURMET_SPACE","SPORTS_COURT","NEAR_SHOPPING_CENTER","PARTY_HALL","INTERCOM","BALCONY","GYM","BARBECUE_GRILL","ELEVATOR","GATED_COMMUNITY","POOL","NEAR_ACCESS_ROADS"],"feedsId":"","usableAreas":[112],"description":"Apartamento em Alphaville de 112m² com 3 suítes e 2 vagas no condomínio Present Alphaville.<br>Entrega do empreendimento prevista para 2017.<br>Condomínio com lazer completo: espaço gourmet, churrasqueira, piscinas adulto e infantil, salão de festas, sauna, sala de jogos, sala fitness, lazer infantil, pet pleace, espaço de conveniência, espaço de descanso, espaço office, segurança 24 horas.<br>Fácil acesso a Castelo Branco, próximo aos centros comerciais da região, shopping, mercados, bancos, farmácias e restaurantes.<br>Qualidade e garantia MPD.<br><br>Simone ( 1 1 ) 9 7 0 9 5 - 5 3 7 0","listingType":"USED","title":"Apartamento em Alphaville com 3 dormitórios e 2 vagas no cond. Present Alphaville por 872mil","createdAt":"2017-05-16T16:12:08.801Z","publisherId":119468,"unitTypes":["APARTMENT"],"providerId":"VIVAREAL","condominiumName":"","propertyType":"UNIT","contact":{"chat":"","phones":["1143699364"],"emails":[]},"listingStatus":"ACTIVE","id":"80980340","parkingSpaces":[2],"updatedAt":"2018-07-09T14:50:01.975Z","owner":false,"address":{"country":"Brasil","state":"São Paulo","city":"Barueri","neighborhood":"Melville Empresarial Ii","street":"Avenida Ômega","streetNumber":"171","unitNumber":"","zipCode":"06472005","locationId":"BR>Sao Paulo>NULL>Barueri>Barrios>Melville Empresarial Ii","zone":"Bairros","district":"","geoLocation":{"location":{"lat":-23.483886,"lon":-46.849025},"precision":"ROOFTOP","optionalPrecision":"precision"}},"suites":[3],"publicationType":"STANDARD","externalId":"10351","bathrooms":[4],"totalAreas":[112],"logoUrl":"","bedrooms":[3],"promotions":[],"highlights":"","pricingInfos":[{"price":"872000","businessType":"SALE"}],"showPrice":true,"displayAddress":"ALL","images":["https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/d50d69bcb19113fb02bae4661e6f620e.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/78472cd5485c11921318f36dba104d17.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/9a0c9b080767236111a63b6e6cb79e11.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/04738057a081cb0ce1bbdcea852e91e4.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/25531d751bd9df125f1e58096c3138be.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/d5929595facfb0553e257c1643798c54.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/10d541a99af93d5d43cdc82d2da23974.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/154d02ea904d1c2f1ca0f9cfc8cea284.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/a1e7fed82eaeec63187305cace652e17.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/2dfc0d1a72b84b903da7fd77579b5484.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/b155cf77db1f0a3c4aafdea8cf352dd2.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/9ba6890f5bc5df5ee099dc339f394b63.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/c39c15c14912b131c905f80c05cd7dff.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/5ff7ac8cdf2f269c4e962fb80b47af19.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/02295ecb87e85bd36fa57a552d10f389.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/786f2397b8ba49dcb519a4672e1bff8d.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/7199927e37656ee1ac89c0db4b1fff3b.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/fc9b32b45c764586ac4e5c760be88013.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/b42b9fc5901cd9d6ddcd765eb1754c32.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/d41972cc4a84a059d41da6481bf52dff.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/b4de53e52cfecd39986cc3f61481f2f8.jpg"],"videos":[]},"publisher":{"id":"119468","name":"SIMONE PEREIRA HAMATI","address":{"country":"Brasil","zipCode":"06414-000","city":"Barueri","streetNumber":"429","zone":"","street":"Rua Marte","locationId":"","district":"","unitNumber":"","state":"SP","neighborhood":"Cidade Jardim II"},"phone":{"leadsPhone":"1143699364","mobile":null,"alternative":"","primary":"1143699364"},"logoUrl":"https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/2d66a9f7e892cbd783cd5face5c95d09.jpg","licenseNumber":"143478-F-SP","websiteUrl":"","leadEmails":[],"createdDate":"2018-03-27T15:08:30Z","showAddress":true},"url":{"id":"80980340","link":{"name":"Apartamento com 3 Quartos à venda, 112m²","href":"/imovel/apartamento-3-quartos-melville-empresarial-ii-bairros-barueri-com-garagem-112m2-venda-RS872000-id-80980340/","rel":""}},"properAddress":null,"publisherUrl":{"link":{"name":"","href":"/119468/simone-pereira-hamati/","rel":""}}},{"listing":{"amenities":["KITCHEN","ELEVATOR","BALCONY","SERVICE_AREA"],"feedsId":"AP21903","usableAreas":[112],"description":"Apartamento NOVO à VENDA<br>Condomínio Present 18 do Forte (Alphaville), Barueri<br>Apartamento de 112m2:<br>3 dormitórios sendo 3 suítes, 2 vagas<br>Repleto de armários.<br><br>O bairro de Alphaville, é internacionalmente conhecido por seus residenciais, pela quantidade de empresas nacionais e internacionais e pelo de setor de serviços.<br>Atualmente, possui toda a infraestrutura dos grandes centros, tais como: shoppings (Iguatemi e Tamboré), agências bancárias, lotéricas, supermercados, academias, cinemas, clínicas estéticas, entre outras muitas opções. -","listingType":"USED","title":"Apartamento residencial à venda, Alphaville, Barueri.","createdAt":"2018-10-05T00:29:55.059Z","publisherId":184722,"unitTypes":["APARTMENT"],"providerId":"9657","condominiumName":"","propertyType":"UNIT","contact":{"chat":"","phones":["1148610724"],"emails":[]},"listingStatus":"ACTIVE","id":"1042032728","parkingSpaces":[2],"updatedAt":"2019-05-21T00:58:10.314Z","owner":false,"address":{"country":"Brasil","state":"São Paulo","city":"Barueri","neighborhood":"Alphaville","street":"Avenida Ômega","streetNumber":"171","unitNumber":"","zipCode":"06472005","locationId":"BR>Sao Paulo>NULL>Barueri>Barrios>Alphaville","zone":"Bairros","district":"","geoLocation":{"location":{"lat":-23.484829,"lon":-46.851078},"precision":"ROOFTOP","optionalPrecision":"precision"}},"suites":[3],"publicationType":"STANDARD","externalId":"AP21903","bathrooms":[4],"totalAreas":[],"logoUrl":"","bedrooms":[3],"promotions":[],"highlights":"","pricingInfos":[{"yearlyIptu":"20","price":"875000","businessType":"SALE","monthlyCondoFee":"676"}],"showPrice":true,"displayAddress":"ALL","buildings":0,"images":["https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/1bf75bff42741735da8c59d2f7af88c5.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/f1395446909d917eb3ea92854c16d9e4.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/f6b7da4acb37abbad18572d31bd4cf37.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/1e7e38a12bdcd206be30e9bc860852e7.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/49606072b2d0bd80f8f18bab36fd199d.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/e0a70feaef2fd37133efed6960d2af2a.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/5d70e3dfc8e817d2617b73126cabf17b.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/1c77fa890b2ed5a65d454ed4a13462dc.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/e03f562e9834992fb2b29cdbd5533a76.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/4e020a9444744814e37c448dc2aa8c24.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/88f62c072aa9d760b176ae6a5d67a46b.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/529e2aa84f79a1602d10c896bd897ecf.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/60f7c6db5688fbcb5f00649ddaaa39fc.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/0f424b1cb93b0a42d2299dba3d0c5d93.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/432b3a4bb171f6da90287628e25de7d3.jpg"],"videos":[]},"publisher":{"id":"184722","name":"ALPHA VENDE","address":{"country":"Brasil","zipCode":"06429-120","city":"Barueri","streetNumber":"","zone":"","street":"Avenida dos Patos","locationId":"","district":"","unitNumber":"","state":"SP","neighborhood":"Residencial Morada das Estrelas (Aldeia da Serra)"},"phone":{"leadsPhone":"1148610724","mobile":null,"alternative":"","primary":"1148610724"},"logoUrl":"https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/4e24b283038ef993c6477a80901ab939.jpg","licenseNumber":"062960-F-SP","websiteUrl":"http://www.alphavende.com","leadEmails":[],"createdDate":"2018-03-27T22:45:40Z","showAddress":true},"url":{"id":"1042032728","link":{"name":"Apartamento com 3 Quartos à venda, 112m²","href":"/imovel/apartamento-3-quartos-alphaville-bairros-barueri-com-garagem-112m2-venda-RS875000-id-1042032728/","rel":""}},"properAddress":null,"publisherUrl":{"link":{"name":"","href":"/184722/alpha-vende/","rel":""}}},{"listing":{"amenities":["LAUNDRY","GOURMET_BALCONY","POOL","GYM","GARAGE","GATED_COMMUNITY","BALCONY"],"feedsId":"1925","usableAreas":[112],"description":"Apartamento com: Área de serviço, Armário de cozinha, Armário na área de serviço, Armário no banheiro, Armário no corredor, Lavanderia<br>Varanda gourmet, Armários Planejados<br><br>Lazer: Piscina, Academia<br><br>Areas Preservadas, Banco, Centro Comercial, Escolas, Farmácia, Hipermercado, Hospital, Laboratório, Padaria, Restaurantes, Shopping Center<br><br>Características do imóvel<br>Academia<br>Área de serviço<br>Areas Preservadas<br>Armário de cozinha<br>Armário na área de serviço<br>Armário no banheiro<br>Armário no corredor<br>Armários Planejados<br>Banco<br>Centro Comercial<br>Escolas<br>Farmácia<br>Hipermercado<br>Hospital<br>Laboratório<br>Lavanderia<br>Padaria<br>Piscina<br>Restaurantes<br>Shopping Center<br>Varanda<br>Varanda gourmet<br><br>Mais informações em www.casaelaralpha.com.br","listingType":"USED","title":"Apartamento Novo à venda no Condomínio Present","createdAt":"2019-05-08T02:01:44.392Z","publisherId":135567,"unitTypes":["APARTMENT"],"providerId":"15862","condominiumName":"","propertyType":"UNIT","contact":{"chat":"","phones":["11944701623","11986530666"],"emails":[]},"listingStatus":"ACTIVE","id":"2443850442","parkingSpaces":[2],"updatedAt":"2019-06-06T20:24:28.673Z","owner":false,"address":{"country":"Brasil","state":"São Paulo","city":"Barueri","neighborhood":"Empresarial 18 do Forte","unitNumber":"","zipCode":"06472005","locationId":"BR>Sao Paulo>NULL>Barueri>Barrios>Empresarial 18 do Forte","zone":"Bairros","district":"","geoLocation":{"location":{"lat":-23.484829,"lon":-46.851078},"precision":"ROOFTOP","optionalPrecision":"precision"}},"suites":[1],"publicationType":"STANDARD","externalId":"1925","bathrooms":[2],"totalAreas":[112],"logoUrl":"","bedrooms":[3],"promotions":[],"highlights":"","pricingInfos":[{"yearlyIptu":"53","price":"895000","businessType":"SALE","monthlyCondoFee":"980"}],"showPrice":true,"displayAddress":"NEIGHBORHOOD","buildings":0,"images":["https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/fe1ee86994cac743d84a60082e820970.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/50ab443b2b0a23cbd5d97c120d5eb6ed.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/23a7483b1c561b86c7ed64def824f829.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/dc17be5ac39fb199cc5280c200df8ca8.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/a53eed34846b751e27e52d6cda2df26f.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/ea84cd0e47047ab8f4ec8fd5cebdf4eb.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/77f95ab066af52a82df24302b4699522.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/eda976cde506b8135a0ffa4196ed3b71.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/48fd754c1cb8b93f5b1d5dd32a419e28.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/b448ef07924c50c5ea2d218faa05fe6c.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/a9aa91c5a0b0f90c183e78ca4e2af950.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/a67da2a96e33bc5c35cb2c09be51e71f.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/64f73c6ffd871fa3bcfac89181d96ce7.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/bd4c42506afd1c975ead1313ca1edc62.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/a25f733807c412805ec3b5a552bc3372.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/ffdf49249ba598b539a47b7f3613ffab.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/67d1304c62b65f63d49119cc025ea8c7.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/62278a3bb62d88baef0bd2ed2cba1490.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/872b1722a1b729f7e912ba216830979c.jpg"],"videos":[]},"publisher":{"id":"135567","name":"Casa e Lar Alpha","phone":{"leadsPhone":"","mobile":"11986530666","alternative":"","primary":"11944701623"},"logoUrl":"https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/dbe7bce4d99544aea50a974d6fac622e.jpg","licenseNumber":"20178-J-SP","websiteUrl":"http://www.casaelaralpha.com.br/","leadEmails":[],"createdDate":"2018-03-27T20:51:41Z","showAddress":false},"url":{"id":"2443850442","link":{"name":"Apartamento com 3 Quartos à venda, 112m²","href":"/imovel/apartamento-3-quartos-empresarial-18-do-forte-bairros-barueri-com-garagem-112m2-venda-RS895000-id-2443850442/","rel":""}},"properAddress":null,"publisherUrl":{"link":{"name":"","href":"/135567/casa-e-lar-alpha/","rel":""}}},{"listing":{"amenities":["SAFETY_CIRCUIT","TEEN_SPACE","GREEN_SPACE","ELECTRIC_GENERATOR","CHILDRENS_POOL","ADULT_POOL","MASSAGE","WATCHMAN","GYM","BARBECUE_GRILL","GATED_COMMUNITY","ELEVATOR","GOURMET_SPACE","GARDEN","LAUNDRY","POOL","PLAYGROUND","SPORTS_COURT","PARTY_HALL","ADULT_GAME_ROOM","SAUNA","SPA","INTERNET_ACCESS","SERVICE_AREA","INTERCOM","CABLE_TV","GOURMET_BALCONY","AIR_CONDITIONING"],"feedsId":"","usableAreas":[112],"description":"Present (MPD) em andar alto. <br>Vista limpa e permanente, varanda gournet.<br>Planejados em todos os cômodos do imóvel.<br>Ponto de ar-condicionado em todas as suítes e sala.<br>02 vagas em condomínio completo e área de lazer na cobertura.<br><br>TENHO UNIDADES SEM ACABAMENTO NESSE MESMO CONDOMÍNIO.","listingType":"USED","title":"Present 112m² - Planejados e vista limpa","createdAt":"2018-10-11T01:53:22.765Z","publisherId":82195,"unitTypes":["APARTMENT"],"providerId":"VIVAREAL","condominiumName":"","propertyType":"UNIT","contact":{"chat":"","phones":["11985217338","11977078609"],"emails":[]},"listingStatus":"ACTIVE","id":"1042224679","parkingSpaces":[2],"updatedAt":"2019-05-04T17:31:25.702Z","owner":false,"address":{"country":"Brasil","state":"São Paulo","city":"Barueri","neighborhood":"Empresarial 18 do Forte","street":"Avenida Ômega","streetNumber":"171","unitNumber":"","zipCode":"06472005","locationId":"BR>Sao Paulo>NULL>Barueri>Barrios>Empresarial 18 do Forte","zone":"Bairros","district":"","geoLocation":{"location":{"lat":-23.48458,"lon":-46.850891},"precision":"ROOFTOP","optionalPrecision":"precision"}},"suites":[3],"publicationType":"PREMIUM","externalId":"APVEPRE","bathrooms":[4],"totalAreas":[112],"logoUrl":"","bedrooms":[3],"promotions":[],"highlights":"","pricingInfos":[{"period":"MONTHLY","yearlyIptu":"600","price":"895000","businessType":"SALE","monthlyCondoFee":"890"}],"showPrice":true,"displayAddress":"ALL","buildings":0,"images":["https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/0259b644c24a9890c509af41d54c4aa1.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/866da960e0a6eb4f2b25ea4d01bbe959.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/2563b6bc604a672655fb1a41db14115a.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/e195161beece424fb30f5061cdf4de45.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/38ed01146f248aa3c88ce88555996a55.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/3b693a94e522b2b63a219e20cef904f1.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/65e47cd6668fc986173a58cf7ec62567.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/fa57b772083b06e314f5ded9717b2753.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/a8f4b4c9cbfe6d37e4b5cb19201c1ea0.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/b8f487fda339a0b6136810b8708f68a8.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/5071297ca9777f9a070932304fa12fc9.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/8a8764c20ee3d2772d39c6d8ef11709a.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/ef113bcf66bacf006aad604cca759984.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/fe28f93cc6ce5774286f57704eeb04e0.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/c13cb6b26d18959a4abbc9adbdfab533.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/5959e343449b6b222fb310c48dda7459.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/a82c1f5220bbb0c7e6b4499be7ad2800.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/1b080fc414c0aed8517c04dd68076a0f.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/e94c92d10bc7a5f9bfe0982af074bdce.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/6d1113f6be2948d7e271b0ffd30664ae.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/ccee331432623aaa106a29e35b3ee291.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/2a796a0d7b6c66ec4216f10e21eb37e8.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/2b82ec907d504ce02fc32053195b34bc.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/006854b92ac3e90fe56141f085a10e18.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/7a7a9e0f52a1e2aedba1cea39eff87e2.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/9d159ccf20538622cba11804779a8292.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/3611d993f2b8f4631cd25bc0be6e6f23.jpg"],"videos":[]},"publisher":{"id":"82195","name":"JEFERSON  SANT ANNA","phone":{"leadsPhone":"","mobile":"11977078609","alternative":"","primary":"11985217338"},"logoUrl":"https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/87bfbe6839b70c27a572b078bc648705.jpg","licenseNumber":"112899-F-SP","websiteUrl":"","leadEmails":[],"createdDate":"2018-03-27T21:04:55Z","showAddress":false},"url":{"id":"1042224679","link":{"name":"Apartamento com 3 Quartos à venda, 112m²","href":"/imovel/apartamento-3-quartos-empresarial-18-do-forte-bairros-barueri-com-garagem-112m2-venda-RS895000-id-1042224679/","rel":""}},"properAddress":null,"publisherUrl":{"link":{"name":"","href":"/82195/jeferson-sant-anna/","rel":""}}},{"listing":{"amenities":["GYM","BARBECUE_GRILL","GOURMET_SPACE","INTERCOM","POOL","HIKING_TRAIL","PLAYGROUND","SPORTS_COURT","ALARM_SYSTEM","SPA","CABLE_TV","GOURMET_BALCONY","PARTY_HALL","HOME_OFFICE","BALCONY","SAUNA","WATCHMAN"],"feedsId":"545","usableAreas":[112],"description":"Um empreendimento diferenciado, valoriza que as pessoas possam aproveitar mais o lazer, e a interação entre elas. Com isto, a cobertura conta com um espaço de lazer panorâmico com vista para uma área de preservação e um lago. É um conceito inédito de lazer com salão de jogos e salão gourmet, o Sky Place.<br><br><br><br>Principais características:<br><br>* Churrasqueira<br><br>* Espaço Gourmet<br><br>* Fitness<br><br>* Lazer Infantil<br><br>* Piscina Adulto<br><br>* Piscina Infantil<br><br>* Sauna<br><br>* Pet Place<br><br>* Salão de festas<br><br>* Espaço convivência<br><br>* Espaço de descanso com sauna seca<br><br><br><br>Opções de planta: 84,68 m² e 112,22 m²<br><br>Nos consulte!","listingType":"USED","title":"Apartamento com 2 dorms, Alphaville, Barueri - R$ 927 mil, Cod: 545","createdAt":"2017-05-26T04:58:54Z","publisherId":114591,"unitTypes":["APARTMENT"],"providerId":"14398","condominiumName":"","propertyType":"UNIT","contact":{"chat":"","phones":["11959433878","11959433878"],"emails":[]},"listingStatus":"ACTIVE","id":"81444510","parkingSpaces":[2],"updatedAt":"2019-06-08T03:43:50.441Z","owner":false,"address":{"country":"Brasil","state":"São Paulo","city":"Barueri","neighborhood":"Alphaville","unitNumber":"","zipCode":"06472005","locationId":"BR>Sao Paulo>NULL>Barueri>Barrios>Alphaville","zone":"Bairros","district":"","geoLocation":{"location":{"lat":-23.484829,"lon":-46.851078},"precision":"ROOFTOP","optionalPrecision":"precision"}},"suites":[2],"publicationType":"STANDARD","externalId":"545","bathrooms":[2],"totalAreas":[2211],"logoUrl":"","bedrooms":[2],"promotions":[],"highlights":"","pricingInfos":[{"yearlyIptu":"0","price":"927547","businessType":"SALE","monthlyCondoFee":"0"}],"showPrice":true,"displayAddress":"NEIGHBORHOOD","buildings":0,"images":["https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/742d61efebd4036cde2da07e5de99ad2.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/05cbb992bc212f76497613dda11f4b25.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/b4ba728c04ec7eaaeb10307569297be3.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/816269dfebc607afdf7161585cd8bee4.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/4da4cd48540ea3adacebbd9988ff1ae6.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/03c193e9d9ada9f37ba274d3bd01776c.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/11ef2d8d24f01db9c3fc27e7e036615e.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/d8d83ada71fa2e99143d795dc3f31114.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/f5453a04698c884871ef652a7f2ceaaf.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/0aa7dcea4523bead5d7ed82bce5f7f32.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/f91d35ac7a10d92ff27a018d935f4897.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/ed10548d48dd4b023510d89cee8bb8a1.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/1511e5e3cbc1338a5e3b75503eb99159.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/caf33a09c3f17c5564d3a68db1cd00e5.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/ff4e0dfd9a73c1a6cb92c187ddcef526.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/a165c14a7a6b48f2918007ce28f2eb17.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/9aff29eaae3496672c39122f7a1d6b02.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/e668549dd5782e21b29e910f0402ef62.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/4bf419774f056af8696aa5deea0b9f34.jpg"],"videos":[]},"publisher":{"id":"114591","name":"MAYUMI IMOVEIS EIRELI - ME","address":{"country":"Brasil","zipCode":"08230-010","city":"São Paulo","streetNumber":"910","zone":"","street":"Rua Francisco Alarico Bérgamo","locationId":"","district":"","unitNumber":"","state":"SP","neighborhood":"Vila Taquari"},"phone":{"leadsPhone":"","mobile":"11959433878","alternative":"","primary":"11959433878"},"logoUrl":"https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/17746dc8110ee72c8cc60d1a9e8b796d.jpg","licenseNumber":"28250-J-SP","websiteUrl":"http://mayumiimoveis.com.br","leadEmails":[],"createdDate":"2018-03-27T15:28:18Z","showAddress":true},"url":{"id":"81444510","link":{"name":"Apartamento com 2 Quartos à venda, 112m²","href":"/imovel/apartamento-2-quartos-alphaville-bairros-barueri-com-garagem-112m2-venda-RS927547-id-81444510/","rel":""}},"properAddress":null,"publisherUrl":{"link":{"name":"","href":"/114591/mayumi-imoveis-eireli-me/","rel":""}}},{"listing":{"amenities":["ELEVATOR"],"feedsId":"AP1211","usableAreas":[112],"description":"Ótima oportunidade! Apartamento para venda. Empreendimento entregue a poucos meses pela construtora. Vista privilegiada! Condomínio completo! Estuda Permuta! -","listingType":"USED","title":"Present Alphaville","createdAt":"2018-09-12T08:13:40.911Z","publisherId":251211,"unitTypes":["APARTMENT"],"providerId":"23014","condominiumName":"","propertyType":"UNIT","contact":{"chat":"","phones":["1141950195","11991076161"],"emails":[]},"listingStatus":"ACTIVE","id":"1041050325","parkingSpaces":[2],"updatedAt":"2019-05-20T23:28:18.474Z","owner":false,"address":{"country":"Brasil","state":"São Paulo","city":"Barueri","neighborhood":"Empresarial 18 do Forte","street":"Avenida Ômega","unitNumber":"","zipCode":"06472005","locationId":"BR>Sao Paulo>NULL>Barueri>Barrios>Empresarial 18 do Forte","zone":"Bairros","district":"","geoLocation":{"location":{"lat":-23.484829,"lon":-46.851078},"precision":"ROOFTOP","optionalPrecision":"precision"}},"suites":[3],"publicationType":"STANDARD","externalId":"AP1211","bathrooms":[4],"totalAreas":[112],"logoUrl":"","bedrooms":[3],"promotions":[],"highlights":"","pricingInfos":[{"yearlyIptu":"0","price":"950000","businessType":"SALE","monthlyCondoFee":"600"}],"showPrice":true,"displayAddress":"STREET","buildings":0,"images":["https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/510f105e8ec614142f94b54ce9026215.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/f9a7098d493717105a8c02639055aa7c.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/917af7d24ffc6007f2ba5ae074784a12.jpg"],"videos":[]},"publisher":{"id":"251211","name":"ALPHA IMÓVEL","address":{"country":"Brasil","zipCode":"06543-001","city":"Santana de Parnaíba","streetNumber":"4000","zone":"","street":"Avenida Marcos Penteado de Ulhôa Rodrigues","locationId":"","district":"","unitNumber":"","state":"SP","neighborhood":"Tamboré"},"phone":{"leadsPhone":"","mobile":"11991076161","alternative":"","primary":"1141950195"},"logoUrl":"https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/46c3a76e0d71a18194a319ab626b4cc5.jpg","licenseNumber":"18786-J-SP","websiteUrl":"http://www.alphaimovel.com.br/","leadEmails":[],"createdDate":"2018-03-28T10:42:55Z","showAddress":true},"url":{"id":"1041050325","link":{"name":"Apartamento com 3 Quartos à venda, 112m²","href":"/imovel/apartamento-3-quartos-empresarial-18-do-forte-bairros-barueri-com-garagem-112m2-venda-RS950000-id-1041050325/","rel":""}},"properAddress":null,"publisherUrl":{"link":{"name":"","href":"/251211/alpha-imovel/","rel":""}}},{"listing":{"amenities":["POOL","BARBECUE_GRILL","GOURMET_SPACE","GATED_COMMUNITY","LAND","SAUNA"],"feedsId":"779","usableAreas":[112],"description":"Apartamento novo, com piso, 112m², sendo 2 suítes, sala ampliada, varanda ampla, confira, só precisará personalizá-lo para que o ambiente fique ainda mais agradável e confortável. <br><br>Eder Soares Negócios Imobiliários, a sua boutique de imóveis em Alphaville e região. <br><br>Marque já a sua visita e conheça mais apartamentos na região de Alphaville.<br><br>O residencial, que possui projeto que valoriza o lazer, as áreas verdes e a interação entre as pessoas em uma localização privilegiada, conta com design moderno com plantas de 85 m² e 112 m², com 2 vagas de garagem, varanda gourmet em todas as unidades e lazer panorâmico na cobertura. É um projeto exclusivo que alia natureza e contemporaneidade.<br>A cobertura, um dos grandes diferenciais do empreendimento, traz um espaço de lazer panorâmico com vista para uma área de preservação e um lago: o Sky Space. Um conceito inédito de lazer com salão de jogos, churrasqueira com forno de pizza, espaço gourmet, espaço de convivência e terraço panorâmico. Já no térreo, a área de lazer é composta por duas piscinas (adulto e infantil), solarium, salão de festas, pet place, brinquedoteca, fitness, sala de ginástica, playground, deck molhado, espaço de convivência e sauna seca com descanso.<br>próximo à Alameda Rio Negro e possui em seus arredores uma completa infraestrutura de comércio e serviços e acessos estratégicos para importantes estradas e rodovias.<br><br>Características do condomínio<br>Churrasqueira<br>Churrasqueira<br>Espaço gourmet<br>Espaço pet<br>Fitness<br>Piscina<br>Piscina<br>Piscina infantil<br>Piscina infantil<br>Salão de festas<br>Salão de festas<br>Sauna seca<br>Sauna seca<br><br>Mais informações em www.edersoaresimoveis.com.br","listingType":"USED","title":"More em um apto novinho em Alphaville: Present Tamboré","createdAt":"2019-05-11T01:43:09.643Z","publisherId":58225,"unitTypes":["APARTMENT"],"providerId":"8966","condominiumName":"","propertyType":"UNIT","contact":{"chat":"","phones":["1141916633","11977931000"],"emails":[]},"listingStatus":"ACTIVE","id":"2444265377","parkingSpaces":[0],"updatedAt":"2019-06-07T02:58:39.814Z","owner":false,"address":{"country":"Brasil","state":"São Paulo","city":"Barueri","neighborhood":"Melville Empresarial Ii","unitNumber":"","zipCode":"06472005","locationId":"BR>Sao Paulo>NULL>Barueri>Barrios>Melville Empresarial Ii","zone":"Bairros","district":"","geoLocation":{"location":{"lat":-23.484829,"lon":-46.851078},"precision":"ROOFTOP","optionalPrecision":"precision"}},"suites":[2],"publicationType":"STANDARD","externalId":"779","bathrooms":[3],"totalAreas":[112],"logoUrl":"","bedrooms":[2],"promotions":[],"highlights":"","pricingInfos":[{"price":"950000","businessType":"SALE"}],"showPrice":true,"displayAddress":"NEIGHBORHOOD","buildings":0,"images":["https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/191f717fa8e560474d41cc23e64838b2.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/b9ff4df600f13f4badc2960c9b96b16d.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/1210671bf05b338d1ef81ddede188cbf.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/898ef9f61c525e4c30004380115500c8.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/6aecf1f3069e8aa305c0b064edf0b564.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/7c2fa3894477b02edf0c9ee957babd83.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/dff9b93c78e13e9df3c7877295f44264.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/68ec4f2c6eb89aa3778660d2668b6ad7.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/1b8a7fcb5e2e72b6d8dc93909707f164.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/8760774f79399f6aa59141a97d8ac4cf.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/0ff8ebe6ed2cffb3cb428001f35f4f63.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/45e52cfa42285d18e8fe632d71106c3f.jpg","https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/b98606691b4123af36168a4c96555680.jpg"],"videos":[]},"publisher":{"id":"58225","name":"EDER SOARES PARTICIPACOES E NEGOCIOS IMOBILIARIOS LTDA","address":{"country":"Brasil","zipCode":"06454-050","city":"Barueri","streetNumber":"614","zone":"","street":"Alameda Grajaú","locationId":"","district":"","unitNumber":"","state":"SP","neighborhood":"Alphaville Industrial"},"phone":{"leadsPhone":"","mobile":"11977931000","alternative":"","primary":"1141916633"},"logoUrl":"https://resizedimgs.vivareal.com/{action}/{width}x{height}/vr.images.sp/1dbf69ce3296cd826899441e82727d75.jpg","licenseNumber":"24345-J-SP","websiteUrl":"http://www.edersoaresimoveis.com.br","leadEmails":[],"createdDate":"2018-03-27T17:06:35Z","showAddress":true},"url":{"id":"2444265377","link":{"name":"Apartamento com 2 Quartos à venda, 112m²","href":"/imovel/apartamento-2-quartos-melville-empresarial-ii-bairros-barueri-112m2-venda-RS950000-id-2444265377/","rel":""}},"properAddress":null,"publisherUrl":{"link":{"name":"","href":"/58225/eder-soares-participacoes-e-negocios-imobiliarios-ltda/","rel":""}}}]}},"page":{"title":"Avenida Ômega, 171 - PRESENT ALPHAVILLE - Viva Real","link":"/condominio/present-alphaville-alphaville-id-6ad8eb6a-e5a8/"},"priceHistory":{"uuid":"6ad8eb6a-41d8-4703-929c-3c5b3898e5a8","priceHistory":[{"year":2017,"month":4,"median":634910},{"year":2017,"month":5,"median":634910},{"year":2017,"month":6,"median":650000},{"year":2017,"month":7,"median":650000},{"year":2017,"month":8,"median":700000},{"year":2017,"month":9,"median":700000},{"year":2017,"month":11,"median":682000},{"year":2017,"month":10,"median":654217},{"year":2017,"month":12,"median":682000},{"year":2018,"month":1,"median":682000},{"year":2018,"month":2,"median":690000},{"year":2018,"month":3,"median":690000},{"year":2018,"month":4,"median":682000},{"year":2018,"month":5,"median":682000},{"year":2018,"month":6,"median":698900},{"year":2018,"month":7,"median":703158}]},"unitTypes":[{"amenities":[],"condominiumUuid":"6ad8eb6a-41d8-4703-929c-3c5b3898e5a8","address":{"zipCode":"06472005","streetNumber":"171","city":"Barueri","geoLocation":{"latitude":-23.484779,"precision":"RANGE_INTERPOLATED","longitude":-46.851354},"street":"Avenida Ômega","neighborhood":"Alphaville","state":"São Paulo"},"suites":3,"description":"","media":[],"type":"APARTMENT","bathrooms":2,"uuid":"8f467744-994a-4439-92c6-4460ddfcded8","bedrooms":3,"createdAt":"2017-05-12T19:45:07.146Z","floors":0,"iptu":0,"buildingUuid":"","parkingSpaces":2,"dimensions":{"grossInternalArea":0,"netInternalArea":112,"grossExternalArea":168},"updatedAt":"2017-05-12T19:45:07.146Z"},{"amenities":[],"condominiumUuid":"6ad8eb6a-41d8-4703-929c-3c5b3898e5a8","address":{"zipCode":"06472005","streetNumber":"171","city":"Barueri","geoLocation":{"latitude":-23.484779,"precision":"RANGE_INTERPOLATED","longitude":-46.851354},"street":"Avenida Ômega","neighborhood":"Alphaville","state":"São Paulo"},"suites":2,"description":"","media":[],"type":"APARTMENT","bathrooms":2,"uuid":"984e57b4-d826-460a-ac46-31cc7da237ba","bedrooms":2,"createdAt":"2017-05-12T19:45:07.146Z","floors":0,"iptu":0,"buildingUuid":"","parkingSpaces":2,"dimensions":{"grossInternalArea":0,"netInternalArea":85,"grossExternalArea":127},"updatedAt":"2017-05-12T19:45:07.146Z"}],"redirect":{"path":"/condominio/present-alphaville-alphaville-id-6ad8eb6a-e5a8/","statusCode":200},"serverRendered":true,"googleTagManagerId":"GTM-82BN","googleTagManagerIdNewContainer":"GTM-NP5VKCD","canonicalUrl":"https://www.vivareal.com.br/condominio/present-alphaville-alphaville-id-6ad8eb6a-e5a8/","showOnlyBody":false,"aldoApiEndpoint":"https://api-aldo.vivareal.com.br","clickstreamTrackerEndpoint":"https://tracking.vivareal.com/events/v2","cdnPath":"https://cdn1.vivareal.com/p/14483-4ce4541/v/static","jsPageAttributes":{"portalContext":"prod","glueApiEndpoint":"https://glue-api.vivareal.com","aldoApiEndpoint":"https://api-aldo.vivareal.com.br","accountApiEndpoint":"https://account-api.grupozap.com","percivalApiEndpoint":"https://growth.percival.vivareal.io","myAccountApiEndpoint":"https://my-account-api.vivareal.com.br","accountLoginUrl":"https://account-api.grupozap.com/oauth/authorize?response_type=code&source=vivareal&client_id=site&redirect_uri=https://my-account-api.vivareal.com.br/user/login?state=","loginUrl":"https://account-api.grupozap.com/oauth/authorize?response_type=code&source=vivareal&client_id=site&redirect_uri=https%3A%2F%2Fmy-account-api.vivareal.com.br%2Fuser%2Flogin%3Fstate%3D","cdnPath":"https://cdn1.vivareal.com/p/14483-4ce4541/v/static"},"googleAnalytics":{"account":"UA-126375-31","companyTrackerAccount":"UA-55331766-1","companyTrackerName":"companyTracker","vrTestTrackerAccount":"UA-76616191-1","vrTestTrackerName":"vrTestTracker","webToLeadTrackerAccount":"UA-126375-71","webToLeadTrackerName":"webToLeadTracker"},"featureToggle":{"dfp":true,"condo_map":true,"tmpNewScriptLoad":true,"login_url_encode":true,"vivapro_maintenance":false,"results_map":true,"split_test_google_like":true,"frontend_sentry":true,"newrelic":true,"verified_publisher":true,"phone_leads":true,"condo_price_history":true,"aldo":false,"googleTagManager":true,"phone_postlead":true,"mktcampaign_teaser":false,"HistNavWrite":false,"split_test_grid_visualization":false,"streets_suggestions":true,"pdpTopRecommendation":true,"nps":true,"vivapro_online_subscription":false,"avm_pagamento":false,"mktcampaign_pdp":false,"pdp_new_layout":false,"mktcampaign_menu":false,"aldo_spin":true,"crazyegg":false,"decision_tree_lead_form":true,"pois_school_data":true,"capitaoLogin":true,"google_optimize":true,"development_highlight":true,"login_capitao":true,"map_with_pois":true,"branch_lead_sms":false,"capitaoZapWa":true,"new_find_by_id":true,"capitaoIntranet":true,"bacon":false,"rp_see_phone":true,"condo_new_catalog_list":true,"minha_casa_minha_vida":true,"googleAnalytics":true,"vivapro_hide_hotlead":true,"styleguide":false,"amplitude":false,"mktcampaign_rp":false,"capitaoApi":true,"user_recommendations":true,"go_page_hiding":false,"HistNavRead":false,"favoriteNewStack":true},"featureToggle-json":"[{\"enabled\":true,\"groups\":[\"site\"],\"id\":7,\"feature\":\"dfp\"},{\"enabled\":true,\"groups\":[\"site\"],\"id\":62,\"feature\":\"condo_map\"},{\"enabled\":true,\"groups\":[\"site\"],\"id\":54,\"feature\":\"tmpNewScriptLoad\"},{\"enabled\":true,\"groups\":[\"site\"],\"id\":3001,\"feature\":\"login_url_encode\"},{\"enabled\":false,\"groups\":[\"vivapro\"],\"id\":1002,\"feature\":\"vivapro_maintenance\"},{\"enabled\":true,\"groups\":[\"site\"],\"id\":135,\"feature\":\"results_map\"},{\"enabled\":true,\"groups\":[\"site\"],\"id\":139,\"feature\":\"split_test_google_like\"},{\"enabled\":true,\"groups\":[\"site\"],\"id\":10,\"feature\":\"frontend_sentry\"},{\"enabled\":true,\"groups\":[\"site\"],\"id\":31,\"feature\":\"newrelic\"},{\"enabled\":true,\"groups\":[\"site\"],\"id\":58,\"feature\":\"verified_publisher\"},{\"enabled\":true,\"groups\":[\"site\"],\"id\":720,\"feature\":\"phone_leads\"},{\"enabled\":true,\"groups\":[\"site\"],\"id\":65,\"feature\":\"condo_price_history\"},{\"enabled\":false,\"groups\":[\"site\"],\"id\":123,\"feature\":\"aldo\"},{\"enabled\":true,\"groups\":[\"site\"],\"id\":2,\"feature\":\"googleTagManager\"},{\"enabled\":true,\"groups\":[\"site\"],\"id\":21,\"feature\":\"phone_postlead\"},{\"enabled\":false,\"groups\":[\"site\"],\"id\":14,\"feature\":\"mktcampaign_teaser\"},{\"enabled\":false,\"groups\":[\"login\",\"zap\"],\"id\":2003,\"feature\":\"HistNavWrite\"},{\"enabled\":false,\"groups\":[\"site\"],\"id\":138,\"feature\":\"split_test_grid_visualization\"},{\"enabled\":true,\"groups\":[\"site\"],\"id\":142,\"feature\":\"streets_suggestions\"},{\"enabled\":true,\"groups\":[\"site\"],\"id\":25,\"feature\":\"pdpTopRecommendation\"},{\"enabled\":true,\"groups\":[\"site\"],\"id\":53,\"feature\":\"nps\"},{\"enabled\":false,\"groups\":[\"vivapro\"],\"id\":1001,\"feature\":\"vivapro_online_subscription\"},{\"enabled\":false,\"groups\":[\"zap_api\"],\"id\":2000,\"feature\":\"avm_pagamento\"},{\"enabled\":false,\"groups\":[\"site\"],\"id\":16,\"feature\":\"mktcampaign_pdp\"},{\"enabled\":false,\"groups\":[\"site\"],\"id\":143,\"feature\":\"pdp_new_layout\"},{\"enabled\":false,\"groups\":[\"site\"],\"id\":17,\"feature\":\"mktcampaign_menu\"},{\"enabled\":true,\"groups\":[\"site\"],\"id\":133,\"feature\":\"aldo_spin\"},{\"enabled\":false,\"groups\":[\"site\"],\"id\":6,\"feature\":\"crazyegg\"},{\"enabled\":true,\"groups\":[\"site\"],\"id\":66,\"feature\":\"decision_tree_lead_form\"},{\"enabled\":true,\"groups\":[\"site\"],\"id\":63,\"feature\":\"pois_school_data\"},{\"enabled\":true,\"groups\":[\"login\",\"zap\"],\"id\":999,\"feature\":\"capitaoLogin\"},{\"enabled\":true,\"groups\":[\"site\"],\"id\":59,\"feature\":\"google_optimize\"},{\"enabled\":true,\"groups\":[\"site\"],\"id\":137,\"feature\":\"development_highlight\"},{\"enabled\":true,\"groups\":[\"anuncie\"],\"id\":3000,\"feature\":\"login_capitao\"},{\"enabled\":true,\"groups\":[\"site\"],\"id\":61,\"feature\":\"map_with_pois\"},{\"enabled\":false,\"groups\":[\"site\"],\"id\":134,\"feature\":\"branch_lead_sms\"},{\"enabled\":true,\"groups\":[\"login\",\"zap\"],\"id\":2002,\"feature\":\"capitaoZapWa\"},{\"enabled\":true,\"groups\":[\"site\"],\"id\":42,\"feature\":\"new_find_by_id\"},{\"enabled\":true,\"groups\":[\"login\"],\"id\":998,\"feature\":\"capitaoIntranet\"},{\"enabled\":false,\"groups\":[\"site\"],\"id\":1,\"feature\":\"bacon\"},{\"enabled\":true,\"groups\":[\"site\"],\"id\":144,\"feature\":\"rp_see_phone\"},{\"enabled\":true,\"groups\":[\"site\"],\"id\":64,\"feature\":\"condo_new_catalog_list\"},{\"enabled\":true,\"groups\":[\"site\"],\"id\":2005,\"feature\":\"minha_casa_minha_vida\"},{\"enabled\":true,\"groups\":[\"site\"],\"id\":5,\"feature\":\"googleAnalytics\"},{\"enabled\":true,\"groups\":[\"vivapro\"],\"id\":1003,\"feature\":\"vivapro_hide_hotlead\"},{\"enabled\":false,\"groups\":[\"internal\"],\"id\":24,\"feature\":\"styleguide\"},{\"enabled\":false,\"groups\":[\"site\"],\"id\":30,\"feature\":\"amplitude\"},{\"enabled\":false,\"groups\":[\"site\"],\"id\":15,\"feature\":\"mktcampaign_rp\"},{\"enabled\":true,\"groups\":[\"login\",\"zap\"],\"id\":2001,\"feature\":\"capitaoApi\"},{\"enabled\":true,\"groups\":[\"site\"],\"id\":67,\"feature\":\"user_recommendations\"},{\"enabled\":false,\"groups\":[\"site\"],\"id\":11,\"feature\":\"go_page_hiding\"},{\"enabled\":false,\"groups\":[\"login\",\"zap\"],\"id\":2004,\"feature\":\"HistNavRead\"},{\"enabled\":true,\"groups\":[\"site\"],\"id\":3003,\"feature\":\"favoriteNewStack\"}]","glossary":{"items":{"amenity":{"items":{"Amenity_NONE":{"singular":"Não informado","plural":"Não informados"},"SECURITY_24_HOURS":{"singular":"Segurança 24h","plural":"Segurança 24h"},"ALARM_SYSTEM":{"singular":"Sistema de alarme","plural":"Sistemas de alarme"},"FIREPLACE":{"singular":"Lareira","plural":"Lareiras"},"DEPOSIT":{"singular":"Depósito","plural":"Depósitos"},"INTERCOM":{"singular":"Interfone","plural":"Interfones"},"GATED_COMMUNITY":{"singular":"Condomínio fechado","plural":"Condomínios fechados"},"BARBECUE_GRILL":{"singular":"Churrasqueira","plural":"Churrasqueiras"},"ELEVATOR":{"singular":"Elevador","plural":"Elevadores"},"GYM":{"singular":"Academia","plural":"Academias"},"POOL":{"singular":"Piscina","plural":"Piscinas"},"SPORTS_COURT":{"singular":"Quadra poliesportiva","plural":"Quadras poliesportivas"},"GARDEN":{"singular":"Jardim","plural":"Jardins"},"GOURMET_SPACE":{"singular":"Espaço gourmet","plural":"Espaços gourmet"},"PLAYGROUND":{"singular":"Playground","plural":"Playgrounds"},"PARTY_HALL":{"singular":"Salão de festas","plural":"Salões de festas"},"NUMBER_OF_FLOORS":{"singular":"Mais de um andar","plural":"Mais de um andar"},"NEAR_ACCESS_ROADS":{"singular":"Perto de vias de acesso","plural":"Perto de vias de acesso"},"ELECTRIC_GENERATOR":{"singular":"Gerador elétrico","plural":"Geradores elétricos"},"PAY_PER_USE_SERVICES":{"singular":"Serviços pay per use","plural":"Serviços pay per use"},"TEEN_SPACE":{"singular":"Espaço teen","plural":"Espaços teen"},"FULL_CABLING":{"singular":"Cabeamento estruturado","plural":"Cabeamentos estruturados"},"CABLE_TV":{"singular":"TV a cabo","plural":"TVs a cabo"},"HOME_CINEMA":{"singular":"Cinema","plural":"Cinemas"},"TENNIS_COURT":{"singular":"Quadra de tênis","plural":"Quadras de tênis"},"NEAR_PUBLIC_TRANSPORT":{"singular":"Próximo a transporte público","plural":"Próximo a transporte público"},"SAFETY_CIRCUIT":{"singular":"Circuito de segurança","plural":"Circuitos de segurança"},"NEAR_SCHOOL":{"singular":"Próximo a escola","plural":"Próximo a escola"},"GREEN_SPACE":{"singular":"Espaço verde / Parque","plural":"Espaços verde / Parques"},"NEAR_SHOPPING_CENTER":{"singular":"Próximo a shopping","plural":"Próximo a shopping"},"ADULT_POOL":{"singular":"Piscina para adulto","plural":"Piscinas para adultos"},"CHILDRENS_POOL":{"singular":"Piscina infantil","plural":"Piscinas infantis"},"CINEMA":{"singular":"Cinema","plural":"Cinemas"},"ADULT_GAME_ROOM":{"singular":"Salão de jogos","plural":"Salões de jogos"},"YOUTH_GAME_ROOM":{"singular":"Salão de jogos","plural":"Salões de jogos"},"RECEPTION":{"singular":"Recepção","plural":"Recepções"},"MASSAGE":{"singular":"Sala de massagem","plural":"Salas de massagem"},"GARAGE_BAND":{"singular":"Garage band","plural":"Garage bands"},"SAUNA":{"singular":"Sauna","plural":"Saunas"},"ESSENTIAL_PUBLIC_SERVICES":{"singular":"Serviços públicos essenciais","plural":"Serviços públicos essenciais"},"HIKING_TRAIL":{"singular":"Pista de cooper","plural":"Pistas de cooper"},"SPA":{"singular":"Spa","plural":"Spas"},"SQUASH":{"singular":"Quadra de squash","plural":"Quadras de squash"},"WATCHMAN":{"singular":"Vigia","plural":"Vigias"},"REFLECTING_POOL":{"singular":"Espelhos d'água","plural":"Espelhos d'água"},"INTERNET_ACCESS":{"singular":"Conexão à internet","plural":"Conexões à internet"},"GARAGE":{"singular":"Garagem","plural":"Garagens"},"LAUNDRY":{"singular":"Lavanderia","plural":"Lavanderias"},"KITCHEN":{"singular":"Cozinha","plural":"Cozinhas"},"BACKYARD":{"singular":"Quintal","plural":"Quintais"},"BALCONY":{"singular":"Varanda","plural":"Varandas"},"AIR_CONDITIONING":{"singular":"Ar-condicionado","plural":"Ares-condicionado"},"FURNISHED":{"singular":"Mobiliado","plural":"Mobiliados"},"SERVICE_AREA":{"singular":"Área de serviço","plural":"Áreas de serviço"},"NEAR_HOSPITAL":{"singular":"Próximo a hospitais","plural":"Próximo a hospitais"},"EXTERIOR_VIEW":{"singular":"Vista exterior","plural":"Vistas exteriores"},"HEATING":{"singular":"Aquecimento","plural":"Aquecimentos"},"SEA_VIEW":{"singular":"Vista para o mar","plural":"Vistas para o mar"},"MOUNTAIN_VIEW":{"singular":"Vista para a montanha","plural":"Vistas para a montanha"},"LAKE_VIEW":{"singular":"Vista para lago","plural":"Vistas para lago"},"GOURMET_BALCONY":{"singular":"Varanda gourmet","plural":"Varandas gourmet"},"CEMENT":{"singular":"Cimento","plural":"Cimentos"},"GRAVEL":{"singular":"Cascalho","plural":"Cascalhos"},"PLAYGROUND_2":{"singular":"Playground","plural":"Playgrounds"},"GRASS":{"singular":"Gramado","plural":"Gramados"},"HOME_OFFICE":{"singular":"Escritório","plural":"Escritórios"},"NEAR_SHOPPING_CENTER_2":{"singular":"Próximo a shopping","plural":"Próximo a shopping"},"LAND":{"singular":"Terra","plural":"Terras"},"PETS_ALLOWED":{"singular":"Aceita animais","plural":"Aceitam animais"},"DISABLED_ACCESS":{"singular":"Acesso para deficientes","plural":"Acessos para deficientes"},"INTEGRATED_ENVIRONMENTS":{"singular":"Ambientes integrados","plural":"Ambientes integrados"},"FULL_FLOOR":{"singular":"Andar inteiro","plural":"Andares inteiros"},"AQUARIUM":{"singular":"Aquário","plural":"Aquários"},"RECREATION_AREA":{"singular":"Área de lazer","plural":"Áreas de lazer"},"SANDY":{"singular":"Arenoso","plural":"Arenosos"},"ARGILLOSE":{"singular":"Argiloso","plural":"Argilosos"},"KITCHEN_CABINETS":{"singular":"Armário na cozinha","plural":"Armários na cozinha"},"BUILTIN_WARDROBE":{"singular":"Armário embutido","plural":"Armários embutidos"},"BEDROOM_WARDROBE":{"singular":"Armário embutido no quarto","plural":"Armários embutidos no quarto"},"BATHROOM_CABINETS":{"singular":"Armário no banheiro","plural":"Armários nos banheiros"},"FRUIT_TREES":{"singular":"Árvore frutífera","plural":"Árvores frutíferas"},"TREE_CLIMBING":{"singular":"Arvorismo","plural":"Arvorismo"},"BATHTUB":{"singular":"Banheira","plural":"Banheiras"},"SERVICE_BATHROOM":{"singular":"Banheiro de serviço","plural":"Banheiros de serviço"},"BAR":{"singular":"Bar","plural":"Bares"},"POOL_BAR":{"singular":"Bar na piscina","plural":"Bares nas piscinas"},"LIBRARY":{"singular":"Biblioteca","plural":"Bibliotecas"},"BICYCLES_PLACE":{"singular":"Bicicletário","plural":"Bicicletários"},"BLINDEX_BOX":{"singular":"Box blindex","plural":"Box blindex"},"TOYS_PLACE":{"singular":"Brinquedoteca","plural":"Brinquedotecas"},"SECURITY_CAMERA":{"singular":"Câmera de segurança","plural":"Câmeras de segurança"},"FOOTBALL_FIELD":{"singular":"Campo de futebol","plural":"Campos de futebol"},"GOLF_FIELD":{"singular":"Campo de golfe","plural":"Campos de golfe"},"DOG_KENNEL":{"singular":"Canil","plural":"Canis"},"CARPET":{"singular":"Carpete","plural":"Carpetes"},"CARETAKER_HOUSE":{"singular":"Casa de caseiro","plural":"Casas de caseiro"},"BACKGROUND_HOUSE":{"singular":"Casa de fundo","plural":"Casas de fundo"},"HEADQUARTERS":{"singular":"Casa sede","plural":"Casas sede"},"BARN":{"singular":"Celeiro","plural":"Celeiros"},"BEAUTY_CENTER":{"singular":"Centro de estética","plural":"Centros de estética"},"FENCE":{"singular":"Cerca","plural":"Cercas"},"CHILDREN_CARE":{"singular":"Children care","plural":"Children care"},"BARBECUE_BALCONY":{"singular":"Churrasqueira na varanda","plural":"Churrasqueiras na varanda"},"GAS_SHOWER":{"singular":"Chuveiro a gás","plural":"Chuveiros a gás"},"BURNT_CEMENT":{"singular":"Cimento queimado","plural":"Cimentos queimado"},"CLOSET":{"singular":"Closet","plural":"Closets"},"COVERAGE":{"singular":"Cobertura coletiva","plural":"Coberturas coletivas"},"COFFEE_SHOP":{"singular":"Coffee shop","plural":"Coffee shop"},"COPA":{"singular":"Copa","plural":"Copas"},"COWORKING":{"singular":"Coworking","plural":"Coworking"},"AMERICAN_KITCHEN":{"singular":"Cozinha americana","plural":"Cozinhas americanas"},"GOURMET_KITCHEN":{"singular":"Cozinha gourmet","plural":"Cozinhas gourmet"},"LARGE_KITCHEN":{"singular":"Cozinha grande","plural":"Cozinhas grandes"},"CORRAL":{"singular":"Curral","plural":"Currais"},"DECK":{"singular":"Deck","plural":"Decks"},"EMPLOYEE_DEPENDENCY":{"singular":"Dependência de empregados","plural":"Dependências de empregados"},"ACLIVE":{"singular":"Desnível para frente (rua)","plural":"Desniveis para frente (rua)"},"DECLIVE":{"singular":"Desnível para trás (fundo)","plural":"Desniveis para trás (fundo)"},"PANTRY":{"singular":"Despensa","plural":"Despensas"},"DRYWALL":{"singular":"Drywall","plural":"Drywalls"},"EDICULE":{"singular":"Edícula","plural":"Edículas"},"ELECTRICITY":{"singular":"Energia elétrica","plural":"Energias elétricas"},"SERVICE_ENTRANCE":{"singular":"Entrada de serviço","plural":"Entradas de serviço"},"SIDE_ENTRANCE":{"singular":"Entrada lateral","plural":"Entradas laterais"},"TRUCK_ENTRANCE":{"singular":"Entrada para caminhões","plural":"Entradas para caminhões"},"STAIR":{"singular":"Escada","plural":"Escadas"},"PET_SPACE":{"singular":"Espaço Pet","plural":"Espaços Pet"},"ZEN_SPACE":{"singular":"Espaço zen","plural":"Espaços zen"},"PARKING":{"singular":"Estacionamento ","plural":"Estacionamentos"},"GUEST_PARKING":{"singular":"Estacionamento para visitantes","plural":"Estacionamento para visitantes"},"COOKER":{"singular":"Fogão","plural":"Fogões"},"PIZZA_OVEN":{"singular":"Forno de pizza","plural":"Fornos de pizza"},"FREEZER":{"singular":"Freezer","plural":"Freezers"},"EAST_FACING":{"singular":"Frente para o leste","plural":"Frentes para o leste"},"NORTH_FACING":{"singular":"Frente para o norte","plural":"Frentes para o norte"},"WEST_FACING":{"singular":"Frente para o oeste","plural":"Frentes para o oeste"},"SOUTH_FACING":{"singular":"Frente para o sul","plural":"Frentes para o sul"},"PLATED_GAS":{"singular":"Gás Encanado","plural":"Gás Encanado"},"GEMINADA":{"singular":"Geminada","plural":"Geminadas"},"SANCA":{"singular":"Gesso - Sanca - Teto Rebaixado","plural":"Gessos - Sancas - Tetos Rebaixados"},"SECURITY_CABIN":{"singular":"Guarita","plural":"Guaritas"},"ENTRANCE_HALL":{"singular":"Hall de entrada","plural":"Halls de entrada"},"HELIPAD":{"singular":"Heliponto","plural":"Helipontos"},"WHIRLPOOL":{"singular":"Hidromassagem","plural":"Hidromassagens"},"VEGETABLE_GARDEN":{"singular":"Horta","plural":"Hortas"},"CORNER_PROPERTY":{"singular":"Imóvel de esquina","plural":"Imóveis de esquina"},"SOUNDPROOFING":{"singular":"Isolamento acústico","plural":"Isolamentos acústicos"},"THERMAL_INSULATION":{"singular":"Isolamento térmico","plural":"Isolamentos térmicos"},"ALUMINUM_WINDOW":{"singular":"Janela de alumínio","plural":"Janelas de alumínio"},"LARGE_WINDOW":{"singular":"Janela grande","plural":"Janelas grandes"},"LAKE":{"singular":"Lago","plural":"Lagos"},"SLAB":{"singular":"Laje","plural":"Lajes"},"LAVABO":{"singular":"Lavabo","plural":"Lavabos"},"MARINA":{"singular":"Marina","plural":"Marinas"},"HALF_FLOOR":{"singular":"Meio andar","plural":"Meio andar"},"MEZZANINE":{"singular":"Mezanino","plural":"Mezaninos"},"MINI_SQUARE":{"singular":"Mini quadra","plural":"Mini quadras"},"PLANNED_FURNITURE":{"singular":"Móvel planejado","plural":"Móveis planejados"},"CLIMBING_WALL":{"singular":"Muro de escalada","plural":"Muros de escalada"},"GLASS_WALL":{"singular":"Muro de vidro","plural":"Muros de vidro"},"WALLS_GRIDS":{"singular":"Muro e grade","plural":"Muros e grades"},"HOT_TUB":{"singular":"Ofurô","plural":"Ofurôs"},"ORCHID_PLACE":{"singular":"Orquidário","plural":"Orquidários"},"PASTURE":{"singular":"Pasto","plural":"Pastos"},"HIGH_CEILING_HEIGHT":{"singular":"Pé direito alto","plural":"Pés direitos altos"},"HEATED_POOL":{"singular":"Piscina aquecida","plural":"Piscinas aquecidas"},"COVERED_POOL":{"singular":"Piscina coberta","plural":"Piscinas cobertas"},"PRIVATE_POOL":{"singular":"Piscina privativa","plural":"Piscinas privativas"},"WOOD_FLOOR":{"singular":"Piso de madeira","plural":"Pisos de madeira"},"RAISED_FLOOR":{"singular":"Piso elevado","plural":"Pisos elevados"},"COLD_FLOOR":{"singular":"Piso frio","plural":"Pisos frios"},"LAMINATED_FLOOR":{"singular":"Piso laminado","plural":"Pisos laminados"},"VINYL_FLOOR":{"singular":"Piso vinílico","plural":"Pisos vinílicos"},"SKATE_LANE":{"singular":"Pista de skate","plural":"Pistas de skate"},"PLAN":{"singular":"Plano","plural":"Planos"},"PLATIBANDA":{"singular":"Platibanda","plural":"Platibandas"},"WELL":{"singular":"Poço","plural":"Poços"},"ARTESIAN_WELL":{"singular":"Poço artesiano","plural":"Poços artesianos"},"POMAR":{"singular":"Pomar","plural":"Pomares"},"PORCELAIN":{"singular":"Porcelanato","plural":"Porcelanatos"},"ELECTRONIC_GATE":{"singular":"Portão eletrônico","plural":"Portões eletrônicos"},"CONCIERGE_24H":{"singular":"Portaria 24h","plural":"Portarias 24h"},"DIVIDERS":{"singular":"Possui divisória","plural":"Possui divisórias"},"SQUARE":{"singular":"Praça","plural":"Praças"},"INDOOR_SOCCER":{"singular":"Quadra de futebol de salão","plural":"Quadras de futebol de salão"},"SERVICE_ROOM":{"singular":"Quarto de serviço","plural":"Quartos de serviços"},"REVERSIBLE_ROOM":{"singular":"Quarto extra reversível","plural":"Quartos extra reversiveis"},"RAMP":{"singular":"Rampa","plural":"Rampas"},"REDARIO":{"singular":"Redario","plural":"Redarios"},"SEWAGE":{"singular":"Rede de água e esgoto","plural":"Redes de água e esgoto"},"REFECTORY":{"singular":"Refeitório","plural":"Refeitórios"},"WATER_TANK":{"singular":"Reservatório de água","plural":"Reservatórios de água"},"RESTAURANT":{"singular":"Restaurante","plural":"Restaurantes"},"RIVER":{"singular":"Rio","plural":"Rios"},"PATROL":{"singular":"Ronda/Vigilância","plural":"Rondas/Vigilâncias"},"PAVED_STREET":{"singular":"Rua asfaltada","plural":"Ruas asfaltadas"},"LUNCH_ROOM":{"singular":"Sala de almoço","plural":"Salas de almoço"},"DINNER_ROOM":{"singular":"Sala de jantar","plural":"Salas de jantar"},"MASSAGE_ROOM":{"singular":"Sala de massagem","plural":"Salas de massagem"},"MEETING_ROOM":{"singular":"Sala de reunião","plural":"Salas de reuniões"},"LARGE_ROOM":{"singular":"Sala grande","plural":"Salas grandes"},"SMALL_ROOM":{"singular":"Sala pequena","plural":"Salas pequenas"},"COVENTION_HALL":{"singular":"Salão de convenção","plural":"Salões de convenções"},"GAMES_ROOM":{"singular":"Salão de jogos","plural":"Salões de jogos"},"SOLARIUM":{"singular":"Solarium","plural":"Solariuns"},"WALL_BALCONY":{"singular":"Varanda fechada com vidro","plural":"Varandas fechadas com vidro"},"NATURAL_VENTILATION":{"singular":"Ventilação natural","plural":"Ventilações naturais"},"DRESS_ROOM":{"singular":"Vestiário","plural":"Vestiários"},"DRESS_ROOM2":{"singular":"Vestiário para diaristas","plural":"Vestiários para diaristas"},"PANORAMIC_VIEW":{"singular":"Vista panorâmica","plural":"Vistas panorâmicas"}}},"businessType":{"items":{"BusinessType_NONE":{"singular":"Não informado","plural":"Não informados"},"RENTAL":{"singular":"Aluguel","plural":"Aluguéis"},"SALE":{"singular":"Venda","plural":"Vendas"}}},"constructionStatus":{"items":{"ConstructionStatus_NONE":{"singular":"Não informado","plural":"Não informados"},"PLAN_ONLY":{"singular":"Na planta","plural":"Na planta"},"UNDER_CONSTRUCTION":{"singular":"Em construção","plural":"Em construção"},"BUILT":{"singular":"Pronto para morar","plural":"Prontos para morar"}}},"displayAddress":{"items":{"DisplayAddress_NONE":{"singular":"Não informado","plural":"Não informados"},"ALL":{"singular":"Endereço completo","plural":"Endereços completo"},"STREET":{"singular":"Apenas rua","plural":"Apenas ruas"},"NEIGHBORHOOD":{"singular":"Apenas bairro","plural":"Apenas bairros"}}},"listingStatus":{"items":{"ListingStatus_NONE":{"singular":"Não informado","plural":"Não informados"},"DRAFT":{"singular":"Rascunho","plural":"Rascunhos"},"ACTIVE":{"singular":"Ativo","plural":"Ativos"},"INACTIVE":{"singular":"Inativo","plural":"Inativos"},"BLOCKED":{"singular":"Bloqueado","plural":"Bloqueados"}}},"listingType":{"items":{"ListingType_NONE":{"singular":"Não informado","plural":"Não informados"},"USED":{"singular":"Imóvel usado","plural":"Imóveis usados"},"DEVELOPMENT":{"singular":"Lançamento","plural":"Lançamentos"}}},"period":{"items":{"Period_NONE":{"singular":"Não informado","plural":"Não informados"},"DAILY":{"singular":"Diário","plural":"Diários"},"WEEKLY":{"singular":"Semanal","plural":"Semanais"},"MONTHLY":{"singular":"Mensal","plural":"Mensais"},"YEARLY":{"singular":"Anual","plural":"Anuais"}}},"promotionPublicationType":{"items":{"PromotionPublicationType_NONE":{"singular":"Não informado","plural":"Não informados"},"STANDARD":{"singular":"Padrão","plural":"Padrões"},"PREMIUM":{"singular":"Destaque","plural":"Destaques"},"SOLD_OUT":{"singular":"Esgotado","plural":"Esgotados"}}},"promotionStatus":{"items":{"PromotionStatus_NONE":{"singular":"Não informado","plural":"Não informados"},"ACTIVE":{"singular":"Ativa","plural":"Ativas"},"INACTIVE":{"singular":"Inativa","plural":"Inativas"}}},"propertyType":{"items":{"PropertyType_NONE":{"singular":"Não informado","plural":"Não informados"},"CONDOMINIUM":{"singular":"Condomínio","plural":"Condomínios"},"UNIT":{"singular":"Unidade","plural":"Unidades"}}},"publicationType":{"items":{"PublicationType_NONE":{"singular":"Não informado","plural":"Não informados"},"PREMIUM":{"singular":"Destaque","plural":"Destaques"},"PREMIUM_FEED":{"singular":"Destaque","plural":"Destaques"},"STANDARD":{"singular":"Padrão","plural":"Padrões"}}},"unitType":{"items":{"UnitType_NONE":{"singular":"Não informado","plural":"Não informados"},"APARTMENT":{"singular":"Apartamento","plural":"Apartamentos"},"TWO_STORY_HOUSE":{"singular":"Sobrado","plural":"Sobrados"},"DUPLEX":{"singular":"Duplex","plural":"Duplex"},"TRIPLEX":{"singular":"Triplex","plural":"Triplex"},"LOFT":{"singular":"Loft","plural":"Lofts"},"FLAT":{"singular":"Flat","plural":"Flats"},"KITNET":{"singular":"Kitnet/Conjugado","plural":"Kitnets/Conjugados"},"HOME":{"singular":"Casa","plural":"Casas"},"CONDOMINIUM":{"singular":"Casa de condomínio","plural":"Casas de condomínio"},"VILLAGE_HOUSE":{"singular":"Vila/Rua Particular","plural":"Vilas/Ruas Particulares"},"PENTHOUSE":{"singular":"Cobertura","plural":"Coberturas"},"RESIDENTIAL_ALLOTMENT_LAND":{"singular":"Lote/Terreno","plural":"Lotes/Terrenos"},"COMMERCIAL_ALLOTMENT_LAND":{"singular":"Lote/Terreno","plural":"Lotes/Terrenos"},"ALLOTMENT_LAND":{"singular":"Lote/Terreno","plural":"Lotes/Terrenos"},"OFFICE":{"singular":"Sala/Conjunto","plural":"Salas/Conjuntos"},"SHED_DEPOSIT_WAREHOUSE":{"singular":"Galpão/Depósito/Armazém","plural":"Galpões/Depósitos/Armazéns"},"STORE":{"singular":"Loja","plural":"Lojas"},"HOTEL":{"singular":"Hotel/Motel/Pousada","plural":"Hotéis/Motéis/Pousadas"},"COMMERCIAL_BUILDING":{"singular":"Prédio comercial","plural":"Prédios comerciais"},"CLINIC":{"singular":"Consultório","plural":"Consultórios"},"BUSINESS":{"singular":"Ponto comercial/Loja/Box","plural":"Pontos comerciais/Lojas/Boxes"},"COUNTRY_HOUSE":{"singular":"Chácara","plural":"Chácaras"},"FARM":{"singular":"Fazenda/Sítio","plural":"Fazendas/Sítios"},"COMMERCIAL_PROPERTY":{"singular":"Imóvel comercial","plural":"Imóveis comerciais"},"RESIDENTIAL_BUILDING":{"singular":"Edifício residencial","plural":"Edifícios residenciais"},"PARKING_SPACE":{"singular":"Garagem","plural":"Garagens"},"FLOOR":{"singular":"Andar/Laje corporativa","plural":"Andares/Lajes corporativas"}}},"unitSubType":{"items":{"UnitSubType_NONE":{"singular":"Não informado","plural":"Não informados"},"RETAIL_CENTER":{"singular":"Centro comercial","plural":"Centros comerciais"},"PENTHOUSE":{"singular":"Cobertura","plural":"Coberturas"},"CONDOMINIUM":{"singular":"Condominio","plural":"Condominios"},"CLINIC":{"singular":"Consultório","plural":"Consultórios"},"DUPLEX":{"singular":"Duplex","plural":"Duplex"},"OFFICE":{"singular":"Escritório","plural":"Escritórios"},"FLAT":{"singular":"Flat","plural":"Flats"},"GALLERY":{"singular":"Galeria","plural":"Galerias"},"LOFT":{"singular":"Loft","plural":"Lofts"},"SHOPPING":{"singular":"Shopping","plural":"Shoppings"},"TWO_STORY_HOUSE":{"singular":"Sobrado","plural":"Sobrados"},"STUDIO":{"singular":"Studio","plural":"Studios"},"TRIPLEX":{"singular":"Triplex","plural":"Triplex"},"SINGLE_STOREY_HOUSE":{"singular":"Térrea","plural":"Térreas"},"VILLAGE_HOUSE":{"singular":"Vila/Rua Particular","plural":"Vilas/Ruas Particulares"}}},"state":{"items":{"AC":{"singular":"Acre"},"AL":{"singular":"Alagoas"},"AP":{"singular":"Amapá"},"AM":{"singular":"Amazonas"},"BA":{"singular":"Bahia"},"CE":{"singular":"Ceará"},"DF":{"singular":"Distrito Federal"},"ES":{"singular":"Espírito Santo"},"GO":{"singular":"Goiás"},"MA":{"singular":"Maranhão"},"MT":{"singular":"Mato Grosso"},"MS":{"singular":"Mato Grosso do Sul"},"MG":{"singular":"Minas Gerais"},"PA":{"singular":"Pará"},"PB":{"singular":"Paraíba"},"PR":{"singular":"Paraná"},"PE":{"singular":"Pernambuco"},"PI":{"singular":"Piauí"},"RJ":{"singular":"Rio de Janeiro"},"RN":{"singular":"Rio Grande do Norte"},"RS":{"singular":"Rio Grande do Sul"},"RO":{"singular":"Rondônia"},"RR":{"singular":"Roraima"},"SC":{"singular":"Santa Catarina"},"SP":{"singular":"São Paulo"},"SE":{"singular":"Sergipe"},"TO":{"singular":"Tocantins"}}}}},"salePriceFrom":{"price":593681,"period":null},"rentalPriceFrom":{"price":4000,"period":"MONTHLY"},"areaFrom":85,"areaTo":112,"bedroomsFrom":2,"bedroomsTo":3,"bathroomsFrom":2,"bathroomsTo":2,"parkingSpacesFrom":2,"parkingSpacesTo":2}}
      )
    }
  
    function getGoogleAnalyticsSettings () {
      return {
        ga: {
            account: 'UA-126375-31',
            companyTrackerAccount: 'UA-55331766-1',
            companyTrackerName: 'companyTracker',
            vrTestTrackerAccount: 'UA-76616191-1',
            vrTestTrackerName: 'vrTestTracker',
            webToLeadTrackerAccount: 'UA-126375-71',
            webToLeadTrackerName: 'webToLeadTracker',
        }
      }
    }
  
      function configureSentry (env) {
        if (env !== 'prod') return
  
        Raven.config('https://f47ae0f379404d47b210578238b7f3d8@sentry-logs.vivareal.com/13', {
          whitelistUrls: [
          /www\.vivareal\.com\.br/,
          /staging\.vivareal\.com\.br/,
          /dev\.vivareal\.com\.br/,
          /cdn\d\.vivareal\.com/
          ]
        }).install()
      }
  </script>
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "Organization",
    "name": "Viva Real",
    "description": "O Viva Real é o maior portal de imóveis no Brasil, com mais de 4 milhões de imóveis anunciados em mais de 3 mil cidades. Acesse e encontre o imóvel dos seus sonhos!",
  
    "address": {
      "@type": "PostalAddress",
      "addressCountry": {
  	    "@type": "Country",
  	    "name": "BR"
      },
      "addressLocality": "São Paulo",
      "addressRegion": "SP",
      "postalCode": "01415-001",
      "streetAddress": "Rua Bela Cintra, 539 - Consolação - São Paulo - SP"
    },
  
    "brand": {
      "@type": "Brand",
      "logo": "https://cdn1.vivareal.com/p/14483-4ce4541/v/static/svg/styleguide/logo/vivareal-5bcdffca.svg"
    },
  
    "founder": {
      "@type": "Person",
      "givenName": "Brian",
      "familyName": "Requarth",
      "jobTitle": "CEO"
    },
  
    "telephone": "+55 11 3150-4646",
    "URL": "https://www.vivareal.com.br/"
  }
  </script>

    <script>
      var googletag=googletag||{};googletag.cmd=googletag.cmd||[],function(){var a=document.createElement("script");a.async=!0,a.type="text/javascript";var b="https:"==document.location.protocol;a.src=(b?"https:":"http:")+"//www.googletagservices.com/tag/js/gpt.js";var c=document.getElementsByTagName("script")[0];c.parentNode.insertBefore(a,c)}();
    </script>
    <script>
      var _comscore=_comscore||[];_comscore.push({c1:"2",c2:"18278794"}),function(){var a=document.createElement("script"),b=document.getElementsByTagName("script")[0];a.async=!0,a.src=("https:"==document.location.protocol?"https://sb":"http://b")+".scorecardresearch.com/beacon.js",b.parentNode.insertBefore(a,b)}();
    </script>
    
    <noscript>
    	<img src="https://sb.scorecardresearch.com/p?c1=2&c2=18278794&cv=2.0&cj=1" alt="">
    </noscript>
        <noscript>
          <iframe src="//www.googletagmanager.com/ns.html?id=GTM-82BN"
            height="0" width="0" style="display:none;visibility:hidden">
          </iframe>
        </noscript>
       
       # Retirado conteudo do window.dataLayer
        <script>
          !function(a,b,c,d,e){a[d]=a[d]||[],a[d].push({"gtm.start":(new Date).getTime(),event:"gtm.js"});var f=b.getElementsByTagName(c)[0],g=b.createElement(c),h="dataLayer"!=d?"&l="+d:"";g.async=!0,g.src="//www.googletagmanager.com/gtm.js?id="+e+h,f.parentNode.insertBefore(g,f)}(window,document,"script","dataLayer","GTM-82BN");
        </script>
</body>
</html>
'''