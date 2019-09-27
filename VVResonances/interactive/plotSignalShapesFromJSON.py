





<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
  <link rel="dns-prefetch" href="https://github.githubassets.com">
  <link rel="dns-prefetch" href="https://avatars0.githubusercontent.com">
  <link rel="dns-prefetch" href="https://avatars1.githubusercontent.com">
  <link rel="dns-prefetch" href="https://avatars2.githubusercontent.com">
  <link rel="dns-prefetch" href="https://avatars3.githubusercontent.com">
  <link rel="dns-prefetch" href="https://github-cloud.s3.amazonaws.com">
  <link rel="dns-prefetch" href="https://user-images.githubusercontent.com/">



  <link crossorigin="anonymous" media="all" integrity="sha512-lEwNhIgWxFtdGboTlCciWWGiX2vG3LOojEE671oRJEhnPj6jpmgQTJtpq3O2KBzCcln6RzwfvHlyFaI/oR+RNQ==" rel="stylesheet" href="https://github.githubassets.com/assets/frameworks-849637ecbd4bd65815cc113d80fee2d4.css" />
  <link crossorigin="anonymous" media="all" integrity="sha512-J91Qhea0f13DaSjx3AXXGO3viFpQAPPnpVDE8Umc73sXEtrah52Hq277J1yN+ALwl/RwH5VQ/Ntc0756LZy/7w==" rel="stylesheet" href="https://github.githubassets.com/assets/site-d20aa35917cf810095fab7458ea2a8e4.css" />
    <link crossorigin="anonymous" media="all" integrity="sha512-nbXfO4fh1nahyjggjTnpWxGoA7FoTdx2f21d62JQeVn0RlLoYci8FX3fuqk4Sn/kD8Yuzgd/IHXroBMoxFLFWA==" rel="stylesheet" href="https://github.githubassets.com/assets/github-8fec968b4bdafcef25940c968feaf09b.css" />
    
    
    
    

  <meta name="viewport" content="width=device-width">
  
  <title>cmgtools-lite/plotSignalShapesFromJSON.py at VV_VH_workinprogress · IreneZoi/cmgtools-lite · GitHub</title>
    <meta name="description" content="CMGTools as a subsystem, not as a CMSSW overlay. Contribute to IreneZoi/cmgtools-lite development by creating an account on GitHub.">
    <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub">
  <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub">
  <meta property="fb:app_id" content="1401488693436528">

    <meta name="twitter:image:src" content="https://avatars1.githubusercontent.com/u/20553929?s=400&amp;v=4" /><meta name="twitter:site" content="@github" /><meta name="twitter:card" content="summary" /><meta name="twitter:title" content="IreneZoi/cmgtools-lite" /><meta name="twitter:description" content="CMGTools as a subsystem, not as a CMSSW overlay. Contribute to IreneZoi/cmgtools-lite development by creating an account on GitHub." />
    <meta property="og:image" content="https://avatars1.githubusercontent.com/u/20553929?s=400&amp;v=4" /><meta property="og:site_name" content="GitHub" /><meta property="og:type" content="object" /><meta property="og:title" content="IreneZoi/cmgtools-lite" /><meta property="og:url" content="https://github.com/IreneZoi/cmgtools-lite" /><meta property="og:description" content="CMGTools as a subsystem, not as a CMSSW overlay. Contribute to IreneZoi/cmgtools-lite development by creating an account on GitHub." />

  <link rel="assets" href="https://github.githubassets.com/">
  
  <meta name="pjax-timeout" content="1000">
  
  <meta name="request-id" content="87B0:433C6:3E6D8E6:5E3300A:5D8DD760" data-pjax-transient>


  

  <meta name="selected-link" value="repo_source" data-pjax-transient>

      <meta name="google-site-verification" content="KT5gs8h0wvaagLKAVWq8bbeNwnZZK1r1XQysX3xurLU">
    <meta name="google-site-verification" content="ZzhVyEFwb7w3e0-uOTltm8Jsck2F5StVihD0exw2fsA">
    <meta name="google-site-verification" content="GXs5KoUUkNCoaAZn7wPN-t01Pywp9M3sEjnt_3_ZWPc">

  <meta name="octolytics-host" content="collector.githubapp.com" /><meta name="octolytics-app-id" content="github" /><meta name="octolytics-event-url" content="https://collector.githubapp.com/github-external/browser_event" /><meta name="octolytics-dimension-request_id" content="87B0:433C6:3E6D8E6:5E3300A:5D8DD760" /><meta name="octolytics-dimension-region_edge" content="ams" /><meta name="octolytics-dimension-region_render" content="iad" /><meta name="octolytics-dimension-ga_id" content="" class="js-octo-ga-id" /><meta name="octolytics-dimension-visitor_id" content="2616476718034966368" />
<meta name="analytics-location" content="/&lt;user-name&gt;/&lt;repo-name&gt;/blob/show" data-pjax-transient="true" />



    <meta name="google-analytics" content="UA-3769691-2">


<meta class="js-ga-set" name="dimension1" content="Logged Out">



  

      <meta name="hostname" content="github.com">
    <meta name="user-login" content="">

      <meta name="expected-hostname" content="github.com">
    <meta name="js-proxy-site-detection-payload" content="ZWViN2EzM2I2NzVjOWJiNWQ3ZWVlNzBjMzRmNTRhMWUzNDBlNzQ3NjI5MTkyZWExOGNmNDAyNTg3ODNmYWUxM3x7InJlbW90ZV9hZGRyZXNzIjoiMTM3LjEzOC43Ni41NSIsInJlcXVlc3RfaWQiOiI4N0IwOjQzM0M2OjNFNkQ4RTY6NUUzMzAwQTo1RDhERDc2MCIsInRpbWVzdGFtcCI6MTU2OTU3NjgwMCwiaG9zdCI6ImdpdGh1Yi5jb20ifQ==">

    <meta name="enabled-features" content="ACTIONS_V2_ON_MARKETPLACE,MARKETPLACE_FEATURED_BLOG_POSTS,MARKETPLACE_INVOICED_BILLING,MARKETPLACE_SOCIAL_PROOF_CUSTOMERS,MARKETPLACE_TRENDING_SOCIAL_PROOF,MARKETPLACE_RECOMMENDATIONS,MARKETPLACE_PENDING_INSTALLATIONS">

  <meta name="html-safe-nonce" content="8f689307e13ee155c0f677405de144ece056f695">

  <meta http-equiv="x-pjax-version" content="26151a0489b3bba3856cd61a7a92e41f">
  

      <link href="https://github.com/IreneZoi/cmgtools-lite/commits/VV_VH_workinprogress.atom" rel="alternate" title="Recent Commits to cmgtools-lite:VV_VH_workinprogress" type="application/atom+xml">

  <meta name="go-import" content="github.com/IreneZoi/cmgtools-lite git https://github.com/IreneZoi/cmgtools-lite.git">

  <meta name="octolytics-dimension-user_id" content="20553929" /><meta name="octolytics-dimension-user_login" content="IreneZoi" /><meta name="octolytics-dimension-repository_id" content="185954683" /><meta name="octolytics-dimension-repository_nwo" content="IreneZoi/cmgtools-lite" /><meta name="octolytics-dimension-repository_public" content="true" /><meta name="octolytics-dimension-repository_is_fork" content="true" /><meta name="octolytics-dimension-repository_parent_id" content="99858396" /><meta name="octolytics-dimension-repository_parent_nwo" content="Diboson3D/cmgtools-lite" /><meta name="octolytics-dimension-repository_network_root_id" content="49954027" /><meta name="octolytics-dimension-repository_network_root_nwo" content="CERN-PH-CMG/cmgtools-lite" /><meta name="octolytics-dimension-repository_explore_github_marketplace_ci_cta_shown" content="false" />


    <link rel="canonical" href="https://github.com/IreneZoi/cmgtools-lite/blob/VV_VH_workinprogress/VVResonances/interactive/plotSignalShapesFromJSON.py" data-pjax-transient>


  <meta name="browser-stats-url" content="https://api.github.com/_private/browser/stats">

  <meta name="browser-errors-url" content="https://api.github.com/_private/browser/errors">

  <link rel="mask-icon" href="https://github.githubassets.com/pinned-octocat.svg" color="#000000">
  <link rel="icon" type="image/x-icon" class="js-site-favicon" href="https://github.githubassets.com/favicon.ico">

<meta name="theme-color" content="#1e2327">





  <link rel="manifest" href="/manifest.json" crossOrigin="use-credentials">

  </head>

  <body class="logged-out env-production page-responsive page-blob">
    

  <div class="position-relative js-header-wrapper ">
    <a href="#start-of-content" tabindex="1" class="px-2 py-4 bg-blue text-white show-on-focus js-skip-to-content">Skip to content</a>
    <div id="js-pjax-loader-bar" class="pjax-loader-bar"><div class="progress"></div></div>

    
    
    


        <header class="Header-old header-logged-out js-details-container Details position-relative f4 py-2" role="banner">
  <div class="container-lg d-lg-flex flex-items-center p-responsive">
    <div class="d-flex flex-justify-between flex-items-center">
        <a class="mr-4" href="https://github.com/" aria-label="Homepage" data-ga-click="(Logged out) Header, go to homepage, icon:logo-wordmark">
          <svg height="32" class="octicon octicon-mark-github text-white" viewBox="0 0 16 16" version="1.1" width="32" aria-hidden="true"><path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"/></svg>
        </a>

          <div class="d-lg-none css-truncate css-truncate-target width-fit p-2">
            
              <svg class="octicon octicon-repo-forked" viewBox="0 0 10 16" version="1.1" width="10" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8 1a1.993 1.993 0 0 0-1 3.72V6L5 8 3 6V4.72A1.993 1.993 0 0 0 2 1a1.993 1.993 0 0 0-1 3.72V6.5l3 3v1.78A1.993 1.993 0 0 0 5 15a1.993 1.993 0 0 0 1-3.72V9.5l3-3V4.72A1.993 1.993 0 0 0 8 1zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zm3 10c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zm3-10c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"/></svg>
    <a class="Header-link" href="/IreneZoi">IreneZoi</a>
    /
    <a class="Header-link" href="/IreneZoi/cmgtools-lite">cmgtools-lite</a>


          </div>

        <div class="d-flex flex-items-center">
            <a href="/join?source=header-repo"
              class="d-inline-block d-lg-none f5 text-white no-underline border border-gray-dark rounded-2 px-2 py-1 mr-3 mr-sm-5"
              data-hydro-click="{&quot;event_type&quot;:&quot;authentication.click&quot;,&quot;payload&quot;:{&quot;location_in_page&quot;:&quot;site header&quot;,&quot;repository_id&quot;:null,&quot;auth_type&quot;:&quot;SIGN_UP&quot;,&quot;client_id&quot;:null,&quot;originating_request_id&quot;:&quot;87B0:433C6:3E6D8E6:5E3300A:5D8DD760&quot;,&quot;originating_url&quot;:&quot;https://github.com/IreneZoi/cmgtools-lite/blob/VV_VH_workinprogress/VVResonances/interactive/plotSignalShapesFromJSON.py&quot;,&quot;referrer&quot;:null,&quot;user_id&quot;:null}}" data-hydro-click-hmac="3c2f21680458c8d2365dd29e06c690421c2c65efd86cad76dd472e370421a989"
              data-ga-click="(Logged out) Header, clicked Sign up, text:sign-up">
              Sign&nbsp;up
            </a>

          <button class="btn-link d-lg-none mt-1 js-details-target" type="button" aria-label="Toggle navigation" aria-expanded="false">
            <svg height="24" class="octicon octicon-three-bars text-white" viewBox="0 0 12 16" version="1.1" width="18" aria-hidden="true"><path fill-rule="evenodd" d="M11.41 9H.59C0 9 0 8.59 0 8c0-.59 0-1 .59-1H11.4c.59 0 .59.41.59 1 0 .59 0 1-.59 1h.01zm0-4H.59C0 5 0 4.59 0 4c0-.59 0-1 .59-1H11.4c.59 0 .59.41.59 1 0 .59 0 1-.59 1h.01zM.59 11H11.4c.59 0 .59.41.59 1 0 .59 0 1-.59 1H.59C0 13 0 12.59 0 12c0-.59 0-1 .59-1z"/></svg>
          </button>
        </div>
    </div>

    <div class="HeaderMenu HeaderMenu--logged-out position-fixed top-0 right-0 bottom-0 height-fit position-lg-relative d-lg-flex flex-justify-between flex-items-center flex-auto">
      <div class="d-flex d-lg-none flex-justify-end border-bottom bg-gray-light p-3">
        <button class="btn-link js-details-target" type="button" aria-label="Toggle navigation" aria-expanded="false">
          <svg height="24" class="octicon octicon-x text-gray" viewBox="0 0 12 16" version="1.1" width="18" aria-hidden="true"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48L7.48 8z"/></svg>
        </button>
      </div>

        <nav class="mt-0 px-3 px-lg-0 mb-5 mb-lg-0" aria-label="Global">
          <ul class="d-lg-flex list-style-none">
              <li class="d-block d-lg-flex flex-lg-nowrap flex-lg-items-center border-bottom border-lg-bottom-0 mr-0 mr-lg-3 edge-item-fix position-relative flex-wrap flex-justify-between d-flex flex-items-center ">
                <details class="HeaderMenu-details details-overlay details-reset width-full">
                  <summary class="HeaderMenu-summary HeaderMenu-link px-0 py-3 border-0 no-wrap d-block d-lg-inline-block">
                    Why GitHub?
                    <svg x="0px" y="0px" viewBox="0 0 14 8" xml:space="preserve" fill="none" class="icon-chevon-down-mktg position-absolute position-lg-relative">
                      <path d="M1,1l6.2,6L13,1"></path>
                    </svg>
                  </summary>
                  <div class="dropdown-menu flex-auto rounded-1 bg-white px-0 mt-0 pb-4 p-lg-4 position-relative position-lg-absolute left-0 left-lg-n4">
                    <a href="/features" class="py-2 lh-condensed-ultra d-block link-gray-dark no-underline h5 Bump-link--hover" data-ga-click="(Logged out) Header, go to Features">Features <span class="Bump-link-symbol float-right text-normal text-gray-light">&rarr;</span></a>
                    <ul class="list-style-none f5 pb-3">
                      <li class="edge-item-fix"><a href="/features/code-review/" class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Code review">Code review</a></li>
                      <li class="edge-item-fix"><a href="/features/project-management/" class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Project management">Project management</a></li>
                      <li class="edge-item-fix"><a href="/features/integrations" class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Integrations">Integrations</a></li>
                      <li class="edge-item-fix"><a href="/features/actions" class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Actions">Actions</a>
                          <li class="edge-item-fix"><a href="/features/package-registry" class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Package Registry">Package registry</a>

                          <li class="edge-item-fix"><a href="/features/security" class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Security">Security</a>

                      <li class="edge-item-fix"><a href="/features#team-management" class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Team management">Team management</a></li>
                      <li class="edge-item-fix"><a href="/features#social-coding" class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Social coding">Social coding</a></li>
                      <li class="edge-item-fix"><a href="/features#documentation" class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Documentation">Documentation</a></li>
                      <li class="edge-item-fix"><a href="/features#code-hosting" class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Code hosting">Code hosting</a></li>
                    </ul>

                    <ul class="list-style-none mb-0 border-lg-top pt-lg-3">
                      <li class="edge-item-fix"><a href="/customer-stories" class="py-2 lh-condensed-ultra d-block no-underline link-gray-dark no-underline h5 Bump-link--hover" data-ga-click="(Logged out) Header, go to Customer stories">Customer stories <span class="Bump-link-symbol float-right text-normal text-gray-light">&rarr;</span></a></li>
                      <li class="edge-item-fix"><a href="/security" class="py-2 lh-condensed-ultra d-block no-underline link-gray-dark no-underline h5 Bump-link--hover" data-ga-click="(Logged out) Header, go to Security">Security <span class="Bump-link-symbol float-right text-normal text-gray-light">&rarr;</span></a></li>
                    </ul>
                  </div>
                </details>
              </li>
              <li class="border-bottom border-lg-bottom-0 mr-0 mr-lg-3">
                <a href="/enterprise" class="HeaderMenu-link no-underline py-3 d-block d-lg-inline-block" data-ga-click="(Logged out) Header, go to Enterprise">Enterprise</a>
              </li>

              <li class="d-block d-lg-flex flex-lg-nowrap flex-lg-items-center border-bottom border-lg-bottom-0 mr-0 mr-lg-3 edge-item-fix position-relative flex-wrap flex-justify-between d-flex flex-items-center ">
                <details class="HeaderMenu-details details-overlay details-reset width-full">
                  <summary class="HeaderMenu-summary HeaderMenu-link px-0 py-3 border-0 no-wrap d-block d-lg-inline-block">
                    Explore
                    <svg x="0px" y="0px" viewBox="0 0 14 8" xml:space="preserve" fill="none" class="icon-chevon-down-mktg position-absolute position-lg-relative">
                      <path d="M1,1l6.2,6L13,1"></path>
                    </svg>
                  </summary>

                  <div class="dropdown-menu flex-auto rounded-1 bg-white px-0 pt-2 pb-0 mt-0 pb-4 p-lg-4 position-relative position-lg-absolute left-0 left-lg-n4">
                    <ul class="list-style-none mb-3">
                      <li class="edge-item-fix"><a href="/explore" class="py-2 lh-condensed-ultra d-block link-gray-dark no-underline h5 Bump-link--hover" data-ga-click="(Logged out) Header, go to Explore">Explore GitHub <span class="Bump-link-symbol float-right text-normal text-gray-light">&rarr;</span></a></li>
                    </ul>

                    <h4 class="text-gray-light text-normal text-mono f5 mb-2 border-lg-top pt-lg-3">Learn &amp; contribute</h4>
                    <ul class="list-style-none mb-3">
                      <li class="edge-item-fix"><a href="/topics" class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Topics">Topics</a></li>
                        <li class="edge-item-fix"><a href="/collections" class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Collections">Collections</a></li>
                      <li class="edge-item-fix"><a href="/trending" class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Trending">Trending</a></li>
                      <li class="edge-item-fix"><a href="https://lab.github.com/" class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Learning lab">Learning Lab</a></li>
                      <li class="edge-item-fix"><a href="https://opensource.guide" class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Open source guides">Open source guides</a></li>
                    </ul>

                    <h4 class="text-gray-light text-normal text-mono f5 mb-2 border-lg-top pt-lg-3">Connect with others</h4>
                    <ul class="list-style-none mb-0">
                      <li class="edge-item-fix"><a href="https://github.com/events" class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Events">Events</a></li>
                      <li class="edge-item-fix"><a href="https://github.community" class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Community forum">Community forum</a></li>
                      <li class="edge-item-fix"><a href="https://education.github.com" class="py-2 pb-0 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to GitHub Education">GitHub Education</a></li>
                    </ul>
                  </div>
                </details>
              </li>

              <li class="border-bottom border-lg-bottom-0 mr-0 mr-lg-3">
                <a href="/marketplace" class="HeaderMenu-link no-underline py-3 d-block d-lg-inline-block" data-ga-click="(Logged out) Header, go to Marketplace">Marketplace</a>
              </li>

              <li class="d-block d-lg-flex flex-lg-nowrap flex-lg-items-center border-bottom border-lg-bottom-0 mr-0 mr-lg-3 edge-item-fix position-relative flex-wrap flex-justify-between d-flex flex-items-center ">
                <details class="HeaderMenu-details details-overlay details-reset width-full">
                  <summary class="HeaderMenu-summary HeaderMenu-link px-0 py-3 border-0 no-wrap d-block d-lg-inline-block">
                    Pricing
                    <svg x="0px" y="0px" viewBox="0 0 14 8" xml:space="preserve" fill="none" class="icon-chevon-down-mktg position-absolute position-lg-relative">
                       <path d="M1,1l6.2,6L13,1"></path>
                    </svg>
                  </summary>

                  <div class="dropdown-menu flex-auto rounded-1 bg-white px-0 pt-2 pb-4 mt-0 p-lg-4 position-relative position-lg-absolute left-0 left-lg-n4">
                    <a href="/pricing" class="pb-2 lh-condensed-ultra d-block link-gray-dark no-underline h5 Bump-link--hover" data-ga-click="(Logged out) Header, go to Pricing">Plans <span class="Bump-link-symbol float-right text-normal text-gray-light">&rarr;</span></a>

                    <ul class="list-style-none mb-3">
                      <li class="edge-item-fix"><a href="/pricing#feature-comparison" class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Compare plans">Compare plans</a></li>
                      <li class="edge-item-fix"><a href="https://enterprise.github.com/contact" class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Contact Sales">Contact Sales</a></li>
                    </ul>

                    <ul class="list-style-none mb-0 border-lg-top pt-lg-3">
                      <li class="edge-item-fix"><a href="/nonprofit" class="py-2 lh-condensed-ultra d-block no-underline link-gray-dark no-underline h5 Bump-link--hover" data-ga-click="(Logged out) Header, go to Nonprofits">Nonprofit <span class="Bump-link-symbol float-right text-normal text-gray-light">&rarr;</span></a></li>
                      <li class="edge-item-fix"><a href="https://education.github.com" class="py-2 pb-0 lh-condensed-ultra d-block no-underline link-gray-dark no-underline h5 Bump-link--hover"  data-ga-click="(Logged out) Header, go to Education">Education <span class="Bump-link-symbol float-right text-normal text-gray-light">&rarr;</span></a></li>
                    </ul>
                  </div>
                </details>
              </li>
          </ul>
        </nav>

      <div class="d-lg-flex flex-items-center px-3 px-lg-0 text-center text-lg-left">
          <div class="d-lg-flex mb-3 mb-lg-0">
            <div class="header-search flex-self-stretch flex-lg-self-auto mr-0 mr-lg-3 mb-3 mb-lg-0 scoped-search site-scoped-search js-site-search position-relative js-jump-to"
  role="combobox"
  aria-owns="jump-to-results"
  aria-label="Search or jump to"
  aria-haspopup="listbox"
  aria-expanded="false"
>
  <div class="position-relative">
    <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="js-site-search-form" role="search" aria-label="Site" data-scope-type="Repository" data-scope-id="185954683" data-scoped-search-url="/IreneZoi/cmgtools-lite/search" data-unscoped-search-url="/search" action="/IreneZoi/cmgtools-lite/search" accept-charset="UTF-8" method="get"><input name="utf8" type="hidden" value="&#x2713;" />
      <label class="form-control input-sm header-search-wrapper p-0 header-search-wrapper-jump-to position-relative d-flex flex-justify-between flex-items-center js-chromeless-input-container">
        <input type="text"
          class="form-control input-sm header-search-input jump-to-field js-jump-to-field js-site-search-focus js-site-search-field is-clearable"
          data-hotkey="s,/"
          name="q"
          value=""
          placeholder="Search"
          data-unscoped-placeholder="Search GitHub"
          data-scoped-placeholder="Search"
          autocapitalize="off"
          aria-autocomplete="list"
          aria-controls="jump-to-results"
          aria-label="Search"
          data-jump-to-suggestions-path="/_graphql/GetSuggestedNavigationDestinations#csrf-token=oAIcRNGCE4P6zXq3kaFQ2vGTPk+1KeDhL3SttC9KvO06DS32F88YPX5znDPGbjbIny0NKLwiBNgYuvQPWK+XFg=="
          spellcheck="false"
          autocomplete="off"
          >
          <input type="hidden" class="js-site-search-type-field" name="type" >
            <img src="https://github.githubassets.com/images/search-key-slash.svg" alt="" class="mr-2 header-search-key-slash">

            <div class="Box position-absolute overflow-hidden d-none jump-to-suggestions js-jump-to-suggestions-container">
              
<ul class="d-none js-jump-to-suggestions-template-container">
  

<li class="d-flex flex-justify-start flex-items-center p-0 f5 navigation-item js-navigation-item js-jump-to-suggestion" role="option">
  <a tabindex="-1" class="no-underline d-flex flex-auto flex-items-center jump-to-suggestions-path js-jump-to-suggestion-path js-navigation-open p-2" href="">
    <div class="jump-to-octicon js-jump-to-octicon flex-shrink-0 mr-2 text-center d-none">
      <svg height="16" width="16" class="octicon octicon-repo flex-shrink-0 js-jump-to-octicon-repo d-none" title="Repository" aria-label="Repository" viewBox="0 0 12 16" version="1.1" role="img"><path fill-rule="evenodd" d="M4 9H3V8h1v1zm0-3H3v1h1V6zm0-2H3v1h1V4zm0-2H3v1h1V2zm8-1v12c0 .55-.45 1-1 1H6v2l-1.5-1.5L3 16v-2H1c-.55 0-1-.45-1-1V1c0-.55.45-1 1-1h10c.55 0 1 .45 1 1zm-1 10H1v2h2v-1h3v1h5v-2zm0-10H2v9h9V1z"/></svg>
      <svg height="16" width="16" class="octicon octicon-project flex-shrink-0 js-jump-to-octicon-project d-none" title="Project" aria-label="Project" viewBox="0 0 15 16" version="1.1" role="img"><path fill-rule="evenodd" d="M10 12h3V2h-3v10zm-4-2h3V2H6v8zm-4 4h3V2H2v12zm-1 1h13V1H1v14zM14 0H1a1 1 0 0 0-1 1v14a1 1 0 0 0 1 1h13a1 1 0 0 0 1-1V1a1 1 0 0 0-1-1z"/></svg>
      <svg height="16" width="16" class="octicon octicon-search flex-shrink-0 js-jump-to-octicon-search d-none" title="Search" aria-label="Search" viewBox="0 0 16 16" version="1.1" role="img"><path fill-rule="evenodd" d="M15.7 13.3l-3.81-3.83A5.93 5.93 0 0 0 13 6c0-3.31-2.69-6-6-6S1 2.69 1 6s2.69 6 6 6c1.3 0 2.48-.41 3.47-1.11l3.83 3.81c.19.2.45.3.7.3.25 0 .52-.09.7-.3a.996.996 0 0 0 0-1.41v.01zM7 10.7c-2.59 0-4.7-2.11-4.7-4.7 0-2.59 2.11-4.7 4.7-4.7 2.59 0 4.7 2.11 4.7 4.7 0 2.59-2.11 4.7-4.7 4.7z"/></svg>
    </div>

    <img class="avatar mr-2 flex-shrink-0 js-jump-to-suggestion-avatar d-none" alt="" aria-label="Team" src="" width="28" height="28">

    <div class="jump-to-suggestion-name js-jump-to-suggestion-name flex-auto overflow-hidden text-left no-wrap css-truncate css-truncate-target">
    </div>

    <div class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none js-jump-to-badge-search">
      <span class="js-jump-to-badge-search-text-default d-none" aria-label="in this repository">
        In this repository
      </span>
      <span class="js-jump-to-badge-search-text-global d-none" aria-label="in all of GitHub">
        All GitHub
      </span>
      <span aria-hidden="true" class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>

    <div aria-hidden="true" class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none d-on-nav-focus js-jump-to-badge-jump">
      Jump to
      <span class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>
  </a>
</li>

</ul>

<ul class="d-none js-jump-to-no-results-template-container">
  <li class="d-flex flex-justify-center flex-items-center f5 d-none js-jump-to-suggestion p-2">
    <span class="text-gray">No suggested jump to results</span>
  </li>
</ul>

<ul id="jump-to-results" role="listbox" class="p-0 m-0 js-navigation-container jump-to-suggestions-results-container js-jump-to-suggestions-results-container">
  

<li class="d-flex flex-justify-start flex-items-center p-0 f5 navigation-item js-navigation-item js-jump-to-scoped-search d-none" role="option">
  <a tabindex="-1" class="no-underline d-flex flex-auto flex-items-center jump-to-suggestions-path js-jump-to-suggestion-path js-navigation-open p-2" href="">
    <div class="jump-to-octicon js-jump-to-octicon flex-shrink-0 mr-2 text-center d-none">
      <svg height="16" width="16" class="octicon octicon-repo flex-shrink-0 js-jump-to-octicon-repo d-none" title="Repository" aria-label="Repository" viewBox="0 0 12 16" version="1.1" role="img"><path fill-rule="evenodd" d="M4 9H3V8h1v1zm0-3H3v1h1V6zm0-2H3v1h1V4zm0-2H3v1h1V2zm8-1v12c0 .55-.45 1-1 1H6v2l-1.5-1.5L3 16v-2H1c-.55 0-1-.45-1-1V1c0-.55.45-1 1-1h10c.55 0 1 .45 1 1zm-1 10H1v2h2v-1h3v1h5v-2zm0-10H2v9h9V1z"/></svg>
      <svg height="16" width="16" class="octicon octicon-project flex-shrink-0 js-jump-to-octicon-project d-none" title="Project" aria-label="Project" viewBox="0 0 15 16" version="1.1" role="img"><path fill-rule="evenodd" d="M10 12h3V2h-3v10zm-4-2h3V2H6v8zm-4 4h3V2H2v12zm-1 1h13V1H1v14zM14 0H1a1 1 0 0 0-1 1v14a1 1 0 0 0 1 1h13a1 1 0 0 0 1-1V1a1 1 0 0 0-1-1z"/></svg>
      <svg height="16" width="16" class="octicon octicon-search flex-shrink-0 js-jump-to-octicon-search d-none" title="Search" aria-label="Search" viewBox="0 0 16 16" version="1.1" role="img"><path fill-rule="evenodd" d="M15.7 13.3l-3.81-3.83A5.93 5.93 0 0 0 13 6c0-3.31-2.69-6-6-6S1 2.69 1 6s2.69 6 6 6c1.3 0 2.48-.41 3.47-1.11l3.83 3.81c.19.2.45.3.7.3.25 0 .52-.09.7-.3a.996.996 0 0 0 0-1.41v.01zM7 10.7c-2.59 0-4.7-2.11-4.7-4.7 0-2.59 2.11-4.7 4.7-4.7 2.59 0 4.7 2.11 4.7 4.7 0 2.59-2.11 4.7-4.7 4.7z"/></svg>
    </div>

    <img class="avatar mr-2 flex-shrink-0 js-jump-to-suggestion-avatar d-none" alt="" aria-label="Team" src="" width="28" height="28">

    <div class="jump-to-suggestion-name js-jump-to-suggestion-name flex-auto overflow-hidden text-left no-wrap css-truncate css-truncate-target">
    </div>

    <div class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none js-jump-to-badge-search">
      <span class="js-jump-to-badge-search-text-default d-none" aria-label="in this repository">
        In this repository
      </span>
      <span class="js-jump-to-badge-search-text-global d-none" aria-label="in all of GitHub">
        All GitHub
      </span>
      <span aria-hidden="true" class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>

    <div aria-hidden="true" class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none d-on-nav-focus js-jump-to-badge-jump">
      Jump to
      <span class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>
  </a>
</li>

  

<li class="d-flex flex-justify-start flex-items-center p-0 f5 navigation-item js-navigation-item js-jump-to-global-search d-none" role="option">
  <a tabindex="-1" class="no-underline d-flex flex-auto flex-items-center jump-to-suggestions-path js-jump-to-suggestion-path js-navigation-open p-2" href="">
    <div class="jump-to-octicon js-jump-to-octicon flex-shrink-0 mr-2 text-center d-none">
      <svg height="16" width="16" class="octicon octicon-repo flex-shrink-0 js-jump-to-octicon-repo d-none" title="Repository" aria-label="Repository" viewBox="0 0 12 16" version="1.1" role="img"><path fill-rule="evenodd" d="M4 9H3V8h1v1zm0-3H3v1h1V6zm0-2H3v1h1V4zm0-2H3v1h1V2zm8-1v12c0 .55-.45 1-1 1H6v2l-1.5-1.5L3 16v-2H1c-.55 0-1-.45-1-1V1c0-.55.45-1 1-1h10c.55 0 1 .45 1 1zm-1 10H1v2h2v-1h3v1h5v-2zm0-10H2v9h9V1z"/></svg>
      <svg height="16" width="16" class="octicon octicon-project flex-shrink-0 js-jump-to-octicon-project d-none" title="Project" aria-label="Project" viewBox="0 0 15 16" version="1.1" role="img"><path fill-rule="evenodd" d="M10 12h3V2h-3v10zm-4-2h3V2H6v8zm-4 4h3V2H2v12zm-1 1h13V1H1v14zM14 0H1a1 1 0 0 0-1 1v14a1 1 0 0 0 1 1h13a1 1 0 0 0 1-1V1a1 1 0 0 0-1-1z"/></svg>
      <svg height="16" width="16" class="octicon octicon-search flex-shrink-0 js-jump-to-octicon-search d-none" title="Search" aria-label="Search" viewBox="0 0 16 16" version="1.1" role="img"><path fill-rule="evenodd" d="M15.7 13.3l-3.81-3.83A5.93 5.93 0 0 0 13 6c0-3.31-2.69-6-6-6S1 2.69 1 6s2.69 6 6 6c1.3 0 2.48-.41 3.47-1.11l3.83 3.81c.19.2.45.3.7.3.25 0 .52-.09.7-.3a.996.996 0 0 0 0-1.41v.01zM7 10.7c-2.59 0-4.7-2.11-4.7-4.7 0-2.59 2.11-4.7 4.7-4.7 2.59 0 4.7 2.11 4.7 4.7 0 2.59-2.11 4.7-4.7 4.7z"/></svg>
    </div>

    <img class="avatar mr-2 flex-shrink-0 js-jump-to-suggestion-avatar d-none" alt="" aria-label="Team" src="" width="28" height="28">

    <div class="jump-to-suggestion-name js-jump-to-suggestion-name flex-auto overflow-hidden text-left no-wrap css-truncate css-truncate-target">
    </div>

    <div class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none js-jump-to-badge-search">
      <span class="js-jump-to-badge-search-text-default d-none" aria-label="in this repository">
        In this repository
      </span>
      <span class="js-jump-to-badge-search-text-global d-none" aria-label="in all of GitHub">
        All GitHub
      </span>
      <span aria-hidden="true" class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>

    <div aria-hidden="true" class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none d-on-nav-focus js-jump-to-badge-jump">
      Jump to
      <span class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>
  </a>
</li>


</ul>

            </div>
      </label>
</form>  </div>
</div>

          </div>

        <a href="/login?return_to=%2FIreneZoi%2Fcmgtools-lite%2Fblob%2FVV_VH_workinprogress%2FVVResonances%2Finteractive%2FplotSignalShapesFromJSON.py"
          class="HeaderMenu-link no-underline mr-3"
          data-hydro-click="{&quot;event_type&quot;:&quot;authentication.click&quot;,&quot;payload&quot;:{&quot;location_in_page&quot;:&quot;site header menu&quot;,&quot;repository_id&quot;:null,&quot;auth_type&quot;:&quot;SIGN_UP&quot;,&quot;client_id&quot;:null,&quot;originating_request_id&quot;:&quot;87B0:433C6:3E6D8E6:5E3300A:5D8DD760&quot;,&quot;originating_url&quot;:&quot;https://github.com/IreneZoi/cmgtools-lite/blob/VV_VH_workinprogress/VVResonances/interactive/plotSignalShapesFromJSON.py&quot;,&quot;referrer&quot;:null,&quot;user_id&quot;:null}}" data-hydro-click-hmac="3f4ef80487466c0ad8387d948ede2bb9bd6d2b1ef7af26f732623f9bd429bf57"
          data-ga-click="(Logged out) Header, clicked Sign in, text:sign-in">
          Sign&nbsp;in
        </a>
          <a href="/join?source=header-repo"
            class="HeaderMenu-link d-inline-block no-underline border border-gray-dark rounded-1 px-2 py-1"
            data-hydro-click="{&quot;event_type&quot;:&quot;authentication.click&quot;,&quot;payload&quot;:{&quot;location_in_page&quot;:&quot;site header menu&quot;,&quot;repository_id&quot;:null,&quot;auth_type&quot;:&quot;SIGN_UP&quot;,&quot;client_id&quot;:null,&quot;originating_request_id&quot;:&quot;87B0:433C6:3E6D8E6:5E3300A:5D8DD760&quot;,&quot;originating_url&quot;:&quot;https://github.com/IreneZoi/cmgtools-lite/blob/VV_VH_workinprogress/VVResonances/interactive/plotSignalShapesFromJSON.py&quot;,&quot;referrer&quot;:null,&quot;user_id&quot;:null}}" data-hydro-click-hmac="3f4ef80487466c0ad8387d948ede2bb9bd6d2b1ef7af26f732623f9bd429bf57"
            data-ga-click="(Logged out) Header, clicked Sign up, text:sign-up">
            Sign&nbsp;up
          </a>
      </div>
    </div>
  </div>
</header>

  </div>

  <div id="start-of-content" class="show-on-focus"></div>


    <div id="js-flash-container">

</div>



  <div class="application-main " data-commit-hovercards-enabled>
        <div itemscope itemtype="http://schema.org/SoftwareSourceCode" class="">
    <main  >
      


  










  <div class="pagehead repohead instapaper_ignore readability-menu experiment-repo-nav pt-0 pt-lg-4 ">
    <div class="repohead-details-container clearfix container-lg p-responsive d-none d-lg-block">

      <ul class="pagehead-actions">




  <li>
    
  <a class="tooltipped tooltipped-s btn btn-sm btn-with-count" aria-label="You must be signed in to watch a repository" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;authentication.click&quot;,&quot;payload&quot;:{&quot;location_in_page&quot;:&quot;notification subscription menu watch&quot;,&quot;repository_id&quot;:null,&quot;auth_type&quot;:&quot;LOG_IN&quot;,&quot;client_id&quot;:null,&quot;originating_request_id&quot;:&quot;87B0:433C6:3E6D8E6:5E3300A:5D8DD760&quot;,&quot;originating_url&quot;:&quot;https://github.com/IreneZoi/cmgtools-lite/blob/VV_VH_workinprogress/VVResonances/interactive/plotSignalShapesFromJSON.py&quot;,&quot;referrer&quot;:null,&quot;user_id&quot;:null}}" data-hydro-click-hmac="4548a3ab461806c8f925b090ffc1b737b72f65681d734f2e0f14c818dfb11128" href="/login?return_to=%2FIreneZoi%2Fcmgtools-lite">
    <svg class="octicon octicon-eye v-align-text-bottom" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8.06 2C3 2 0 8 0 8s3 6 8.06 6C13 14 16 8 16 8s-3-6-7.94-6zM8 12c-2.2 0-4-1.78-4-4 0-2.2 1.8-4 4-4 2.22 0 4 1.8 4 4 0 2.22-1.78 4-4 4zm2-4c0 1.11-.89 2-2 2-1.11 0-2-.89-2-2 0-1.11.89-2 2-2 1.11 0 2 .89 2 2z"/></svg>
    Watch
</a>    <a class="social-count" href="/IreneZoi/cmgtools-lite/watchers"
       aria-label="1 user is watching this repository">
      1
    </a>

  </li>

  <li>
        <a class="btn btn-sm btn-with-count tooltipped tooltipped-s" aria-label="You must be signed in to star a repository" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;authentication.click&quot;,&quot;payload&quot;:{&quot;location_in_page&quot;:&quot;star button&quot;,&quot;repository_id&quot;:185954683,&quot;auth_type&quot;:&quot;LOG_IN&quot;,&quot;client_id&quot;:null,&quot;originating_request_id&quot;:&quot;87B0:433C6:3E6D8E6:5E3300A:5D8DD760&quot;,&quot;originating_url&quot;:&quot;https://github.com/IreneZoi/cmgtools-lite/blob/VV_VH_workinprogress/VVResonances/interactive/plotSignalShapesFromJSON.py&quot;,&quot;referrer&quot;:null,&quot;user_id&quot;:null}}" data-hydro-click-hmac="0a9f13273c176575ba19fd825a46725a8074130ffc711e4b342e572b8ed2e7bd" href="/login?return_to=%2FIreneZoi%2Fcmgtools-lite">
      <svg class="octicon octicon-star v-align-text-bottom" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M14 6l-4.9-.64L7 1 4.9 5.36 0 6l3.6 3.26L2.67 14 7 11.67 11.33 14l-.93-4.74L14 6z"/></svg>
      Star
</a>
    <a class="social-count js-social-count" href="/IreneZoi/cmgtools-lite/stargazers"
      aria-label="0 users starred this repository">
      0
    </a>

  </li>

  <li>
      <a class="btn btn-sm btn-with-count tooltipped tooltipped-s" aria-label="You must be signed in to fork a repository" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;authentication.click&quot;,&quot;payload&quot;:{&quot;location_in_page&quot;:&quot;repo details fork button&quot;,&quot;repository_id&quot;:185954683,&quot;auth_type&quot;:&quot;LOG_IN&quot;,&quot;client_id&quot;:null,&quot;originating_request_id&quot;:&quot;87B0:433C6:3E6D8E6:5E3300A:5D8DD760&quot;,&quot;originating_url&quot;:&quot;https://github.com/IreneZoi/cmgtools-lite/blob/VV_VH_workinprogress/VVResonances/interactive/plotSignalShapesFromJSON.py&quot;,&quot;referrer&quot;:null,&quot;user_id&quot;:null}}" data-hydro-click-hmac="3fd73146da94bf7c44b35b8b1196e23beed291d4dba3c7ea8237e0904bbdec02" href="/login?return_to=%2FIreneZoi%2Fcmgtools-lite">
        <svg class="octicon octicon-repo-forked v-align-text-bottom" viewBox="0 0 10 16" version="1.1" width="10" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8 1a1.993 1.993 0 0 0-1 3.72V6L5 8 3 6V4.72A1.993 1.993 0 0 0 2 1a1.993 1.993 0 0 0-1 3.72V6.5l3 3v1.78A1.993 1.993 0 0 0 5 15a1.993 1.993 0 0 0 1-3.72V9.5l3-3V4.72A1.993 1.993 0 0 0 8 1zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zm3 10c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zm3-10c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"/></svg>
        Fork
</a>
    <a href="/IreneZoi/cmgtools-lite/network/members" class="social-count"
       aria-label="197 users forked this repository">
      197
    </a>
  </li>
</ul>

      <h1 class="public ">
    <svg class="octicon octicon-repo-forked" viewBox="0 0 10 16" version="1.1" width="10" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8 1a1.993 1.993 0 0 0-1 3.72V6L5 8 3 6V4.72A1.993 1.993 0 0 0 2 1a1.993 1.993 0 0 0-1 3.72V6.5l3 3v1.78A1.993 1.993 0 0 0 5 15a1.993 1.993 0 0 0 1-3.72V9.5l3-3V4.72A1.993 1.993 0 0 0 8 1zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zm3 10c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zm3-10c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"/></svg>
  <span class="author" itemprop="author"><a class="url fn" rel="author" data-hovercard-type="user" data-hovercard-url="/hovercards?user_id=20553929" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/IreneZoi">IreneZoi</a></span><!--
--><span class="path-divider">/</span><!--
--><strong itemprop="name"><a data-pjax="#js-repo-pjax-container" href="/IreneZoi/cmgtools-lite">cmgtools-lite</a></strong>
  

    <span class="fork-flag" data-repository-hovercards-enabled>
      <span class="text">forked from <a data-hovercard-type="repository" data-hovercard-url="/Diboson3D/cmgtools-lite/hovercard" href="/Diboson3D/cmgtools-lite">Diboson3D/cmgtools-lite</a></span>
    </span>
</h1>

    </div>
    
<nav class="hx_reponav reponav js-repo-nav js-sidenav-container-pjax container-lg p-responsive d-none d-lg-block"
     itemscope
     itemtype="http://schema.org/BreadcrumbList"
    aria-label="Repository"
     data-pjax="#js-repo-pjax-container">

  <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
    <a class="js-selected-navigation-item selected reponav-item" itemprop="url" data-hotkey="g c" aria-current="page" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches repo_packages /IreneZoi/cmgtools-lite" href="/IreneZoi/cmgtools-lite">
      <svg class="octicon octicon-code" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M9.5 3L8 4.5 11.5 8 8 11.5 9.5 13 14 8 9.5 3zm-5 0L0 8l4.5 5L6 11.5 2.5 8 6 4.5 4.5 3z"/></svg>
      <span itemprop="name">Code</span>
      <meta itemprop="position" content="1">
</a>  </span>


  <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
    <a data-hotkey="g p" itemprop="url" class="js-selected-navigation-item reponav-item" data-selected-links="repo_pulls checks /IreneZoi/cmgtools-lite/pulls" href="/IreneZoi/cmgtools-lite/pulls">
      <svg class="octicon octicon-git-pull-request" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"/></svg>
      <span itemprop="name">Pull requests</span>
      <span class="Counter">0</span>
      <meta itemprop="position" content="3">
</a>  </span>


    <a data-hotkey="g b" class="js-selected-navigation-item reponav-item" data-selected-links="repo_projects new_repo_project repo_project /IreneZoi/cmgtools-lite/projects" href="/IreneZoi/cmgtools-lite/projects">
      <svg class="octicon octicon-project" viewBox="0 0 15 16" version="1.1" width="15" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M10 12h3V2h-3v10zm-4-2h3V2H6v8zm-4 4h3V2H2v12zm-1 1h13V1H1v14zM14 0H1a1 1 0 0 0-1 1v14a1 1 0 0 0 1 1h13a1 1 0 0 0 1-1V1a1 1 0 0 0-1-1z"/></svg>
      Projects
      <span class="Counter" >0</span>
</a>


    <a data-skip-pjax="true" class="js-selected-navigation-item reponav-item" data-selected-links="security alerts policy code_scanning /IreneZoi/cmgtools-lite/security/advisories" href="/IreneZoi/cmgtools-lite/security/advisories">
      <svg class="octicon octicon-shield" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M0 2l7-2 7 2v6.02C14 12.69 8.69 16 7 16c-1.69 0-7-3.31-7-7.98V2zm1 .75L7 1l6 1.75v5.268C13 12.104 8.449 15 7 15c-1.449 0-6-2.896-6-6.982V2.75zm1 .75L7 2v12c-1.207 0-5-2.482-5-5.985V3.5z"/></svg>
      Security
</a>
    <a class="js-selected-navigation-item reponav-item" data-selected-links="repo_graphs repo_contributors dependency_graph pulse people /IreneZoi/cmgtools-lite/pulse" href="/IreneZoi/cmgtools-lite/pulse">
      <svg class="octicon octicon-graph" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M16 14v1H0V0h1v14h15zM5 13H3V8h2v5zm4 0H7V3h2v10zm4 0h-2V6h2v7z"/></svg>
      Insights
</a>

</nav>

  <div class="reponav-wrapper reponav-small d-lg-none">
  <nav class="reponav js-reponav text-center no-wrap"
       itemscope
       itemtype="http://schema.org/BreadcrumbList">

    <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
      <a class="js-selected-navigation-item selected reponav-item" itemprop="url" aria-current="page" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches repo_packages /IreneZoi/cmgtools-lite" href="/IreneZoi/cmgtools-lite">
        <span itemprop="name">Code</span>
        <meta itemprop="position" content="1">
</a>    </span>


    <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
      <a itemprop="url" class="js-selected-navigation-item reponav-item" data-selected-links="repo_pulls checks /IreneZoi/cmgtools-lite/pulls" href="/IreneZoi/cmgtools-lite/pulls">
        <span itemprop="name">Pull requests</span>
        <span class="Counter">0</span>
        <meta itemprop="position" content="3">
</a>    </span>

      <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
        <a itemprop="url" class="js-selected-navigation-item reponav-item" data-selected-links="repo_projects new_repo_project repo_project /IreneZoi/cmgtools-lite/projects" href="/IreneZoi/cmgtools-lite/projects">
          <span itemprop="name">Projects</span>
          <span class="Counter">0</span>
          <meta itemprop="position" content="4">
</a>      </span>


      <a itemprop="url" class="js-selected-navigation-item reponav-item" data-selected-links="security alerts policy code_scanning /IreneZoi/cmgtools-lite/security/advisories" href="/IreneZoi/cmgtools-lite/security/advisories">
        <span itemprop="name">Security</span>
        <meta itemprop="position" content="6">
</a>
      <a class="js-selected-navigation-item reponav-item" data-selected-links="pulse /IreneZoi/cmgtools-lite/pulse" href="/IreneZoi/cmgtools-lite/pulse">
        Pulse
</a>

  </nav>
</div>


  </div>
<div class="container-lg clearfix new-discussion-timeline experiment-repo-nav  p-responsive">
  <div class="repository-content ">

    
    


  


    <a class="d-none js-permalink-shortcut" data-hotkey="y" href="/IreneZoi/cmgtools-lite/blob/36f0f02d480c3c6dec6b9a970594efff50bb2b1b/VVResonances/interactive/plotSignalShapesFromJSON.py">Permalink</a>

    <!-- blob contrib key: blob_contributors:v21:c3c3e598163edb05eec05cb988e139f1 -->
          <div class="signup-prompt-bg rounded-1">
      <div class="signup-prompt p-4 text-center mb-4 rounded-1">
        <div class="position-relative">
          <!-- '"` --><!-- </textarea></xmp> --></option></form><form action="/prompt_dismissals/signup" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="_method" value="put" /><input type="hidden" name="authenticity_token" value="ZEY9oaeIuyGgkHF+8l8596VgEwcF5k3Z6XTxpaqruXUhc/GZsBqe5XmJXrZNx/Cdt/62Dx6zgbOpMMx8z5lfgQ==" />
            <button type="submit" class="position-absolute top-0 right-0 btn-link link-gray" data-ga-click="(Logged out) Sign up prompt, clicked Dismiss, text:dismiss">
              Dismiss
            </button>
</form>          <h3 class="pt-2">Join GitHub today</h3>
          <p class="col-6 mx-auto">GitHub is home to over 40 million developers working together to host and review code, manage projects, and build software together.</p>
          <a class="btn btn-primary" data-hydro-click="{&quot;event_type&quot;:&quot;authentication.click&quot;,&quot;payload&quot;:{&quot;location_in_page&quot;:&quot;files signup prompt&quot;,&quot;repository_id&quot;:null,&quot;auth_type&quot;:&quot;SIGN_UP&quot;,&quot;client_id&quot;:null,&quot;originating_request_id&quot;:&quot;87B0:433C6:3E6D8E6:5E3300A:5D8DD760&quot;,&quot;originating_url&quot;:&quot;https://github.com/IreneZoi/cmgtools-lite/blob/VV_VH_workinprogress/VVResonances/interactive/plotSignalShapesFromJSON.py&quot;,&quot;referrer&quot;:null,&quot;user_id&quot;:null}}" data-hydro-click-hmac="01fe2fe30ba0b19a0fdb1dfa778f789d04a7161a20edd69c4dafded3f2ef3122" data-ga-click="(Logged out) Sign up prompt, clicked Sign up, text:sign-up" href="/join?source=prompt-blob-show">Sign up</a>
        </div>
      </div>
    </div>


    <div class="d-flex flex-items-start flex-shrink-0 pb-3 flex-column flex-md-row">
      <span class="d-flex flex-justify-between width-full width-md-auto">
        
<details class="details-reset details-overlay select-menu branch-select-menu  hx_rsm" id="branch-select-menu">
  <summary class="btn btn-sm select-menu-button css-truncate"
           data-hotkey="w"
           title="VV_VH_workinprogress">
    <i>Branch:</i>
    <span class="css-truncate-target" data-menu-button>VV_VH_workinpr…</span>
  </summary>

  <details-menu class="select-menu-modal hx_rsm-modal position-absolute" style="z-index: 99;" src="/IreneZoi/cmgtools-lite/ref-list/VV_VH_workinprogress/VVResonances/interactive/plotSignalShapesFromJSON.py?source_action=show&amp;source_controller=blob" preload>
    <include-fragment class="select-menu-loading-overlay anim-pulse">
      <svg height="32" class="octicon octicon-octoface" viewBox="0 0 16 16" version="1.1" width="32" aria-hidden="true"><path fill-rule="evenodd" d="M14.7 5.34c.13-.32.55-1.59-.13-3.31 0 0-1.05-.33-3.44 1.3-1-.28-2.07-.32-3.13-.32s-2.13.04-3.13.32c-2.39-1.64-3.44-1.3-3.44-1.3-.68 1.72-.26 2.99-.13 3.31C.49 6.21 0 7.33 0 8.69 0 13.84 3.33 15 7.98 15S16 13.84 16 8.69c0-1.36-.49-2.48-1.3-3.35zM8 14.02c-3.3 0-5.98-.15-5.98-3.35 0-.76.38-1.48 1.02-2.07 1.07-.98 2.9-.46 4.96-.46 2.07 0 3.88-.52 4.96.46.65.59 1.02 1.3 1.02 2.07 0 3.19-2.68 3.35-5.98 3.35zM5.49 9.01c-.66 0-1.2.8-1.2 1.78s.54 1.79 1.2 1.79c.66 0 1.2-.8 1.2-1.79s-.54-1.78-1.2-1.78zm5.02 0c-.66 0-1.2.79-1.2 1.78s.54 1.79 1.2 1.79c.66 0 1.2-.8 1.2-1.79s-.53-1.78-1.2-1.78z"/></svg>
    </include-fragment>
  </details-menu>
</details>

        <div class="BtnGroup flex-shrink-0 d-md-none">
          <a href="/IreneZoi/cmgtools-lite/find/VV_VH_workinprogress"
                class="js-pjax-capture-input btn btn-sm BtnGroup-item"
                data-pjax
                data-hotkey="t">
            Find file
          </a>
          <clipboard-copy value="VVResonances/interactive/plotSignalShapesFromJSON.py" class="btn btn-sm BtnGroup-item">
            Copy path
          </clipboard-copy>
        </div>
      </span>
      <h2 id="blob-path" class="breadcrumb flex-auto min-width-0 text-normal flex-md-self-center ml-md-2 mr-md-3 my-2 my-md-0">
        <span class="js-repo-root text-bold"><span class="js-path-segment"><a data-pjax="true" href="/IreneZoi/cmgtools-lite"><span>cmgtools-lite</span></a></span></span><span class="separator">/</span><span class="js-path-segment"><a data-pjax="true" href="/IreneZoi/cmgtools-lite/tree/VV_VH_workinprogress/VVResonances"><span>VVResonances</span></a></span><span class="separator">/</span><span class="js-path-segment"><a data-pjax="true" href="/IreneZoi/cmgtools-lite/tree/VV_VH_workinprogress/VVResonances/interactive"><span>interactive</span></a></span><span class="separator">/</span><strong class="final-path">plotSignalShapesFromJSON.py</strong>
      </h2>

      <div class="BtnGroup flex-shrink-0 d-none d-md-inline-block">
        <a href="/IreneZoi/cmgtools-lite/find/VV_VH_workinprogress"
              class="js-pjax-capture-input btn btn-sm BtnGroup-item"
              data-pjax
              data-hotkey="t">
          Find file
        </a>
        <clipboard-copy value="VVResonances/interactive/plotSignalShapesFromJSON.py" class="btn btn-sm BtnGroup-item">
          Copy path
        </clipboard-copy>
      </div>
    </div>



    
  <div class="Box Box--condensed d-flex flex-column flex-shrink-0">
      <div class="Box-body d-flex flex-justify-between bg-blue-light flex-column flex-md-row flex-items-start flex-md-items-center">
        <span class="pr-md-4 f6">
          <a rel="author" data-skip-pjax="true" data-hovercard-type="user" data-hovercard-url="/hovercards?user_id=20553929" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/IreneZoi"><img class="avatar" src="https://avatars0.githubusercontent.com/u/20553929?s=40&amp;v=4" width="20" height="20" alt="@IreneZoi" /></a>
          <a class="text-bold link-gray-dark lh-default v-align-middle" rel="author" data-hovercard-type="user" data-hovercard-url="/hovercards?user_id=20553929" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/IreneZoi">IreneZoi</a>
            <span class="lh-default v-align-middle">
              <a data-pjax="true" title="removed commented parts and empty lines" class="link-gray" href="/IreneZoi/cmgtools-lite/commit/36f0f02d480c3c6dec6b9a970594efff50bb2b1b">removed commented parts and empty lines</a>
            </span>
        </span>
        <span class="d-inline-block flex-shrink-0 v-align-bottom f6 mt-2 mt-md-0">
          <a class="pr-2 text-mono link-gray" href="/IreneZoi/cmgtools-lite/commit/36f0f02d480c3c6dec6b9a970594efff50bb2b1b" data-pjax>36f0f02</a>
          <relative-time datetime="2019-09-27T09:20:59Z">Sep 27, 2019</relative-time>
        </span>
      </div>

    <div class="Box-body d-flex flex-items-center flex-auto f6 border-bottom-0 flex-wrap" >
      <details class="details-reset details-overlay details-overlay-dark lh-default text-gray-dark float-left mr-2" id="blob_contributors_box">
        <summary class="btn-link">
          <span><strong>3</strong> contributors</span>
        </summary>
        <details-dialog
          class="Box Box--overlay d-flex flex-column anim-fade-in fast"
          aria-label="Users who have contributed to this file"
          src="/IreneZoi/cmgtools-lite/contributors/VV_VH_workinprogress/VVResonances/interactive/plotSignalShapesFromJSON.py/list" preload>
          <div class="Box-header">
            <button class="Box-btn-octicon btn-octicon float-right" type="button" aria-label="Close dialog" data-close-dialog>
              <svg class="octicon octicon-x" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48L7.48 8z"/></svg>
            </button>
            <h3 class="Box-title">
              Users who have contributed to this file
            </h3>
          </div>
          <include-fragment class="octocat-spinner my-3" aria-label="Loading..."></include-fragment>
        </details-dialog>
      </details>
        <span class="">
    <a class="avatar-link" data-hovercard-type="user" data-hovercard-url="/hovercards?user_id=20553929" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/IreneZoi/cmgtools-lite/commits/VV_VH_workinprogress/VVResonances/interactive/plotSignalShapesFromJSON.py?author=IreneZoi">
      <img class="avatar mr-1" src="https://avatars0.githubusercontent.com/u/20553929?s=40&amp;v=4" width="20" height="20" alt="@IreneZoi" /> 
</a>    <a class="avatar-link" data-hovercard-type="user" data-hovercard-url="/hovercards?user_id=5552832" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/IreneZoi/cmgtools-lite/commits/VV_VH_workinprogress/VVResonances/interactive/plotSignalShapesFromJSON.py?author=thaarres">
      <img class="avatar mr-1" src="https://avatars1.githubusercontent.com/u/5552832?s=40&amp;v=4" width="20" height="20" alt="@thaarres" /> 
</a>    <a class="avatar-link" data-hovercard-type="user" data-hovercard-url="/hovercards?user_id=5583089" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/IreneZoi/cmgtools-lite/commits/VV_VH_workinprogress/VVResonances/interactive/plotSignalShapesFromJSON.py?author=jngadiub">
      <img class="avatar mr-1" src="https://avatars2.githubusercontent.com/u/5583089?s=40&amp;v=4" width="20" height="20" alt="@jngadiub" /> 
</a>
</span>

    </div>
  </div>





    <div class="Box mt-3 position-relative">
      
<div class="Box-header py-2 d-flex flex-column flex-shrink-0 flex-md-row flex-md-items-center">

  <div class="text-mono f6 flex-auto pr-3 flex-order-2 flex-md-order-1 mt-2 mt-md-0">
      433 lines (373 sloc)
      <span class="file-info-divider"></span>
    18.3 KB
  </div>

  <div class="d-flex py-1 py-md-0 flex-auto flex-order-1 flex-md-order-2 flex-sm-grow-0 flex-justify-between">

    <div class="BtnGroup">
      <a id="raw-url" class="btn btn-sm BtnGroup-item" href="/IreneZoi/cmgtools-lite/raw/VV_VH_workinprogress/VVResonances/interactive/plotSignalShapesFromJSON.py">Raw</a>
        <a class="btn btn-sm js-update-url-with-hash BtnGroup-item" data-hotkey="b" href="/IreneZoi/cmgtools-lite/blame/VV_VH_workinprogress/VVResonances/interactive/plotSignalShapesFromJSON.py">Blame</a>
      <a rel="nofollow" class="btn btn-sm BtnGroup-item" href="/IreneZoi/cmgtools-lite/commits/VV_VH_workinprogress/VVResonances/interactive/plotSignalShapesFromJSON.py">History</a>
    </div>


    <div>

          <button type="button" class="btn-octicon disabled tooltipped tooltipped-nw"
            aria-label="You must be signed in to make or propose changes">
            <svg class="octicon octicon-pencil" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M0 12v3h3l8-8-3-3-8 8zm3 2H1v-2h1v1h1v1zm10.3-9.3L12 6 9 3l1.3-1.3a.996.996 0 0 1 1.41 0l1.59 1.59c.39.39.39 1.02 0 1.41z"/></svg>
          </button>
          <button type="button" class="btn-octicon btn-octicon-danger disabled tooltipped tooltipped-nw"
            aria-label="You must be signed in to make or propose changes">
            <svg class="octicon octicon-trashcan" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M11 2H9c0-.55-.45-1-1-1H5c-.55 0-1 .45-1 1H2c-.55 0-1 .45-1 1v1c0 .55.45 1 1 1v9c0 .55.45 1 1 1h7c.55 0 1-.45 1-1V5c.55 0 1-.45 1-1V3c0-.55-.45-1-1-1zm-1 12H3V5h1v8h1V5h1v8h1V5h1v8h1V5h1v9zm1-10H2V3h9v1z"/></svg>
          </button>
    </div>
  </div>
</div>




      

  <div itemprop="text" class="Box-body p-0 blob-wrapper data type-python ">
      
<table class="highlight tab-size js-file-line-container" data-tab-size="8">
      <tr>
        <td id="L1" class="blob-num js-line-number" data-line-number="1"></td>
        <td id="LC1" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>!/bin/env python</span></td>
      </tr>
      <tr>
        <td id="L2" class="blob-num js-line-number" data-line-number="2"></td>
        <td id="LC2" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> <span class="pl-c1">ROOT</span></td>
      </tr>
      <tr>
        <td id="L3" class="blob-num js-line-number" data-line-number="3"></td>
        <td id="LC3" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> json</td>
      </tr>
      <tr>
        <td id="L4" class="blob-num js-line-number" data-line-number="4"></td>
        <td id="LC4" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> math</td>
      </tr>
      <tr>
        <td id="L5" class="blob-num js-line-number" data-line-number="5"></td>
        <td id="LC5" class="blob-code blob-code-inner js-file-line"><span class="pl-c1">ROOT</span>.gSystem.Load(<span class="pl-s"><span class="pl-pds">&quot;</span>libHiggsAnalysisCombinedLimit<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L6" class="blob-num js-line-number" data-line-number="6"></td>
        <td id="LC6" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> time <span class="pl-k">import</span> sleep</td>
      </tr>
      <tr>
        <td id="L7" class="blob-num js-line-number" data-line-number="7"></td>
        <td id="LC7" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> optparse, sys</td>
      </tr>
      <tr>
        <td id="L8" class="blob-num js-line-number" data-line-number="8"></td>
        <td id="LC8" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span>  CMGTools.VVResonances.plotting.<span class="pl-c1">CMS_lumi</span> <span class="pl-k">import</span> <span class="pl-k">*</span></td>
      </tr>
      <tr>
        <td id="L9" class="blob-num js-line-number" data-line-number="9"></td>
        <td id="LC9" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L10" class="blob-num js-line-number" data-line-number="10"></td>
        <td id="LC10" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> ROOT.gROOT.SetBatch(True)</span></td>
      </tr>
      <tr>
        <td id="L11" class="blob-num js-line-number" data-line-number="11"></td>
        <td id="LC11" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L12" class="blob-num js-line-number" data-line-number="12"></td>
        <td id="LC12" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">getLegend</span>(<span class="pl-smi">textsize</span><span class="pl-k">=</span><span class="pl-c1">0.20</span>,<span class="pl-smi">x1</span><span class="pl-k">=</span><span class="pl-c1">0.5809045</span>,<span class="pl-smi">y1</span><span class="pl-k">=</span><span class="pl-c1">0.6363636</span>,<span class="pl-smi">x2</span><span class="pl-k">=</span><span class="pl-c1">0.9522613</span>,<span class="pl-smi">y2</span><span class="pl-k">=</span><span class="pl-c1">0.9020979</span>):</td>
      </tr>
      <tr>
        <td id="L13" class="blob-num js-line-number" data-line-number="13"></td>
        <td id="LC13" class="blob-code blob-code-inner js-file-line">  legend <span class="pl-k">=</span> <span class="pl-c1">ROOT</span>.TLegend(x1,y1,x2,y2)</td>
      </tr>
      <tr>
        <td id="L14" class="blob-num js-line-number" data-line-number="14"></td>
        <td id="LC14" class="blob-code blob-code-inner js-file-line">  legend.SetTextSize(textsize)</td>
      </tr>
      <tr>
        <td id="L15" class="blob-num js-line-number" data-line-number="15"></td>
        <td id="LC15" class="blob-code blob-code-inner js-file-line">  legend.SetLineColor(<span class="pl-c1">0</span>)</td>
      </tr>
      <tr>
        <td id="L16" class="blob-num js-line-number" data-line-number="16"></td>
        <td id="LC16" class="blob-code blob-code-inner js-file-line">  legend.SetShadowColor(<span class="pl-c1">0</span>)</td>
      </tr>
      <tr>
        <td id="L17" class="blob-num js-line-number" data-line-number="17"></td>
        <td id="LC17" class="blob-code blob-code-inner js-file-line">  legend.SetLineStyle(<span class="pl-c1">1</span>)</td>
      </tr>
      <tr>
        <td id="L18" class="blob-num js-line-number" data-line-number="18"></td>
        <td id="LC18" class="blob-code blob-code-inner js-file-line">  legend.SetLineWidth(<span class="pl-c1">1</span>)</td>
      </tr>
      <tr>
        <td id="L19" class="blob-num js-line-number" data-line-number="19"></td>
        <td id="LC19" class="blob-code blob-code-inner js-file-line">  legend.SetFillColor(<span class="pl-c1">0</span>)</td>
      </tr>
      <tr>
        <td id="L20" class="blob-num js-line-number" data-line-number="20"></td>
        <td id="LC20" class="blob-code blob-code-inner js-file-line">  legend.SetFillStyle(<span class="pl-c1">0</span>)</td>
      </tr>
      <tr>
        <td id="L21" class="blob-num js-line-number" data-line-number="21"></td>
        <td id="LC21" class="blob-code blob-code-inner js-file-line">  legend.SetMargin(<span class="pl-c1">0.35</span>)</td>
      </tr>
      <tr>
        <td id="L22" class="blob-num js-line-number" data-line-number="22"></td>
        <td id="LC22" class="blob-code blob-code-inner js-file-line">  legend.SetTextFont(<span class="pl-c1">42</span>)</td>
      </tr>
      <tr>
        <td id="L23" class="blob-num js-line-number" data-line-number="23"></td>
        <td id="LC23" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">return</span> legend</td>
      </tr>
      <tr>
        <td id="L24" class="blob-num js-line-number" data-line-number="24"></td>
        <td id="LC24" class="blob-code blob-code-inner js-file-line">  </td>
      </tr>
      <tr>
        <td id="L25" class="blob-num js-line-number" data-line-number="25"></td>
        <td id="LC25" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">getCanvasPaper</span>(<span class="pl-smi">cname</span>):</td>
      </tr>
      <tr>
        <td id="L26" class="blob-num js-line-number" data-line-number="26"></td>
        <td id="LC26" class="blob-code blob-code-inner js-file-line"> <span class="pl-c1">ROOT</span>.gStyle.SetOptStat(<span class="pl-c1">0</span>)</td>
      </tr>
      <tr>
        <td id="L27" class="blob-num js-line-number" data-line-number="27"></td>
        <td id="LC27" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L28" class="blob-num js-line-number" data-line-number="28"></td>
        <td id="LC28" class="blob-code blob-code-inner js-file-line"> H_ref <span class="pl-k">=</span> <span class="pl-c1">700</span> </td>
      </tr>
      <tr>
        <td id="L29" class="blob-num js-line-number" data-line-number="29"></td>
        <td id="LC29" class="blob-code blob-code-inner js-file-line"> W_ref <span class="pl-k">=</span> <span class="pl-c1">600</span> </td>
      </tr>
      <tr>
        <td id="L30" class="blob-num js-line-number" data-line-number="30"></td>
        <td id="LC30" class="blob-code blob-code-inner js-file-line"> W <span class="pl-k">=</span> W_ref</td>
      </tr>
      <tr>
        <td id="L31" class="blob-num js-line-number" data-line-number="31"></td>
        <td id="LC31" class="blob-code blob-code-inner js-file-line"> H  <span class="pl-k">=</span> H_ref</td>
      </tr>
      <tr>
        <td id="L32" class="blob-num js-line-number" data-line-number="32"></td>
        <td id="LC32" class="blob-code blob-code-inner js-file-line"> iPeriod <span class="pl-k">=</span> <span class="pl-c1">0</span></td>
      </tr>
      <tr>
        <td id="L33" class="blob-num js-line-number" data-line-number="33"></td>
        <td id="LC33" class="blob-code blob-code-inner js-file-line"> <span class="pl-c"><span class="pl-c">#</span> references for T, B, L, R</span></td>
      </tr>
      <tr>
        <td id="L34" class="blob-num js-line-number" data-line-number="34"></td>
        <td id="LC34" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">if</span> options.var <span class="pl-k">==</span><span class="pl-s"><span class="pl-pds">&quot;</span>mVV<span class="pl-pds">&quot;</span></span>:</td>
      </tr>
      <tr>
        <td id="L35" class="blob-num js-line-number" data-line-number="35"></td>
        <td id="LC35" class="blob-code blob-code-inner js-file-line">    T <span class="pl-k">=</span> <span class="pl-c1">0.3</span><span class="pl-k">*</span>H_ref</td>
      </tr>
      <tr>
        <td id="L36" class="blob-num js-line-number" data-line-number="36"></td>
        <td id="LC36" class="blob-code blob-code-inner js-file-line">    B <span class="pl-k">=</span> <span class="pl-c1">0.35</span><span class="pl-k">*</span>H_ref </td>
      </tr>
      <tr>
        <td id="L37" class="blob-num js-line-number" data-line-number="37"></td>
        <td id="LC37" class="blob-code blob-code-inner js-file-line">    L <span class="pl-k">=</span> <span class="pl-c1">0.10</span><span class="pl-k">*</span>W_ref</td>
      </tr>
      <tr>
        <td id="L38" class="blob-num js-line-number" data-line-number="38"></td>
        <td id="LC38" class="blob-code blob-code-inner js-file-line">    R <span class="pl-k">=</span> <span class="pl-c1">0.07</span><span class="pl-k">*</span>W_ref</td>
      </tr>
      <tr>
        <td id="L39" class="blob-num js-line-number" data-line-number="39"></td>
        <td id="LC39" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L40" class="blob-num js-line-number" data-line-number="40"></td>
        <td id="LC40" class="blob-code blob-code-inner js-file-line">    T <span class="pl-k">=</span> <span class="pl-c1">0.08</span><span class="pl-k">*</span>H_ref</td>
      </tr>
      <tr>
        <td id="L41" class="blob-num js-line-number" data-line-number="41"></td>
        <td id="LC41" class="blob-code blob-code-inner js-file-line">    B <span class="pl-k">=</span> <span class="pl-c1">0.12</span><span class="pl-k">*</span>H_ref</td>
      </tr>
      <tr>
        <td id="L42" class="blob-num js-line-number" data-line-number="42"></td>
        <td id="LC42" class="blob-code blob-code-inner js-file-line">    L <span class="pl-k">=</span> <span class="pl-c1">0.14</span><span class="pl-k">*</span>W_ref</td>
      </tr>
      <tr>
        <td id="L43" class="blob-num js-line-number" data-line-number="43"></td>
        <td id="LC43" class="blob-code blob-code-inner js-file-line">    R <span class="pl-k">=</span> <span class="pl-c1">0.04</span><span class="pl-k">*</span>W_ref</td>
      </tr>
      <tr>
        <td id="L44" class="blob-num js-line-number" data-line-number="44"></td>
        <td id="LC44" class="blob-code blob-code-inner js-file-line"> canvas <span class="pl-k">=</span> <span class="pl-c1">ROOT</span>.TCanvas(cname,cname,<span class="pl-c1">50</span>,<span class="pl-c1">50</span>,W,H)</td>
      </tr>
      <tr>
        <td id="L45" class="blob-num js-line-number" data-line-number="45"></td>
        <td id="LC45" class="blob-code blob-code-inner js-file-line"> canvas.SetFillColor(<span class="pl-c1">0</span>)</td>
      </tr>
      <tr>
        <td id="L46" class="blob-num js-line-number" data-line-number="46"></td>
        <td id="LC46" class="blob-code blob-code-inner js-file-line"> canvas.SetBorderMode(<span class="pl-c1">0</span>)</td>
      </tr>
      <tr>
        <td id="L47" class="blob-num js-line-number" data-line-number="47"></td>
        <td id="LC47" class="blob-code blob-code-inner js-file-line"> canvas.SetFrameFillStyle(<span class="pl-c1">0</span>)</td>
      </tr>
      <tr>
        <td id="L48" class="blob-num js-line-number" data-line-number="48"></td>
        <td id="LC48" class="blob-code blob-code-inner js-file-line"> canvas.SetFrameBorderMode(<span class="pl-c1">0</span>)</td>
      </tr>
      <tr>
        <td id="L49" class="blob-num js-line-number" data-line-number="49"></td>
        <td id="LC49" class="blob-code blob-code-inner js-file-line"> canvas.SetLeftMargin( L<span class="pl-k">/</span>W )</td>
      </tr>
      <tr>
        <td id="L50" class="blob-num js-line-number" data-line-number="50"></td>
        <td id="LC50" class="blob-code blob-code-inner js-file-line"> canvas.SetRightMargin( R<span class="pl-k">/</span>W )</td>
      </tr>
      <tr>
        <td id="L51" class="blob-num js-line-number" data-line-number="51"></td>
        <td id="LC51" class="blob-code blob-code-inner js-file-line"> canvas.SetTopMargin( T<span class="pl-k">/</span>H )</td>
      </tr>
      <tr>
        <td id="L52" class="blob-num js-line-number" data-line-number="52"></td>
        <td id="LC52" class="blob-code blob-code-inner js-file-line"> canvas.SetBottomMargin( B<span class="pl-k">/</span>H )</td>
      </tr>
      <tr>
        <td id="L53" class="blob-num js-line-number" data-line-number="53"></td>
        <td id="LC53" class="blob-code blob-code-inner js-file-line"> canvas.SetTickx()</td>
      </tr>
      <tr>
        <td id="L54" class="blob-num js-line-number" data-line-number="54"></td>
        <td id="LC54" class="blob-code blob-code-inner js-file-line"> canvas.SetTicky()</td>
      </tr>
      <tr>
        <td id="L55" class="blob-num js-line-number" data-line-number="55"></td>
        <td id="LC55" class="blob-code blob-code-inner js-file-line"> <span class="pl-c"><span class="pl-c">#</span>legend = getLegend()</span></td>
      </tr>
      <tr>
        <td id="L56" class="blob-num js-line-number" data-line-number="56"></td>
        <td id="LC56" class="blob-code blob-code-inner js-file-line"> </td>
      </tr>
      <tr>
        <td id="L57" class="blob-num js-line-number" data-line-number="57"></td>
        <td id="LC57" class="blob-code blob-code-inner js-file-line"> </td>
      </tr>
      <tr>
        <td id="L58" class="blob-num js-line-number" data-line-number="58"></td>
        <td id="LC58" class="blob-code blob-code-inner js-file-line"> pt <span class="pl-k">=</span> <span class="pl-c1">ROOT</span>.TPaveText(<span class="pl-c1">0.1746231</span>,<span class="pl-c1">0.6031469</span>,<span class="pl-c1">0.5251256</span>,<span class="pl-c1">0.7517483</span>,<span class="pl-s"><span class="pl-pds">&quot;</span>NDC<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L59" class="blob-num js-line-number" data-line-number="59"></td>
        <td id="LC59" class="blob-code blob-code-inner js-file-line"> pt.SetTextFont(<span class="pl-c1">42</span>)</td>
      </tr>
      <tr>
        <td id="L60" class="blob-num js-line-number" data-line-number="60"></td>
        <td id="LC60" class="blob-code blob-code-inner js-file-line"> pt.SetTextSize(<span class="pl-c1">0.04</span>)</td>
      </tr>
      <tr>
        <td id="L61" class="blob-num js-line-number" data-line-number="61"></td>
        <td id="LC61" class="blob-code blob-code-inner js-file-line"> pt.SetTextAlign(<span class="pl-c1">12</span>)</td>
      </tr>
      <tr>
        <td id="L62" class="blob-num js-line-number" data-line-number="62"></td>
        <td id="LC62" class="blob-code blob-code-inner js-file-line"> pt.SetFillColor(<span class="pl-c1">0</span>)</td>
      </tr>
      <tr>
        <td id="L63" class="blob-num js-line-number" data-line-number="63"></td>
        <td id="LC63" class="blob-code blob-code-inner js-file-line"> pt.SetBorderSize(<span class="pl-c1">0</span>)</td>
      </tr>
      <tr>
        <td id="L64" class="blob-num js-line-number" data-line-number="64"></td>
        <td id="LC64" class="blob-code blob-code-inner js-file-line"> pt.SetFillStyle(<span class="pl-c1">0</span>)</td>
      </tr>
      <tr>
        <td id="L65" class="blob-num js-line-number" data-line-number="65"></td>
        <td id="LC65" class="blob-code blob-code-inner js-file-line"> </td>
      </tr>
      <tr>
        <td id="L66" class="blob-num js-line-number" data-line-number="66"></td>
        <td id="LC66" class="blob-code blob-code-inner js-file-line"> </td>
      </tr>
      <tr>
        <td id="L67" class="blob-num js-line-number" data-line-number="67"></td>
        <td id="LC67" class="blob-code blob-code-inner js-file-line"> <span class="pl-k">return</span> canvas, pt</td>
      </tr>
      <tr>
        <td id="L68" class="blob-num js-line-number" data-line-number="68"></td>
        <td id="LC68" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L69" class="blob-num js-line-number" data-line-number="69"></td>
        <td id="LC69" class="blob-code blob-code-inner js-file-line">	</td>
      </tr>
      <tr>
        <td id="L70" class="blob-num js-line-number" data-line-number="70"></td>
        <td id="LC70" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">getMVVPdf</span>(<span class="pl-smi">w</span>,<span class="pl-smi">j</span>,<span class="pl-smi">MH</span>,<span class="pl-smi">postfix</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-pds">&quot;</span></span>):</td>
      </tr>
      <tr>
        <td id="L71" class="blob-num js-line-number" data-line-number="71"></td>
        <td id="LC71" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L72" class="blob-num js-line-number" data-line-number="72"></td>
        <td id="LC72" class="blob-code blob-code-inner js-file-line">        var <span class="pl-k">=</span> w.var(options.var)</td>
      </tr>
      <tr>
        <td id="L73" class="blob-num js-line-number" data-line-number="73"></td>
        <td id="LC73" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L74" class="blob-num js-line-number" data-line-number="74"></td>
        <td id="LC74" class="blob-code blob-code-inner js-file-line">        pdfName 	<span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span>signal_<span class="pl-c1">%d%s</span><span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span>(<span class="pl-c1">MH</span>,postfix)</td>
      </tr>
      <tr>
        <td id="L75" class="blob-num js-line-number" data-line-number="75"></td>
        <td id="LC75" class="blob-code blob-code-inner js-file-line">        Jmean 		<span class="pl-k">=</span> <span class="pl-c1">eval</span>(j[<span class="pl-s"><span class="pl-pds">&#39;</span>MEAN<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L76" class="blob-num js-line-number" data-line-number="76"></td>
        <td id="LC76" class="blob-code blob-code-inner js-file-line">        Jsigma		<span class="pl-k">=</span> <span class="pl-c1">eval</span>(j[<span class="pl-s"><span class="pl-pds">&#39;</span>SIGMA<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L77" class="blob-num js-line-number" data-line-number="77"></td>
        <td id="LC77" class="blob-code blob-code-inner js-file-line">        Jalpha1     <span class="pl-k">=</span> <span class="pl-c1">eval</span>(j[<span class="pl-s"><span class="pl-pds">&#39;</span>ALPHA1<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L78" class="blob-num js-line-number" data-line-number="78"></td>
        <td id="LC78" class="blob-code blob-code-inner js-file-line">        Jalpha2     <span class="pl-k">=</span> <span class="pl-c1">eval</span>(j[<span class="pl-s"><span class="pl-pds">&#39;</span>ALPHA2<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L79" class="blob-num js-line-number" data-line-number="79"></td>
        <td id="LC79" class="blob-code blob-code-inner js-file-line">        Jn1 		<span class="pl-k">=</span> <span class="pl-c1">eval</span>(j[<span class="pl-s"><span class="pl-pds">&#39;</span>N1<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L80" class="blob-num js-line-number" data-line-number="80"></td>
        <td id="LC80" class="blob-code blob-code-inner js-file-line">        Jn2 		<span class="pl-k">=</span> <span class="pl-c1">eval</span>(j[<span class="pl-s"><span class="pl-pds">&#39;</span>N2<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L81" class="blob-num js-line-number" data-line-number="81"></td>
        <td id="LC81" class="blob-code blob-code-inner js-file-line">        </td>
      </tr>
      <tr>
        <td id="L82" class="blob-num js-line-number" data-line-number="82"></td>
        <td id="LC82" class="blob-code blob-code-inner js-file-line">        mean        <span class="pl-k">=</span> <span class="pl-c1">ROOT</span>.RooRealVar(<span class="pl-s"><span class="pl-pds">&quot;</span>mean_<span class="pl-c1">%d%s</span><span class="pl-pds">&quot;</span></span><span class="pl-k">%</span>(<span class="pl-c1">MH</span>,postfix),<span class="pl-s"><span class="pl-pds">&quot;</span>mean_<span class="pl-c1">%d%s</span><span class="pl-pds">&quot;</span></span><span class="pl-k">%</span>(<span class="pl-c1">MH</span>,postfix),Jmean)</td>
      </tr>
      <tr>
        <td id="L83" class="blob-num js-line-number" data-line-number="83"></td>
        <td id="LC83" class="blob-code blob-code-inner js-file-line">        sigma       <span class="pl-k">=</span> <span class="pl-c1">ROOT</span>.RooRealVar(<span class="pl-s"><span class="pl-pds">&quot;</span>sigma_<span class="pl-c1">%d%s</span><span class="pl-pds">&quot;</span></span><span class="pl-k">%</span>(<span class="pl-c1">MH</span>,postfix),<span class="pl-s"><span class="pl-pds">&quot;</span>sigma_<span class="pl-c1">%d%s</span><span class="pl-pds">&quot;</span></span><span class="pl-k">%</span>(<span class="pl-c1">MH</span>,postfix),Jsigma)        </td>
      </tr>
      <tr>
        <td id="L84" class="blob-num js-line-number" data-line-number="84"></td>
        <td id="LC84" class="blob-code blob-code-inner js-file-line">        alpha1      <span class="pl-k">=</span> <span class="pl-c1">ROOT</span>.RooRealVar(<span class="pl-s"><span class="pl-pds">&quot;</span>alpha1_<span class="pl-c1">%d%s</span><span class="pl-pds">&quot;</span></span><span class="pl-k">%</span>(<span class="pl-c1">MH</span>,postfix),<span class="pl-s"><span class="pl-pds">&quot;</span>alpha1_<span class="pl-c1">%d%s</span><span class="pl-pds">&quot;</span></span><span class="pl-k">%</span>(<span class="pl-c1">MH</span>,postfix),Jalpha1)</td>
      </tr>
      <tr>
        <td id="L85" class="blob-num js-line-number" data-line-number="85"></td>
        <td id="LC85" class="blob-code blob-code-inner js-file-line">        alpha2      <span class="pl-k">=</span> <span class="pl-c1">ROOT</span>.RooRealVar(<span class="pl-s"><span class="pl-pds">&quot;</span>alpha2_<span class="pl-c1">%d%s</span><span class="pl-pds">&quot;</span></span><span class="pl-k">%</span>(<span class="pl-c1">MH</span>,postfix),<span class="pl-s"><span class="pl-pds">&quot;</span>alpha2_<span class="pl-c1">%d%s</span><span class="pl-pds">&quot;</span></span><span class="pl-k">%</span>(<span class="pl-c1">MH</span>,postfix),Jalpha2)</td>
      </tr>
      <tr>
        <td id="L86" class="blob-num js-line-number" data-line-number="86"></td>
        <td id="LC86" class="blob-code blob-code-inner js-file-line">        n1          <span class="pl-k">=</span> <span class="pl-c1">ROOT</span>.RooRealVar(<span class="pl-s"><span class="pl-pds">&quot;</span>n1_<span class="pl-c1">%d%s</span><span class="pl-pds">&quot;</span></span><span class="pl-k">%</span>(<span class="pl-c1">MH</span>,postfix),<span class="pl-s"><span class="pl-pds">&quot;</span>n1_<span class="pl-c1">%d%s</span><span class="pl-pds">&quot;</span></span><span class="pl-k">%</span>(<span class="pl-c1">MH</span>,postfix),Jn1)</td>
      </tr>
      <tr>
        <td id="L87" class="blob-num js-line-number" data-line-number="87"></td>
        <td id="LC87" class="blob-code blob-code-inner js-file-line">        n2          <span class="pl-k">=</span> <span class="pl-c1">ROOT</span>.RooRealVar(<span class="pl-s"><span class="pl-pds">&quot;</span>n2_<span class="pl-c1">%d%s</span><span class="pl-pds">&quot;</span></span><span class="pl-k">%</span>(<span class="pl-c1">MH</span>,postfix),<span class="pl-s"><span class="pl-pds">&quot;</span>n2_<span class="pl-c1">%d%s</span><span class="pl-pds">&quot;</span></span><span class="pl-k">%</span>(<span class="pl-c1">MH</span>,postfix),Jn2)</td>
      </tr>
      <tr>
        <td id="L88" class="blob-num js-line-number" data-line-number="88"></td>
        <td id="LC88" class="blob-code blob-code-inner js-file-line">        </td>
      </tr>
      <tr>
        <td id="L89" class="blob-num js-line-number" data-line-number="89"></td>
        <td id="LC89" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L90" class="blob-num js-line-number" data-line-number="90"></td>
        <td id="LC90" class="blob-code blob-code-inner js-file-line">        alpha1.setConstant(<span class="pl-c1">ROOT</span>.kTRUE)</td>
      </tr>
      <tr>
        <td id="L91" class="blob-num js-line-number" data-line-number="91"></td>
        <td id="LC91" class="blob-code blob-code-inner js-file-line">        alpha2.setConstant(<span class="pl-c1">ROOT</span>.kTRUE)</td>
      </tr>
      <tr>
        <td id="L92" class="blob-num js-line-number" data-line-number="92"></td>
        <td id="LC92" class="blob-code blob-code-inner js-file-line">        n2.setConstant(<span class="pl-c1">ROOT</span>.kTRUE)</td>
      </tr>
      <tr>
        <td id="L93" class="blob-num js-line-number" data-line-number="93"></td>
        <td id="LC93" class="blob-code blob-code-inner js-file-line">        n1.setConstant(<span class="pl-c1">ROOT</span>.kTRUE)</td>
      </tr>
      <tr>
        <td id="L94" class="blob-num js-line-number" data-line-number="94"></td>
        <td id="LC94" class="blob-code blob-code-inner js-file-line">        mean.setConstant(<span class="pl-c1">ROOT</span>.kTRUE)</td>
      </tr>
      <tr>
        <td id="L95" class="blob-num js-line-number" data-line-number="95"></td>
        <td id="LC95" class="blob-code blob-code-inner js-file-line">        sigma.setConstant(<span class="pl-c1">ROOT</span>.kTRUE)</td>
      </tr>
      <tr>
        <td id="L96" class="blob-num js-line-number" data-line-number="96"></td>
        <td id="LC96" class="blob-code blob-code-inner js-file-line">                </td>
      </tr>
      <tr>
        <td id="L97" class="blob-num js-line-number" data-line-number="97"></td>
        <td id="LC97" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> gauss     = ROOT.RooGaussian(&quot;gauss_%d%s&quot;%(MH,postfix), &quot;gauss_%d%s&quot;%(MH,postfix), var, mean, gsigma)</span></td>
      </tr>
      <tr>
        <td id="L98" class="blob-num js-line-number" data-line-number="98"></td>
        <td id="LC98" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> cb        = ROOT.RooCBShape(&quot;cb_%d%s&quot;%(MH,postfix), &quot;cb_%d%s&quot;%(MH,postfix),var, mean, sigma, alpha, sign)</span></td>
      </tr>
      <tr>
        <td id="L99" class="blob-num js-line-number" data-line-number="99"></td>
        <td id="LC99" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> function = ROOT.RooAddPdf(pdfName, pdfName,gauss, cb, sigfrac)</span></td>
      </tr>
      <tr>
        <td id="L100" class="blob-num js-line-number" data-line-number="100"></td>
        <td id="LC100" class="blob-code blob-code-inner js-file-line">        function <span class="pl-k">=</span> <span class="pl-c1">ROOT</span>.RooDoubleCB(pdfName, pdfName,var, mean,sigma,alpha1,n1,alpha2,n2)</td>
      </tr>
      <tr>
        <td id="L101" class="blob-num js-line-number" data-line-number="101"></td>
        <td id="LC101" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">getattr</span>(w,<span class="pl-s"><span class="pl-pds">&#39;</span>import<span class="pl-pds">&#39;</span></span>)(function,<span class="pl-c1">ROOT</span>.RooFit.Rename(pdfName))</td>
      </tr>
      <tr>
        <td id="L102" class="blob-num js-line-number" data-line-number="102"></td>
        <td id="LC102" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L103" class="blob-num js-line-number" data-line-number="103"></td>
        <td id="LC103" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">getMJPdf</span>(<span class="pl-smi">w</span>,<span class="pl-smi">j</span>,<span class="pl-smi">MH</span>,<span class="pl-smi">postfix</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-pds">&quot;</span></span>,<span class="pl-smi">jH</span><span class="pl-k">=</span><span class="pl-c1">None</span>):</td>
      </tr>
      <tr>
        <td id="L104" class="blob-num js-line-number" data-line-number="104"></td>
        <td id="LC104" class="blob-code blob-code-inner js-file-line">        </td>
      </tr>
      <tr>
        <td id="L105" class="blob-num js-line-number" data-line-number="105"></td>
        <td id="LC105" class="blob-code blob-code-inner js-file-line">        var <span class="pl-k">=</span> w.var(options.var)</td>
      </tr>
      <tr>
        <td id="L106" class="blob-num js-line-number" data-line-number="106"></td>
        <td id="LC106" class="blob-code blob-code-inner js-file-line">	<span class="pl-k">if</span> postfix.find(<span class="pl-s"><span class="pl-pds">&quot;</span>H<span class="pl-pds">&quot;</span></span>)<span class="pl-k">==</span><span class="pl-k">-</span><span class="pl-c1">1</span>:</td>
      </tr>
      <tr>
        <td id="L107" class="blob-num js-line-number" data-line-number="107"></td>
        <td id="LC107" class="blob-code blob-code-inner js-file-line">            pdfName 	<span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span>signal_<span class="pl-c1">%d%s</span><span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span>(<span class="pl-c1">MH</span>,postfix)</td>
      </tr>
      <tr>
        <td id="L108" class="blob-num js-line-number" data-line-number="108"></td>
        <td id="LC108" class="blob-code blob-code-inner js-file-line">            Jmean 		<span class="pl-k">=</span> <span class="pl-c1">eval</span>(j[<span class="pl-s"><span class="pl-pds">&#39;</span>mean<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L109" class="blob-num js-line-number" data-line-number="109"></td>
        <td id="LC109" class="blob-code blob-code-inner js-file-line">            Jsigma		<span class="pl-k">=</span> <span class="pl-c1">eval</span>(j[<span class="pl-s"><span class="pl-pds">&#39;</span>sigma<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L110" class="blob-num js-line-number" data-line-number="110"></td>
        <td id="LC110" class="blob-code blob-code-inner js-file-line">            Jalpha 		<span class="pl-k">=</span> <span class="pl-c1">eval</span>(j[<span class="pl-s"><span class="pl-pds">&#39;</span>alpha<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L111" class="blob-num js-line-number" data-line-number="111"></td>
        <td id="LC111" class="blob-code blob-code-inner js-file-line">            Jalpha2 	<span class="pl-k">=</span> <span class="pl-c1">eval</span>(j[<span class="pl-s"><span class="pl-pds">&#39;</span>alpha2<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L112" class="blob-num js-line-number" data-line-number="112"></td>
        <td id="LC112" class="blob-code blob-code-inner js-file-line">            Jn 		<span class="pl-k">=</span> <span class="pl-c1">eval</span>(j[<span class="pl-s"><span class="pl-pds">&#39;</span>n<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L113" class="blob-num js-line-number" data-line-number="113"></td>
        <td id="LC113" class="blob-code blob-code-inner js-file-line">            Jn2 		<span class="pl-k">=</span> <span class="pl-c1">eval</span>(j[<span class="pl-s"><span class="pl-pds">&#39;</span>n2<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L114" class="blob-num js-line-number" data-line-number="114"></td>
        <td id="LC114" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L115" class="blob-num js-line-number" data-line-number="115"></td>
        <td id="LC115" class="blob-code blob-code-inner js-file-line">            mean        <span class="pl-k">=</span> <span class="pl-c1">ROOT</span>.RooRealVar(<span class="pl-s"><span class="pl-pds">&quot;</span>mean_<span class="pl-c1">%d%s</span><span class="pl-pds">&quot;</span></span><span class="pl-k">%</span>(<span class="pl-c1">MH</span>,postfix),<span class="pl-s"><span class="pl-pds">&quot;</span>mean_<span class="pl-c1">%d%s</span><span class="pl-pds">&quot;</span></span><span class="pl-k">%</span>(<span class="pl-c1">MH</span>,postfix),Jmean)</td>
      </tr>
      <tr>
        <td id="L116" class="blob-num js-line-number" data-line-number="116"></td>
        <td id="LC116" class="blob-code blob-code-inner js-file-line">            sigma       <span class="pl-k">=</span> <span class="pl-c1">ROOT</span>.RooRealVar(<span class="pl-s"><span class="pl-pds">&quot;</span>sigma_<span class="pl-c1">%d%s</span><span class="pl-pds">&quot;</span></span><span class="pl-k">%</span>(<span class="pl-c1">MH</span>,postfix),<span class="pl-s"><span class="pl-pds">&quot;</span>sigma_<span class="pl-c1">%d%s</span><span class="pl-pds">&quot;</span></span><span class="pl-k">%</span>(<span class="pl-c1">MH</span>,postfix),Jsigma)</td>
      </tr>
      <tr>
        <td id="L117" class="blob-num js-line-number" data-line-number="117"></td>
        <td id="LC117" class="blob-code blob-code-inner js-file-line">            alpha       <span class="pl-k">=</span> <span class="pl-c1">ROOT</span>.RooRealVar(<span class="pl-s"><span class="pl-pds">&quot;</span>alpha_<span class="pl-c1">%d%s</span><span class="pl-pds">&quot;</span></span><span class="pl-k">%</span>(<span class="pl-c1">MH</span>,postfix),<span class="pl-s"><span class="pl-pds">&quot;</span>alpha_<span class="pl-c1">%d%s</span><span class="pl-pds">&quot;</span></span><span class="pl-k">%</span>(<span class="pl-c1">MH</span>,postfix),Jalpha)</td>
      </tr>
      <tr>
        <td id="L118" class="blob-num js-line-number" data-line-number="118"></td>
        <td id="LC118" class="blob-code blob-code-inner js-file-line">            alpha2      <span class="pl-k">=</span> <span class="pl-c1">ROOT</span>.RooRealVar(<span class="pl-s"><span class="pl-pds">&quot;</span>alpha2_<span class="pl-c1">%d%s</span><span class="pl-pds">&quot;</span></span><span class="pl-k">%</span>(<span class="pl-c1">MH</span>,postfix),<span class="pl-s"><span class="pl-pds">&quot;</span>alpha2_<span class="pl-c1">%d%s</span><span class="pl-pds">&quot;</span></span><span class="pl-k">%</span>(<span class="pl-c1">MH</span>,postfix),Jalpha2)</td>
      </tr>
      <tr>
        <td id="L119" class="blob-num js-line-number" data-line-number="119"></td>
        <td id="LC119" class="blob-code blob-code-inner js-file-line">            sign        <span class="pl-k">=</span> <span class="pl-c1">ROOT</span>.RooRealVar(<span class="pl-s"><span class="pl-pds">&quot;</span>sign_<span class="pl-c1">%d%s</span><span class="pl-pds">&quot;</span></span><span class="pl-k">%</span>(<span class="pl-c1">MH</span>,postfix),<span class="pl-s"><span class="pl-pds">&quot;</span>sign_<span class="pl-c1">%d%s</span><span class="pl-pds">&quot;</span></span><span class="pl-k">%</span>(<span class="pl-c1">MH</span>,postfix),Jn)</td>
      </tr>
      <tr>
        <td id="L120" class="blob-num js-line-number" data-line-number="120"></td>
        <td id="LC120" class="blob-code blob-code-inner js-file-line">            sign2        <span class="pl-k">=</span> <span class="pl-c1">ROOT</span>.RooRealVar(<span class="pl-s"><span class="pl-pds">&quot;</span>sign2_<span class="pl-c1">%d%s</span><span class="pl-pds">&quot;</span></span><span class="pl-k">%</span>(<span class="pl-c1">MH</span>,postfix),<span class="pl-s"><span class="pl-pds">&quot;</span>sign2_<span class="pl-c1">%d%s</span><span class="pl-pds">&quot;</span></span><span class="pl-k">%</span>(<span class="pl-c1">MH</span>,postfix),Jn2)        </td>
      </tr>
      <tr>
        <td id="L121" class="blob-num js-line-number" data-line-number="121"></td>
        <td id="LC121" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L122" class="blob-num js-line-number" data-line-number="122"></td>
        <td id="LC122" class="blob-code blob-code-inner js-file-line">            alpha.setConstant(<span class="pl-c1">ROOT</span>.kTRUE)</td>
      </tr>
      <tr>
        <td id="L123" class="blob-num js-line-number" data-line-number="123"></td>
        <td id="LC123" class="blob-code blob-code-inner js-file-line">            sign.setConstant(<span class="pl-c1">ROOT</span>.kTRUE)</td>
      </tr>
      <tr>
        <td id="L124" class="blob-num js-line-number" data-line-number="124"></td>
        <td id="LC124" class="blob-code blob-code-inner js-file-line">            alpha2.setConstant(<span class="pl-c1">ROOT</span>.kTRUE)</td>
      </tr>
      <tr>
        <td id="L125" class="blob-num js-line-number" data-line-number="125"></td>
        <td id="LC125" class="blob-code blob-code-inner js-file-line">            sign2.setConstant(<span class="pl-c1">ROOT</span>.kTRUE)</td>
      </tr>
      <tr>
        <td id="L126" class="blob-num js-line-number" data-line-number="126"></td>
        <td id="LC126" class="blob-code blob-code-inner js-file-line">            mean.setConstant(<span class="pl-c1">ROOT</span>.kTRUE)</td>
      </tr>
      <tr>
        <td id="L127" class="blob-num js-line-number" data-line-number="127"></td>
        <td id="LC127" class="blob-code blob-code-inner js-file-line">            sigma.setConstant(<span class="pl-c1">ROOT</span>.kTRUE)</td>
      </tr>
      <tr>
        <td id="L128" class="blob-num js-line-number" data-line-number="128"></td>
        <td id="LC128" class="blob-code blob-code-inner js-file-line">            </td>
      </tr>
      <tr>
        <td id="L129" class="blob-num js-line-number" data-line-number="129"></td>
        <td id="LC129" class="blob-code blob-code-inner js-file-line">            function <span class="pl-k">=</span> <span class="pl-c1">ROOT</span>.RooDoubleCB(pdfName, pdfName, var, mean, sigma, alpha, sign,  alpha2, sign2)  </td>
      </tr>
      <tr>
        <td id="L130" class="blob-num js-line-number" data-line-number="130"></td>
        <td id="LC130" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">getattr</span>(w,<span class="pl-s"><span class="pl-pds">&#39;</span>import<span class="pl-pds">&#39;</span></span>)(function,<span class="pl-c1">ROOT</span>.RooFit.Rename(pdfName))</td>
      </tr>
      <tr>
        <td id="L131" class="blob-num js-line-number" data-line-number="131"></td>
        <td id="LC131" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L132" class="blob-num js-line-number" data-line-number="132"></td>
        <td id="LC132" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> postfix <span class="pl-k">==</span><span class="pl-s"><span class="pl-pds">&quot;</span>H<span class="pl-pds">&quot;</span></span>: postfix <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L133" class="blob-num js-line-number" data-line-number="133"></td>
        <td id="LC133" class="blob-code blob-code-inner js-file-line">            pdfName 	<span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span>signal_<span class="pl-c1">%d%s</span><span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span>(<span class="pl-c1">MH</span>,postfix)</td>
      </tr>
      <tr>
        <td id="L134" class="blob-num js-line-number" data-line-number="134"></td>
        <td id="LC134" class="blob-code blob-code-inner js-file-line">            Jmean 		<span class="pl-k">=</span> <span class="pl-c1">eval</span>(j[<span class="pl-s"><span class="pl-pds">&#39;</span>mean<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L135" class="blob-num js-line-number" data-line-number="135"></td>
        <td id="LC135" class="blob-code blob-code-inner js-file-line">            Jsigma		<span class="pl-k">=</span> <span class="pl-c1">eval</span>(j[<span class="pl-s"><span class="pl-pds">&#39;</span>sigma<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L136" class="blob-num js-line-number" data-line-number="136"></td>
        <td id="LC136" class="blob-code blob-code-inner js-file-line">            Jalpha 		<span class="pl-k">=</span> <span class="pl-c1">eval</span>(j[<span class="pl-s"><span class="pl-pds">&#39;</span>alpha<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L137" class="blob-num js-line-number" data-line-number="137"></td>
        <td id="LC137" class="blob-code blob-code-inner js-file-line">            Jalpha2 	<span class="pl-k">=</span> <span class="pl-c1">eval</span>(j[<span class="pl-s"><span class="pl-pds">&#39;</span>alpha2<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L138" class="blob-num js-line-number" data-line-number="138"></td>
        <td id="LC138" class="blob-code blob-code-inner js-file-line">            Jn 		<span class="pl-k">=</span> <span class="pl-c1">eval</span>(j[<span class="pl-s"><span class="pl-pds">&#39;</span>n<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L139" class="blob-num js-line-number" data-line-number="139"></td>
        <td id="LC139" class="blob-code blob-code-inner js-file-line">            Jn2 		<span class="pl-k">=</span> <span class="pl-c1">eval</span>(j[<span class="pl-s"><span class="pl-pds">&#39;</span>n2<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L140" class="blob-num js-line-number" data-line-number="140"></td>
        <td id="LC140" class="blob-code blob-code-inner js-file-line">            </td>
      </tr>
      <tr>
        <td id="L141" class="blob-num js-line-number" data-line-number="141"></td>
        <td id="LC141" class="blob-code blob-code-inner js-file-line">            JmeanH 		<span class="pl-k">=</span> <span class="pl-c1">eval</span>(jH[<span class="pl-s"><span class="pl-pds">&#39;</span>meanH<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L142" class="blob-num js-line-number" data-line-number="142"></td>
        <td id="LC142" class="blob-code blob-code-inner js-file-line">            JsigmaH		<span class="pl-k">=</span> <span class="pl-c1">eval</span>(jH[<span class="pl-s"><span class="pl-pds">&#39;</span>sigmaH<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L143" class="blob-num js-line-number" data-line-number="143"></td>
        <td id="LC143" class="blob-code blob-code-inner js-file-line">            JalphaH 		<span class="pl-k">=</span> <span class="pl-c1">eval</span>(jH[<span class="pl-s"><span class="pl-pds">&#39;</span>alphaH<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L144" class="blob-num js-line-number" data-line-number="144"></td>
        <td id="LC144" class="blob-code blob-code-inner js-file-line">            Jalpha2H 	<span class="pl-k">=</span> <span class="pl-c1">eval</span>(jH[<span class="pl-s"><span class="pl-pds">&#39;</span>alpha2H<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L145" class="blob-num js-line-number" data-line-number="145"></td>
        <td id="LC145" class="blob-code blob-code-inner js-file-line">            JnH 		<span class="pl-k">=</span> <span class="pl-c1">eval</span>(jH[<span class="pl-s"><span class="pl-pds">&#39;</span>nH<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L146" class="blob-num js-line-number" data-line-number="146"></td>
        <td id="LC146" class="blob-code blob-code-inner js-file-line">            Jn2H 		<span class="pl-k">=</span> <span class="pl-c1">eval</span>(jH[<span class="pl-s"><span class="pl-pds">&#39;</span>n2H<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L147" class="blob-num js-line-number" data-line-number="147"></td>
        <td id="LC147" class="blob-code blob-code-inner js-file-line">            </td>
      </tr>
      <tr>
        <td id="L148" class="blob-num js-line-number" data-line-number="148"></td>
        <td id="LC148" class="blob-code blob-code-inner js-file-line">            </td>
      </tr>
      <tr>
        <td id="L149" class="blob-num js-line-number" data-line-number="149"></td>
        <td id="LC149" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L150" class="blob-num js-line-number" data-line-number="150"></td>
        <td id="LC150" class="blob-code blob-code-inner js-file-line">            mean        <span class="pl-k">=</span> <span class="pl-c1">ROOT</span>.RooRealVar(<span class="pl-s"><span class="pl-pds">&quot;</span>mean_<span class="pl-c1">%d%s</span><span class="pl-pds">&quot;</span></span><span class="pl-k">%</span>(<span class="pl-c1">MH</span>,postfix),<span class="pl-s"><span class="pl-pds">&quot;</span>mean_<span class="pl-c1">%d%s</span><span class="pl-pds">&quot;</span></span><span class="pl-k">%</span>(<span class="pl-c1">MH</span>,postfix),Jmean)</td>
      </tr>
      <tr>
        <td id="L151" class="blob-num js-line-number" data-line-number="151"></td>
        <td id="LC151" class="blob-code blob-code-inner js-file-line">            sigma       <span class="pl-k">=</span> <span class="pl-c1">ROOT</span>.RooRealVar(<span class="pl-s"><span class="pl-pds">&quot;</span>sigma_<span class="pl-c1">%d%s</span><span class="pl-pds">&quot;</span></span><span class="pl-k">%</span>(<span class="pl-c1">MH</span>,postfix),<span class="pl-s"><span class="pl-pds">&quot;</span>sigma_<span class="pl-c1">%d%s</span><span class="pl-pds">&quot;</span></span><span class="pl-k">%</span>(<span class="pl-c1">MH</span>,postfix),Jsigma)</td>
      </tr>
      <tr>
        <td id="L152" class="blob-num js-line-number" data-line-number="152"></td>
        <td id="LC152" class="blob-code blob-code-inner js-file-line">            alpha       <span class="pl-k">=</span> <span class="pl-c1">ROOT</span>.RooRealVar(<span class="pl-s"><span class="pl-pds">&quot;</span>alpha_<span class="pl-c1">%d%s</span><span class="pl-pds">&quot;</span></span><span class="pl-k">%</span>(<span class="pl-c1">MH</span>,postfix),<span class="pl-s"><span class="pl-pds">&quot;</span>alpha_<span class="pl-c1">%d%s</span><span class="pl-pds">&quot;</span></span><span class="pl-k">%</span>(<span class="pl-c1">MH</span>,postfix),Jalpha)</td>
      </tr>
      <tr>
        <td id="L153" class="blob-num js-line-number" data-line-number="153"></td>
        <td id="LC153" class="blob-code blob-code-inner js-file-line">            alpha2      <span class="pl-k">=</span> <span class="pl-c1">ROOT</span>.RooRealVar(<span class="pl-s"><span class="pl-pds">&quot;</span>alpha2_<span class="pl-c1">%d%s</span><span class="pl-pds">&quot;</span></span><span class="pl-k">%</span>(<span class="pl-c1">MH</span>,postfix),<span class="pl-s"><span class="pl-pds">&quot;</span>alpha2_<span class="pl-c1">%d%s</span><span class="pl-pds">&quot;</span></span><span class="pl-k">%</span>(<span class="pl-c1">MH</span>,postfix),Jalpha2)</td>
      </tr>
      <tr>
        <td id="L154" class="blob-num js-line-number" data-line-number="154"></td>
        <td id="LC154" class="blob-code blob-code-inner js-file-line">            sign        <span class="pl-k">=</span> <span class="pl-c1">ROOT</span>.RooRealVar(<span class="pl-s"><span class="pl-pds">&quot;</span>sign_<span class="pl-c1">%d%s</span><span class="pl-pds">&quot;</span></span><span class="pl-k">%</span>(<span class="pl-c1">MH</span>,postfix),<span class="pl-s"><span class="pl-pds">&quot;</span>sign_<span class="pl-c1">%d%s</span><span class="pl-pds">&quot;</span></span><span class="pl-k">%</span>(<span class="pl-c1">MH</span>,postfix),Jn)</td>
      </tr>
      <tr>
        <td id="L155" class="blob-num js-line-number" data-line-number="155"></td>
        <td id="LC155" class="blob-code blob-code-inner js-file-line">            sign2        <span class="pl-k">=</span> <span class="pl-c1">ROOT</span>.RooRealVar(<span class="pl-s"><span class="pl-pds">&quot;</span>sign2_<span class="pl-c1">%d%s</span><span class="pl-pds">&quot;</span></span><span class="pl-k">%</span>(<span class="pl-c1">MH</span>,postfix),<span class="pl-s"><span class="pl-pds">&quot;</span>sign2_<span class="pl-c1">%d%s</span><span class="pl-pds">&quot;</span></span><span class="pl-k">%</span>(<span class="pl-c1">MH</span>,postfix),Jn2)</td>
      </tr>
      <tr>
        <td id="L156" class="blob-num js-line-number" data-line-number="156"></td>
        <td id="LC156" class="blob-code blob-code-inner js-file-line">            </td>
      </tr>
      <tr>
        <td id="L157" class="blob-num js-line-number" data-line-number="157"></td>
        <td id="LC157" class="blob-code blob-code-inner js-file-line">            meanH        <span class="pl-k">=</span> <span class="pl-c1">ROOT</span>.RooRealVar(<span class="pl-s"><span class="pl-pds">&quot;</span>Hmean_<span class="pl-c1">%d%s</span><span class="pl-pds">&quot;</span></span><span class="pl-k">%</span>(<span class="pl-c1">MH</span>,postfix),<span class="pl-s"><span class="pl-pds">&quot;</span>Hmean_<span class="pl-c1">%d%s</span><span class="pl-pds">&quot;</span></span><span class="pl-k">%</span>(<span class="pl-c1">MH</span>,postfix),JmeanH)</td>
      </tr>
      <tr>
        <td id="L158" class="blob-num js-line-number" data-line-number="158"></td>
        <td id="LC158" class="blob-code blob-code-inner js-file-line">            sigmaH       <span class="pl-k">=</span> <span class="pl-c1">ROOT</span>.RooRealVar(<span class="pl-s"><span class="pl-pds">&quot;</span>Hsigma_<span class="pl-c1">%d%s</span><span class="pl-pds">&quot;</span></span><span class="pl-k">%</span>(<span class="pl-c1">MH</span>,postfix),<span class="pl-s"><span class="pl-pds">&quot;</span>Hsigma_<span class="pl-c1">%d%s</span><span class="pl-pds">&quot;</span></span><span class="pl-k">%</span>(<span class="pl-c1">MH</span>,postfix),JsigmaH)</td>
      </tr>
      <tr>
        <td id="L159" class="blob-num js-line-number" data-line-number="159"></td>
        <td id="LC159" class="blob-code blob-code-inner js-file-line">            alphaH       <span class="pl-k">=</span> <span class="pl-c1">ROOT</span>.RooRealVar(<span class="pl-s"><span class="pl-pds">&quot;</span>Halpha_<span class="pl-c1">%d%s</span><span class="pl-pds">&quot;</span></span><span class="pl-k">%</span>(<span class="pl-c1">MH</span>,postfix),<span class="pl-s"><span class="pl-pds">&quot;</span>Halpha_<span class="pl-c1">%d%s</span><span class="pl-pds">&quot;</span></span><span class="pl-k">%</span>(<span class="pl-c1">MH</span>,postfix),JalphaH)</td>
      </tr>
      <tr>
        <td id="L160" class="blob-num js-line-number" data-line-number="160"></td>
        <td id="LC160" class="blob-code blob-code-inner js-file-line">            alpha2H      <span class="pl-k">=</span> <span class="pl-c1">ROOT</span>.RooRealVar(<span class="pl-s"><span class="pl-pds">&quot;</span>Halpha2_<span class="pl-c1">%d%s</span><span class="pl-pds">&quot;</span></span><span class="pl-k">%</span>(<span class="pl-c1">MH</span>,postfix),<span class="pl-s"><span class="pl-pds">&quot;</span>Halpha2_<span class="pl-c1">%d%s</span><span class="pl-pds">&quot;</span></span><span class="pl-k">%</span>(<span class="pl-c1">MH</span>,postfix),Jalpha2H)</td>
      </tr>
      <tr>
        <td id="L161" class="blob-num js-line-number" data-line-number="161"></td>
        <td id="LC161" class="blob-code blob-code-inner js-file-line">            signH        <span class="pl-k">=</span> <span class="pl-c1">ROOT</span>.RooRealVar(<span class="pl-s"><span class="pl-pds">&quot;</span>Hsign_<span class="pl-c1">%d%s</span><span class="pl-pds">&quot;</span></span><span class="pl-k">%</span>(<span class="pl-c1">MH</span>,postfix),<span class="pl-s"><span class="pl-pds">&quot;</span>Hsign_<span class="pl-c1">%d%s</span><span class="pl-pds">&quot;</span></span><span class="pl-k">%</span>(<span class="pl-c1">MH</span>,postfix),JnH)</td>
      </tr>
      <tr>
        <td id="L162" class="blob-num js-line-number" data-line-number="162"></td>
        <td id="LC162" class="blob-code blob-code-inner js-file-line">            sign2H        <span class="pl-k">=</span> <span class="pl-c1">ROOT</span>.RooRealVar(<span class="pl-s"><span class="pl-pds">&quot;</span>Hsign2_<span class="pl-c1">%d%s</span><span class="pl-pds">&quot;</span></span><span class="pl-k">%</span>(<span class="pl-c1">MH</span>,postfix),<span class="pl-s"><span class="pl-pds">&quot;</span>Hsign2_<span class="pl-c1">%d%s</span><span class="pl-pds">&quot;</span></span><span class="pl-k">%</span>(<span class="pl-c1">MH</span>,postfix),Jn2H)</td>
      </tr>
      <tr>
        <td id="L163" class="blob-num js-line-number" data-line-number="163"></td>
        <td id="LC163" class="blob-code blob-code-inner js-file-line">            </td>
      </tr>
      <tr>
        <td id="L164" class="blob-num js-line-number" data-line-number="164"></td>
        <td id="LC164" class="blob-code blob-code-inner js-file-line">            ratio        <span class="pl-k">=</span> <span class="pl-c1">ROOT</span>.RooRealVar(<span class="pl-s"><span class="pl-pds">&quot;</span>ratio_<span class="pl-c1">%d%s</span><span class="pl-pds">&quot;</span></span><span class="pl-k">%</span>(<span class="pl-c1">MH</span>,postfix),<span class="pl-s"><span class="pl-pds">&quot;</span>ratio_<span class="pl-c1">%d%s</span><span class="pl-pds">&quot;</span></span><span class="pl-k">%</span>(<span class="pl-c1">MH</span>,postfix),<span class="pl-c1">0.5</span>)</td>
      </tr>
      <tr>
        <td id="L165" class="blob-num js-line-number" data-line-number="165"></td>
        <td id="LC165" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L166" class="blob-num js-line-number" data-line-number="166"></td>
        <td id="LC166" class="blob-code blob-code-inner js-file-line">            alpha.setConstant(<span class="pl-c1">ROOT</span>.kTRUE)</td>
      </tr>
      <tr>
        <td id="L167" class="blob-num js-line-number" data-line-number="167"></td>
        <td id="LC167" class="blob-code blob-code-inner js-file-line">            sign.setConstant(<span class="pl-c1">ROOT</span>.kTRUE)</td>
      </tr>
      <tr>
        <td id="L168" class="blob-num js-line-number" data-line-number="168"></td>
        <td id="LC168" class="blob-code blob-code-inner js-file-line">            alpha2.setConstant(<span class="pl-c1">ROOT</span>.kTRUE)</td>
      </tr>
      <tr>
        <td id="L169" class="blob-num js-line-number" data-line-number="169"></td>
        <td id="LC169" class="blob-code blob-code-inner js-file-line">            sign2.setConstant(<span class="pl-c1">ROOT</span>.kTRUE)</td>
      </tr>
      <tr>
        <td id="L170" class="blob-num js-line-number" data-line-number="170"></td>
        <td id="LC170" class="blob-code blob-code-inner js-file-line">            mean.setConstant(<span class="pl-c1">ROOT</span>.kTRUE)</td>
      </tr>
      <tr>
        <td id="L171" class="blob-num js-line-number" data-line-number="171"></td>
        <td id="LC171" class="blob-code blob-code-inner js-file-line">            sigma.setConstant(<span class="pl-c1">ROOT</span>.kTRUE)</td>
      </tr>
      <tr>
        <td id="L172" class="blob-num js-line-number" data-line-number="172"></td>
        <td id="LC172" class="blob-code blob-code-inner js-file-line">            </td>
      </tr>
      <tr>
        <td id="L173" class="blob-num js-line-number" data-line-number="173"></td>
        <td id="LC173" class="blob-code blob-code-inner js-file-line">            alphaH.setConstant(<span class="pl-c1">ROOT</span>.kTRUE)</td>
      </tr>
      <tr>
        <td id="L174" class="blob-num js-line-number" data-line-number="174"></td>
        <td id="LC174" class="blob-code blob-code-inner js-file-line">            signH.setConstant(<span class="pl-c1">ROOT</span>.kTRUE)</td>
      </tr>
      <tr>
        <td id="L175" class="blob-num js-line-number" data-line-number="175"></td>
        <td id="LC175" class="blob-code blob-code-inner js-file-line">            alpha2H.setConstant(<span class="pl-c1">ROOT</span>.kTRUE)</td>
      </tr>
      <tr>
        <td id="L176" class="blob-num js-line-number" data-line-number="176"></td>
        <td id="LC176" class="blob-code blob-code-inner js-file-line">            sign2H.setConstant(<span class="pl-c1">ROOT</span>.kTRUE)</td>
      </tr>
      <tr>
        <td id="L177" class="blob-num js-line-number" data-line-number="177"></td>
        <td id="LC177" class="blob-code blob-code-inner js-file-line">            meanH.setConstant(<span class="pl-c1">ROOT</span>.kTRUE)</td>
      </tr>
      <tr>
        <td id="L178" class="blob-num js-line-number" data-line-number="178"></td>
        <td id="LC178" class="blob-code blob-code-inner js-file-line">            sigmaH.setConstant(<span class="pl-c1">ROOT</span>.kTRUE)</td>
      </tr>
      <tr>
        <td id="L179" class="blob-num js-line-number" data-line-number="179"></td>
        <td id="LC179" class="blob-code blob-code-inner js-file-line">            </td>
      </tr>
      <tr>
        <td id="L180" class="blob-num js-line-number" data-line-number="180"></td>
        <td id="LC180" class="blob-code blob-code-inner js-file-line">            function1 <span class="pl-k">=</span> <span class="pl-c1">ROOT</span>.RooDoubleCB(pdfName<span class="pl-k">+</span><span class="pl-s"><span class="pl-pds">&quot;</span>1<span class="pl-pds">&quot;</span></span>, pdfName<span class="pl-k">+</span><span class="pl-s"><span class="pl-pds">&quot;</span>1<span class="pl-pds">&quot;</span></span>, var, mean, sigma, alpha, sign,  alpha2, sign2) </td>
      </tr>
      <tr>
        <td id="L181" class="blob-num js-line-number" data-line-number="181"></td>
        <td id="LC181" class="blob-code blob-code-inner js-file-line">            function2 <span class="pl-k">=</span> <span class="pl-c1">ROOT</span>.RooDoubleCB(pdfName<span class="pl-k">+</span><span class="pl-s"><span class="pl-pds">&quot;</span>2<span class="pl-pds">&quot;</span></span>, pdfName<span class="pl-k">+</span><span class="pl-s"><span class="pl-pds">&quot;</span>2<span class="pl-pds">&quot;</span></span>, var, meanH, sigmaH, alphaH, signH,  alpha2H, sign2H)</td>
      </tr>
      <tr>
        <td id="L182" class="blob-num js-line-number" data-line-number="182"></td>
        <td id="LC182" class="blob-code blob-code-inner js-file-line">            function <span class="pl-k">=</span>  <span class="pl-c1">ROOT</span>.RooAddPdf(pdfName,pdfName,function1,function2,ratio)</td>
      </tr>
      <tr>
        <td id="L183" class="blob-num js-line-number" data-line-number="183"></td>
        <td id="LC183" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">getattr</span>(w,<span class="pl-s"><span class="pl-pds">&#39;</span>import<span class="pl-pds">&#39;</span></span>)(function,<span class="pl-c1">ROOT</span>.RooFit.Rename(pdfName))</td>
      </tr>
      <tr>
        <td id="L184" class="blob-num js-line-number" data-line-number="184"></td>
        <td id="LC184" class="blob-code blob-code-inner js-file-line">            </td>
      </tr>
      <tr>
        <td id="L185" class="blob-num js-line-number" data-line-number="185"></td>
        <td id="LC185" class="blob-code blob-code-inner js-file-line">		</td>
      </tr>
      <tr>
        <td id="L186" class="blob-num js-line-number" data-line-number="186"></td>
        <td id="LC186" class="blob-code blob-code-inner js-file-line">parser <span class="pl-k">=</span> optparse.OptionParser()</td>
      </tr>
      <tr>
        <td id="L187" class="blob-num js-line-number" data-line-number="187"></td>
        <td id="LC187" class="blob-code blob-code-inner js-file-line">parser.add_option(<span class="pl-s"><span class="pl-pds">&quot;</span>-f<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>--file<span class="pl-pds">&quot;</span></span>,<span class="pl-v">dest</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>file<span class="pl-pds">&quot;</span></span>,<span class="pl-v">default</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>JJ_BulkGWW_2016_MVV.json<span class="pl-pds">&#39;</span></span>,<span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>input file (JJ_<span class="pl-c1">{sig}</span>_2016_MVV.json,JJ_<span class="pl-c1">{sig}</span>_2016_MJrandom_VV_HPLP.json)<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L188" class="blob-num js-line-number" data-line-number="188"></td>
        <td id="LC188" class="blob-code blob-code-inner js-file-line">parser.add_option(<span class="pl-s"><span class="pl-pds">&quot;</span>-v<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>--var<span class="pl-pds">&quot;</span></span>,<span class="pl-v">dest</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>var<span class="pl-pds">&quot;</span></span>,<span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>mVV or mJ<span class="pl-pds">&quot;</span></span>,<span class="pl-v">default</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>mVV<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L189" class="blob-num js-line-number" data-line-number="189"></td>
        <td id="LC189" class="blob-code blob-code-inner js-file-line">parser.add_option(<span class="pl-s"><span class="pl-pds">&quot;</span>-y<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>--year<span class="pl-pds">&quot;</span></span>,<span class="pl-v">dest</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>year<span class="pl-pds">&quot;</span></span>,<span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>2016 or 2017 or 2018<span class="pl-pds">&quot;</span></span>,<span class="pl-v">default</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>2016<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L190" class="blob-num js-line-number" data-line-number="190"></td>
        <td id="LC190" class="blob-code blob-code-inner js-file-line">parser.add_option(<span class="pl-s"><span class="pl-pds">&quot;</span>-c<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>--category<span class="pl-pds">&quot;</span></span>,<span class="pl-v">dest</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>category<span class="pl-pds">&quot;</span></span>,<span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>VV_HPHP or VV_HPLP or VH_HPHP etc<span class="pl-pds">&quot;</span></span>,<span class="pl-v">default</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>VV_HPLP<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L191" class="blob-num js-line-number" data-line-number="191"></td>
        <td id="LC191" class="blob-code blob-code-inner js-file-line">parser.add_option(<span class="pl-s"><span class="pl-pds">&quot;</span>-o<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>--outdir<span class="pl-pds">&quot;</span></span>,<span class="pl-v">dest</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>outdir<span class="pl-pds">&quot;</span></span>,<span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>output directory<span class="pl-pds">&quot;</span></span>,<span class="pl-v">default</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>../plots/<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L192" class="blob-num js-line-number" data-line-number="192"></td>
        <td id="LC192" class="blob-code blob-code-inner js-file-line">parser.add_option(<span class="pl-s"><span class="pl-pds">&quot;</span>-i<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>--indir<span class="pl-pds">&quot;</span></span>,<span class="pl-v">dest</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>indir<span class="pl-pds">&quot;</span></span>,<span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>input directory<span class="pl-pds">&quot;</span></span>,<span class="pl-v">default</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>results_2016/<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L193" class="blob-num js-line-number" data-line-number="193"></td>
        <td id="LC193" class="blob-code blob-code-inner js-file-line">parser.add_option(<span class="pl-s"><span class="pl-pds">&quot;</span>-n<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>--name<span class="pl-pds">&quot;</span></span>,<span class="pl-v">dest</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>name<span class="pl-pds">&quot;</span></span>,<span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>you may specify an additional label for the output file<span class="pl-pds">&quot;</span></span>,<span class="pl-v">default</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>test<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L194" class="blob-num js-line-number" data-line-number="194"></td>
        <td id="LC194" class="blob-code blob-code-inner js-file-line">parser.add_option(<span class="pl-s"><span class="pl-pds">&quot;</span>-l<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>--leg<span class="pl-pds">&quot;</span></span>,<span class="pl-v">dest</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>leg<span class="pl-pds">&quot;</span></span>,<span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>mVV or mJ<span class="pl-pds">&quot;</span></span>,<span class="pl-v">default</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>l1<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L195" class="blob-num js-line-number" data-line-number="195"></td>
        <td id="LC195" class="blob-code blob-code-inner js-file-line">parser.add_option(<span class="pl-s"><span class="pl-pds">&quot;</span>-p<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>--prelim<span class="pl-pds">&quot;</span></span>,<span class="pl-v">dest</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>prelim<span class="pl-pds">&quot;</span></span>,<span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>with label preliminary or not<span class="pl-pds">&quot;</span></span>,<span class="pl-v">default</span><span class="pl-k">=</span><span class="pl-c1">0</span>)</td>
      </tr>
      <tr>
        <td id="L196" class="blob-num js-line-number" data-line-number="196"></td>
        <td id="LC196" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L197" class="blob-num js-line-number" data-line-number="197"></td>
        <td id="LC197" class="blob-code blob-code-inner js-file-line">(options,args) <span class="pl-k">=</span> parser.parse_args()</td>
      </tr>
      <tr>
        <td id="L198" class="blob-num js-line-number" data-line-number="198"></td>
        <td id="LC198" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L199" class="blob-num js-line-number" data-line-number="199"></td>
        <td id="LC199" class="blob-code blob-code-inner js-file-line">path <span class="pl-k">=</span> options.outdir</td>
      </tr>
      <tr>
        <td id="L200" class="blob-num js-line-number" data-line-number="200"></td>
        <td id="LC200" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L201" class="blob-num js-line-number" data-line-number="201"></td>
        <td id="LC201" class="blob-code blob-code-inner js-file-line">purity  <span class="pl-k">=</span> options.category</td>
      </tr>
      <tr>
        <td id="L202" class="blob-num js-line-number" data-line-number="202"></td>
        <td id="LC202" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L203" class="blob-num js-line-number" data-line-number="203"></td>
        <td id="LC203" class="blob-code blob-code-inner js-file-line">inFileName <span class="pl-k">=</span> options.file</td>
      </tr>
      <tr>
        <td id="L204" class="blob-num js-line-number" data-line-number="204"></td>
        <td id="LC204" class="blob-code blob-code-inner js-file-line">massPoints <span class="pl-k">=</span> [<span class="pl-c1">1200</span>,<span class="pl-c1">1400</span>,<span class="pl-c1">1600</span>,<span class="pl-c1">1800</span>,<span class="pl-c1">2000</span>,<span class="pl-c1">2500</span>,<span class="pl-c1">3000</span>,<span class="pl-c1">3500</span>,<span class="pl-c1">4000</span>,<span class="pl-c1">4500</span>]</td>
      </tr>
      <tr>
        <td id="L205" class="blob-num js-line-number" data-line-number="205"></td>
        <td id="LC205" class="blob-code blob-code-inner js-file-line">postfix <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span>Jet 1 <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L206" class="blob-num js-line-number" data-line-number="206"></td>
        <td id="LC206" class="blob-code blob-code-inner js-file-line"><span class="pl-k">if</span> options.leg <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&quot;</span>l2<span class="pl-pds">&quot;</span></span> <span class="pl-k">!=</span><span class="pl-k">-</span><span class="pl-c1">1</span>: postfix <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span>Jet 2 <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L207" class="blob-num js-line-number" data-line-number="207"></td>
        <td id="LC207" class="blob-code blob-code-inner js-file-line">varName <span class="pl-k">=</span> {<span class="pl-s"><span class="pl-pds">&#39;</span>mVV<span class="pl-pds">&#39;</span></span>:<span class="pl-s"><span class="pl-pds">&#39;</span>Dijet invariant mass [GeV]<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>mJ<span class="pl-pds">&#39;</span></span>:<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-c1">%s</span>Jet mass [GeV]<span class="pl-pds">&#39;</span></span><span class="pl-k">%</span>postfix}</td>
      </tr>
      <tr>
        <td id="L208" class="blob-num js-line-number" data-line-number="208"></td>
        <td id="LC208" class="blob-code blob-code-inner js-file-line">varBins <span class="pl-k">=</span> {<span class="pl-s"><span class="pl-pds">&#39;</span>mVV<span class="pl-pds">&#39;</span></span>:<span class="pl-s"><span class="pl-pds">&#39;</span>[37,1000,5500]<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>mJ<span class="pl-pds">&#39;</span></span>:<span class="pl-s"><span class="pl-pds">&#39;</span>[80,55,215]<span class="pl-pds">&#39;</span></span>}</td>
      </tr>
      <tr>
        <td id="L209" class="blob-num js-line-number" data-line-number="209"></td>
        <td id="LC209" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>w=ROOT.RooWorkspace(&quot;w&quot;,&quot;w&quot;)</span></td>
      </tr>
      <tr>
        <td id="L210" class="blob-num js-line-number" data-line-number="210"></td>
        <td id="LC210" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>w.factory(options.var+varBins[options.var])</span></td>
      </tr>
      <tr>
        <td id="L211" class="blob-num js-line-number" data-line-number="211"></td>
        <td id="LC211" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>w.var(options.var).SetTitle(varName[options.var])</span></td>
      </tr>
      <tr>
        <td id="L212" class="blob-num js-line-number" data-line-number="212"></td>
        <td id="LC212" class="blob-code blob-code-inner js-file-line">colors<span class="pl-k">=</span> []</td>
      </tr>
      <tr>
        <td id="L213" class="blob-num js-line-number" data-line-number="213"></td>
        <td id="LC213" class="blob-code blob-code-inner js-file-line">colors.append([<span class="pl-s"><span class="pl-pds">&quot;</span>#000080<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>#0000CD<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>#0000FF<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>#3D59AB<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>#4169E1<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>#4876FF<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>#6495ED<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>#1E90FF<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>#63B8FF<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>#87CEFA<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>#C6E2FF<span class="pl-pds">&quot;</span></span>]<span class="pl-k">*</span><span class="pl-c1">3</span>)   </td>
      </tr>
      <tr>
        <td id="L214" class="blob-num js-line-number" data-line-number="214"></td>
        <td id="LC214" class="blob-code blob-code-inner js-file-line">colors.append([<span class="pl-s"><span class="pl-pds">&quot;</span>#006400<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>#308014<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>#228B22<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>#32CD32<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>#00CD00<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>#00EE00<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>#00FF00<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>#7CCD7C<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>#7CFC00<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>#ADFF2F<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>#C0FF3E<span class="pl-pds">&quot;</span></span>]<span class="pl-k">*</span><span class="pl-c1">3</span>)   </td>
      </tr>
      <tr>
        <td id="L215" class="blob-num js-line-number" data-line-number="215"></td>
        <td id="LC215" class="blob-code blob-code-inner js-file-line">colors.append([<span class="pl-s"><span class="pl-pds">&quot;</span>#CD8500<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>#CD950C<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>#EE9A00<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>#EEAD0E<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>#FFA500<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>#FFB90F<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>#FFC125<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>#EEC900<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>#FFD700<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>#FFEC8B<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>#FFF68F<span class="pl-pds">&quot;</span></span>]<span class="pl-k">*</span><span class="pl-c1">3</span>) </td>
      </tr>
      <tr>
        <td id="L216" class="blob-num js-line-number" data-line-number="216"></td>
        <td id="LC216" class="blob-code blob-code-inner js-file-line">colors.append([<span class="pl-s"><span class="pl-pds">&quot;</span>#8B2500<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>#CD3700<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>#EE4000<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>#FF4500<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>#CD4F39<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>#EE5C42<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>#EE6A50<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>#FF7256<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>#FA8072<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>#FFA07A<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>#EEB4B4<span class="pl-pds">&quot;</span></span>]<span class="pl-k">*</span><span class="pl-c1">3</span>)</td>
      </tr>
      <tr>
        <td id="L217" class="blob-num js-line-number" data-line-number="217"></td>
        <td id="LC217" class="blob-code blob-code-inner js-file-line">colors.append([<span class="pl-s"><span class="pl-pds">&quot;</span>#EE82EE<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>#FF00FF<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>#D02090<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>#C71585<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>#B03060 <span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>#DB7093<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>#FFB6C1<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>#FFC0CB<span class="pl-pds">&quot;</span></span>]<span class="pl-k">*</span><span class="pl-c1">3</span>)</td>
      </tr>
      <tr>
        <td id="L218" class="blob-num js-line-number" data-line-number="218"></td>
        <td id="LC218" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L219" class="blob-num js-line-number" data-line-number="219"></td>
        <td id="LC219" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">doSingle</span>():</td>
      </tr>
      <tr>
        <td id="L220" class="blob-num js-line-number" data-line-number="220"></td>
        <td id="LC220" class="blob-code blob-code-inner js-file-line">    w<span class="pl-k">=</span><span class="pl-c1">ROOT</span>.RooWorkspace(<span class="pl-s"><span class="pl-pds">&quot;</span>w<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>w<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L221" class="blob-num js-line-number" data-line-number="221"></td>
        <td id="LC221" class="blob-code blob-code-inner js-file-line">    w.factory(options.var<span class="pl-k">+</span>varBins[options.var])</td>
      </tr>
      <tr>
        <td id="L222" class="blob-num js-line-number" data-line-number="222"></td>
        <td id="LC222" class="blob-code blob-code-inner js-file-line">    w.var(options.var).SetTitle(varName[options.var])</td>
      </tr>
      <tr>
        <td id="L223" class="blob-num js-line-number" data-line-number="223"></td>
        <td id="LC223" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">with</span> <span class="pl-c1">open</span>(inFileName) <span class="pl-k">as</span> jsonFile:</td>
      </tr>
      <tr>
        <td id="L224" class="blob-num js-line-number" data-line-number="224"></td>
        <td id="LC224" class="blob-code blob-code-inner js-file-line">      j <span class="pl-k">=</span> json.load(jsonFile)</td>
      </tr>
      <tr>
        <td id="L225" class="blob-num js-line-number" data-line-number="225"></td>
        <td id="LC225" class="blob-code blob-code-inner js-file-line">    </td>
      </tr>
      <tr>
        <td id="L226" class="blob-num js-line-number" data-line-number="226"></td>
        <td id="LC226" class="blob-code blob-code-inner js-file-line">      c1 <span class="pl-k">=</span> getCanvasPaper(<span class="pl-s"><span class="pl-pds">&quot;</span>c1<span class="pl-pds">&quot;</span></span>)[<span class="pl-c1">0</span>]</td>
      </tr>
      <tr>
        <td id="L227" class="blob-num js-line-number" data-line-number="227"></td>
        <td id="LC227" class="blob-code blob-code-inner js-file-line">      c1.Draw()</td>
      </tr>
      <tr>
        <td id="L228" class="blob-num js-line-number" data-line-number="228"></td>
        <td id="LC228" class="blob-code blob-code-inner js-file-line">      leg <span class="pl-k">=</span> <span class="pl-c1">ROOT</span>.TLegend(<span class="pl-c1">0.8</span>, <span class="pl-c1">0.2</span>, <span class="pl-c1">0.95</span>, <span class="pl-c1">0.8</span>)</td>
      </tr>
      <tr>
        <td id="L229" class="blob-num js-line-number" data-line-number="229"></td>
        <td id="LC229" class="blob-code blob-code-inner js-file-line">      frame <span class="pl-k">=</span> w.var(options.var).frame()   </td>
      </tr>
      <tr>
        <td id="L230" class="blob-num js-line-number" data-line-number="230"></td>
        <td id="LC230" class="blob-code blob-code-inner js-file-line">      </td>
      </tr>
      <tr>
        <td id="L231" class="blob-num js-line-number" data-line-number="231"></td>
        <td id="LC231" class="blob-code blob-code-inner js-file-line">      <span class="pl-k">for</span> i, <span class="pl-c1">MH</span> <span class="pl-k">in</span> <span class="pl-c1">enumerate</span>(massPoints):  <span class="pl-c"><span class="pl-c">#</span> mind that MH is evaluated below</span></td>
      </tr>
      <tr>
        <td id="L232" class="blob-num js-line-number" data-line-number="232"></td>
        <td id="LC232" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> options.var <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>mVV<span class="pl-pds">&#39;</span></span>: getMVVPdf(w,j,<span class="pl-c1">MH</span>)</td>
      </tr>
      <tr>
        <td id="L233" class="blob-num js-line-number" data-line-number="233"></td>
        <td id="LC233" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">else</span>: </td>
      </tr>
      <tr>
        <td id="L234" class="blob-num js-line-number" data-line-number="234"></td>
        <td id="LC234" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> inFileName.find(<span class="pl-s"><span class="pl-pds">&quot;</span>H<span class="pl-pds">&quot;</span></span>)<span class="pl-k">==</span><span class="pl-k">-</span><span class="pl-c1">1</span>:</td>
      </tr>
      <tr>
        <td id="L235" class="blob-num js-line-number" data-line-number="235"></td>
        <td id="LC235" class="blob-code blob-code-inner js-file-line">                getMJPdf(w,j,<span class="pl-c1">MH</span>)</td>
      </tr>
      <tr>
        <td id="L236" class="blob-num js-line-number" data-line-number="236"></td>
        <td id="LC236" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> inFileName.find(<span class="pl-s"><span class="pl-pds">&quot;</span>Vjet<span class="pl-pds">&quot;</span></span>)<span class="pl-k">!=</span><span class="pl-k">-</span><span class="pl-c1">1</span>:</td>
      </tr>
      <tr>
        <td id="L237" class="blob-num js-line-number" data-line-number="237"></td>
        <td id="LC237" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">with</span> <span class="pl-c1">open</span>(inFileName.replace(<span class="pl-s"><span class="pl-pds">&quot;</span>Vjet<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>Hjet<span class="pl-pds">&quot;</span></span>)) <span class="pl-k">as</span> jsonFileH:</td>
      </tr>
      <tr>
        <td id="L238" class="blob-num js-line-number" data-line-number="238"></td>
        <td id="LC238" class="blob-code blob-code-inner js-file-line">                    jH <span class="pl-k">=</span> json.load(jsonFileH)</td>
      </tr>
      <tr>
        <td id="L239" class="blob-num js-line-number" data-line-number="239"></td>
        <td id="LC239" class="blob-code blob-code-inner js-file-line">                getMJPdf(j,<span class="pl-c1">MH</span>,<span class="pl-s"><span class="pl-pds">&quot;</span>H<span class="pl-pds">&quot;</span></span>,jH)</td>
      </tr>
      <tr>
        <td id="L240" class="blob-num js-line-number" data-line-number="240"></td>
        <td id="LC240" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> inFileName.find(<span class="pl-s"><span class="pl-pds">&quot;</span>Hjet<span class="pl-pds">&quot;</span></span>)<span class="pl-k">!=</span><span class="pl-k">-</span><span class="pl-c1">1</span>:</td>
      </tr>
      <tr>
        <td id="L241" class="blob-num js-line-number" data-line-number="241"></td>
        <td id="LC241" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">with</span> <span class="pl-c1">open</span>(inFileName.replace(<span class="pl-s"><span class="pl-pds">&quot;</span>Hjet<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>Vjet<span class="pl-pds">&quot;</span></span>)) <span class="pl-k">as</span> jsonFileV:</td>
      </tr>
      <tr>
        <td id="L242" class="blob-num js-line-number" data-line-number="242"></td>
        <td id="LC242" class="blob-code blob-code-inner js-file-line">                    jV <span class="pl-k">=</span> json.load(jsonFileV)</td>
      </tr>
      <tr>
        <td id="L243" class="blob-num js-line-number" data-line-number="243"></td>
        <td id="LC243" class="blob-code blob-code-inner js-file-line">                getMJPdf(w,jV,<span class="pl-c1">MH</span>,<span class="pl-s"><span class="pl-pds">&quot;</span>H<span class="pl-pds">&quot;</span></span>,j)</td>
      </tr>
      <tr>
        <td id="L244" class="blob-num js-line-number" data-line-number="244"></td>
        <td id="LC244" class="blob-code blob-code-inner js-file-line">                </td>
      </tr>
      <tr>
        <td id="L245" class="blob-num js-line-number" data-line-number="245"></td>
        <td id="LC245" class="blob-code blob-code-inner js-file-line">        w.pdf(<span class="pl-s"><span class="pl-pds">&#39;</span>signal_<span class="pl-c1">%d</span><span class="pl-pds">&#39;</span></span><span class="pl-k">%</span><span class="pl-c1">MH</span>).plotOn(frame, <span class="pl-c1">ROOT</span>.RooFit.LineColor(<span class="pl-c1">ROOT</span>.TColor.GetColor(colors[<span class="pl-c1">0</span>][i])),<span class="pl-c1">ROOT</span>.RooFit.Name(<span class="pl-c1">str</span>(<span class="pl-c1">MH</span>)))<span class="pl-c"><span class="pl-c">#</span>,ROOT.RooFit.Range(MH*0.8,1.2*MH))#ROOT.RooFit.Normalization(1, ROOT.RooAbsReal.RelativeExpected),</span></td>
      </tr>
      <tr>
        <td id="L246" class="blob-num js-line-number" data-line-number="246"></td>
        <td id="LC246" class="blob-code blob-code-inner js-file-line">        leg.AddEntry(frame.findObject(<span class="pl-c1">str</span>(<span class="pl-c1">MH</span>)), <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-c1">%d</span> GeV<span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span> <span class="pl-c1">MH</span>, <span class="pl-s"><span class="pl-pds">&quot;</span>L<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L247" class="blob-num js-line-number" data-line-number="247"></td>
        <td id="LC247" class="blob-code blob-code-inner js-file-line">      frame.GetYaxis().SetTitle(<span class="pl-s"><span class="pl-pds">&quot;</span>A.U<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L248" class="blob-num js-line-number" data-line-number="248"></td>
        <td id="LC248" class="blob-code blob-code-inner js-file-line">      frame.GetYaxis().SetNdivisions(<span class="pl-c1">4</span>,<span class="pl-c1">5</span>,<span class="pl-c1">0</span>)</td>
      </tr>
      <tr>
        <td id="L249" class="blob-num js-line-number" data-line-number="249"></td>
        <td id="LC249" class="blob-code blob-code-inner js-file-line">      frame.SetMaximum(<span class="pl-c1">0.1</span>)</td>
      </tr>
      <tr>
        <td id="L250" class="blob-num js-line-number" data-line-number="250"></td>
        <td id="LC250" class="blob-code blob-code-inner js-file-line">      <span class="pl-k">if</span> options.var <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>mVV<span class="pl-pds">&#39;</span></span>:frame.SetMaximum(<span class="pl-c1">0.5</span>)</td>
      </tr>
      <tr>
        <td id="L251" class="blob-num js-line-number" data-line-number="251"></td>
        <td id="LC251" class="blob-code blob-code-inner js-file-line">      frame.Draw()</td>
      </tr>
      <tr>
        <td id="L252" class="blob-num js-line-number" data-line-number="252"></td>
        <td id="LC252" class="blob-code blob-code-inner js-file-line">      <span class="pl-c"><span class="pl-c">#</span> leg.Draw(&quot;same&quot;)</span></td>
      </tr>
      <tr>
        <td id="L253" class="blob-num js-line-number" data-line-number="253"></td>
        <td id="LC253" class="blob-code blob-code-inner js-file-line">      model <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span>G_<span class="pl-c1">{B}</span> #rightarrow WW<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L254" class="blob-num js-line-number" data-line-number="254"></td>
        <td id="LC254" class="blob-code blob-code-inner js-file-line">      <span class="pl-k">if</span> options.file.find(<span class="pl-s"><span class="pl-pds">&quot;</span>ZZ<span class="pl-pds">&quot;</span></span>)<span class="pl-k">!=</span><span class="pl-k">-</span><span class="pl-c1">1</span>:</td>
      </tr>
      <tr>
        <td id="L255" class="blob-num js-line-number" data-line-number="255"></td>
        <td id="LC255" class="blob-code blob-code-inner js-file-line">          model <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span>G_<span class="pl-c1">{B}</span> #rightarrow ZZ<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L256" class="blob-num js-line-number" data-line-number="256"></td>
        <td id="LC256" class="blob-code blob-code-inner js-file-line">      <span class="pl-k">if</span> options.file.find(<span class="pl-s"><span class="pl-pds">&quot;</span>WZ<span class="pl-pds">&quot;</span></span>)<span class="pl-k">!=</span><span class="pl-k">-</span><span class="pl-c1">1</span>:</td>
      </tr>
      <tr>
        <td id="L257" class="blob-num js-line-number" data-line-number="257"></td>
        <td id="LC257" class="blob-code blob-code-inner js-file-line">          model <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span>W&#39; #rightarrow WZ<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L258" class="blob-num js-line-number" data-line-number="258"></td>
        <td id="LC258" class="blob-code blob-code-inner js-file-line">      <span class="pl-k">if</span> options.file.find(<span class="pl-s"><span class="pl-pds">&quot;</span>Zprime<span class="pl-pds">&quot;</span></span>)<span class="pl-k">!=</span><span class="pl-k">-</span><span class="pl-c1">1</span>:</td>
      </tr>
      <tr>
        <td id="L259" class="blob-num js-line-number" data-line-number="259"></td>
        <td id="LC259" class="blob-code blob-code-inner js-file-line">          model <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span>Z&#39; #rightarrow WW<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L260" class="blob-num js-line-number" data-line-number="260"></td>
        <td id="LC260" class="blob-code blob-code-inner js-file-line">      <span class="pl-k">if</span>   options.file.find(<span class="pl-s"><span class="pl-pds">&quot;</span>HPHP<span class="pl-pds">&quot;</span></span>)<span class="pl-k">!=</span><span class="pl-k">-</span><span class="pl-c1">1</span>: purity <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span>HPHP<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L261" class="blob-num js-line-number" data-line-number="261"></td>
        <td id="LC261" class="blob-code blob-code-inner js-file-line">      <span class="pl-k">elif</span> options.file.find(<span class="pl-s"><span class="pl-pds">&quot;</span>HPLP<span class="pl-pds">&quot;</span></span>)<span class="pl-k">!=</span><span class="pl-k">-</span><span class="pl-c1">1</span>: purity <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span>HPLP<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L262" class="blob-num js-line-number" data-line-number="262"></td>
        <td id="LC262" class="blob-code blob-code-inner js-file-line">      <span class="pl-k">else</span>:purity <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span>HPLP+HPHP<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L263" class="blob-num js-line-number" data-line-number="263"></td>
        <td id="LC263" class="blob-code blob-code-inner js-file-line">      c1.cd()</td>
      </tr>
      <tr>
        <td id="L264" class="blob-num js-line-number" data-line-number="264"></td>
        <td id="LC264" class="blob-code blob-code-inner js-file-line">      pt <span class="pl-k">=</span><span class="pl-c1">ROOT</span>.TPaveText(<span class="pl-c1">0.81</span>,<span class="pl-c1">0.82</span>,<span class="pl-c1">0.84</span>,<span class="pl-c1">0.89</span>,<span class="pl-s"><span class="pl-pds">&quot;</span>brNDC<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L265" class="blob-num js-line-number" data-line-number="265"></td>
        <td id="LC265" class="blob-code blob-code-inner js-file-line">      pt.SetBorderSize(<span class="pl-c1">0</span>)</td>
      </tr>
      <tr>
        <td id="L266" class="blob-num js-line-number" data-line-number="266"></td>
        <td id="LC266" class="blob-code blob-code-inner js-file-line">      pt.SetTextAlign(<span class="pl-c1">12</span>)</td>
      </tr>
      <tr>
        <td id="L267" class="blob-num js-line-number" data-line-number="267"></td>
        <td id="LC267" class="blob-code blob-code-inner js-file-line">      pt.SetFillStyle(<span class="pl-c1">0</span>)</td>
      </tr>
      <tr>
        <td id="L268" class="blob-num js-line-number" data-line-number="268"></td>
        <td id="LC268" class="blob-code blob-code-inner js-file-line">      pt.SetTextFont(<span class="pl-c1">42</span>)</td>
      </tr>
      <tr>
        <td id="L269" class="blob-num js-line-number" data-line-number="269"></td>
        <td id="LC269" class="blob-code blob-code-inner js-file-line">      pt.SetTextSize(<span class="pl-c1">0.04</span>)</td>
      </tr>
      <tr>
        <td id="L270" class="blob-num js-line-number" data-line-number="270"></td>
        <td id="LC270" class="blob-code blob-code-inner js-file-line">      pt.AddText(model)</td>
      </tr>
      <tr>
        <td id="L271" class="blob-num js-line-number" data-line-number="271"></td>
        <td id="LC271" class="blob-code blob-code-inner js-file-line">      <span class="pl-c"><span class="pl-c">#</span> pt.AddText(purity)</span></td>
      </tr>
      <tr>
        <td id="L272" class="blob-num js-line-number" data-line-number="272"></td>
        <td id="LC272" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L273" class="blob-num js-line-number" data-line-number="273"></td>
        <td id="LC273" class="blob-code blob-code-inner js-file-line">      pt.Draw()</td>
      </tr>
      <tr>
        <td id="L274" class="blob-num js-line-number" data-line-number="274"></td>
        <td id="LC274" class="blob-code blob-code-inner js-file-line">      cmslabel_sim(c1,<span class="pl-s"><span class="pl-pds">&#39;</span>2016<span class="pl-pds">&#39;</span></span>,<span class="pl-c1">11</span>)</td>
      </tr>
      <tr>
        <td id="L275" class="blob-num js-line-number" data-line-number="275"></td>
        <td id="LC275" class="blob-code blob-code-inner js-file-line">      c1.Update()</td>
      </tr>
      <tr>
        <td id="L276" class="blob-num js-line-number" data-line-number="276"></td>
        <td id="LC276" class="blob-code blob-code-inner js-file-line">      </td>
      </tr>
      <tr>
        <td id="L277" class="blob-num js-line-number" data-line-number="277"></td>
        <td id="LC277" class="blob-code blob-code-inner js-file-line">      c1.SaveAs(path<span class="pl-k">+</span><span class="pl-s"><span class="pl-pds">&quot;</span>signalShapes<span class="pl-c1">%s</span>_<span class="pl-c1">%s</span>.png<span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span>(options.var, inFileName.rsplit(<span class="pl-s"><span class="pl-pds">&quot;</span>.<span class="pl-pds">&quot;</span></span>, <span class="pl-c1">1</span>)[<span class="pl-c1">0</span>]))</td>
      </tr>
      <tr>
        <td id="L278" class="blob-num js-line-number" data-line-number="278"></td>
        <td id="LC278" class="blob-code blob-code-inner js-file-line">      c1.SaveAs(path<span class="pl-k">+</span><span class="pl-s"><span class="pl-pds">&quot;</span>signalShapes<span class="pl-c1">%s</span>_<span class="pl-c1">%s</span>.pdf<span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span>(options.var, inFileName.rsplit(<span class="pl-s"><span class="pl-pds">&quot;</span>.<span class="pl-pds">&quot;</span></span>, <span class="pl-c1">1</span>)[<span class="pl-c1">0</span>]))</td>
      </tr>
      <tr>
        <td id="L279" class="blob-num js-line-number" data-line-number="279"></td>
        <td id="LC279" class="blob-code blob-code-inner js-file-line">      c1.SaveAs(path<span class="pl-k">+</span><span class="pl-s"><span class="pl-pds">&quot;</span>signalShapes<span class="pl-c1">%s</span>_<span class="pl-c1">%s</span>.C<span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span>(options.var, inFileName.rsplit(<span class="pl-s"><span class="pl-pds">&quot;</span>.<span class="pl-pds">&quot;</span></span>, <span class="pl-c1">1</span>)[<span class="pl-c1">0</span>]))</td>
      </tr>
      <tr>
        <td id="L280" class="blob-num js-line-number" data-line-number="280"></td>
        <td id="LC280" class="blob-code blob-code-inner js-file-line">      c1.SaveAs(path<span class="pl-k">+</span><span class="pl-s"><span class="pl-pds">&quot;</span>signalShapes<span class="pl-c1">%s</span>_<span class="pl-c1">%s</span>.root<span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span>(options.var, inFileName.rsplit(<span class="pl-s"><span class="pl-pds">&quot;</span>.<span class="pl-pds">&quot;</span></span>, <span class="pl-c1">1</span>)[<span class="pl-c1">0</span>]))</td>
      </tr>
      <tr>
        <td id="L281" class="blob-num js-line-number" data-line-number="281"></td>
        <td id="LC281" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L282" class="blob-num js-line-number" data-line-number="282"></td>
        <td id="LC282" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">doAll</span>(<span class="pl-smi">category</span>,<span class="pl-smi">jsons</span>,<span class="pl-smi">legs</span>):</td>
      </tr>
      <tr>
        <td id="L283" class="blob-num js-line-number" data-line-number="283"></td>
        <td id="LC283" class="blob-code blob-code-inner js-file-line">    w<span class="pl-k">=</span><span class="pl-c1">ROOT</span>.RooWorkspace(<span class="pl-s"><span class="pl-pds">&quot;</span>w<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>w<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L284" class="blob-num js-line-number" data-line-number="284"></td>
        <td id="LC284" class="blob-code blob-code-inner js-file-line">    w.factory(options.var<span class="pl-k">+</span>varBins[options.var])</td>
      </tr>
      <tr>
        <td id="L285" class="blob-num js-line-number" data-line-number="285"></td>
        <td id="LC285" class="blob-code blob-code-inner js-file-line">    w.var(options.var).SetTitle(varName[options.var])</td>
      </tr>
      <tr>
        <td id="L286" class="blob-num js-line-number" data-line-number="286"></td>
        <td id="LC286" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"><span class="pl-c">#</span>legs = [&quot;G_{bulk} #rightarrow ZZ&quot;,&quot;W&#39; #rightarrow WZ&quot;,&quot;G_{bulk} #rightarrow WW&quot;,&quot;Z&#39;#rightarrow WW&quot;,&quot;Z&#39; #rightarrow ZH&quot;]</span></td>
      </tr>
      <tr>
        <td id="L287" class="blob-num js-line-number" data-line-number="287"></td>
        <td id="LC287" class="blob-code blob-code-inner js-file-line">    c1,pt <span class="pl-k">=</span> getCanvasPaper(<span class="pl-s"><span class="pl-pds">&quot;</span>c1<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L288" class="blob-num js-line-number" data-line-number="288"></td>
        <td id="LC288" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L289" class="blob-num js-line-number" data-line-number="289"></td>
        <td id="LC289" class="blob-code blob-code-inner js-file-line">    c1.Draw()</td>
      </tr>
      <tr>
        <td id="L290" class="blob-num js-line-number" data-line-number="290"></td>
        <td id="LC290" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> options.var <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>mVV<span class="pl-pds">&#39;</span></span>:</td>
      </tr>
      <tr>
        <td id="L291" class="blob-num js-line-number" data-line-number="291"></td>
        <td id="LC291" class="blob-code blob-code-inner js-file-line">        c1.Divide(<span class="pl-c1">1</span>,<span class="pl-c1">5</span>,<span class="pl-c1">0.0</span>,<span class="pl-c1">0.0</span>)</td>
      </tr>
      <tr>
        <td id="L292" class="blob-num js-line-number" data-line-number="292"></td>
        <td id="LC292" class="blob-code blob-code-inner js-file-line">    leg <span class="pl-k">=</span> []</td>
      </tr>
      <tr>
        <td id="L293" class="blob-num js-line-number" data-line-number="293"></td>
        <td id="LC293" class="blob-code blob-code-inner js-file-line">    frame <span class="pl-k">=</span> []  </td>
      </tr>
      <tr>
        <td id="L294" class="blob-num js-line-number" data-line-number="294"></td>
        <td id="LC294" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"><span class="pl-c">#</span>frame.SetTitle(&quot;&quot;)</span></td>
      </tr>
      <tr>
        <td id="L295" class="blob-num js-line-number" data-line-number="295"></td>
        <td id="LC295" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">for</span> ii,f <span class="pl-k">in</span> <span class="pl-c1">enumerate</span>(jsons):</td>
      </tr>
      <tr>
        <td id="L296" class="blob-num js-line-number" data-line-number="296"></td>
        <td id="LC296" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> options.var <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>mVV<span class="pl-pds">&#39;</span></span>:</td>
      </tr>
      <tr>
        <td id="L297" class="blob-num js-line-number" data-line-number="297"></td>
        <td id="LC297" class="blob-code blob-code-inner js-file-line">            c1.cd(ii)</td>
      </tr>
      <tr>
        <td id="L298" class="blob-num js-line-number" data-line-number="298"></td>
        <td id="LC298" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> ii<span class="pl-k">==</span><span class="pl-c1">len</span>(jsons)<span class="pl-k">-</span><span class="pl-c1">1</span>:</td>
      </tr>
      <tr>
        <td id="L299" class="blob-num js-line-number" data-line-number="299"></td>
        <td id="LC299" class="blob-code blob-code-inner js-file-line">                leg.append(getLegend(<span class="pl-c1">0.15</span>))</td>
      </tr>
      <tr>
        <td id="L300" class="blob-num js-line-number" data-line-number="300"></td>
        <td id="LC300" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L301" class="blob-num js-line-number" data-line-number="301"></td>
        <td id="LC301" class="blob-code blob-code-inner js-file-line">                leg.append(getLegend())</td>
      </tr>
      <tr>
        <td id="L302" class="blob-num js-line-number" data-line-number="302"></td>
        <td id="LC302" class="blob-code blob-code-inner js-file-line">            frame.append( w.var(options.var).frame() ) </td>
      </tr>
      <tr>
        <td id="L303" class="blob-num js-line-number" data-line-number="303"></td>
        <td id="LC303" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L304" class="blob-num js-line-number" data-line-number="304"></td>
        <td id="LC304" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> ii <span class="pl-k">==</span><span class="pl-c1">0</span>:</td>
      </tr>
      <tr>
        <td id="L305" class="blob-num js-line-number" data-line-number="305"></td>
        <td id="LC305" class="blob-code blob-code-inner js-file-line">                leg.append(getLegend(<span class="pl-c1">0.05</span>,<span class="pl-c1">0.46</span>))</td>
      </tr>
      <tr>
        <td id="L306" class="blob-num js-line-number" data-line-number="306"></td>
        <td id="LC306" class="blob-code blob-code-inner js-file-line">                frame.append( w.var(options.var).frame() ) </td>
      </tr>
      <tr>
        <td id="L307" class="blob-num js-line-number" data-line-number="307"></td>
        <td id="LC307" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> options.var<span class="pl-k">==</span><span class="pl-s"><span class="pl-pds">&#39;</span>mJ<span class="pl-pds">&#39;</span></span>:</td>
      </tr>
      <tr>
        <td id="L308" class="blob-num js-line-number" data-line-number="308"></td>
        <td id="LC308" class="blob-code blob-code-inner js-file-line">            frame[<span class="pl-k">-</span><span class="pl-c1">1</span>].SetAxisRange(<span class="pl-c1">55</span>,<span class="pl-c1">150</span>)</td>
      </tr>
      <tr>
        <td id="L309" class="blob-num js-line-number" data-line-number="309"></td>
        <td id="LC309" class="blob-code blob-code-inner js-file-line">        frame[<span class="pl-k">-</span><span class="pl-c1">1</span>].SetTitle(<span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L310" class="blob-num js-line-number" data-line-number="310"></td>
        <td id="LC310" class="blob-code blob-code-inner js-file-line">        name <span class="pl-k">=</span> f.split(<span class="pl-s"><span class="pl-pds">&quot;</span>_<span class="pl-pds">&quot;</span></span>)[<span class="pl-c1">1</span>]</td>
      </tr>
      <tr>
        <td id="L311" class="blob-num js-line-number" data-line-number="311"></td>
        <td id="LC311" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">with</span> <span class="pl-c1">open</span>(options.indir<span class="pl-k">+</span>f) <span class="pl-k">as</span> jsonFile:</td>
      </tr>
      <tr>
        <td id="L312" class="blob-num js-line-number" data-line-number="312"></td>
        <td id="LC312" class="blob-code blob-code-inner js-file-line">          j <span class="pl-k">=</span> json.load(jsonFile)</td>
      </tr>
      <tr>
        <td id="L313" class="blob-num js-line-number" data-line-number="313"></td>
        <td id="LC313" class="blob-code blob-code-inner js-file-line">          <span class="pl-k">for</span> i, <span class="pl-c1">MH</span> <span class="pl-k">in</span> <span class="pl-c1">enumerate</span>(massPoints):  <span class="pl-c"><span class="pl-c">#</span> mind that MH is evaluated below</span></td>
      </tr>
      <tr>
        <td id="L314" class="blob-num js-line-number" data-line-number="314"></td>
        <td id="LC314" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> options.var <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>mVV<span class="pl-pds">&#39;</span></span>: getMVVPdf(w,j,<span class="pl-c1">MH</span>,name)</td>
      </tr>
      <tr>
        <td id="L315" class="blob-num js-line-number" data-line-number="315"></td>
        <td id="LC315" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">else</span>: </td>
      </tr>
      <tr>
        <td id="L316" class="blob-num js-line-number" data-line-number="316"></td>
        <td id="LC316" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">if</span> f.find(<span class="pl-s"><span class="pl-pds">&quot;</span>ZH<span class="pl-pds">&quot;</span></span>)<span class="pl-k">==</span><span class="pl-k">-</span><span class="pl-c1">1</span>:</td>
      </tr>
      <tr>
        <td id="L317" class="blob-num js-line-number" data-line-number="317"></td>
        <td id="LC317" class="blob-code blob-code-inner js-file-line">                    <span class="pl-c1">print</span> <span class="pl-s"><span class="pl-pds">&quot;</span>no H boson in sample <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L318" class="blob-num js-line-number" data-line-number="318"></td>
        <td id="LC318" class="blob-code blob-code-inner js-file-line">                    getMJPdf(w,j,<span class="pl-c1">MH</span>,name)</td>
      </tr>
      <tr>
        <td id="L319" class="blob-num js-line-number" data-line-number="319"></td>
        <td id="LC319" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">if</span> f.find(<span class="pl-s"><span class="pl-pds">&quot;</span>Vjet<span class="pl-pds">&quot;</span></span>)<span class="pl-k">!=</span><span class="pl-k">-</span><span class="pl-c1">1</span>:</td>
      </tr>
      <tr>
        <td id="L320" class="blob-num js-line-number" data-line-number="320"></td>
        <td id="LC320" class="blob-code blob-code-inner js-file-line">                    <span class="pl-k">with</span> <span class="pl-c1">open</span>(options.indir<span class="pl-k">+</span>f.replace(<span class="pl-s"><span class="pl-pds">&quot;</span>Vjet<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>Hjet<span class="pl-pds">&quot;</span></span>)) <span class="pl-k">as</span> jsonFileH:</td>
      </tr>
      <tr>
        <td id="L321" class="blob-num js-line-number" data-line-number="321"></td>
        <td id="LC321" class="blob-code blob-code-inner js-file-line">                        jH <span class="pl-k">=</span> json.load(jsonFileH)</td>
      </tr>
      <tr>
        <td id="L322" class="blob-num js-line-number" data-line-number="322"></td>
        <td id="LC322" class="blob-code blob-code-inner js-file-line">                    getMJPdf(j,<span class="pl-c1">MH</span>,name,jH)</td>
      </tr>
      <tr>
        <td id="L323" class="blob-num js-line-number" data-line-number="323"></td>
        <td id="LC323" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">if</span> f.find(<span class="pl-s"><span class="pl-pds">&quot;</span>Hjet<span class="pl-pds">&quot;</span></span>)<span class="pl-k">!=</span><span class="pl-k">-</span><span class="pl-c1">1</span>:</td>
      </tr>
      <tr>
        <td id="L324" class="blob-num js-line-number" data-line-number="324"></td>
        <td id="LC324" class="blob-code blob-code-inner js-file-line">                    <span class="pl-k">with</span> <span class="pl-c1">open</span>(options.indir<span class="pl-k">+</span>f.replace(<span class="pl-s"><span class="pl-pds">&quot;</span>Hjet<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>Vjet<span class="pl-pds">&quot;</span></span>)) <span class="pl-k">as</span> jsonFileV:</td>
      </tr>
      <tr>
        <td id="L325" class="blob-num js-line-number" data-line-number="325"></td>
        <td id="LC325" class="blob-code blob-code-inner js-file-line">                        jV <span class="pl-k">=</span> json.load(jsonFileV)</td>
      </tr>
      <tr>
        <td id="L326" class="blob-num js-line-number" data-line-number="326"></td>
        <td id="LC326" class="blob-code blob-code-inner js-file-line">                    getMJPdf(w,jV,<span class="pl-c1">MH</span>,name,j)</td>
      </tr>
      <tr>
        <td id="L327" class="blob-num js-line-number" data-line-number="327"></td>
        <td id="LC327" class="blob-code blob-code-inner js-file-line">  </td>
      </tr>
      <tr>
        <td id="L328" class="blob-num js-line-number" data-line-number="328"></td>
        <td id="LC328" class="blob-code blob-code-inner js-file-line">  </td>
      </tr>
      <tr>
        <td id="L329" class="blob-num js-line-number" data-line-number="329"></td>
        <td id="LC329" class="blob-code blob-code-inner js-file-line">            w.pdf(<span class="pl-s"><span class="pl-pds">&#39;</span>signal_<span class="pl-c1">%d%s</span><span class="pl-pds">&#39;</span></span><span class="pl-k">%</span>(<span class="pl-c1">MH</span>,name)).plotOn(frame[<span class="pl-k">-</span><span class="pl-c1">1</span>], <span class="pl-c1">ROOT</span>.RooFit.LineColor(<span class="pl-c1">ROOT</span>.TColor.GetColor(colors[ii][i])),<span class="pl-c1">ROOT</span>.RooFit.Name(<span class="pl-c1">str</span>(<span class="pl-c1">MH</span>)<span class="pl-k">+</span>name))<span class="pl-c"><span class="pl-c">#</span>,ROOT.RooFit.Range(MH*0.8,1.2*MH))#ROOT.RooFit.Normalization(1, ROOT.RooAbsReal.RelativeExpected),</span></td>
      </tr>
      <tr>
        <td id="L330" class="blob-num js-line-number" data-line-number="330"></td>
        <td id="LC330" class="blob-code blob-code-inner js-file-line">      </td>
      </tr>
      <tr>
        <td id="L331" class="blob-num js-line-number" data-line-number="331"></td>
        <td id="LC331" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> options.var <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>mVV<span class="pl-pds">&#39;</span></span>: </td>
      </tr>
      <tr>
        <td id="L332" class="blob-num js-line-number" data-line-number="332"></td>
        <td id="LC332" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> ii,f <span class="pl-k">in</span> <span class="pl-c1">enumerate</span>(jsons):</td>
      </tr>
      <tr>
        <td id="L333" class="blob-num js-line-number" data-line-number="333"></td>
        <td id="LC333" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">print</span> <span class="pl-c1">len</span>(jsons)</td>
      </tr>
      <tr>
        <td id="L334" class="blob-num js-line-number" data-line-number="334"></td>
        <td id="LC334" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">print</span> ii</td>
      </tr>
      <tr>
        <td id="L335" class="blob-num js-line-number" data-line-number="335"></td>
        <td id="LC335" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">print</span> <span class="pl-s"><span class="pl-pds">&quot;</span>json <span class="pl-pds">&quot;</span></span><span class="pl-k">+</span><span class="pl-c1">str</span>(jsons[<span class="pl-c1">len</span>(jsons)<span class="pl-k">-</span>ii<span class="pl-k">-</span><span class="pl-c1">1</span>])</td>
      </tr>
      <tr>
        <td id="L336" class="blob-num js-line-number" data-line-number="336"></td>
        <td id="LC336" class="blob-code blob-code-inner js-file-line">            name <span class="pl-k">=</span> jsons[ii].split(<span class="pl-s"><span class="pl-pds">&quot;</span>_<span class="pl-pds">&quot;</span></span>)[<span class="pl-c1">1</span>]</td>
      </tr>
      <tr>
        <td id="L337" class="blob-num js-line-number" data-line-number="337"></td>
        <td id="LC337" class="blob-code blob-code-inner js-file-line">            leg[ii].AddEntry(frame[ii].findObject(<span class="pl-c1">str</span>(<span class="pl-c1">2000</span>)<span class="pl-k">+</span>name), legs[ii], <span class="pl-s"><span class="pl-pds">&quot;</span>L<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L338" class="blob-num js-line-number" data-line-number="338"></td>
        <td id="LC338" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L339" class="blob-num js-line-number" data-line-number="339"></td>
        <td id="LC339" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> ii,f <span class="pl-k">in</span> <span class="pl-c1">enumerate</span>(jsons):</td>
      </tr>
      <tr>
        <td id="L340" class="blob-num js-line-number" data-line-number="340"></td>
        <td id="LC340" class="blob-code blob-code-inner js-file-line">            name <span class="pl-k">=</span> jsons[<span class="pl-c1">len</span>(jsons)<span class="pl-k">-</span>ii<span class="pl-k">-</span><span class="pl-c1">1</span>].split(<span class="pl-s"><span class="pl-pds">&quot;</span>_<span class="pl-pds">&quot;</span></span>)[<span class="pl-c1">1</span>]</td>
      </tr>
      <tr>
        <td id="L341" class="blob-num js-line-number" data-line-number="341"></td>
        <td id="LC341" class="blob-code blob-code-inner js-file-line">            leg[<span class="pl-k">-</span><span class="pl-c1">1</span>].AddEntry(frame[<span class="pl-c1">0</span>].findObject(<span class="pl-c1">str</span>(<span class="pl-c1">2000</span>)<span class="pl-k">+</span>name),legs[<span class="pl-c1">len</span>(jsons)<span class="pl-k">-</span>ii<span class="pl-k">-</span><span class="pl-c1">1</span>],<span class="pl-s"><span class="pl-pds">&quot;</span>L<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L342" class="blob-num js-line-number" data-line-number="342"></td>
        <td id="LC342" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L343" class="blob-num js-line-number" data-line-number="343"></td>
        <td id="LC343" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">for</span> i <span class="pl-k">in</span> <span class="pl-c1">range</span>(<span class="pl-c1">1</span>,<span class="pl-c1">len</span>(frame)<span class="pl-k">+</span><span class="pl-c1">1</span>):</td>
      </tr>
      <tr>
        <td id="L344" class="blob-num js-line-number" data-line-number="344"></td>
        <td id="LC344" class="blob-code blob-code-inner js-file-line">        c1.cd(i)</td>
      </tr>
      <tr>
        <td id="L345" class="blob-num js-line-number" data-line-number="345"></td>
        <td id="LC345" class="blob-code blob-code-inner js-file-line">        c1.cd(i).SetTickx()</td>
      </tr>
      <tr>
        <td id="L346" class="blob-num js-line-number" data-line-number="346"></td>
        <td id="LC346" class="blob-code blob-code-inner js-file-line">        c1.cd(i).SetTicky()</td>
      </tr>
      <tr>
        <td id="L347" class="blob-num js-line-number" data-line-number="347"></td>
        <td id="LC347" class="blob-code blob-code-inner js-file-line">      </td>
      </tr>
      <tr>
        <td id="L348" class="blob-num js-line-number" data-line-number="348"></td>
        <td id="LC348" class="blob-code blob-code-inner js-file-line">      </td>
      </tr>
      <tr>
        <td id="L349" class="blob-num js-line-number" data-line-number="349"></td>
        <td id="LC349" class="blob-code blob-code-inner js-file-line">        frame[i<span class="pl-k">-</span><span class="pl-c1">1</span>].GetYaxis().SetTitle(<span class="pl-s"><span class="pl-pds">&quot;</span>a. u.<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L350" class="blob-num js-line-number" data-line-number="350"></td>
        <td id="LC350" class="blob-code blob-code-inner js-file-line">        frame[i<span class="pl-k">-</span><span class="pl-c1">1</span>].GetYaxis().SetTitleOffset(<span class="pl-c1">1.18</span>)</td>
      </tr>
      <tr>
        <td id="L351" class="blob-num js-line-number" data-line-number="351"></td>
        <td id="LC351" class="blob-code blob-code-inner js-file-line">        frame[i<span class="pl-k">-</span><span class="pl-c1">1</span>].GetXaxis().SetTitleOffset(<span class="pl-c1">0.9</span>)</td>
      </tr>
      <tr>
        <td id="L352" class="blob-num js-line-number" data-line-number="352"></td>
        <td id="LC352" class="blob-code blob-code-inner js-file-line">        frame[i<span class="pl-k">-</span><span class="pl-c1">1</span>].GetYaxis().SetNdivisions(<span class="pl-c1">6</span>,<span class="pl-c1">5</span>,<span class="pl-c1">1</span>)</td>
      </tr>
      <tr>
        <td id="L353" class="blob-num js-line-number" data-line-number="353"></td>
        <td id="LC353" class="blob-code blob-code-inner js-file-line">        frame[i<span class="pl-k">-</span><span class="pl-c1">1</span>].GetXaxis().SetNdivisions(<span class="pl-c1">6</span>,<span class="pl-c1">5</span>,<span class="pl-c1">1</span>)</td>
      </tr>
      <tr>
        <td id="L354" class="blob-num js-line-number" data-line-number="354"></td>
        <td id="LC354" class="blob-code blob-code-inner js-file-line">        frame[i<span class="pl-k">-</span><span class="pl-c1">1</span>].SetMaximum(<span class="pl-c1">0.17</span>)</td>
      </tr>
      <tr>
        <td id="L355" class="blob-num js-line-number" data-line-number="355"></td>
        <td id="LC355" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> options.var <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>mVV<span class="pl-pds">&#39;</span></span>:</td>
      </tr>
      <tr>
        <td id="L356" class="blob-num js-line-number" data-line-number="356"></td>
        <td id="LC356" class="blob-code blob-code-inner js-file-line">            frame[i<span class="pl-k">-</span><span class="pl-c1">1</span>].SetMaximum(<span class="pl-c1">0.45</span>)</td>
      </tr>
      <tr>
        <td id="L357" class="blob-num js-line-number" data-line-number="357"></td>
        <td id="LC357" class="blob-code blob-code-inner js-file-line">            frame[i<span class="pl-k">-</span><span class="pl-c1">1</span>].GetYaxis().SetNdivisions(<span class="pl-c1">0</span>,<span class="pl-c1">5</span>,<span class="pl-c1">0</span>,<span class="pl-c1">False</span>)</td>
      </tr>
      <tr>
        <td id="L358" class="blob-num js-line-number" data-line-number="358"></td>
        <td id="LC358" class="blob-code blob-code-inner js-file-line">            frame[i<span class="pl-k">-</span><span class="pl-c1">1</span>].GetYaxis().SetTitleOffset(<span class="pl-c1">0.25</span>)</td>
      </tr>
      <tr>
        <td id="L359" class="blob-num js-line-number" data-line-number="359"></td>
        <td id="LC359" class="blob-code blob-code-inner js-file-line">            frame[i<span class="pl-k">-</span><span class="pl-c1">1</span>].GetXaxis().SetTitleSize(<span class="pl-c1">0.20</span>)</td>
      </tr>
      <tr>
        <td id="L360" class="blob-num js-line-number" data-line-number="360"></td>
        <td id="LC360" class="blob-code blob-code-inner js-file-line">            frame[i<span class="pl-k">-</span><span class="pl-c1">1</span>].GetYaxis().SetTitleSize(<span class="pl-c1">0.20</span>)</td>
      </tr>
      <tr>
        <td id="L361" class="blob-num js-line-number" data-line-number="361"></td>
        <td id="LC361" class="blob-code blob-code-inner js-file-line">            frame[i<span class="pl-k">-</span><span class="pl-c1">1</span>].GetYaxis().SetLabelSize(<span class="pl-c1">0.20</span>)</td>
      </tr>
      <tr>
        <td id="L362" class="blob-num js-line-number" data-line-number="362"></td>
        <td id="LC362" class="blob-code blob-code-inner js-file-line">            frame[i<span class="pl-k">-</span><span class="pl-c1">1</span>].GetXaxis().SetLabelSize(<span class="pl-c1">0.20</span>)</td>
      </tr>
      <tr>
        <td id="L363" class="blob-num js-line-number" data-line-number="363"></td>
        <td id="LC363" class="blob-code blob-code-inner js-file-line">            <span class="pl-c"><span class="pl-c">#</span>frame[i-1].Draw()</span></td>
      </tr>
      <tr>
        <td id="L364" class="blob-num js-line-number" data-line-number="364"></td>
        <td id="LC364" class="blob-code blob-code-inner js-file-line">            frame[i<span class="pl-k">-</span><span class="pl-c1">1</span>].GetXaxis().SetTickLength(<span class="pl-c1">0.1</span>)</td>
      </tr>
      <tr>
        <td id="L365" class="blob-num js-line-number" data-line-number="365"></td>
        <td id="LC365" class="blob-code blob-code-inner js-file-line">            frame[<span class="pl-k">-</span><span class="pl-c1">1</span>].GetYaxis().SetLabelSize(<span class="pl-c1">0.14</span>) </td>
      </tr>
      <tr>
        <td id="L366" class="blob-num js-line-number" data-line-number="366"></td>
        <td id="LC366" class="blob-code blob-code-inner js-file-line">            frame[<span class="pl-k">-</span><span class="pl-c1">1</span>].GetXaxis().SetLabelSize(<span class="pl-c1">0.14</span>)</td>
      </tr>
      <tr>
        <td id="L367" class="blob-num js-line-number" data-line-number="367"></td>
        <td id="LC367" class="blob-code blob-code-inner js-file-line">            frame[<span class="pl-k">-</span><span class="pl-c1">1</span>].GetXaxis().SetTitleSize(<span class="pl-c1">0.14</span>)</td>
      </tr>
      <tr>
        <td id="L368" class="blob-num js-line-number" data-line-number="368"></td>
        <td id="LC368" class="blob-code blob-code-inner js-file-line">            frame[<span class="pl-k">-</span><span class="pl-c1">1</span>].GetYaxis().SetTitleSize(<span class="pl-c1">0.14</span>)</td>
      </tr>
      <tr>
        <td id="L369" class="blob-num js-line-number" data-line-number="369"></td>
        <td id="LC369" class="blob-code blob-code-inner js-file-line">            frame[<span class="pl-k">-</span><span class="pl-c1">1</span>].GetYaxis().SetTitleOffset(<span class="pl-c1">0.35</span>)</td>
      </tr>
      <tr>
        <td id="L370" class="blob-num js-line-number" data-line-number="370"></td>
        <td id="LC370" class="blob-code blob-code-inner js-file-line">            frame[<span class="pl-k">-</span><span class="pl-c1">1</span>].GetXaxis().SetTitleOffset(<span class="pl-c1">1.05</span>)</td>
      </tr>
      <tr>
        <td id="L371" class="blob-num js-line-number" data-line-number="371"></td>
        <td id="LC371" class="blob-code blob-code-inner js-file-line">            frame[<span class="pl-k">-</span><span class="pl-c1">1</span>].GetXaxis().SetLabelOffset(<span class="pl-c1">0.05</span>)</td>
      </tr>
      <tr>
        <td id="L372" class="blob-num js-line-number" data-line-number="372"></td>
        <td id="LC372" class="blob-code blob-code-inner js-file-line">            frame[<span class="pl-k">-</span><span class="pl-c1">1</span>].GetXaxis().SetTickLength(<span class="pl-c1">0.08</span>)</td>
      </tr>
      <tr>
        <td id="L373" class="blob-num js-line-number" data-line-number="373"></td>
        <td id="LC373" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">else</span>:    </td>
      </tr>
      <tr>
        <td id="L374" class="blob-num js-line-number" data-line-number="374"></td>
        <td id="LC374" class="blob-code blob-code-inner js-file-line">            </td>
      </tr>
      <tr>
        <td id="L375" class="blob-num js-line-number" data-line-number="375"></td>
        <td id="LC375" class="blob-code blob-code-inner js-file-line">            frame[i<span class="pl-k">-</span><span class="pl-c1">1</span>].GetXaxis().SetTitleSize(<span class="pl-c1">0.06</span>)</td>
      </tr>
      <tr>
        <td id="L376" class="blob-num js-line-number" data-line-number="376"></td>
        <td id="LC376" class="blob-code blob-code-inner js-file-line">            frame[i<span class="pl-k">-</span><span class="pl-c1">1</span>].GetYaxis().SetTitleSize(<span class="pl-c1">0.06</span>)</td>
      </tr>
      <tr>
        <td id="L377" class="blob-num js-line-number" data-line-number="377"></td>
        <td id="LC377" class="blob-code blob-code-inner js-file-line">            frame[i<span class="pl-k">-</span><span class="pl-c1">1</span>].GetYaxis().SetLabelSize(<span class="pl-c1">0.05</span>)</td>
      </tr>
      <tr>
        <td id="L378" class="blob-num js-line-number" data-line-number="378"></td>
        <td id="LC378" class="blob-code blob-code-inner js-file-line">            frame[i<span class="pl-k">-</span><span class="pl-c1">1</span>].GetXaxis().SetLabelSize(<span class="pl-c1">0.05</span>)</td>
      </tr>
      <tr>
        <td id="L379" class="blob-num js-line-number" data-line-number="379"></td>
        <td id="LC379" class="blob-code blob-code-inner js-file-line">                </td>
      </tr>
      <tr>
        <td id="L380" class="blob-num js-line-number" data-line-number="380"></td>
        <td id="LC380" class="blob-code blob-code-inner js-file-line">        frame[i<span class="pl-k">-</span><span class="pl-c1">1</span>].Draw()</td>
      </tr>
      <tr>
        <td id="L381" class="blob-num js-line-number" data-line-number="381"></td>
        <td id="LC381" class="blob-code blob-code-inner js-file-line">        leg[i<span class="pl-k">-</span><span class="pl-c1">1</span>].Draw(<span class="pl-s"><span class="pl-pds">&quot;</span>same<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L382" class="blob-num js-line-number" data-line-number="382"></td>
        <td id="LC382" class="blob-code blob-code-inner js-file-line">    </td>
      </tr>
      <tr>
        <td id="L383" class="blob-num js-line-number" data-line-number="383"></td>
        <td id="LC383" class="blob-code blob-code-inner js-file-line">    </td>
      </tr>
      <tr>
        <td id="L384" class="blob-num js-line-number" data-line-number="384"></td>
        <td id="LC384" class="blob-code blob-code-inner js-file-line">    pt2 <span class="pl-k">=</span> <span class="pl-c1">ROOT</span>.TPaveText(<span class="pl-c1">0.16</span>,<span class="pl-c1">0.62</span>,<span class="pl-c1">0.63</span>,<span class="pl-c1">0.76</span>,<span class="pl-s"><span class="pl-pds">&quot;</span>NDC<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L385" class="blob-num js-line-number" data-line-number="385"></td>
        <td id="LC385" class="blob-code blob-code-inner js-file-line">    pt2.SetTextFont(<span class="pl-c1">42</span>)</td>
      </tr>
      <tr>
        <td id="L386" class="blob-num js-line-number" data-line-number="386"></td>
        <td id="LC386" class="blob-code blob-code-inner js-file-line">    pt2.SetTextSize(<span class="pl-c1">0.04</span>)</td>
      </tr>
      <tr>
        <td id="L387" class="blob-num js-line-number" data-line-number="387"></td>
        <td id="LC387" class="blob-code blob-code-inner js-file-line">    pt2.SetTextAlign(<span class="pl-c1">12</span>)</td>
      </tr>
      <tr>
        <td id="L388" class="blob-num js-line-number" data-line-number="388"></td>
        <td id="LC388" class="blob-code blob-code-inner js-file-line">    pt2.SetFillColor(<span class="pl-c1">0</span>)</td>
      </tr>
      <tr>
        <td id="L389" class="blob-num js-line-number" data-line-number="389"></td>
        <td id="LC389" class="blob-code blob-code-inner js-file-line">    pt2.SetBorderSize(<span class="pl-c1">0</span>)</td>
      </tr>
      <tr>
        <td id="L390" class="blob-num js-line-number" data-line-number="390"></td>
        <td id="LC390" class="blob-code blob-code-inner js-file-line">    pt2.SetFillStyle(<span class="pl-c1">0</span>)</td>
      </tr>
      <tr>
        <td id="L391" class="blob-num js-line-number" data-line-number="391"></td>
        <td id="LC391" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L392" class="blob-num js-line-number" data-line-number="392"></td>
        <td id="LC392" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> options.var <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>mJ<span class="pl-pds">&#39;</span></span>: pt2.AddText(category)</td>
      </tr>
      <tr>
        <td id="L393" class="blob-num js-line-number" data-line-number="393"></td>
        <td id="LC393" class="blob-code blob-code-inner js-file-line">    pt2.Draw()</td>
      </tr>
      <tr>
        <td id="L394" class="blob-num js-line-number" data-line-number="394"></td>
        <td id="LC394" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>    if options.var ==&quot;mVV&quot;: category = &quot;Vall&quot;</span></td>
      </tr>
      <tr>
        <td id="L395" class="blob-num js-line-number" data-line-number="395"></td>
        <td id="LC395" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> options.prelim<span class="pl-k">==</span><span class="pl-s"><span class="pl-pds">&quot;</span>1<span class="pl-pds">&quot;</span></span>:</td>
      </tr>
      <tr>
        <td id="L396" class="blob-num js-line-number" data-line-number="396"></td>
        <td id="LC396" class="blob-code blob-code-inner js-file-line">        cmslabel_sim_prelim(c1,<span class="pl-s"><span class="pl-pds">&#39;</span>sim<span class="pl-pds">&#39;</span></span>,<span class="pl-c1">11</span>)</td>
      </tr>
      <tr>
        <td id="L397" class="blob-num js-line-number" data-line-number="397"></td>
        <td id="LC397" class="blob-code blob-code-inner js-file-line">        c1.Update()</td>
      </tr>
      <tr>
        <td id="L398" class="blob-num js-line-number" data-line-number="398"></td>
        <td id="LC398" class="blob-code blob-code-inner js-file-line">        c1.SaveAs(path<span class="pl-k">+</span><span class="pl-s"><span class="pl-pds">&quot;</span>signalShapes_<span class="pl-c1">%s</span>_<span class="pl-c1">%s</span>_<span class="pl-c1">%s</span>_All_<span class="pl-c1">%s</span>_prelim.png<span class="pl-pds">&quot;</span></span>  <span class="pl-k">%</span>(options.var,category,options.year,options.name))</td>
      </tr>
      <tr>
        <td id="L399" class="blob-num js-line-number" data-line-number="399"></td>
        <td id="LC399" class="blob-code blob-code-inner js-file-line">        c1.SaveAs(path<span class="pl-k">+</span><span class="pl-s"><span class="pl-pds">&quot;</span>signalShapes_<span class="pl-c1">%s</span>_<span class="pl-c1">%s</span>_<span class="pl-c1">%s</span>_All_<span class="pl-c1">%s</span>_prelim.pdf<span class="pl-pds">&quot;</span></span>  <span class="pl-k">%</span>(options.var,category,options.year,options.name))</td>
      </tr>
      <tr>
        <td id="L400" class="blob-num js-line-number" data-line-number="400"></td>
        <td id="LC400" class="blob-code blob-code-inner js-file-line">        c1.SaveAs(path<span class="pl-k">+</span><span class="pl-s"><span class="pl-pds">&quot;</span>signalShapes_<span class="pl-c1">%s</span>_<span class="pl-c1">%s</span>_<span class="pl-c1">%s</span>_All_<span class="pl-c1">%s</span>_prelim.C<span class="pl-pds">&quot;</span></span>    <span class="pl-k">%</span>(options.var,category,options.year,options.name))</td>
      </tr>
      <tr>
        <td id="L401" class="blob-num js-line-number" data-line-number="401"></td>
        <td id="LC401" class="blob-code blob-code-inner js-file-line">        c1.SaveAs(path<span class="pl-k">+</span><span class="pl-s"><span class="pl-pds">&quot;</span>signalShapes_<span class="pl-c1">%s</span>_<span class="pl-c1">%s</span>_<span class="pl-c1">%s</span>_All_<span class="pl-c1">%s</span>_prelim.root<span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span>(options.var,category,options.year,options.name))</td>
      </tr>
      <tr>
        <td id="L402" class="blob-num js-line-number" data-line-number="402"></td>
        <td id="LC402" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L403" class="blob-num js-line-number" data-line-number="403"></td>
        <td id="LC403" class="blob-code blob-code-inner js-file-line">        cmslabel_sim(c1,<span class="pl-s"><span class="pl-pds">&#39;</span>sim<span class="pl-pds">&#39;</span></span>,<span class="pl-c1">11</span>)</td>
      </tr>
      <tr>
        <td id="L404" class="blob-num js-line-number" data-line-number="404"></td>
        <td id="LC404" class="blob-code blob-code-inner js-file-line">        c1.Update()</td>
      </tr>
      <tr>
        <td id="L405" class="blob-num js-line-number" data-line-number="405"></td>
        <td id="LC405" class="blob-code blob-code-inner js-file-line">        </td>
      </tr>
      <tr>
        <td id="L406" class="blob-num js-line-number" data-line-number="406"></td>
        <td id="LC406" class="blob-code blob-code-inner js-file-line">        c1.SaveAs(path<span class="pl-k">+</span><span class="pl-s"><span class="pl-pds">&quot;</span>signalShapes_<span class="pl-c1">%s</span>_<span class="pl-c1">%s</span>_<span class="pl-c1">%s</span>_All_<span class="pl-c1">%s</span>.png<span class="pl-pds">&quot;</span></span>  <span class="pl-k">%</span>(options.var,category,options.year,options.name))</td>
      </tr>
      <tr>
        <td id="L407" class="blob-num js-line-number" data-line-number="407"></td>
        <td id="LC407" class="blob-code blob-code-inner js-file-line">        c1.SaveAs(path<span class="pl-k">+</span><span class="pl-s"><span class="pl-pds">&quot;</span>signalShapes_<span class="pl-c1">%s</span>_<span class="pl-c1">%s</span>_<span class="pl-c1">%s</span>_All_<span class="pl-c1">%s</span>.pdf<span class="pl-pds">&quot;</span></span>  <span class="pl-k">%</span>(options.var,category,options.year,options.name))</td>
      </tr>
      <tr>
        <td id="L408" class="blob-num js-line-number" data-line-number="408"></td>
        <td id="LC408" class="blob-code blob-code-inner js-file-line">        c1.SaveAs(path<span class="pl-k">+</span><span class="pl-s"><span class="pl-pds">&quot;</span>signalShapes_<span class="pl-c1">%s</span>_<span class="pl-c1">%s</span>_<span class="pl-c1">%s</span>_All_<span class="pl-c1">%s</span>.C<span class="pl-pds">&quot;</span></span>    <span class="pl-k">%</span>(options.var,category,options.year,options.name))</td>
      </tr>
      <tr>
        <td id="L409" class="blob-num js-line-number" data-line-number="409"></td>
        <td id="LC409" class="blob-code blob-code-inner js-file-line">        c1.SaveAs(path<span class="pl-k">+</span><span class="pl-s"><span class="pl-pds">&quot;</span>signalShapes_<span class="pl-c1">%s</span>_<span class="pl-c1">%s</span>_<span class="pl-c1">%s</span>_All_<span class="pl-c1">%s</span>.root<span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span>(options.var,category,options.year,options.name))</td>
      </tr>
      <tr>
        <td id="L410" class="blob-num js-line-number" data-line-number="410"></td>
        <td id="LC410" class="blob-code blob-code-inner js-file-line">    </td>
      </tr>
      <tr>
        <td id="L411" class="blob-num js-line-number" data-line-number="411"></td>
        <td id="LC411" class="blob-code blob-code-inner js-file-line">      </td>
      </tr>
      <tr>
        <td id="L412" class="blob-num js-line-number" data-line-number="412"></td>
        <td id="LC412" class="blob-code blob-code-inner js-file-line"><span class="pl-k">if</span> <span class="pl-c1">__name__</span> <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>__main__<span class="pl-pds">&#39;</span></span>:</td>
      </tr>
      <tr>
        <td id="L413" class="blob-num js-line-number" data-line-number="413"></td>
        <td id="LC413" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"><span class="pl-c">#</span>doSingle()</span></td>
      </tr>
      <tr>
        <td id="L414" class="blob-num js-line-number" data-line-number="414"></td>
        <td id="LC414" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>    legs = [&quot;G_{bulk} #rightarrow WW&quot;]</span></td>
      </tr>
      <tr>
        <td id="L415" class="blob-num js-line-number" data-line-number="415"></td>
        <td id="LC415" class="blob-code blob-code-inner js-file-line">    legs <span class="pl-k">=</span> [<span class="pl-s"><span class="pl-pds">&quot;</span>G_<span class="pl-c1">{bulk}</span> #rightarrow ZZ<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>W&#39; #rightarrow WZ<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>G_<span class="pl-c1">{bulk}</span> #rightarrow WW<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>Z&#39;#rightarrow WW<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>Z&#39; #rightarrow ZH<span class="pl-pds">&quot;</span></span>]</td>
      </tr>
      <tr>
        <td id="L416" class="blob-num js-line-number" data-line-number="416"></td>
        <td id="LC416" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>    signals = [&quot;BulkGWW&quot;]</span></td>
      </tr>
      <tr>
        <td id="L417" class="blob-num js-line-number" data-line-number="417"></td>
        <td id="LC417" class="blob-code blob-code-inner js-file-line">    signals <span class="pl-k">=</span> [<span class="pl-s"><span class="pl-pds">&quot;</span>BulkGZZ<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>WprimeWZ<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>BulkGWW<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>ZprimeWW<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>ZprimeZH<span class="pl-pds">&quot;</span></span>]</td>
      </tr>
      <tr>
        <td id="L418" class="blob-num js-line-number" data-line-number="418"></td>
        <td id="LC418" class="blob-code blob-code-inner js-file-line">    categories <span class="pl-k">=</span> [<span class="pl-s"><span class="pl-pds">&quot;</span>VH_LPHP<span class="pl-pds">&quot;</span></span>] <span class="pl-c"><span class="pl-c">#</span>,&quot;VV_HPHP&quot;,&quot;VH_HPLP&quot;,&quot;VH_HPHP&quot;,&quot;VH_LPHP&quot;]</span></td>
      </tr>
      <tr>
        <td id="L419" class="blob-num js-line-number" data-line-number="419"></td>
        <td id="LC419" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>    categories = [&quot;VH_LPHP&quot;,&quot;VV_HPHP&quot;,&quot;VH_HPLP&quot;,&quot;VH_HPHP&quot;,&quot;VH_LPHP&quot;]</span></td>
      </tr>
      <tr>
        <td id="L420" class="blob-num js-line-number" data-line-number="420"></td>
        <td id="LC420" class="blob-code blob-code-inner js-file-line">    jsons<span class="pl-k">=</span>[]</td>
      </tr>
      <tr>
        <td id="L421" class="blob-num js-line-number" data-line-number="421"></td>
        <td id="LC421" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">for</span> category <span class="pl-k">in</span> categories:</td>
      </tr>
      <tr>
        <td id="L422" class="blob-num js-line-number" data-line-number="422"></td>
        <td id="LC422" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> s <span class="pl-k">in</span> signals:</td>
      </tr>
      <tr>
        <td id="L423" class="blob-num js-line-number" data-line-number="423"></td>
        <td id="LC423" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> options.var <span class="pl-k">==</span><span class="pl-s"><span class="pl-pds">&quot;</span>mJ<span class="pl-pds">&quot;</span></span> <span class="pl-k">and</span> s <span class="pl-k">!=</span> <span class="pl-s"><span class="pl-pds">&quot;</span>ZprimeZH<span class="pl-pds">&quot;</span></span>:</td>
      </tr>
      <tr>
        <td id="L424" class="blob-num js-line-number" data-line-number="424"></td>
        <td id="LC424" class="blob-code blob-code-inner js-file-line">                jsons.append(<span class="pl-s"><span class="pl-pds">&quot;</span>JJ_<span class="pl-pds">&quot;</span></span><span class="pl-k">+</span>s<span class="pl-k">+</span><span class="pl-s"><span class="pl-pds">&quot;</span>_2016_MJrandom_<span class="pl-pds">&quot;</span></span><span class="pl-k">+</span>category<span class="pl-k">+</span><span class="pl-s"><span class="pl-pds">&quot;</span>.json<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L425" class="blob-num js-line-number" data-line-number="425"></td>
        <td id="LC425" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L426" class="blob-num js-line-number" data-line-number="426"></td>
        <td id="LC426" class="blob-code blob-code-inner js-file-line">              <span class="pl-k">if</span> s <span class="pl-k">!=</span> <span class="pl-s"><span class="pl-pds">&quot;</span>ZprimeZH<span class="pl-pds">&quot;</span></span> <span class="pl-k">and</span> s <span class="pl-k">!=</span> <span class="pl-s"><span class="pl-pds">&quot;</span>WprimeWZ<span class="pl-pds">&quot;</span></span>:  jsons.append(<span class="pl-s"><span class="pl-pds">&quot;</span>JJ_<span class="pl-pds">&quot;</span></span><span class="pl-k">+</span>s<span class="pl-k">+</span><span class="pl-s"><span class="pl-pds">&quot;</span>_2016_MVV.json<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L427" class="blob-num js-line-number" data-line-number="427"></td>
        <td id="LC427" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> options.var<span class="pl-k">==</span><span class="pl-s"><span class="pl-pds">&quot;</span>mJ<span class="pl-pds">&quot;</span></span>:</td>
      </tr>
      <tr>
        <td id="L428" class="blob-num js-line-number" data-line-number="428"></td>
        <td id="LC428" class="blob-code blob-code-inner js-file-line">            jsons.append(<span class="pl-s"><span class="pl-pds">&quot;</span>JJ_Hjet_ZprimeZH_2016_MJrandom_<span class="pl-pds">&quot;</span></span><span class="pl-k">+</span>category<span class="pl-k">+</span><span class="pl-s"><span class="pl-pds">&quot;</span>.json<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L429" class="blob-num js-line-number" data-line-number="429"></td>
        <td id="LC429" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L430" class="blob-num js-line-number" data-line-number="430"></td>
        <td id="LC430" class="blob-code blob-code-inner js-file-line">          jsons.append(<span class="pl-s"><span class="pl-pds">&quot;</span>JJ_j1<span class="pl-pds">&quot;</span></span><span class="pl-k">+</span>s<span class="pl-k">+</span><span class="pl-s"><span class="pl-pds">&quot;</span>_2016_MVV.json<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L431" class="blob-num js-line-number" data-line-number="431"></td>
        <td id="LC431" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L432" class="blob-num js-line-number" data-line-number="432"></td>
        <td id="LC432" class="blob-code blob-code-inner js-file-line">        doAll(category,jsons,legs)</td>
      </tr>
</table>

  <details class="details-reset details-overlay BlobToolbar position-absolute js-file-line-actions dropdown d-none" aria-hidden="true">
    <summary class="btn-octicon ml-0 px-2 p-0 bg-white border border-gray-dark rounded-1" aria-label="Inline file action toolbar">
      <svg class="octicon octicon-kebab-horizontal" viewBox="0 0 13 16" version="1.1" width="13" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M1.5 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3zm5 0a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3zM13 7.5a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0z"/></svg>
    </summary>
    <details-menu>
      <ul class="BlobToolbar-dropdown dropdown-menu dropdown-menu-se mt-2" style="width:185px">
        <li>
          <clipboard-copy role="menuitem" class="dropdown-item" id="js-copy-lines" style="cursor:pointer;">
            Copy lines
          </clipboard-copy>
        </li>
        <li>
          <clipboard-copy role="menuitem" class="dropdown-item" id="js-copy-permalink" style="cursor:pointer;">
            Copy permalink
          </clipboard-copy>
        </li>
        <li><a class="dropdown-item js-update-url-with-hash" id="js-view-git-blame" role="menuitem" href="/IreneZoi/cmgtools-lite/blame/36f0f02d480c3c6dec6b9a970594efff50bb2b1b/VVResonances/interactive/plotSignalShapesFromJSON.py">View git blame</a></li>
      </ul>
    </details-menu>
  </details>

  </div>

    </div>

  

  <details class="details-reset details-overlay details-overlay-dark">
    <summary data-hotkey="l" aria-label="Jump to line"></summary>
    <details-dialog class="Box Box--overlay d-flex flex-column anim-fade-in fast linejump" aria-label="Jump to line">
      <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="js-jump-to-line-form Box-body d-flex" action="" accept-charset="UTF-8" method="get"><input name="utf8" type="hidden" value="&#x2713;" />
        <input class="form-control flex-auto mr-3 linejump-input js-jump-to-line-field" type="text" placeholder="Jump to line&hellip;" aria-label="Jump to line" autofocus>
        <button type="submit" class="btn" data-close-dialog>Go</button>
</form>    </details-dialog>
  </details>



  </div>
</div>

    </main>
  </div>
  

  </div>

        
<div class="footer container-lg width-full p-responsive" role="contentinfo">
  <div class="position-relative d-flex flex-row-reverse flex-lg-row flex-wrap flex-lg-nowrap flex-justify-center flex-lg-justify-between pt-6 pb-2 mt-6 f6 text-gray border-top border-gray-light ">
    <ul class="list-style-none d-flex flex-wrap col-12 col-lg-5 flex-justify-center flex-lg-justify-between mb-2 mb-lg-0">
      <li class="mr-3 mr-lg-0">&copy; 2019 <span title="0.29164s from unicorn-56c8bf5f74-mf688">GitHub</span>, Inc.</li>
        <li class="mr-3 mr-lg-0"><a data-ga-click="Footer, go to terms, text:terms" href="https://github.com/site/terms">Terms</a></li>
        <li class="mr-3 mr-lg-0"><a data-ga-click="Footer, go to privacy, text:privacy" href="https://github.com/site/privacy">Privacy</a></li>
        <li class="mr-3 mr-lg-0"><a data-ga-click="Footer, go to security, text:security" href="https://github.com/security">Security</a></li>
        <li class="mr-3 mr-lg-0"><a href="https://githubstatus.com/" data-ga-click="Footer, go to status, text:status">Status</a></li>
        <li><a data-ga-click="Footer, go to help, text:help" href="https://help.github.com">Help</a></li>
    </ul>

    <a aria-label="Homepage" title="GitHub" class="footer-octicon d-none d-lg-block mx-lg-4" href="https://github.com">
      <svg height="24" class="octicon octicon-mark-github" viewBox="0 0 16 16" version="1.1" width="24" aria-hidden="true"><path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"/></svg>
</a>
   <ul class="list-style-none d-flex flex-wrap col-12 col-lg-5 flex-justify-center flex-lg-justify-between mb-2 mb-lg-0">
        <li class="mr-3 mr-lg-0"><a data-ga-click="Footer, go to contact, text:contact" href="https://github.com/contact">Contact GitHub</a></li>
        <li class="mr-3 mr-lg-0"><a href="https://github.com/pricing" data-ga-click="Footer, go to Pricing, text:Pricing">Pricing</a></li>
      <li class="mr-3 mr-lg-0"><a href="https://developer.github.com" data-ga-click="Footer, go to api, text:api">API</a></li>
      <li class="mr-3 mr-lg-0"><a href="https://training.github.com" data-ga-click="Footer, go to training, text:training">Training</a></li>
        <li class="mr-3 mr-lg-0"><a href="https://github.blog" data-ga-click="Footer, go to blog, text:blog">Blog</a></li>
        <li><a data-ga-click="Footer, go to about, text:about" href="https://github.com/about">About</a></li>

    </ul>
  </div>
  <div class="d-flex flex-justify-center pb-6">
    <span class="f6 text-gray-light"></span>
  </div>
</div>



  <div id="ajax-error-message" class="ajax-error-message flash flash-error">
    <svg class="octicon octicon-alert" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8.893 1.5c-.183-.31-.52-.5-.887-.5s-.703.19-.886.5L.138 13.499a.98.98 0 0 0 0 1.001c.193.31.53.501.886.501h13.964c.367 0 .704-.19.877-.5a1.03 1.03 0 0 0 .01-1.002L8.893 1.5zm.133 11.497H6.987v-2.003h2.039v2.003zm0-3.004H6.987V5.987h2.039v4.006z"/></svg>
    <button type="button" class="flash-close js-ajax-error-dismiss" aria-label="Dismiss error">
      <svg class="octicon octicon-x" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48L7.48 8z"/></svg>
    </button>
    You can’t perform that action at this time.
  </div>


    <script crossorigin="anonymous" integrity="sha512-RwS+8T0XPR5cCcBdDmGcf/cL+FfKUdIjfRL93fvzAzjVUdgaknI2UpShICXEAx0szS45xu9lpIDeacN+3d3hZw==" type="application/javascript" src="https://github.githubassets.com/assets/compat-bootstrap-94789d4c.js"></script>
    <script crossorigin="anonymous" integrity="sha512-2e003yIUkuCG1IeaeQwIgzMwqYiC+7wN/ouvY2yay84wnLng3/MScKxudf02uj4T4RZAnF5zJumvacsF9lfTMw==" type="application/javascript" src="https://github.githubassets.com/assets/frameworks-8e9b232b.js"></script>
    
    <script crossorigin="anonymous" async="async" integrity="sha512-mcmHw7hIuXtLZC0Osul3Ua16sxQbp4NacU9maZbuKdB3ja+sQs5MJplJHEgyGuZv17JocEgD405+gMl+3ZY9+A==" type="application/javascript" src="https://github.githubassets.com/assets/github-bootstrap-e45d460a.js"></script>
    
    
    
  <div class="js-stale-session-flash stale-session-flash flash flash-warn flash-banner" hidden
    >
    <svg class="octicon octicon-alert" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8.893 1.5c-.183-.31-.52-.5-.887-.5s-.703.19-.886.5L.138 13.499a.98.98 0 0 0 0 1.001c.193.31.53.501.886.501h13.964c.367 0 .704-.19.877-.5a1.03 1.03 0 0 0 .01-1.002L8.893 1.5zm.133 11.497H6.987v-2.003h2.039v2.003zm0-3.004H6.987V5.987h2.039v4.006z"/></svg>
    <span class="signed-in-tab-flash">You signed in with another tab or window. <a href="">Reload</a> to refresh your session.</span>
    <span class="signed-out-tab-flash">You signed out in another tab or window. <a href="">Reload</a> to refresh your session.</span>
  </div>
  <template id="site-details-dialog">
  <details class="details-reset details-overlay details-overlay-dark lh-default text-gray-dark hx_rsm" open>
    <summary role="button" aria-label="Close dialog"></summary>
    <details-dialog class="Box Box--overlay d-flex flex-column anim-fade-in fast hx_rsm-dialog hx_rsm-modal">
      <button class="Box-btn-octicon m-0 btn-octicon position-absolute right-0 top-0" type="button" aria-label="Close dialog" data-close-dialog>
        <svg class="octicon octicon-x" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48L7.48 8z"/></svg>
      </button>
      <div class="octocat-spinner my-6 js-details-dialog-spinner"></div>
    </details-dialog>
  </details>
</template>

  <div class="Popover js-hovercard-content position-absolute" style="display: none; outline: none;" tabindex="0">
  <div class="Popover-message Popover-message--bottom-left Popover-message--large Box box-shadow-large" style="width:360px;">
  </div>
</div>

  <div aria-live="polite" class="js-global-screen-reader-notice sr-only"></div>

  </body>
</html>

