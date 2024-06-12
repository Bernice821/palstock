<template>
  <div class="dashboard">
    <!-- Dashboard Navigation -->
    <div class="dashboard-nav">
      <header>
        <a href="#!" class="menu-toggle" @click="toggleMenu">
          <i class="fas fa-bars"></i>
        </a>
        <a href="#" class="brand-logo">
          <i class="fas fa-anchor"></i>
          <div class="row">
            <div class="col">
              <img style="width:60px;height:50px;padding-top: 4px;" src="../../logo.png">
            </div>
            <div class="col">
              <h3 class="font-bold text-xl pt-2 pr-3" style="color:#fff">PalStock</h3>
            </div>
          </div>
        </a>
      </header>
      <nav class="dashboard-nav-list">
        <router-link to="/home"><a href="#" class="dashboard-nav-item"><i class="fas fa-file-upload"></i>首頁 </a></router-link>
        <router-link to="/research"><a href="#" class="dashboard-nav-item"><i class="fas fa-file-upload"></i>策略研究</a></router-link>
        <router-link to="/about"><a href="#" class="dashboard-nav-item"><i class="fas fa-file-upload"></i>個股資訊 </a></router-link>

        <router-link to="/market"><a href="#" class="dashboard-nav-item"><i class="fas fa-cogs"></i>大盤市況 </a></router-link>
        <router-link to="/news"><a href="#" class="dashboard-nav-item"><i class="fas fa-user"></i>股票新聞</a></router-link>
        <div class="nav-item-divider"></div>
      </nav>
    </div>

    <!-- Dashboard Content -->
    <div class="dashboard-app">
      <header class="dashboard-toolbar">
        <a href="#!" class="menu-toggle" @click="toggleMenu">
          <svg viewBox="0 0 20 20" fill="#fff" strokeWidth="2" class="w-5 h-5">
            <path fill-rule="evenodd"
              d="M3 5a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM3 10a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM3 15a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1z"
              clip-rule="evenodd"></path>
          </svg>
        </a>

      </header>
      <div class="dashboard-content">
        <div class="container">
          <!-- Router View for Dynamic Content -->
          <router-view></router-view>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      dropdownOpen: false,
      mobileScreen: window.matchMedia("(max-width: 990px)")
    };
  },
  methods: {
    toggleDropdown() {
      // Toggle dropdown visibility
      this.dropdownOpen = !this.dropdownOpen;
    },
    toggleMenu() {
      // Toggle dashboard navigation based on screen size
      if (this.mobileScreen.matches) {
        // Mobile screen: toggle mobile navigation visibility
        const dashboardNav = document.querySelector(".dashboard-nav");
        if (dashboardNav) {
          dashboardNav.classList.toggle("mobile-show");
        }
      } else {
        // Desktop screen: toggle compact dashboard view
        const dashboard = document.querySelector(".dashboard");
        if (dashboard) {
          dashboard.classList.toggle("dashboard-compact");
        }
      }
    }
  },
  mounted() {
    // Reset dashboard view on mobile screen resize
    this.mobileScreen.addListener(() => {
      if (this.mobileScreen.matches) {
        const dashboard = document.querySelector(".dashboard");
        if (dashboard) {
          dashboard.classList.remove("dashboard-compact");
        }
      }
    });
  }
};
</script>


<style scoped>
*,
*::before,
*::after {
  -webkit-box-sizing: border-box;
  box-sizing: border-box;
}

html {
  line-height: 1.15;
  -webkit-text-size-adjust: 100%;
  -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
}

nav {
  display: block;
}

body {
  margin: 0;
  font-size: 1rem;
  font-weight: 400;
  line-height: 1.5;
  color: #fff;
  text-align: left;
  background-color: #fff;
}

a {
  text-decoration: none;
  background-color: transparent;
}

a:hover {
  color: #0458eb;
  text-decoration: underline;
}


.card {
  position: relative;
  display: -webkit-box;
  display: -webkit-flex;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-orient: vertical;
  -webkit-box-direction: normal;
  -webkit-flex-direction: column;
  -ms-flex-direction: column;
  flex-direction: column;
  min-width: 0;
  word-wrap: break-word;
  background-color: #fff;
  background-clip: border-box;
  border: 1px solid rgba(0, 0, 0, 0.125);
  border-radius: 0;
}

.card-body {
  -webkit-box-flex: 1;
  -webkit-flex: 1 1 auto;
  -ms-flex: 1 1 auto;
  flex: 1 1 auto;
  padding: 1.25rem;
}

.card-header {
  padding: 0.75rem 1.25rem;
  margin-bottom: 0;
  background-color: rgba(0, 0, 0, 0.03);
  border-bottom: 1px solid rgba(0, 0, 0, 0.125);
  text-align: center;
}

.dashboard {
  display: -webkit-box;
  display: -webkit-flex;
  display: -ms-flexbox;
  display: flex;
  min-height: 100vh;
}

.dashboard-app {
  display: -webkit-box;
  display: -webkit-flex;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-orient: vertical;
  -webkit-box-direction: normal;
  -webkit-flex-direction: column;
  -ms-flex-direction: column;
  flex-direction: column;
  -webkit-box-flex: 2;
  -webkit-flex-grow: 2;
  -ms-flex-positive: 2;
  flex-grow: 2;
  margin-top: 84px;
}

.dashboard-content {
  -webkit-box-flex: 2;
  -webkit-flex-grow: 2;
  -ms-flex-positive: 2;
  flex-grow: 2;
  padding: 25px;
}

.dashboard-nav {
  min-width: 238px;
  position: fixed;
  left: 0;
  top: 0;
  bottom: 0;
  overflow: auto;
  background-color: #373193;
}

.dashboard-compact .dashboard-nav {
  display: none;
}

.dashboard-nav header {
  min-height: 84px;
  padding: 8px 27px;
  display: -webkit-box;
  display: -webkit-flex;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-pack: center;
  -webkit-justify-content: center;
  -ms-flex-pack: center;
  justify-content: center;
  -webkit-box-align: center;
  -webkit-align-items: center;
  -ms-flex-align: center;
  align-items: center;
}

.dashboard-nav header .menu-toggle {
  display: none;
  margin-right: auto;
}

.dashboard-nav a {
  color: #515151;
}

.dashboard-nav a:hover {
  text-decoration: none;
}

.dashboard-nav {
  background-color: #6d91b3;
}

.dashboard-nav a {
  color: #fff;
}

.brand-logo {
  font-weight: bold;
  font-size: 20px;
  display: -webkit-box;
  display: -webkit-flex;
  display: -ms-flexbox;
  display: flex;
  color: #515151;
  -webkit-box-align: center;
  -webkit-align-items: center;
  -ms-flex-align: center;
  align-items: center;
}

.brand-logo:focus,
.brand-logo:active,
.brand-logo:hover {
  color: #080b13;
  text-decoration: none;
}

.brand-logo i {
  font-size: 27px;
  margin-right: 10px;
}

.dashboard-nav-list {
  display: -webkit-box;
  display: -webkit-flex;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-orient: vertical;
  -webkit-box-direction: normal;
  -webkit-flex-direction: column;
  -ms-flex-direction: column;
  flex-direction: column;
}

.dashboard-nav-item {
  min-height: 56px;
  padding: 8px 20px 8px 20px;
  display: -webkit-box;
  display: -webkit-flex;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-align: center;
  -webkit-align-items: center;
  -ms-flex-align: center;
  align-items: center;
  letter-spacing: 0.02em;
  transition: ease-out 0.5s;
}

.dashboard-nav-item i {
  width: 50px;
  font-size: 19px;
  margin-left: -20px;
}

.dashboard-nav-item:hover {
  background: rgba(255, 255, 255, 0.04);
}

.active {
  background: #1e3d73;
  border-radius: 30px;
  color: #080b13;
}

.dashboard-nav-dropdown {
  display: -webkit-box;
  display: -webkit-flex;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-orient: vertical;
  -webkit-box-direction: normal;
  -webkit-flex-direction: column;
  -ms-flex-direction: column;
  flex-direction: column;
}

.dashboard-nav-dropdown.show {
  background: rgba(255, 255, 255, 0.04);
}

.dashboard-nav-dropdown.show>.dashboard-nav-dropdown-toggle {
  font-weight: bold;
}

.dashboard-nav-dropdown.show>.dashboard-nav-dropdown-toggle:after {
  -webkit-transform: none;
  -o-transform: none;
  transform: none;
}

.dashboard-nav-dropdown.show>.dashboard-nav-dropdown-menu {
  display: -webkit-box;
  display: -webkit-flex;
  display: -ms-flexbox;
  display: flex;
}

.dashboard-nav-dropdown-toggle:after {
  content: "";
  margin-left: auto;
  display: inline-block;
  width: 0;
  height: 0;
  border-left: 5px solid transparent;
  border-right: 5px solid transparent;
  border-top: 5px solid rgba(81, 81, 81, 0.8);
  -webkit-transform: rotate(90deg);
  -o-transform: rotate(90deg);
  transform: rotate(90deg);
}

.dashboard-nav .dashboard-nav-dropdown-toggle:after {
  border-top-color: rgba(255, 255, 255, 0.72);
}


.menu-toggle {
  position: relative;
  width: 42px;
  height: 42px;
  display: -webkit-box;
  display: -webkit-flex;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-align: center;
  -webkit-align-items: center;
  -ms-flex-align: center;
  align-items: center;
  -webkit-box-pack: center;
  -webkit-justify-content: center;
  -ms-flex-pack: center;
  justify-content: center;
  color: #443ea2;
}

.menu-toggle:hover,
.menu-toggle:active,
.menu-toggle:focus {
  text-decoration: none;
  color: #fefefe;
}

.menu-toggle i {
  font-size: 20px;
}

.dashboard-toolbar {
  min-height: 44px;
  background-color: #d2dde8;
  display: -webkit-box;
  display: -webkit-flex;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-align: center;
  -webkit-align-items: center;
  -ms-flex-align: center;
  align-items: center;
  padding: 8px 27px;
  position: fixed;
  top: 0;
  right: 0;
  left: 0;
  z-index: 1000;
}

.nav-item-divider {
  height: 1px;
  margin: 1rem 0;
  overflow: hidden;
  background-color: rgba(236, 238, 239, 0.3);
}

@media (min-width: 992px) {
  .dashboard-app {
    margin-left: 238px;
  }

  .dashboard-compact .dashboard-app {
    margin-left: 0;
  }
}


@media (max-width: 768px) {
  .dashboard-content {
    padding: 15px 0px;
  }
}

@media (max-width: 992px) {
  .dashboard-nav {
    display: none;
    position: fixed;
    top: 0;
    right: 0;
    left: 0;
    bottom: 0;
    z-index: 1070;
  }

  .dashboard-nav.mobile-show {
    display: block;
  }
}
@media (min-width: 700px) {
  .dashboard-toolbar {
    left: 0vw;
  }

  .dashboard-compact .dashboard-toolbar {
    left: 0;
  }
}

@media (min-width: 900px) {
  .dashboard-toolbar {
    left: 0vw;
  }

  .dashboard-compact .dashboard-toolbar {
    left: 0;
  }
}
@media (min-width: 1000px) {
  .dashboard-toolbar {
    left: 26vw;
  }

  .dashboard-compact .dashboard-toolbar {
    left: 0;
  }
}
@media (min-width: 1100px) {
  .dashboard-toolbar {
    left: 23vw;
  }

  .dashboard-compact .dashboard-toolbar {
    left: 0;
  }
}
@media (min-width: 1200px) {
  .dashboard-toolbar {
    left: 22vw;
  }

  .dashboard-compact .dashboard-toolbar {
    left: 0;
  }
}

@media (min-width: 1300px) {
  .dashboard-toolbar {
    left: 20vw;
  }

  .dashboard-compact .dashboard-toolbar {
    left: 0;
  }
}

@media (min-width: 1400px) {
  .dashboard-toolbar {
    left: 18%;
  }

  .dashboard-compact .dashboard-toolbar {
    left: 0;
  }
}

@media (max-width: 620px) {
  .dashboard-toolbar {
    left: 25%;
  }

  .dashboard-compact .dashboard-toolbar {
    left: 0;
  }
}

@media (max-width: 500px) {
  .dashboard-toolbar {
    left: 0vw;
  }

  .dashboard-compact .dashboard-toolbar {
    left: 0;
  }
}
</style>