<template>
  <div id="chart" >
    <apexchart type="bar" height="350" :options="chartOptions2" :series="seriesㄉ"></apexchart>
  </div>
</template>

<script>
import VueApexCharts from 'vue-apexcharts'
// import { seriesData } from '../data/stockPrice.js'

export default {
  components: {
    apexchart: VueApexCharts
  },
  data () {
    return {
      series2: [{ 
        data: generateDayWiseTimeSeries(new Date('2024-02-01').getTime(), 60, { min: 6203,max: 100000})
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