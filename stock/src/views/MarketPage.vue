<template>
  <div>
    <h3 class="text-2xl font-bold text-left py-2" style="color:#1B3C73;text-align:left">大盤市況</h3>
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
            <h1 style="text-align:center;font-size:40px;margin-top:30%">{{ Indicators }}/45</h1>
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
        <span id="stock-name" style="margin-right: 10px;">台灣加權指數</span>
        <span id="stock-symbol">TWII</span>
      </span>
      <span class="current-price">
        <span id="price-today" style="font-size: 48px;">{{ TaiwanPriceToday }}</span>
        <span id="price-change" style="margin-left: 10px;">{{ priceChange(TaiwanPriceToday, TaiwanPriceYesterday)
          }}</span>
        <span id="price-change-percent" style="margin-left: 10px;">({{ priceChangePercent(priceChange(TaiwanPriceToday,
              TaiwanPriceYesterday), TaiwanPriceYesterday) }}%)</span>
      </span>
    </div>
    <div class="stock-tab">
      <div class="col-3" style="z-index: 1; width:100%">
        <div style="margin-left:2%; width:50%">
          <select id="time-select" name="time" v-model="selectedTime_Taiwan">
            <option disabled value='30'>一個月</option>
            <option value='30'>一個月</option>
            <option value='90'>三個月</option>
            <option value='365'>一年</option>
            <option value="custom">自選</option>
          </select>
          <div v-if="selectedTime_Taiwan === 'custom'" style="margin-top:2%;">
            <b-form-group label="開始日期">
              <b-form-input type="date" v-model="StartDate_Taiwan"></b-form-input>
            </b-form-group>
            <b-form-group label="結束日期">
              <b-form-input type="date" v-model="EndDate_Taiwan"></b-form-input>
            </b-form-group>
          </div>
        </div>
      </div>
      <div id='stock1' style="width:80%;">
        <trend />
      </div>
    </div>

    <div id="DJ index" class="stock-info" style="width:100%; margin-top: 5%;">
      <span class="stock-name">
        <span style="margin-right: 10px;">道瓊工業指數</span>
        <span>DJI</span>
      </span>
      <span class="current-price">
        <span id="price-today" style="font-size: 48px;">{{ DJPriceToday }}</span>
        <span id="price-change" style="margin-left: 10px;">{{ priceChange(DJPriceToday, DJPriceYesterday) }}</span>
        <span id="price-change-percent" style="margin-left: 10px;">({{ priceChangePercent(priceChange(DJPriceToday,
              DJPriceYesterday), DJPriceYesterday) }}%)</span>
      </span>
    </div>
    <div class="stock-tab">
      <div class="col-3" style="z-index: 1; width:100%">
        <div style="margin-left:2%; width:50%">
          <select name="time" v-model="selectedTime_DJ">
            <option disabled value='30'>一個月</option>
            <option value='30'>一個月</option>
            <option value='90'>三個月</option>
            <option value='365'>一年</option>
            <option value="custom">自選</option>
          </select>
          <div v-if="selectedTime_DJ === 'custom'" style="margin-top:2%;">
            <b-form-group label="開始日期">
              <b-form-input type="date" v-model="StartDate_DJ"></b-form-input>
            </b-form-group>
            <b-form-group label="結束日期">
              <b-form-input type="date" v-model="EndDate_DJ"></b-form-input>
            </b-form-group>
          </div>
        </div>
      </div>
      <div id='stock1' style="width:80%;">
        <DJtrend />
      </div>
    </div>
  </div>
</template>
<script>
import VueApexCharts from 'vue-apexcharts'
import trend from './graph/trend.vue'
import DJtrend from './graph/DJtrend.vue'
// import { seriesData } from './data/stockPrice.js'
import axios from 'axios'
import {IndicatorsHistory} from './data/stock.js'

export default {
  components: {
    apexchart: VueApexCharts,
    trend,
    DJtrend
  },
  data() {
    return {
      TaiwanPriceToday: 19,
      TaiwanPriceYesterday: 134.12,
      DJPriceToday: 379.29,
      DJPriceYesterday: 365.23,
      StartDate_Taiwan: '',
      EndDate_Taiwan: '',
      StartDate_DJ: '',
      EndDate_DJ: '',
      Indicators: 32,
      selectedTime_Taiwan: '30',
      selectedTime_DJ: '30',
      seriesIndicator: [{
        name: 'score',
        data: IndicatorsHistory
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
            format: 'yyyy-MM',
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
  },
  watch: {
    selectedTime_DJ: {
      handler: 'fetchInfo', // 調用 fetchInfo 函數
      immediate: true // 立即調用一次，以處理初始選擇
    },
    selectedTime_Taiwan: {
      handler: 'fetchInfo', // 調用 fetchInfo 函數
      immediate: true // 立即調用一次，以處理初始選擇
    },
    StartDate_Taiwan: {
      handler: 'checkBothDate_Taiwan'
    },
    EndDate_Taiwan: {
      handler: 'checkBothDate_Taiwan'
    },
    StartDate_DJ: {
      handler: 'checkBothDate_DJ'
    },
    EndDate_DJ: {
      handler: 'checkBothDate_DJ'
    }
  },
  methods: {
    async checkBothDate_Taiwan() {
      // 確保 StartDate_P 和 EndDate_P 都已經設置
      if (this.StartDate_Taiwan && this.EndDate_Taiwan) {
        // 都已經設置，可以調用 fetchInfo 函數
        await this.fetchInfo();
      } else {
        // 如果其中一個日期未設置，則不執行任何操作
        console.log('Both StartDate_Taiwan and EndDate_Taiwan must be set.');
      }
    },
    async checkBothDate_DJ() {
      // 確保 StartDate_P 和 EndDate_P 都已經設置
      if (this.StartDate_DJ && this.EndDate_DJ) {
        // 都已經設置，可以調用 fetchInfo 函數
        await this.fetchInfo();
      } else {
        // 如果其中一個日期未設置，則不執行任何操作
        console.log('Both StartDate_DJ and EndDate_DJ must be set.');
      }
    },
    async fetchInfo() {
      let startDate_T = this.StartDate_Taiwan;
      let endDate_T = this.EndDate_Taiwan;
      let startDate_P = this.StartDate_DJ;
      let endDate_P = this.EndDate_DJ;

      if (this.selectedTime_Taiwan !== "custom") {
        let today = new Date();
        let selectedDays = parseInt(this.selectedTime_Taiwan);
        let pastDate = new Date(today);
        pastDate.setDate(today.getDate() - selectedDays);
        startDate_T = pastDate.toISOString().split('T')[0];
        endDate_T = today.toISOString().split('T')[0];
        if (!isNaN(pastDate.getTime())) {
          startDate_T = pastDate.toISOString().split('T')[0];
          endDate_T = today.toISOString().split('T')[0];
        } else {
          console.error('Invalid date:', pastDate);
        }
      }
      if (this.selectedTime_DJ !== "custom") {
        let today = new Date();
        let selectedDays = parseInt(this.selectedTime_DJ);
        let pastDate = new Date(today);
        pastDate.setDate(today.getDate() - selectedDays);
        if (!isNaN(pastDate.getTime())) {
          startDate_P = pastDate.toISOString().split('T')[0];
          endDate_P = today.toISOString().split('T')[0];
        } else {
          console.error('Invalid date:', pastDate);
        }
      }

      try {
        const response = await axios.post('http://127.0.0.1:12000/api/Market', {
          StartDate_Taiwan: startDate_T,
          EndDate_Taiwan: endDate_T,
          StartDate_DJ: startDate_P,
          EndDate_DJ: endDate_P
        });

        const returnData = response.data;
        //console.log(returnData)
        this.TaiwanPriceToday = returnData.TaiwanPriceToday;
        this.TaiwanPriceYesterday = returnData.TaiwanPriceYesterday;

        this.DJPriceToday = returnData.DJPriceToday;
        this.DJPriceYesterday = returnData.DJPriceYesterday;
        this.changeColor();

        this.Indicators = returnData.Indicators;

      } catch (error) {
        console.error('Error fetching index:', error);
      }
    },
    changeColor() {
      const elm1 = document.querySelectorAll("#price-change");
      const elm2 = document.querySelectorAll("#price-change-percent");
      const elm3 = document.querySelectorAll("#price-today");
      let Change;
      for (var i = 0; i < elm1.length; i++) {
        if (i == 0) {
          Change = this.priceChange(this.TaiwanPriceToday, this.TaiwanPriceYesterday);
        }
        else {
          Change = this.priceChange(this.DJPriceToday, this.DJPriceYesterday);
        }
        if (Change > 0) {
          elm1[i].style.color = '#EF403C';
          elm1[i].textContent = `▲${Change}`;
          elm2[i].style.color = '#EF403C';
          elm3[i].style.color = '#EF403C';
        } else if (Change < 0) {
          elm1[i].style.color = '#00B746';
          elm2[i].style.color = '#00B746';
          elm3[i].style.color = '#00B746';
          let noMinus = Math.abs(Change);
          elm1[i].textContent = `▼${noMinus}`;
        }
      }
    },
    priceChange(priceToday, priceYesterday) {
      return (priceToday - priceYesterday).toFixed(2);
    },
    priceChangePercent(priceChange, priceYesterday) {
      return ((priceChange / priceYesterday) * 100).toFixed(2);
    }
  },
  mounted() {
    this.fetchInfo();
    this.changeColor();
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
  height: 90%;
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
  font-size: 24px;
  font-weight: bold;
  margin-left: 15px;
  display: flex;
  align-items: center;
}

.stock-name {
  font-size: 36px;
  border: 2px solid rgb(153, 184, 206);
  border-radius: 12px;
  padding: 10px;
}

.stock-tab {
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
