<template>
  <div>
    <h3 class='text-2xl font-bold text-left py-2' style='color:#1B3C73;text-align:left'>個股資訊</h3>

    <div class="input">
      <b-dropdown id="dropdown-1" v-model='inputType' text="選擇輸入項目" class="m-md-2" variant="outline-secondary">
        <b-dropdown-item>股票名稱</b-dropdown-item>
        <b-dropdown-item>股票代碼</b-dropdown-item>
      </b-dropdown>
      <b-form-input type='text' v-model='target' placeholder='請輸入欲查詢股票' style="width:50%; margin-left:1%;" @keyup.enter="submitQuery" required></b-form-input>
      <b-button @click="submitQuery" variant="outline-secondary" style="margin-left:1%">搜尋</b-button>
    </div>

    <div class="stock-info" style="width:100%">
      <span class="stock-name">
        <span> 股票名稱 </span>
        <span> 2330 </span>
      </span>
      <span class="current-price" style="margin-left: 15px;">237.23</span>
      <span class="change">+ 5.34</span>
      <span class="change"> (0.03%)</span>
    </div>

    <div class="stock-tab">
      <b-tabs content-class='mt-3'>
        <b-tab title='走勢圖'>
          <div style="margin-left:2%; width:50%">
            <!-- <label for="period-select">選擇期間：</label> -->
            <select id="time-select" name="time" v-model="selectedTime">
                <option disabled value="one_month">一個月</option>
                <option value="one_month">一個月</option>
                <option value="three_months">三個月</option>
                <option value="one_year">一年</option>
                <option value="custom">自選</option>
            </select>
            <div v-if="selectedTime === 'custom'" style="margin-top:2%;">
              <b-form-group label="開始日期">
                <b-form-input type="date" v-model="customStartDate_T"></b-form-input>
              </b-form-group>
              <b-form-group label="結束日期">
                <b-form-input type="date" v-model="customEndDate_T"></b-form-input>
              </b-form-group>
            </div>
          </div>

          <div id='stock1' style="width:80%;">
            <trend />
          </div>
        </b-tab>
        <b-tab title='分析' lazy>
          <!-- <b-table striped :items="items" style="margin-left: 20px; width:70%; text-align: center;"></b-table> -->
          <!-- <div class="col-3" style="z-index: 1; width:100%">
            <b-dropdown id="dropdown-2" text="日線" class="m-md-2" variant="outline-secondary">
              <b-dropdown-item>日線</b-dropdown-item>
              <b-dropdown-item>週線</b-dropdown-item>
              <b-dropdown-item>月線</b-dropdown-item>
            </b-dropdown>
          </div>
          <div class="col-3" style="z-index: 1; width:100%">
            <b-dropdown id="dropdown-3" text="KD,J值" class="m-md-2" variant="outline-secondary">
              <b-dropdown-item>KD,J值</b-dropdown-item>
              <b-dropdown-item>MACD</b-dropdown-item>
              <b-dropdown-item>RSI</b-dropdown-item>
            </b-dropdown>
          </div> -->
          <div style="margin-left: 2%;">
            <select id="period-select" name="period" v-model="selectedPeriod">
              <option disabled value="daily">日線</option>
              <option value="daily">日線</option>
              <option value="weekly">週線</option>
              <option value="monthly">月線</option>
              <option value="custom">自選</option>
            </select>
            <div v-if="selectedPeriod === 'custom'" style="margin-top:2%; margin-bottom: 2%;">
              <b-form-group label="開始日期">
                <b-form-input type="date" v-model="customStartDate_P"></b-form-input>
              </b-form-group>
              <b-form-group label="結束日期">
                <b-form-input type="date" v-model="customEndDate_P"></b-form-input>
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
            <analysis />
          </div>
        </b-tab>
      </b-tabs>
    </div>
  </div>
</template>

<script >
import trend from './graph/trend.vue'
import analysis from './graph/analysis.vue'

export default {
  name: 'StockPage',
  components: {
    trend,
    analysis
  },
  data () {
    return {
      inputType: '股票代號',
      target: '',
      selectedPeriod: 'one_month',

    }
  },
  methods: {
    submitQuery() {
      const data = {
        inputType: this.inputType, 
        target: this.target,
        selectedPeriod: this.selectedPeriod
      }
    },
    async fetchInfo(){
      try {
        const response = await axios.post('http://127.0.0.1:12000/api/Stockinformation', {
          StocksID:2330,
          Stockstitle: "台積電",
          time:7
        });
        const data = response.data;
      } catch (error) {
        console.error('Error fetching index:', error);
      }
    },
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

/* 選項樣式 */
select option {
    padding: 10px;
}

</style>
