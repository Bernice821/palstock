<template>
    <div id="wrapper" style="margin-left: 15%;">
        <div id="stock">
            <apexchart type="candlestick" height="400" :options="chartOptions1" :series="series1"></apexchart>
        </div>
        <div id="analysis">
            <apexchart type="line" height="200" :options="chartOptions2" :series="series2" style="margin-top: 5%;">
            </apexchart>
        </div>

    </div>
</template>

<script>
import VueApexCharts from 'vue-apexcharts'
import { seriesData } from '../data/stockPrice.js'
import { k, d, j } from '../data/kdj.js'

export default {
    components: {
        apexchart: VueApexCharts
    },
    data() {
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
                    },
                    fixed: {
                        enabled: true,
                        position: 'top',
                        offsetX: -150,
                        offsetY: 150, // 在這裡設置頂部偏移量
                    },
                },
            },
            series2: [
                {
                    name: "K",
                    data: k
                },
                {
                    name: "D",
                    data: d
                },
                {
                    name: "J",
                    data: j
                },
            ],
            chartOptions2: {
                chart: {
                    group: 'stock',
                    id: 'analysis',
                    type: 'line',
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
                    curve: 'straight',
                    width: 2,
                    dashArray: [0, 0, 3]
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
                        // title: {
                        //     formatter: () => '成交量 = ', 
                        // }
                    },
                    fixed: {
                        enabled: true,
                        position: 'top',
                        offsetX: -150,
                        offsetY: 0, // 在這裡設置頂部偏移量
                    },
                },
                colors: ['#7ED7C1', '#F0DBAF', '#DC8686'],
            }
        }
    }
}
</script>
