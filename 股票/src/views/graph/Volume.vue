<template>
  <div id="chart" >
    <apexchart type="bar" height="350" :options="chartOptions2" :series="series2"></apexchart>
  </div>
</template>

<script>
import VueApexCharts from 'vue-apexcharts'
import { VolData } from '../data/volume.js'

export default {
  components: {
    apexchart: VueApexCharts
  },
  data () {
    return {
      series2: [{ 
        name: '成交量',
        data: VolData
      }],
      chartOptions2: {
        chart: {
          group: 'stock',
          id: 'volume',
          type: 'bar',
          height: 350
        },
        plotOptions: {
            bar: {
            horizontal: false,
            columnWidth: '55%',
            endingShape: 'rounded'
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
            enabled: true
          }
        },
        fill: {
            opacity: 1
        }
      }
    }
  }
}
</script>