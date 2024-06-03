<template>
  <div>
    <h3 class='text-2xl font-bold text-left py-2' style='color:#1B3C73;text-align:left'>個股資訊</h3>

    <div class="input">
      <select id="query_type" name="type" v-model="queryType">
        <option disabled value="symbol">股票代碼</option>
        <option value="symbol">股票代碼</option>
        <option value="name">股票名稱</option>
      </select>
      <b-form-input type='text' v-model='queryTarget' placeholder='請輸入欲查詢股票' style="width:50%; margin-left:1%;" @keyup.enter="submitQuery" required></b-form-input>
      <b-button @click="submitQuery" variant="outline-secondary" style="margin-left:1%">搜尋</b-button>
    </div>

    <div class="stock-info" style="width:100%">
      <span class="stock-name">
        <span id="stock-name" style="margin-right: 10px;">{{ stockName }}</span>
        <span id="stock-symbol">{{ stockSymbol }}</span>
      </span>
      <span class="current-price">
        <span id="price-today" style="font-size: 48px;">{{ priceToday }}</span>
        <span id="price-change" style="margin-left: 10px;">{{ priceChange }}</span>
        <span id="price-change-percent" style="margin-left: 10px;">({{ priceChangePercent }}%)</span>
      </span>
    </div>

    <div class="stock-tab">
      <b-tabs content-class='mt-3'>
        <b-tab title='走勢圖'>
          <div style="margin-left:2%; width:50%">
            <select id="time-select" name="time" v-model="selectedTime">
              <option disabled value='20' >一個月</option>
              <option value='20' >一個月</option>
              <option value='60' >三個月</option>
              <option value='240' >一年</option>
              <option value="custom">自選</option>
            </select>
            <div v-if="selectedTime === 'custom'" style="margin-top:2%;">
              <b-form-group label="開始日期">
                <b-form-input type="date" v-model="StartDate_T"></b-form-input>
              </b-form-group>
              <b-form-group label="結束日期">
                <b-form-input type="date" v-model="EndDate_T"></b-form-input>
              </b-form-group>
            </div>
          </div>

          <div id='stock1' style="width:80%;">
            <trend />
          </div>
        </b-tab>
        <b-tab title='分析' lazy>
          <div style="margin-left: 2%;">
            <select id="period-select" name="period" v-model="selectedPeriod">
              <option disabled value='5' >週線</option>
              <option value='5' >週線</option>
              <option value='20' >月線</option>
              <option value='240' >年線</option>
              <option value="custom">自選</option>
            </select>
            <div v-if="selectedPeriod === 'custom'" style="margin-top:2%; margin-bottom: 2%;">
              <b-form-group label="開始日期">
                <b-form-input type="date" v-model="StartDate_P"></b-form-input>
              </b-form-group>
              <b-form-group label="結束日期">
                <b-form-input type="date" v-model="EndDate_P"></b-form-input>
              </b-form-group>
            </div>

            <select id="index-select" name="index" v-model="selectedIndex" style="margin-left: 2%;">
              <option disabled value="KDJ">KD,J值</option>
              <option value="KDJ">KD,J值</option>
              <option value="MACD">MACD</option>
              <option value="RSI">RSI</option>
            </select>
          </div>
          <div id='stock2' style="width:80%;">
            <div v-if="selectedIndex === 'KDJ'">
              <kdjGraph />
            </div>
            <div v-if="selectedIndex === 'MACD'">
              <macdGraph />
            </div>
            <div v-if="selectedIndex === 'RSI'">
              <rsiGraph />
            </div>
          </div>
        </b-tab>
      </b-tabs>
    </div>
  </div>
</template>

<script >
import trend from './graph/trend.vue'
import kdjGraph from './graph/KDJ.vue'
import rsiGraph from './graph/RSI.vue'
import macdGraph from './graph/MACD.vue'
import axios from 'axios'

export default {
  name: 'StockPage',
  components: {
    trend,
    kdjGraph,
    rsiGraph,
    macdGraph
  },
  data () {
    return {
      stockName: '台積電',
      stockSymbol: '2330',
      queryType: 'symbol',
      queryTarget: '2330',
      selectedTime: '20',
      StartDate_T: '',  
      EndDate_T: '',
      selectedPeriod: '5',
      StartDate_P: '',  
      EndDate_P: '',
      selectedIndex:'KDJ',
      priceToday: 213.12, 
      priceYesterday: 211.94,
      // priceChange: '',
      // priceChangePercent: ''
    }
  },
  watch: {
    selectedTime: {
      handler: 'fetchInfo', // 調用 fetchInfo 函數
      immediate: true // 立即調用一次，以處理初始選擇
    },
    selectedPeriod: {
      handler: 'fetchInfo', // 調用 fetchInfo 函數
      immediate: true // 立即調用一次，以處理初始選擇
    },
    StartDate_T: {
      handler: 'checkBothDate_T' 
    },
    EndDate_T: {
      handler: 'checkBothDate_T' 
    },
    StartDate_P: {
      handler: 'checkBothDate_P' 
    },
    EndDate_P: {
      handler: 'checkBothDate_P' 
    }
  },
  methods: {
    submitQuery() {
      if (!this.queryType) {
        alert('請選擇股票代碼或股票名稱');
        return;
      }

      if (this.queryType === 'symbol') {
        if (!/^[A-Za-z0-9]+$/.test(this.queryTarget)) {
          alert('請輸入有效的股票代碼');
          return;
        }
      } else if (this.queryType === 'name') {
        if (!this.queryTarget.trim()) {
          alert('請輸入有效的股票名稱');
          return;
        }
      }
      this.fetchInfo();
    },
    async checkBothDate_T() {
      // 確保 StartDate_P 和 EndDate_P 都已經設置
      if (this.StartDate_T && this.EndDate_T) {
        // 都已經設置，可以調用 fetchInfo 函數
        await this.fetchInfo();
      } else {
        // 如果其中一個日期未設置，則不執行任何操作
        console.log('Both StartDate_T and EndDate_T must be set.');
      }
    },
    async checkBothDate_P() {
      // 確保 StartDate_P 和 EndDate_P 都已經設置
      if (this.StartDate_P && this.EndDate_P) {
        // 都已經設置，可以調用 fetchInfo 函數
        await this.fetchInfo();
      } else {
        // 如果其中一個日期未設置，則不執行任何操作
        console.log('Both StartDate_P and EndDate_P must be set.');
      }
    },
    async fetchInfo(){
      let startDate_T = this.StartDate_T;
      let endDate_T = this.EndDate_T;
      let startDate_P = this.StartDate_P;
      let endDate_P = this.EndDate_P;

      if (this.selectedTime !== "custom") {
        let today = new Date();
        let selectedDays = parseInt(this.selectedTime);
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
      if (this.selectedPeriod !== "custom") {
        let today = new Date();
        let selectedDays = parseInt(this.selectedPeriod);
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
        const response = await axios.post('http://127.0.0.1:12000/api/Stockinformation', {
          queryType: this.queryType,
          queryTarget: this.queryTarget,
          StartDate_T: startDate_T,
          EndDate_T: endDate_T,
          StartDate_P: startDate_P,
          EndDate_P: endDate_P,
          selectedIndex: this.selectedIndex
        });
        const data = response.data;
        const fs = require('fs');
        const path = require('path');

        if (data.StatusCode === 200) {
          const returnData = data.ReturnData;

          const stockName = returnData.stockName;
          document.getElementById('stock-name').textContent = stockName;

          const stockSymbol = returnData.stockSymbol;
          document.getElementById('stock-symbol').textContent = stockSymbol;

          // this.priceToday = 319.31;
          // this.priceYesterday = 315.23;
          this.priceToday = returnData.priceToday;
          this.priceYesterday = returnData.priceYesterday;
          this.changeColor();
          const stockPriceFilePath = path.join(__dirname, 'data', 'stockPrice.js');
          const stockPriceFileContent = `const stockPriceData = ${JSON.stringify(returnData.stockPrice, null, 2)};\nexport default stockPriceData;`;

          fs.writeFile(stockPriceFilePath, stockPriceFileContent, 'utf8', (err) => {
            if (err) {
              console.error('Error writing stockPrice data to file:', err);
            } else {
              console.log('Stock price data successfully written to ./data/stockPrice.js');
            }
          });

          // 寫入 volume 到 volume.js
          const volumeFilePath = path.join(__dirname, 'data', 'volume.js');
          const volumeFileContent = `const VolData = ${JSON.stringify(returnData.volume, null, 2)};\nexport default VolData;`;

          fs.writeFile(volumeFilePath, volumeFileContent, 'utf8', (err) => {
            if (err) {
              console.error('Error writing volume data to file:', err);
            } else {
              console.log('Volume data successfully written to ./data/Volume.js');
            }
          })
        }
        // console.log('queryType:', this.queryType);
        // console.log('queryTarget:', this.queryTarget);
        // console.log('priceToday:', this.priceToday)   
      } catch (error) {
        console.error('Error fetching index:', error);
      }
    },
    changeColor() {
      const elm1 = document.getElementById("price-change");
      const elm2 = document.getElementById("price-change-percent");
      const elm3 = document.getElementById("price-today");
      if(this.priceChange > 0){       
        elm1.style.color = '#EF403C';
        elm1.textContent = `▲${this.priceChange}`;
        elm2.style.color = '#EF403C';
        elm3.style.color = '#EF403C';
      }else if (this.priceChange < 0) {
        elm1.style.color = '#00B746';       
        elm2.style.color = '#00B746';
        elm3.style.color = '#00B746';
        let noMinus = Math.abs(this.priceChange);
        elm1.textContent = `▼${noMinus}`;
      }
    },
  },
  computed: {
    priceChange() {
      return (this.priceToday - this.priceYesterday).toFixed(2);
    },
    priceChangePercent()
    {
      return ((this.priceChange/this.priceYesterday)*100).toFixed(2);
    }
  },
  mounted() {
    this.fetchInfo();
  }
}
</script>

<style lang='scss' scoped>
.custom-dropdown .dropdown-menu {
    left: 0 !important;
}

@import url(https://fonts.googleapis.com/css?family=Roboto);

body {
  font-family: Roboto, sans-serif;
  left :0;
}

#chart {
  max-width: 650px;
  margin: 35px auto;
}

.input{
  display: flex;
  align-items: center;
  font-size: 36px;
  margin-top: 10px;
  margin-bottom: 20px;
  margin-left: 20px;
  // padding: 20px;
}

.stock-info {
    display: flex;
    align-items: center;
    font-size: 36px;
    margin-bottom: 10px;
    font-weight: bold;
    margin-left: 20px;
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

.stock-tab{
    margin-top: 3%;
    text-align: left;
}

label {
    font-size: 16px;
    color: #333;
    margin-right: 10px;
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

select option {
    padding: 10px;
}

</style>
