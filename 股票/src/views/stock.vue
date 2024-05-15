<template>
  <div>
    <h3 class='text-2xl font-bold text-left py-2' style='color:#1B3C73'>個股資訊</h3>
    <div class="input">
      <b-dropdown id="dropdown-1" text="選擇輸入項目" class="m-md-2" variant="outline-secondary">
        <b-dropdown-item>股票名稱</b-dropdown-item>
        <b-dropdown-item>股票代碼</b-dropdown-item>
      </b-dropdown>
      <b-form-input type='text' v-model='target' placeholder='請輸入欲查詢股票' style="width:50%; margin-left:10px;"></b-form-input>
      <b-button variant="outline-secondary" style="margin-left:1%">搜尋</b-button>
    </div>
    <!-- <h3>value:{{target}}</h3>
    <h3>value:{{inputType}}</h3> -->
    <div class="stock-info" style="width:100%">
      <span class="stock-name">
        <span> 股票名稱 </span>
        <span> 2330 </span>
      </span>
      <span class="current-price" style="margin-left: 15px;">237.23</span>
      <span class="change">+ 5.34</span>
      <span class="change"> (0.03%)</span>
    </div>

    <div class="stock-tab" style="margin-top:3%">
      <b-tabs content-class='mt-3' >
        <b-tab title='走勢圖'>
          <div class="col-3" style="width:100%">
            <b-dropdown id="dropdown-1" text="期間" class="m-md-2" variant="outline-secondary">
              <b-dropdown-item>當日</b-dropdown-item>
              <b-dropdown-item>一個月</b-dropdown-item>
              <b-dropdown-item>一年</b-dropdown-item>
              <b-dropdown-item>五年</b-dropdown-item>
              <b-dropdown-item>全部期間</b-dropdown-item>
            </b-dropdown>
          </div>
          <div class='example' style="width:90%;">
            <apexcharts height='270vh' type='line' :options='chartOptions' :series='series'></apexcharts>
          </div>
        </b-tab>
        <b-tab title='分析' lazy>
          <b-table striped :items="items" style="margin-left: 20px; width:70%; text-align: center;"></b-table>
          <div class='example' style="width:90%;">
            <apexcharts height='270vh' type='line' :options='chartOptions' :series='series'></apexcharts>
          </div>
        </b-tab>
      </b-tabs>
    </div>
</div>
</template>

<script >
import VueApexCharts from 'vue-apexcharts'

export default {
  name: 'StockPage',
  components: {
    apexcharts: VueApexCharts
  },
  data () {
    return {
      inputType: '股票代號',
      target: '',
      chartOptions: {
        dataLabels: {
          enabled: false
        },
        colors: ['#247BA0'],
        stroke: {
          width: [4]
        },
        plotOptions: {
          bar: {
            columnWidth: '2%'
          }
        },
        xaxis: {
          type: 'datetime',
          categories: ['1/1', '1/2', '1/3', '1/4', '1/5', '1/6', '1/7', '1/8', '1/9', '1/10', '1/11', '1/12', '1/13', '1/14', '1/15', '1/16', '1/17', '1/18', '1/19', '1/20', '1/21', '1/22', '1/23', '1/24', '1/25', '1/26', '1/27', '1/28', '1/29', '1/30', '1/31'],
          labels: {
            show: true,
            rotate: -45,
            datetimeUTC: true,
            datetimeFormatter: {
              year: 'yyyy',
              month: "MMM 'yy",
              day: 'dd MMM',
              hour: 'HH:mm'
            }
          }
        },
        yaxis: [
          {
            axisTicks: {
              show: true
            },
            axisBorder: {
              show: true
            },
            title: {
              style: {
                color: '#247BA0'
              }
            }
          }
        ],
        tooltip: {
          shared: false,
          intersect: true,
          x: {
            show: false
          }
        },
        legend: {
          horizontalAlign: 'left',
          offsetX: 40
        }
      },
      series: [
        {
          name: 'Series A',
          data: [160.11, 154.82, 155.88, 154.91, 150.84, 150.72, 151.64, 153.88, 150.98, 159.29, 151.6, 151.96, 151.35, 157.17, 155.55, 160.08, 150.63, 155.68, 159.83, 157.17, 159.54, 153.48, 155.44, 150.5, 153.85, 159.09, 155.49, 152.1, 159.1, 152.91, 150.38]
        }
      ],
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

.choose {
  font-size: 36px;
  margin-bottom: 10px;
  float: left;
  margin-left: 20px;
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
    text-align: left;
}
.input .b-dropdown {
  display: block;
  float: left;

  .dropdown-menu {
      margin-bottom: 10px;
      margin-left: 0px;
  }
}
</style>
