<template>
  <div>
    <h3 class="text-2xl font-bold text-left py-2" style="color:#1B3C73;text-align:left">大盤市況</h3>
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
            <apexchart width="90%" type="area" :options="chartOptions" :series="seriesMarket"></apexchart>
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
            <h1 style="text-align:center;font-size:40px;margin-top:30%">37/45</h1>
          </ul>

        </div>
      </div>
      <div class="col-6">
        <div class="card2" style="width:100%">
          <h1 style="margin:2%;font-size: 24px;color:black;font-weight: 600;text-align:left">景氣燈號歷史</h1>
          <div>
            <apexchart width="90%" type="area" :options="chartOptions" :series="seriesIndicator"></apexchart>
          </div>
        </div>
      </div>
    </div>

    <div id="TW index" class="stock-info" style="width:100%; margin-top: 5%;">
      <span class="stock-name">
        <span> 台灣加權指數 </span>
      </span>
      <span class="current-price" style="margin-left: 15px;">237.23</span>
      <span class="change">+ 5.34</span>
      <span class="change"> (0.03%)</span>
    </div>

    <div class="stock-tab" >
      <div class="col-3" style="z-index: 1; width:100%">
        <div style="margin-left:2%; width:50%">
            <select id="time-select-Taiwan" name="time" v-model="selectedTime_Taiwan">
              <option disabled value="one_month" p>一個月</option>
              <option value="one_month">一個月</option>
              <option value="three_months">三個月</option>
              <option value="one_year">一年</option>
              <option value="custom">自選</option>
            </select>
            <div v-if="selectedTime_Taiwan === 'custom'" style="margin-top:2%;">
              <b-form-group label="開始日期">
                <b-form-input type="date" v-model="customStartDate_Taiwan"></b-form-input>
              </b-form-group>
              <b-form-group label="結束日期">
                <b-form-input type="date" v-model="customEndDate_Taiwan"></b-form-input>
              </b-form-group>
            </div>
          </div>
      </div>
      <div id='stock1' style="width:80%;"><trend/></div>

    </div>

    <div id="DJ index" class="stock-info" style="width:100%; margin-top: 10%;">
      <span class="stock-name">
        <span> 道瓊工業指數 </span>
      </span>
      <span class="current-price" style="margin-left: 15px;">237.23</span>
      <span class="change">+ 5.34</span>
      <span class="change"> (0.03%)</span>
    </div>

    <div class="stock-tab" >
      <div class="col-3" style="z-index: 1; width:100%">
        <div style="margin-left:2%; width:50%">
            <select id="time-select-DJ" name="time" v-model="selectedTime_DJ">
              <option disabled value="one_month" p>一個月</option>
              <option value="one_month">一個月</option>
              <option value="three_months">三個月</option>
              <option value="one_year">一年</option>
              <option value="custom">自選</option>
            </select>
            <div v-if="selectedTime_DJ === 'custom'" style="margin-top:2%;">
              <b-form-group label="開始日期">
                <b-form-input type="date" v-model="customStartDate_DJ"></b-form-input>
              </b-form-group>
              <b-form-group label="結束日期">
                <b-form-input type="date" v-model="customEndDate_DJ"></b-form-input>
              </b-form-group>
            </div>
          </div>
      </div>
      <div id='stock3' style="width:80%;"><trend/></div>
    </div>
  </div>
</template>
<script>
import VueApexCharts from 'vue-apexcharts'
import trend from './graph/trend.vue'
import Volume from './graph/Volume.vue'
import { seriesData } from './data/stockPrice.js'


export default {
  components: {
    apexchart: VueApexCharts,
    trend,
    Volume
  },
  data () {
    return {
      selectedTime_Taiwan: 'one_month',
      customStartDate_Taiwan: '',  
      customEndDate_Taiwan: '',
      selectedTime_DJ: 'one_month',
      customStartDate_DJ: '',  
      customEndDate_DJ: '',
      seriesMarket: [{ 
        name: 'score',
        data: seriesData 
      }],
      seriesIndicator: [{ 
        name: 'score',
        data: seriesData 
      }],
      chartOptions: {
        chart: {
          id: 'vuechart-example'
        },
        xaxis: {
          type: 'datetime',
        },
        colors: ['#7FC7D9'],
        tooltip: {
          enabled: true,
          x: {
              show: true,
              format: 'yyyy/MM/dd',
          }
        },
        dataLabels: {
          enabled: false
        },
        fill: {
          type: "gradient",
          gradient: {
            shadeIntensity: 1,
            opacityFrom: 0.7,
            opacityTo: 0.9,
            stops: [0, 90, 100]
          }
        },
      },
    }
  }
}
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

.stock-info {
    display: flex;
    align-items: center;
    font-size: 36px;
    margin-bottom: 10px;
    font-weight: bold;
    margin-left: 2%;
    margin-bottom: 10px;
}

.current-price {
    font-size: 48px;
    font-weight: bold;
    margin-right: 10px;
}

.change {
    font-size: 20px;
    color: #D24545; /*或者是red，根据涨跌情况设置颜色*/
}

.stock-name {
  font-size: 36px;
  border: 2px solid rgb(153, 184, 206);
  border-radius: 12px;
  padding: 10px;
}

.stock-tab{
    margin-top: 2%;
    text-align: left;
    margin-left: 2%;
}

select {
    font-size: 16px;
    color: #333;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
    background-color: #f9f9f9;
    transition: border-color 0.3s, box-shadow 0.3s;
}

select:focus {
    border-color: #66afe9;
    outline: none;
    box-shadow: 0 0 5px rgba(102, 175, 233, 0.6);
}

/* 選項樣式 */
select option {
    padding: 10px;
}
</style>
