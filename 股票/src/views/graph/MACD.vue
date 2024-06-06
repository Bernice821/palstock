<template>
    <div id="wrapper" style="margin-left: 15%;">
        <div id="stock">
            <apexchart type="candlestick" height="400" :options="chartOptions1" :series="series1"></apexchart>
        </div>
        <div id="analysis">
            <apexchart height="200" :options="chartOptions2" :series="series2" style="margin-top: 5%;">
            </apexchart>
        </div>

    </div>
</template>

<script>
import VueApexCharts from 'vue-apexcharts'
import { seriesData } from '../data/stockPrice.js'
import { var1, var2, var3 } from '../data/analysis.js'

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
                    tooltip: {
                        enabled: false
                    }
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
                        // format: 'yyyy/MM/dd',
                    },
                    y: {
                        show: true,
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
            },
            series2: [
                {
                    name: "DIF",
                    data: var1,
                    type: "line"
                },
                {
                    name: "MACD",
                    data: var2,
                    type: "line",
                    color: '#FEB019'
                    
                },
                {
                    name: "DIF_MACD",
                    data: var3,
                    type: 'column'
                },
            ],
            chartOptions2: {
                chart: {
                    group: 'stock',
                    id: 'analysis',
                },
                plotOptions: {
                    bar: {
                        horizontal: false,
                        columnWidth: '55%',
                        colors: {
                            ranges: [{
                                from: -999,
                                to: 0,
                                color: '#006030'
                            }, {
                                from: 0,
                                to: 999,
                                color: '#CE0000'
                            }]
                        },
                    }
                },
                dataLabels: {
                    enabled: false
                },
                stroke: {
                    curve: 'straight',
                    width: [2,2,0],
                },
                xaxis: {
                    type: 'datetime',
                    tooltip: {
                        enabled: false
                    }
                },
                yaxis: {
                    tooltip: {
                        enabled: false,
                    }
                },
                tooltip: {
                    enabled: true,
                    marker: {
                        fillColors: ['#008FFB', '#FEB019', '#CE0000']
                    },
                    x: {
                        show: true,
                        format: 'yyyy/MM/dd'
                    },
                    y: {
                        show: true,
                    },
                    fixed: {
                        enabled: true,
                        position: 'top',
                        offsetX: -125,
                        offsetY: 0, // 在這裡設置頂部偏移量
                    },
                },
                legend: {
                    markers: {
                        fillColors: ['#008FFB', '#FEB019', '#CE0000']
                    },
                }                
            }
        }
    }
}
</script>
