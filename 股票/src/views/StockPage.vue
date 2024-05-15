<template>
  <div>
    <h3 class='text-2xl font-bold text-left py-2' style='color:#1B3C73;text-align:left'>個股資訊</h3>

    <div class="input">
      <b-dropdown id="dropdown-1" text="選擇輸入項目" class="m-md-2" variant="outline-secondary">
        <b-dropdown-item>股票名稱</b-dropdown-item>
        <b-dropdown-item>股票代碼</b-dropdown-item>
      </b-dropdown>
      <b-form-input type='text' v-model='target' placeholder='請輸入欲查詢股票'
        style="width:50%; margin-left:1%;"></b-form-input>
      <b-button variant="outline-secondary" style="margin-left:1%">搜尋</b-button>
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
          <div class="col-3" style="z-index: 1; width:100%">
            <b-dropdown id="dropdown-1" text="期間" class="m-md-2" variant="outline-secondary">
              <b-dropdown-item>當日</b-dropdown-item>
              <b-dropdown-item>一個月</b-dropdown-item>
              <b-dropdown-item>一年</b-dropdown-item>
              <b-dropdown-item>五年</b-dropdown-item>
              <b-dropdown-item>全部期間</b-dropdown-item>
            </b-dropdown>
          </div>
          <div id='stock1' style="width:80%;">
            <trend />
          </div>
        </b-tab>
        <b-tab title='分析' lazy>
          <!-- <b-table striped :items="items" style="margin-left: 20px; width:70%; text-align: center;"></b-table> -->
          <div class="col-3" style="z-index: 1; width:100%">
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
import trend from '@/components/trend.vue'
import analysis from '@/components/analysis.vue'

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
      items: [
        { 日期: '2024/1/2', 開: 159.23, 高: 161.23, 低: 158.22, 收: 160.23, 成交量: 402312 }
      ]
    }
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

</style>
