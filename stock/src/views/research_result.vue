<template>
  <div>
    <h4 class="text-2xl font-bold text-left py-2" style="color:#1B3C73;text-align:left;margin-left:2%">策略研究</h4>
    <h1
      style="margin-left:1%;color:#1B3C73;font-size:20px;font-weight:500;text-align: left;background-color: #e1ecf4;padding:15px;width:8%;border-radius: 10px;">
      Result</h1>
    <div class="container" style="margin-top: 3%">
      <div class="form-wrap">
        <form id="survey-form">
          <div class="row mt-8">
            <div class="col-md-12">
              <div class="empty-input-table">
                <table class="table">
                  <thead>
                    <tr>
                      <th>#</th>
                      <th>FinalBalance</th>
                      <th>CAGR</th>
                      <th>TWRR</th>
                      <th>MWRR</th>
                      <th>Stdev</th>
                      <th>BestYear</th>
                      <th>WorstYear</th>
                      <th>Max.Drawdown</th>
                      <th>SharpeRatio</th>
                      <th>SortioRatio</th>
                      <th>Benchmark</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr v-for="(portfolio, index) in seriesData.ReturnData" :key="index">
                      <td>{{ index + 1 }}</td>
                      <td>{{ portfolio.FinalBalance }}</td>
                      <td>{{ portfolio.CAGR }}</td>
                      <td>{{ portfolio.TWRR }}</td>
                      <td>{{ portfolio.MIRR }}</td>
                      <td>{{ portfolio.Stdev }}</td>
                      <td>{{ portfolio.BestYear }}</td>
                      <td>{{ portfolio.WorstYear }}</td>
                      <td>{{ portfolio['Max.Drawdown'] }}</td>
                      <td>{{ portfolio.SharpeRatio }}</td>
                      <td>{{ portfolio.SortioRatio }}</td>
                      <td>{{ portfolio.Benchmark }}</td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
          </div>
        </form>
      </div>
    </div>
<h4>更多詳細資訊請點連結：<a href="https://vivid-armchair-d6c.notion.site/cc786cadb6eb4b21808cab401476e1dc?pvs=4" title="https://vivid-armchair-d6c.notion.site/cc786cadb6eb4b21808cab401476e1dc?pvs=4">點擊這裡！</a></h4>
  </div>

</template>

<script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script>
import axios from 'axios';
import {seriesData} from './data/buyandhold.js'
export default {
  components: {
  },
  data() {
    return {
      seriesData: seriesData,
    };
  },

  computed: {

  },
  mounted() {
  }
}
</script>
<style scoped>
body {
  margin: 0;
  font-size: 1rem;
  font-weight: 400;
  line-height: 1.5;
  color: #fff;
  text-align: left;
  background-color: #fff;
}

h4 {
  font-size: 20px;
}

h2 {
  font-size: 28px
}

.form-group {
  margin-top: 3%
}

table {
  width: 100%;
  border-collapse: collapse;
}

th,
td {
  border: 1px solid #dddddd;
  padding: 8px;
  text-align: left;
}

th {
  background-color: #f2f2f2;
}
</style>
