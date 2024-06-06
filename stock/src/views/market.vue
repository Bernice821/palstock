<template>
  <div>
    <h3 class="text-2xl font-bold text-left py-2" style="color:#1B3C73">大盤市況</h3>
    <div class="row">
      <div class="col-6">
        <div class="card2">
          <h1 style="margin:2%;font-size: 24px;color:black;font-weight: 600;text-align:left">大盤總分</h1>
          <ul class="chart-skills">
            <li>
              <span></span>
            </li>
            <li>
              <span></span>
            </li>
            <li>
              <span></span>
            </li>
            <li>
              <span></span>
            </li>
            <h1 style="text-align:center;font-size:40px;margin-top:30%">8/10</h1>
          </ul>

        </div>
      </div>
      <div class="col-6">
        <div class="card2" style="width:100%">
          <h1 style="margin:2%;font-size: 24px;color:black;font-weight: 600;text-align:left">大盤總分歷史</h1>
          <div>
            <apexchart width="90%" type="area" :options="chartOptions" :series="chartSeries"></apexchart>
          </div>
        </div>
      </div>
    </div>
    <div class="row">
      <div class="col">
        <div class="card2">
          <h1 style="margin:2%;font-size: 24px;color:black;font-weight: 600;text-align:left">景氣燈號總分</h1>
          <ul class="chart-skills">
            <li>
              <span></span>
            </li>
            <li>
              <span></span>
            </li>
            <li>
              <span></span>
            </li>
            <li>
              <span></span>
            </li>
            <h1 style="text-align:center;font-size:40px;margin-top:30%">7/10</h1>
          </ul>

        </div>
      </div>
      <div class="col-6">
        <div class="card2" style="width:100%">
          <h1 style="margin:2%;font-size: 24px;color:black;font-weight: 600;text-align:left">景氣燈號歷史</h1>
          <div>
            <apexchart width="90%" type="area" :options="chartOptions" :series="chartSeries"></apexchart>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import VueApexCharts from 'vue-apexcharts';
import axios from 'axios';
export default {
  components: {
    apexchart: VueApexCharts,
  },
  data() {
    return {
      chartOptions: {
        chart: {
          id: 'vuechart-example',
        },
        xaxis: {
          categories: [8, 9, 10, 11, 12, 13, 14,15,16,17,18,19,20],
        },
        colors: ['#0E46A3'],
      },
      chartSeries: [
        {
          name: 'Vue Chart',
          data: [155.95, 155.61, 156.92, 156.93, 157.01, 156.85,157.01,157.01,157.02,157.01,157.01,157.01,157.01]
        }
      ],
    };

  }
};
</script>
<style>
.chart-skills {
  margin: 0 auto;
  padding: 0;
  list-style-type: none;
}

.chart-skills *,
.chart-skills::before {
  box-sizing: border-box;
}

.card2 {
  margin-top: 2%;
  margin-left: 2%;
  border-radius: 10px;
  background-color: #fff;
  padding: 20px;
  overflow: hidden;
  box-shadow: 0 4px 8px 0 rgba(182, 182, 182, 0.8);
  transition: 0.3s;
  width: 80%;
  height:90%;
}


/* CHART-SKILLS STYLES
–––––––––––––––––––––––––––––––––––––––––––––––––– */

.chart-skills {
  position: relative;
  width: 350px;
  height: 175px;
  overflow: hidden;
}

.chart-skills::before,
.chart-skills::after {
  position: absolute;
}

.chart-skills li {
  position: absolute;
  top: 100%;
  left: 0;
  width: inherit;
  height: inherit;
  border: 45px solid;
  border-top: none;
  border-bottom-left-radius: 175px;
  border-bottom-right-radius: 175px;
  transform-origin: 50% 0;
  transform-style: preserve-3d;
  backface-visibility: hidden;
  animation-fill-mode: forwards;
  animation-duration: .4s;
  animation-timing-function: linear;
}

.chart-skills li:nth-child(1) {
  z-index: 4;
  border-color: #DCF2F1;
  animation-name: rotate-one;
}

.chart-skills li:nth-child(2) {
  z-index: 3;
  border-color: #7FC7D9;
  animation-name: rotate-two;
  animation-delay: .4s;
}

.chart-skills li:nth-child(3) {
  z-index: 2;
  border-color: #365486;
  animation-name: rotate-three;
  animation-delay: .8s;
}

.chart-skills li:nth-child(4) {
  z-index: 1;
  border-color: #0F1035;
  animation-name: rotate-four;
  animation-delay: 1.2s;
}

.chart-skills span {
  position: absolute;
  font-size: .85rem;
  backface-visibility: hidden;
  animation: fade-in .4s linear forwards;
}

.chart-skills li:nth-child(1) span {
  top: 5px;
  left: 10px;
  transform: rotate(-45deg);
}

.chart-skills li:nth-child(2) span {
  top: 20px;
  left: 10px;
  transform: rotate(-90deg);
  animation-delay: .4s;
}

.chart-skills li:nth-child(3) span {
  top: 18px;
  left: 10px;
  transform: rotate(-135deg);
  animation-delay: .8s;
}

.chart-skills li:nth-child(4) span {
  top: 10px;
  left: 10px;
  transform: rotate(-180deg);
  animation-delay: 1.2s;
}


/* ANIMATIONS
–––––––––––––––––––––––––––––––––––––––––––––––––– */

@keyframes rotate-one {
  100% {
    transform: rotate(45deg);
    /**
     * 12% => 21.6deg
     */
  }
}

@keyframes rotate-two {
  0% {
    transform: rotate(45deg);
  }

  100% {
    transform: rotate(90deg);
    /**
     * 32% => 57.6deg 
     * 57.6 + 21.6 => 79.2deg
     */
  }
}

@keyframes rotate-three {
  0% {
    transform: rotate(90deg);
  }

  100% {
    transform: rotate(135deg);
    /**
     * 34% => 61.2deg 
     * 61.2 + 79.2 => 140.4deg
     */
  }
}

@keyframes rotate-four {
  0% {
    transform: rotate(135deg);
  }

  100% {
    transform: rotate(180deg);
    /**
     * 22% => 39.6deg  
     * 140.4 + 39.6 => 180deg
     */
  }
}

@keyframes fade-in {

  0%,
  90% {
    opacity: 0;
  }

  100% {
    opacity: 1;
  }
}
</style>