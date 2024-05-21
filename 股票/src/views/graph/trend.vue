<template>
  <div id="wrapper" style="margin-left: 15%;">
    <div id="stock">
      <apexchart type="candlestick" height="400" :options="chartOptions1" :series="series1"></apexchart>
    </div>
    <div id="volume">
      <apexchart type="bar" height="150" :options="chartOptions2" :series="series2" style="margin-top: 5%;"></apexchart>
    </div>

  </div>
</template>

<script>
import VueApexCharts from 'vue-apexcharts'
import { seriesData } from '../data/stockPrice.js'
import { VolData } from '../data/volume.js'

export default {
  components: {
    apexchart: VueApexCharts
  },
  data () {
    return {
      series1: [{ data: seriesData }],
      chartOptions1: {
        chart: {
          group: 'stock',
          id: 'price',
          type: 'candlestick',
          height: 350
        },
        xaxis: {
          type: 'datetime',
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
            offsetX: -150,
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
      },
      series2: [{ 
        name: '成交量',
        data: VolData
      }],
      chartOptions2: {
        chart: {
          group: 'stock',
          id: 'volume',
          type: 'bar',
        },
        plotOptions: {
            bar: {
              horizontal: false,
              columnWidth: '55%',
              endingShape: 'rounded',
            }
        },
        dataLabels: {
            enabled: false
        },
        stroke: {
            show: true,
            width: 2,
            colors: ['transparent']
        },
        xaxis: {
          type: 'datetime'
        },
        yaxis: {
          tooltip: {
            enabled: false,
          }
        },
        tooltip: {
          enabled: true,
          x: {
            show: true,
            format: 'yyyy/MM/dd'
          },
          y: {
            show: true,
            title: {
              formatter: () => '成交量 = ', // 將 y 軸的標題命名為 "Volume"
            }
          },
          fixed: {
            enabled: true,
            position: 'top',
            offsetX: -150,
            offsetY: 0, // 在這裡設置頂部偏移量
          },
        },
        fill: {
            opacity: 1
        }
      }
    }
  }
}
</script>
