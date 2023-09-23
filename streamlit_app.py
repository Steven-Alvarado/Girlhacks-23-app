import streamlit as st
import streamlit.components.v1 as com

html = '''

<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Solar System Explorer </title>
    <meta property="og:title" content="Character NFT (Template 11)" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta charset="utf-8" />
    <meta property="twitter:card" content="summary_large_image" />

    <style data-tag="reset-style-sheet">
      html {  line-height: 1.15;}body {  margin: 0;}* {  box-sizing: border-box;  border-width: 0;  border-style: solid;}p,li,ul,pre,div,h1,h2,h3,h4,h5,h6,figure,blockquote,figcaption {  margin: 0;  padding: 0;}button {  background-color: transparent;}button,input,optgroup,select,textarea {  font-family: inherit;  font-size: 100%;  line-height: 1.15;  margin: 0;}button,select {  text-transform: none;}button,[type="button"],[type="reset"],[type="submit"] {  -webkit-appearance: button;}button::-moz-focus-inner,[type="button"]::-moz-focus-inner,[type="reset"]::-moz-focus-inner,[type="submit"]::-moz-focus-inner {  border-style: none;  padding: 0;}button:-moz-focus,[type="button"]:-moz-focus,[type="reset"]:-moz-focus,[type="submit"]:-moz-focus {  outline: 1px dotted ButtonText;}a {  color: inherit;  text-decoration: inherit;}input {  padding: 2px 4px;}img {  display: block;}html { scroll-behavior: smooth  }
    </style>
    <style data-tag="default-style-sheet">
      html {
        font-family: Inter;
        font-size: 16px;
      }

      body {
        font-weight: 400;
        font-style:normal;
        text-decoration: none;
        text-transform: none;
        letter-spacing: normal;
        line-height: 1.15;
        color: var(--dl-color-gray-black);
        background-color: var(--dl-color-gray-white);

      }
    </style>
    <link
      rel="stylesheet"
      href="https://fonts.googleapis.com/css2?family=Inter:wght@100;200;300;400;500;600;700;800;900&amp;display=swap"
      data-tag="font"
    />
    <!--This is the head section-->
    <!-- <style> ... </style> -->
  </head>
  <body>
    <link rel="stylesheet" href="./style.css" />
    <div>
      <link href="./index.css" rel="stylesheet" />

      <div class="home-container">
        <header data-thq="thq-navbar" class="home-navbar">
          <span class="home-logo">Solar System</span>
          <div
            data-thq="thq-navbar-nav"
            data-role="Nav"
            class="home-desktop-menu"
          >
            <nav
              data-thq="thq-navbar-nav-links"
              data-role="Nav"
              class="home-nav"
            >
              <button class="home-button button-clean button">Mercury</button>
              <button class="home-button1 button-clean button">Venus</button>
              <button class="home-button2 button-clean button">Earth</button>
              <button class="home-button3 button-clean button">Mars</button>
              <button class="home-button4 button-clean button">Jupiter</button>
              <button class="home-button4 button-clean button">Saturn</button>
              <button class="home-button4 button-clean button">Uranus</button>
              <button class="home-button4 button-clean button">Neptune</button>


            </nav>
          </div>
          <div data-thq="thq-navbar-btn-group" class="home-btn-group">
            <div class="home-socials">
              <button class="social button">
                <img
                  alt="image"
                  src="public/Icons/twitter.svg"
                  class="home-image"
                />
              </button>
              <button class="social button">
                <img
                  alt="image"
                  src="public/Icons/discord.svg"
                  class="home-image01"
                />
              </button>
            </div>
            <button class="button">View the Solar System</button>
          </div>
          <div data-thq="thq-burger-menu" class="home-burger-menu">
            <button class="button home-button5">
              <svg viewBox="0 0 1024 1024" class="home-icon">
                <path
                  d="M128 554.667h768c23.552 0 42.667-19.115 42.667-42.667s-19.115-42.667-42.667-42.667h-768c-23.552 0-42.667 19.115-42.667 42.667s19.115 42.667 42.667 42.667zM128 298.667h768c23.552 0 42.667-19.115 42.667-42.667s-19.115-42.667-42.667-42.667h-768c-23.552 0-42.667 19.115-42.667 42.667s19.115 42.667 42.667 42.667zM128 810.667h768c23.552 0 42.667-19.115 42.667-42.667s-19.115-42.667-42.667-42.667h-768c-23.552 0-42.667 19.115-42.667 42.667s19.115 42.667 42.667 42.667z"
                ></path>
              </svg>
            </button>
          </div>
          <div data-thq="thq-mobile-menu" class="home-mobile-menu">
            <div
              data-thq="thq-mobile-menu-nav"
              data-role="Nav"
              class="home-nav1"
            >
              <div class="home-container1">
                <span class="home-logo1">Explore</span>
                <div data-thq="thq-close-menu" class="home-menu-close">
                  <svg viewBox="0 0 1024 1024" class="home-icon02">
                    <path
                      d="M810 274l-238 238 238 238-60 60-238-238-238 238-60-60 238-238-238-238 60-60 238 238 238-238z"
                    ></path>
                  </svg>
                </div>
              </div>
              <nav
                data-thq="thq-mobile-menu-nav-links"
                data-role="Nav"
                class="home-nav2"
              >
                <span class="home-text">Mercury</span>
                <span class="home-text01">Venus</span>
                <span class="home-text02">Earth</span>
                <span class="home-text03">Mars</span>
                <span class="home-text04">Jupiter</span>
                <span class="home-text04">Saturn</span>
                <span class="home-text04">Uranus</span>
                <span class="home-text04">Neptune</span>

              </nav>
              <div class="home-container2">
                <button class="home-login button">Login</button>
                <button class="button">Register</button>
              </div>
            </div>
            <div class="home-icon-group">
              <svg viewBox="0 0 950.8571428571428 1024" class="home-icon04">
                <path
                  d="M925.714 233.143c-25.143 36.571-56.571 69.143-92.571 95.429 0.571 8 0.571 16 0.571 24 0 244-185.714 525.143-525.143 525.143-104.571 0-201.714-30.286-283.429-82.857 14.857 1.714 29.143 2.286 44.571 2.286 86.286 0 165.714-29.143 229.143-78.857-81.143-1.714-149.143-54.857-172.571-128 11.429 1.714 22.857 2.857 34.857 2.857 16.571 0 33.143-2.286 48.571-6.286-84.571-17.143-148-91.429-148-181.143v-2.286c24.571 13.714 53.143 22.286 83.429 23.429-49.714-33.143-82.286-89.714-82.286-153.714 0-34.286 9.143-65.714 25.143-93.143 90.857 112 227.429 185.143 380.571 193.143-2.857-13.714-4.571-28-4.571-42.286 0-101.714 82.286-184.571 184.571-184.571 53.143 0 101.143 22.286 134.857 58.286 41.714-8 81.714-23.429 117.143-44.571-13.714 42.857-42.857 78.857-81.143 101.714 37.143-4 73.143-14.286 106.286-28.571z"
                ></path></svg
              ><svg viewBox="0 0 877.7142857142857 1024" class="home-icon06">
                <path
                  d="M585.143 512c0-80.571-65.714-146.286-146.286-146.286s-146.286 65.714-146.286 146.286 65.714 146.286 146.286 146.286 146.286-65.714 146.286-146.286zM664 512c0 124.571-100.571 225.143-225.143 225.143s-225.143-100.571-225.143-225.143 100.571-225.143 225.143-225.143 225.143 100.571 225.143 225.143zM725.714 277.714c0 29.143-23.429 52.571-52.571 52.571s-52.571-23.429-52.571-52.571 23.429-52.571 52.571-52.571 52.571 23.429 52.571 52.571zM438.857 152c-64 0-201.143-5.143-258.857 17.714-20 8-34.857 17.714-50.286 33.143s-25.143 30.286-33.143 50.286c-22.857 57.714-17.714 194.857-17.714 258.857s-5.143 201.143 17.714 258.857c8 20 17.714 34.857 33.143 50.286s30.286 25.143 50.286 33.143c57.714 22.857 194.857 17.714 258.857 17.714s201.143 5.143 258.857-17.714c20-8 34.857-17.714 50.286-33.143s25.143-30.286 33.143-50.286c22.857-57.714 17.714-194.857 17.714-258.857s5.143-201.143-17.714-258.857c-8-20-17.714-34.857-33.143-50.286s-30.286-25.143-50.286-33.143c-57.714-22.857-194.857-17.714-258.857-17.714zM877.714 512c0 60.571 0.571 120.571-2.857 181.143-3.429 70.286-19.429 132.571-70.857 184s-113.714 67.429-184 70.857c-60.571 3.429-120.571 2.857-181.143 2.857s-120.571 0.571-181.143-2.857c-70.286-3.429-132.571-19.429-184-70.857s-67.429-113.714-70.857-184c-3.429-60.571-2.857-120.571-2.857-181.143s-0.571-120.571 2.857-181.143c3.429-70.286 19.429-132.571 70.857-184s113.714-67.429 184-70.857c60.571-3.429 120.571-2.857 181.143-2.857s120.571-0.571 181.143 2.857c70.286 3.429 132.571 19.429 184 70.857s67.429 113.714 70.857 184c3.429 60.571 2.857 120.571 2.857 181.143z"
                ></path></svg
              ><svg viewBox="0 0 602.2582857142856 1024" class="home-icon08">
                <path
                  d="M548 6.857v150.857h-89.714c-70.286 0-83.429 33.714-83.429 82.286v108h167.429l-22.286 169.143h-145.143v433.714h-174.857v-433.714h-145.714v-169.143h145.714v-124.571c0-144.571 88.571-223.429 217.714-223.429 61.714 0 114.857 4.571 130.286 6.857z"
                ></path>
              </svg>
            </div>
          </div>
        </header>
        <section class="home-hero">
          <div class="home-heading">
            <h1 class="home-header">Curious about the Solar System?</h1>
            <p class="home-caption">
              Find out live information and facts, or ask our expert SpaceBot AI.
            </p>
          </div>
          <div class="home-buttons">
            <button class="button">View on Opensea</button>
            <button class="home-learn button-clean button">Learn more</button>
          </div>
        </section>
        <section class="home-description">
          <img
            alt="image"
            src="public/hero-divider-1500w.png"
            class="home-divider-image"
          />
          <div class="home-container3">
            <div class="home-description01">
              <div class="home-content">
                <p class="home-paragraph">
                  We are a team of digital aute irure dolor in reprehenderit in
                  voluptate velit esse cillum dolore eu fugiat.
                </p>
                <p class="home-paragraph1">
                  Excepteur sint occaecat cupidatat non proident, sunt in culpa
                  qui officia deserunt mollit anim id est laborum. Nemo enim
                  ipsam voluptatem quia voluptas sit aspernatur aut odit aut
                  fugit.
                </p>
              </div>
              <div class="home-links">
                <a
                  href="https://twitter.com"
                  target="_blank"
                  rel="noreferrer noopener"
                  class="home-link button-link button"
                >
                  <span>Follow us on Twitter</span>
                  <img
                    alt="image"
                    src="public/Icons/arrow.svg"
                    class="home-arrow"
                  />
                </a>
                <a
                  href="https://discord.com"
                  target="_blank"
                  rel="noreferrer noopener"
                  class="home-link01 button-link button"
                >
                  <span>Join us on Discord</span>
                  <img
                    alt="image"
                    src="public/Icons/arrow.svg"
                    class="home-arrow1"
                  />
                </a>
              </div>
            </div>
          </div>
        </section>
        <section class="home-cards">
          <div class="home-row">
            <div class="home-card">
              <div class="home-avatar">
                <img
                  alt="image"
                  src="public/Avatars/avatar.svg"
                  class="home-avatar1"
                />
              </div>
              <div class="home-main">
                <div class="home-content01">
                  <h2 class="home-header01">10,000+ unique characters</h2>
                  <p class="home-description02">
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed
                    do eiusmod tempor incididunt ut labore et dolore magna
                    aliquat enim ad minim veniam, quis nostrud exercitation
                    ullamco laboris nisi
                  </p>
                </div>
                <button class="home-learn1 button">
                  <span class="home-text07">Learn more</span>
                  <img
                    alt="image"
                    src="public/Icons/arrow.svg"
                    class="home-image02"
                  />
                </button>
              </div>
            </div>
            <div class="home-card01">
              <div class="home-avatar2">
                <img
                  alt="image"
                  src="public/Avatars/default-avatar.svg"
                  class="home-avatar3"
                />
              </div>
              <div class="home-main1">
                <div class="home-content02">
                  <h2 class="home-header02">
                    Create yourself for the metaverse
                  </h2>
                  <p class="home-description03">
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed
                    do eiusmod tempor incididunt ut labore et dolore magna
                    aliquat enim ad minim veniam, quis nostrud exercitation
                    ullamco laboris nisi
                  </p>
                </div>
                <button class="home-learn2 button">
                  <span class="home-text08">Learn more</span>
                  <img
                    alt="image"
                    src="public/Icons/arrow-2.svg"
                    class="home-image03"
                  />
                </button>
              </div>
            </div>
          </div>
          <div class="home-card02">
            <div class="home-avatar4">
              <img
                alt="image"
                src="public/Avatars/light-avatar.svg"
                class="home-avatar5"
              />
            </div>
            <div class="home-row1">
              <div class="home-main2">
                <div class="home-content03">
                  <h2 class="home-header03">
                    Create yourself for the metaverse
                  </h2>
                  <p class="home-description04">
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed
                    do eiusmod tempor incididunt ut labore et dolore magna
                    aliquat enim ad minim veniam, quis nostrud exercitation
                    ullamco laboris nisi
                  </p>
                </div>
                <button class="home-learn3 button">
                  <span class="home-text09">Learn more</span>
                  <img
                    alt="image"
                    src="public/Icons/arrow-2.svg"
                    class="home-image04"
                  />
                </button>
              </div>
              <img
                alt="image"
                src="public/group%202262.svg"
                class="home-image05"
              />
            </div>
          </div>
        </section>
        <section class="home-collection">
          <div class="home-content04">
            <span class="home-caption01">collection</span>
            <div class="home-heading01">
              <h2 class="home-header04">All time best collections</h2>
              <p class="home-header05">
                Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
                eiusmod tempor incididunt ut labore et dolore.
              </p>
            </div>
          </div>
          <div class="home-main3">
            <div class="home-card03">
              <div class="home-image06">
                <img
                  alt="image"
                  src="public/Characters/character-1.svg"
                  class="home-image07"
                />
              </div>
              <div class="home-content05">
                <span class="home-caption02">Character #1</span>
                <h3 class="home-title">0.05 ETH</h3>
              </div>
            </div>
            <div class="home-card04">
              <div class="home-image08">
                <img
                  alt="image"
                  src="public/Characters/character-2.svg"
                  class="home-image09"
                />
              </div>
              <div class="home-content06">
                <span class="home-caption03">Character #2</span>
                <h3 class="home-title1">0.05 ETH</h3>
              </div>
            </div>
            <div class="home-card05">
              <div class="home-image10">
                <img
                  alt="image"
                  src="public/Characters/character-3.svg"
                  class="home-image11"
                />
              </div>
              <div class="home-content07">
                <span class="home-caption04">Character #3</span>
                <h3 class="home-title2">0.05 ETH</h3>
              </div>
            </div>
            <div class="home-card06">
              <div class="home-image12">
                <img
                  alt="image"
                  src="public/Characters/character-4.svg"
                  class="home-image13"
                />
              </div>
              <div class="home-content08">
                <span class="home-caption05">
                  <span>Character #4</span>
                  <br />
                </span>
                <h3 class="home-title3">0.05 ETH</h3>
              </div>
            </div>
            <div class="home-card07">
              <div class="home-image14">
                <img
                  alt="image"
                  src="public/Characters/character-5.svg"
                  class="home-image15"
                />
              </div>
              <div class="home-content09">
                <span class="home-caption06">Character #5</span>
                <h3 class="home-title4">0.05 ETH</h3>
              </div>
            </div>
            <div class="home-card08">
              <div class="home-image16">
                <img
                  alt="image"
                  src="public/Characters/character-6.svg"
                  class="home-image17"
                />
              </div>
              <div class="home-content10">
                <span class="home-caption07">Character #6</span>
                <h3 class="home-title5">0.05 ETH</h3>
              </div>
            </div>
            <div class="home-card09">
              <div class="home-image18">
                <img
                  alt="image"
                  src="public/Characters/character-7.svg"
                  class="home-image19"
                />
              </div>
              <div class="home-content11">
                <span class="home-caption08">Character #7</span>
                <h3 class="home-title6">0.05 ETH</h3>
              </div>
            </div>
            <div class="home-card10">
              <div class="home-image20">
                <img
                  alt="image"
                  src="public/Characters/character-8.svg"
                  class="home-image21"
                />
              </div>
              <div class="home-content12">
                <span class="home-caption09">Character #8</span>
                <h3 class="home-title7">0.05 ETH</h3>
              </div>
            </div>
          </div>
          <button class="home-view2 button-link button">View all</button>
        </section>
        <section class="home-project">
          <div class="home-understand">
            <div class="home-content13">
              <span class="home-caption10">Project</span>
              <div class="home-heading02">
                <h2 class="home-header06">Understand the project</h2>
                <p class="home-header07">
                  Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed
                  do eiusmod tempor incididunt ut labore et dolore magna aliqua.
                  Ut enim ad minim veniam, quis nostrud exercitation ullamco
                  laboris nisi ut aliquip ex ea commodo consequat.
                </p>
              </div>
              <button class="home-view3 button-link button">
                <span>Learn More</span>
                <img
                  alt="image"
                  src="public/Icons/arrow.svg"
                  class="home-image22"
                />
              </button>
            </div>
            <img
              alt="image"
              src="public/group%202415.svg"
              class="home-image23"
            />
          </div>
          <div class="home-mining">
            <img
              alt="image"
              src="public/group%202422.svg"
              class="home-image24"
            />
            <div class="home-content14">
              <span class="home-caption11">Project</span>
              <div class="home-heading03">
                <h2 class="home-header08">How the minting works</h2>
                <p class="home-header09">
                  <span>
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed
                    do eiusmod tempor incididunt ut labore et dolore magna
                    aliqua. Ut enim ad minim veniam, quis nostrud exercitation
                    ullamco laboris nisi ut aliquip ex ea commodo consequat.
                  </span>
                  <br />
                  <br />
                  <span>
                    Duis aute irure dolor in reprehenderit in voluptate velit
                    esse cillum dolore eu fugiat nulla pariatur.
                  </span>
                  <br />
                </p>
              </div>
              <button class="home-view4 button-link button">
                <span>Learn More</span>
                <img
                  alt="image"
                  src="public/Icons/arrow.svg"
                  class="home-image25"
                />
              </button>
            </div>
          </div>
        </section>
        <section class="home-roadmap">
          <div class="home-heading04">
            <h2 class="home-header10">Roadmap</h2>
            <p class="home-header11">
              Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
              eiusmod tempor incididunt ut labore
            </p>
          </div>
          <div class="home-list">
            <div class="home-step">
              <span class="home-caption12">01</span>
              <div class="home-heading05">
                <h2 class="home-header12">Project Launch</h2>
                <p class="home-header13">
                  Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed
                  do eiusmod tempor incididunt ut labore et dolore magna aliqua.
                  Ut enim ad minim veniam, quis nostrud exercitation ullamco
                  laboris nisi ut aliquip ex ea commodo consequat.
                </p>
              </div>
              <button class="home-button6 button">View on Opensea</button>
            </div>
            <div class="home-step1">
              <span class="home-caption13">02</span>
              <div class="home-heading06">
                <h2 class="home-header14">Metadata and Character</h2>
                <p class="home-header15">
                  <span>
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed
                    do eiusmod tempor incididunt ut labore et dolore magna
                    aliqua.
                  </span>
                  <br />
                  <br />
                  <span>
                    Ut enim ad minim veniam, quis nostrud exercitation ullamco
                    laboris nisi ut aliquip ex ea commodo consequat.
                  </span>
                  <br />
                </p>
              </div>
            </div>
            <div class="home-step2">
              <span class="home-caption14">03</span>
              <div class="home-heading07">
                <h2 class="home-header16">Get Physical</h2>
                <p class="home-header17">
                  <span>
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed
                    do eiusmod tempor incididunt ut labore et dolore magna
                    aliqua.
                  </span>
                  <br />
                  <br />
                  <span>
                    Ut enim ad minim veniam, quis nostrud exercitation ullamco
                    laboris nisi ut aliquip ex ea commodo consequat.
                  </span>
                  <br />
                </p>
              </div>
            </div>
            <div class="home-step3">
              <span class="home-caption15">04</span>
              <div class="home-heading08">
                <h2 class="home-header18">Private club community</h2>
                <p class="home-header19">
                  Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed
                  do eiusmod tempor incididunt ut labore et dolore magna aliqua.
                </p>
                <div class="home-benefits">
                  <div class="home-item">
                    <img
                      alt="image"
                      src="public/Icons/people.svg"
                      class="home-image26"
                    />
                    <p class="home-header20">Consectetur adipiscing elit</p>
                  </div>
                  <div class="home-item1">
                    <img
                      alt="image"
                      src="public/Icons/paper.svg"
                      class="home-image27"
                    />
                    <p class="home-header21">Consectetur adipiscing elit</p>
                  </div>
                  <div class="home-item2">
                    <img
                      alt="image"
                      src="public/Icons/checklist.svg"
                      class="home-image28"
                    />
                    <p class="home-header22">Consectetur adipiscing elit</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </section>
        <section class="home-join-us">
          <div class="home-content15">
            <div class="home-main4">
              <div class="home-heading09">
                <h2 class="home-header23">Create your character now</h2>
                <p class="home-caption16">
                  A character custom collection is joining the NFT space on
                  Opensea.
                </p>
              </div>
              <button class="home-view5 button">View on Opensea</button>
            </div>
            <img
              alt="image"
              src="public/group%202273.svg"
              class="home-image29"
            />
          </div>
        </section>
        <section class="home-faq">
          <h2 class="home-header24">We have all the answers</h2>
          <div class="home-accordion">
            <div data-role="accordion-container" class="home-element accordion">
              <div class="home-content16">
                <span class="home-header25">
                  Lorem ipsum dolor sit ametetur elit?
                </span>
                <span data-role="accordion-content" class="home-description05">
                  Sed ut perspiciatis unde omnis iste natus error sit voluptatem
                  accusantium doloremque laudantium, totam rem aperiam, eaque
                  ipsa quae ab illo inventore veritatis et quasi architecto
                  beatae vitae dicta sunt explicabo.
                </span>
              </div>
              <div class="home-icon-container">
                <svg
                  viewBox="0 0 1024 1024"
                  data-role="accordion-icon-closed"
                  class="home-icon10"
                >
                  <path
                    d="M213.333 554.667h256v256c0 23.552 19.115 42.667 42.667 42.667s42.667-19.115 42.667-42.667v-256h256c23.552 0 42.667-19.115 42.667-42.667s-19.115-42.667-42.667-42.667h-256v-256c0-23.552-19.115-42.667-42.667-42.667s-42.667 19.115-42.667 42.667v256h-256c-23.552 0-42.667 19.115-42.667 42.667s19.115 42.667 42.667 42.667z"
                  ></path></svg
                ><svg
                  viewBox="0 0 1024 1024"
                  data-role="accordion-icon-open"
                  class="home-icon12"
                >
                  <path
                    d="M213.333 554.667h597.333c23.552 0 42.667-19.115 42.667-42.667s-19.115-42.667-42.667-42.667h-597.333c-23.552 0-42.667 19.115-42.667 42.667s19.115 42.667 42.667 42.667z"
                  ></path>
                </svg>
              </div>
            </div>
            <div
              data-role="accordion-container"
              class="home-element1 accordion"
            >
              <div class="home-content17">
                <span class="home-header26">
                  Excepteur sint occaecat cupidatat non sunt in culpa qui
                  officia deserunt mollit anim id est laborum?
                </span>
                <span data-role="accordion-content" class="home-description06">
                  Sed ut perspiciatis unde omnis iste natus error sit voluptatem
                  accusantium doloremque laudantium, totam rem aperiam, eaque
                  ipsa quae ab illo inventore veritatis et quasi architecto
                  beatae vitae dicta sunt explicabo.
                </span>
              </div>
              <div class="home-icon-container1">
                <svg
                  viewBox="0 0 1024 1024"
                  data-role="accordion-icon-closed"
                  class="home-icon14"
                >
                  <path
                    d="M213.333 554.667h256v256c0 23.552 19.115 42.667 42.667 42.667s42.667-19.115 42.667-42.667v-256h256c23.552 0 42.667-19.115 42.667-42.667s-19.115-42.667-42.667-42.667h-256v-256c0-23.552-19.115-42.667-42.667-42.667s-42.667 19.115-42.667 42.667v256h-256c-23.552 0-42.667 19.115-42.667 42.667s19.115 42.667 42.667 42.667z"
                  ></path></svg
                ><svg
                  viewBox="0 0 1024 1024"
                  data-role="accordion-icon-open"
                  class="home-icon16"
                >
                  <path
                    d="M213.333 554.667h597.333c23.552 0 42.667-19.115 42.667-42.667s-19.115-42.667-42.667-42.667h-597.333c-23.552 0-42.667 19.115-42.667 42.667s19.115 42.667 42.667 42.667z"
                  ></path>
                </svg>
              </div>
            </div>
            <div
              data-role="accordion-container"
              class="home-element2 accordion"
            >
              <div class="home-content18">
                <span class="home-header27">
                  Tempor incididunt ut labore et dolore magna aliquat enim ad
                  minim?
                </span>
                <span data-role="accordion-content" class="home-description07">
                  Sed ut perspiciatis unde omnis iste natus error sit voluptatem
                  accusantium doloremque laudantium, totam rem aperiam, eaque
                  ipsa quae ab illo inventore veritatis et quasi architecto
                  beatae vitae dicta sunt explicabo.
                </span>
              </div>
              <div class="home-icon-container2">
                <svg
                  viewBox="0 0 1024 1024"
                  data-role="accordion-icon-closed"
                  class="home-icon18"
                >
                  <path
                    d="M213.333 554.667h256v256c0 23.552 19.115 42.667 42.667 42.667s42.667-19.115 42.667-42.667v-256h256c23.552 0 42.667-19.115 42.667-42.667s-19.115-42.667-42.667-42.667h-256v-256c0-23.552-19.115-42.667-42.667-42.667s-42.667 19.115-42.667 42.667v256h-256c-23.552 0-42.667 19.115-42.667 42.667s19.115 42.667 42.667 42.667z"
                  ></path></svg
                ><svg
                  viewBox="0 0 1024 1024"
                  data-role="accordion-icon-open"
                  class="home-icon20"
                >
                  <path
                    d="M213.333 554.667h597.333c23.552 0 42.667-19.115 42.667-42.667s-19.115-42.667-42.667-42.667h-597.333c-23.552 0-42.667 19.115-42.667 42.667s19.115 42.667 42.667 42.667z"
                  ></path>
                </svg>
              </div>
            </div>
            <div
              data-role="accordion-container"
              class="home-element3 accordion"
            >
              <div class="home-content19">
                <span class="home-header28">
                  Lorem ipsum dolor sit ametetur elit?
                </span>
                <span data-role="accordion-content" class="home-description08">
                  Sed ut perspiciatis unde omnis iste natus error sit voluptatem
                  accusantium doloremque laudantium, totam rem aperiam, eaque
                  ipsa quae ab illo inventore veritatis et quasi architecto
                  beatae vitae dicta sunt explicabo.
                </span>
              </div>
              <div class="home-icon-container3">
                <svg
                  viewBox="0 0 1024 1024"
                  data-role="accordion-icon-closed"
                  class="home-icon22"
                >
                  <path
                    d="M213.333 554.667h256v256c0 23.552 19.115 42.667 42.667 42.667s42.667-19.115 42.667-42.667v-256h256c23.552 0 42.667-19.115 42.667-42.667s-19.115-42.667-42.667-42.667h-256v-256c0-23.552-19.115-42.667-42.667-42.667s-42.667 19.115-42.667 42.667v256h-256c-23.552 0-42.667 19.115-42.667 42.667s19.115 42.667 42.667 42.667z"
                  ></path></svg
                ><svg
                  viewBox="0 0 1024 1024"
                  data-role="accordion-icon-open"
                  class="home-icon24"
                >
                  <path
                    d="M213.333 554.667h597.333c23.552 0 42.667-19.115 42.667-42.667s-19.115-42.667-42.667-42.667h-597.333c-23.552 0-42.667 19.115-42.667 42.667s19.115 42.667 42.667 42.667z"
                  ></path>
                </svg>
              </div>
            </div>
            <div
              data-role="accordion-container"
              class="home-element4 accordion"
            >
              <div class="home-content20">
                <span class="home-header29">
                  Incididunt ut labore et dolore?
                </span>
                <span data-role="accordion-content" class="home-description09">
                  Sed ut perspiciatis unde omnis iste natus error sit voluptatem
                  accusantium doloremque laudantium, totam rem aperiam, eaque
                  ipsa quae ab illo inventore veritatis et quasi architecto
                  beatae vitae dicta sunt explicabo.
                </span>
              </div>
              <div class="home-icon-container4">
                <svg
                  viewBox="0 0 1024 1024"
                  data-role="accordion-icon-closed"
                  class="home-icon26"
                >
                  <path
                    d="M213.333 554.667h256v256c0 23.552 19.115 42.667 42.667 42.667s42.667-19.115 42.667-42.667v-256h256c23.552 0 42.667-19.115 42.667-42.667s-19.115-42.667-42.667-42.667h-256v-256c0-23.552-19.115-42.667-42.667-42.667s-42.667 19.115-42.667 42.667v256h-256c-23.552 0-42.667 19.115-42.667 42.667s19.115 42.667 42.667 42.667z"
                  ></path></svg
                ><svg
                  viewBox="0 0 1024 1024"
                  data-role="accordion-icon-open"
                  class="home-icon28"
                >
                  <path
                    d="M213.333 554.667h597.333c23.552 0 42.667-19.115 42.667-42.667s-19.115-42.667-42.667-42.667h-597.333c-23.552 0-42.667 19.115-42.667 42.667s19.115 42.667 42.667 42.667z"
                  ></path>
                </svg>
              </div>
            </div>
          </div>
        </section>
        <section class="home-get-yours">
          <div class="home-row2">
            <div class="home-column">
              <div class="home-card11">
                <img
                  alt="image"
                  src="public/Characters/character-9.svg"
                  class="home-image30"
                />
              </div>
            </div>
            <div class="home-column1">
              <div class="home-card12">
                <img
                  alt="image"
                  src="public/Characters/character-10.svg"
                  class="home-image31"
                />
              </div>
            </div>
          </div>
          <div class="home-column2">
            <div class="home-card13">
              <div class="home-content21">
                <h2 class="home-header30">Get yours now</h2>
                <p class="home-description10">
                  Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed
                  do eiusmod tempor incididunt ut labore et dolore magna aliquat
                  enim ad minim veniam.
                </p>
              </div>
              <button class="home-button7 button">View on Opensea</button>
            </div>
          </div>
        </section>
        <footer class="home-footer">
          <div class="home-main5">
            <div class="home-branding">
              <div class="home-heading10">
                <h2 class="home-logo2">Character</h2>
                <p class="home-caption17">
                  Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed
                  do eiusmod tempor incididunt ut labore et dolore.
                </p>
              </div>
              <div class="home-socials1">
                <a
                  href="https://twitter.com"
                  target="_blank"
                  rel="noreferrer noopener"
                  class="home-twitter1 social button"
                >
                  <img
                    alt="image"
                    src="public/Icons/twitter.svg"
                    class="home-image32"
                  />
                </a>
                <a
                  href="https://discord.com"
                  target="_blank"
                  rel="noreferrer noopener"
                  class="home-discord1 social button"
                >
                  <img
                    alt="image"
                    src="public/Icons/discord.svg"
                    class="home-image33"
                  />
                </a>
              </div>
            </div>
            <div class="home-links1">
              <div class="home-list1">
                <h3 class="home-heading11">Site</h3>
                <div class="home-items">
                  <button class="home-link02 button-clean button">About</button>
                  <button class="home-link03 button-clean button">
                    Collection
                  </button>
                  <button class="home-link04 button-clean button">
                    Roadmap
                  </button>
                  <button class="home-link05 button-clean button">
                    Features
                  </button>
                </div>
              </div>
              <div class="home-list2">
                <h3 class="home-heading12">Company</h3>
                <div class="home-items1">
                  <button class="home-link06 button-clean button">Team</button>
                  <button class="home-link07 button-clean button">Press</button>
                  <button class="home-link08 button-clean button">Terms</button>
                  <button class="home-link09 button-clean button">
                    Limitations
                  </button>
                  <button class="home-link10 button-clean button">
                    Licenses
                  </button>
                </div>
              </div>
            </div>
            <div class="home-socials2">
              <a
                href="https://twitter.com"
                target="_blank"
                rel="noreferrer noopener"
                class="home-twitter2 social button"
              >
                <img
                  alt="image"
                  src="public/Icons/twitter.svg"
                  class="home-image34"
                />
              </a>
              <a
                href="https://discord.com"
                target="_blank"
                rel="noreferrer noopener"
                class="home-discord2 social button"
              >
                <img
                  alt="image"
                  src="public/Icons/discord.svg"
                  class="home-image35"
                />
              </a>
            </div>
          </div>
          <span class="home-copyright">
            © 2022 Character. All Rights Reserved.
          </span>
        </footer>
        <div class="home-accordion1">
          <script>
            /*
             Accordion - Code Embed
             */
             const accordionContainers = document.querySelectorAll('[data-role='accordion-container']'); // All accordion containers
             const accordionContents = document.querySelectorAll('[data-role='accordion-content']'); // All accordion content
             const accordionIconsClosed = document.querySelectorAll('[data-role='accordion-icon-closed']'); // All accordion closed icons
             const accordionIconsOpen = document.querySelectorAll('[data-role='accordion-icon-open']'); // All accordion open icons

             accordionContents.forEach((accordionContent) => {
                 accordionContent.style.display = 'none'; //Hides all accordion contents
             });

             accordionIconsClosed.forEach((icon) => {
               icon.style.display = 'flex'
             })

             accordionIconsOpen.forEach((icon) => {
               icon.style.display = 'none'
             })

             accordionContainers.forEach((accordionContainer, index) => {
                 accordionContainer.addEventListener('click', () => {
                     if (accordionContents[index].style.display === 'flex') {
                         // If the accordion is already open, close it
                         accordionContents[index].style.display = 'none';
                         accordionIconsClosed[index].style.display = 'flex';
                         accordionIconsOpen[index].style.display = 'none'
                     } else {
                         // If the accordion is closed, open it
                         accordionContents.forEach((accordionContent) => {
                             accordionContent.style.display = 'none'; //Hides all accordion contents
                         });

                         accordionIconsClosed.forEach((accordionIcon) => {
                             accordionIcon.style.display = 'flex'; // Resets all icon transforms to 0deg (default)
                         });

                         accordionIconsOpen.forEach((accordionIcon) => {
                           accordionIcon.style.display = 'none';
                         })

                         accordionContents[index].style.display = 'flex'; // Shows accordion content
                         accordionIconsClosed[index].style.display = 'none'; // Rotates accordion icon 180deg
                         accordionIconsOpen[index].style.display = 'flex';
                     }
                 });
             });
          </script>
        </div>
      </div>
    </div>
    <script
      data-section-id="navbar"
      src="https://unpkg.com/@teleporthq/teleport-custom-scripts"
    ></script>
  </body>
</html>

'''
com.html(html, width=800, height=600)
##st.markdown(html_code, unsafe_allow_html=True)

