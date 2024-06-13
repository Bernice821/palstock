<template>
  <div id="wrapper" style="margin-left: 15%;">
    <div id="stock">
      <apexchart type="candlestick" height="400" :options="chartOptions1" :series="series1"></apexchart>
    </div>
  </div>
</template>

<script>
import VueApexCharts from 'vue-apexcharts'
import { series } from '../data/DJstockPrice.js'

export default {
  components: {
    apexchart: VueApexCharts
  },
  data () {
    return {
      series1: [{ data: series }],
      chartOptions1: {
        chart: {
          group: 'stock_dj',
          id: 'price',
          type: 'candlestick',
          height: 350
        },
        xaxis: {
          type: 'category',
          labels: {
            formatter: function(value) {
              const date = new Date(value);
              const year = date.getFullYear();
              const month = String(date.getMonth() + 1).padStart(2, '0'); // 获取月份并补零
              const day = String(date.getDate()).padStart(2, '0'); // 获取日期并补零
              return `${year}/${month}/${day}`; // 格式化为 '2023/02/01'
            }
          },
        },
        tooltip: {
          enabled: true,
          x: {
            show: true,
            format: 'yyyy/MM/dd',
            // offsetY: 100
          },
          fixed: {
            enabled: true,
            position: 'top',
            offsetX: -125,
            offsetY: 150, // 在這裡設置頂部偏移量
          },
        },
        plotOptions: {
          candlestick: {
            colors: {
              upward: '#EF403C',
              downward: '#00B746'
            }
          }
        }
      }
    }
  }
}
</script>
