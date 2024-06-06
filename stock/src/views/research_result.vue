<template>
  <div>
    <h3 class="text-2xl font-bold text-left py-2" style="color:#1B3C73;text-align:left;margin-left:2%">策略研究</h3>
    <h1
      style="margin-left:1%;color:#1B3C73;font-size:20px;font-weight:500;text-align: left;background-color: #e1ecf4;padding:15px;width:8%;border-radius: 10px;">
      Result</h1>
    <div class="container" style="margin-top:3%">
      <div class="form-wrap">
        <form id="survey-form">
          <div class="row mt-8" >
            <div class="col-md-12">
              <div class="empty-input-table">
                <table class="table">
                  <thead>
                    <tr>
                      <th>#</th>
                      <th>FinalBalance</th>
                      <th> CAGR</th>
                      <th>TWRR</th>
                      <th>MWRR</th>
                      <th>Stdev</th>
                      <th>BestYear</th>
                      <th>worst year</th>
                      <th>Max.Drawdown</th>
                      <th>SharpeRatio</th>
                      <th>SortioRatio</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr v-for="index in 3" :key="index">
                      <td>{{ index }}</td>
                      <td>
                        <div class="input-group mb-2">
                          <input type="number" class="form-control" placeholder=""
                            v-model="rowData[index - 1].name" disabled>
                        </div>
                      </td>
                      <td>
                        <div class="input-group mb-2">
                          
                          <input type="number" class="form-control" placeholder=""
                            v-model="rowData[index - 1].name" disabled>
                        </div>
                      </td>
                      <td>
                        <div class="input-group mb-2">
                          
                          <input type="number" class="form-control" placeholder=""
                            v-model="rowData[index - 1].name" disabled>
                        </div>
                      </td>
                      <td>
                        <div class="input-group mb-2">
                          
                          <input type="number" class="form-control" placeholder=""
                            v-model="rowData[index - 1].name" disabled>
                        </div>
                      </td>
                      <td>
                        <div class="input-group mb-2">
                          
                          <input type="number" class="form-control" placeholder=""
                            v-model="rowData[index - 1].name" disabled>
                        </div>
                      </td>
                      <td>
                        <div class="input-group mb-2">
                          
                          <input type="number" class="form-control" placeholder=""
                            v-model="rowData[index - 1].name" disabled>
                        </div>
                      </td>
                      <td>
                        <div class="input-group mb-2">
                          
                          <input type="number" class="form-control" placeholder=""
                            v-model="rowData[index - 1].name" disabled>
                        </div>
                      </td>
                      <td>
                        <div class="input-group mb-2">
                          
                          <input type="number" class="form-control" placeholder=""
                            v-model="rowData[index - 1].name" disabled>
                        </div>
                      </td>
                      <td>
                        <div class="input-group mb-2">
                          
                          <input type="number" class="form-control" placeholder=""
                            v-model="rowData[index - 1].name" disabled>
                        </div>
                      </td>
                      <td>
                        <div class="input-group mb-2">
                          <input type="number" class="form-control" placeholder=""
                            v-model="rowData[index - 1].name" disabled>
                        </div>
                      </td>

                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
          </div>

        </form>
      </div>
    </div>
    <div class="container" style="text-align: left;">
      <h3 style="color:#1B3C73;font-size:20px;font-weight:500;text-align:left">說明：</h3>
      <p>FinalBalance：最終餘額</p>
      <p style="font-weight:600">CAGR</p>
      <p>CAGR (Compound Annual Growth Rate) 是一個用來衡量某項投資或業務在特定期間內平均每年的增長率的指標。它考慮了初始值和最終值之間的增長，而忽略了期間內的波動。這個指標特別適合用來比較不同投資的長期表現。CAGR 的公式如下：</p>
      <div id="formula-container">
        這是CAGR公式：$$ \text{CAGR} = \left( \frac{EV}{BV} \right)^{\frac{1}{n}} - 1 $$
      </div>
    </div>
  </div>
</template>
<script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id="MathJax-script" async
  src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<script>
import axios from 'axios';
export default {
  data() {
    return {
      TimePeriods: "Year-To-Year",
      StartYear: 0,
      EndYear: 0,
      FirstMonth: 0,
      LastMonth: 0,
      IncludeYTD: 0,
      initialAmount: 0,
      CashFlows: "固定投入",
      ContributionAmount: "",
      ContributionFrequency: "",
      Rebalancing: "",
      ReinvestDividends: 0,
      DisplayIncome: 0,
      Benhmark: 0,
      Portfolios: {},
      StockID: 0,
      part: [],
      rowData: Array.from({ length: 5 }, () => ({
        name: '',
        allocation1: 0,
        allocation2: 0,
        allocation3: 0,
      })),
    };
  }, methods: {renderMath() {
      if (window.MathJax) {
        window.MathJax.typesetPromise();
      }
    },
    async analysis() {
      if (this.totalAllocation1 > 100 || this.totalAllocation2 > 100 || this.totalAllocation3 > 100) {
        alert('請勿超過100%!');
        return;
      }
      if (this.TimePeriods === "" || this.StartYear === 0 || this.EndYear === 0 || this.FirstMonth === 0 || this.LastMonth === 0 ||
        this.IncludeYTD===0 || this.initialAmount === 0 || this.CashFlows==="" || this.Rebalancing === ""|| this.ReinvestDividends === 0 || this.DisplayIncome === "" || this.Benchmark === 0) {
        alert('未完成填寫！');
        return; // 不執行分析操作
      }
      try {
        console.log(this.initialAmount)
        const response = await axios.post('http://127.0.0.1:12000/api/StrategyStock', {
          TimePeriods: this.TimePeriods,
          StartYear: this.StartYear,
          EndYear: this.EndYear,
          FirstMonth: this.FirstMonth,
          LastMonth: this.LastMonth,
          IncludeYTD: this.IncludeYTD,
          initialAmount: this.initialAmount,
          CashFlows: this.CashFlows,
          ContributionAmount: this.ContributionAmount,
          ContributionFrequency: this.ContributionFrequency,
          Rebalancing: this.Rebalancing,
          ReinvestDividends: this.ReinvestDividends,
          DisplayIncome: this.DisplayIncome,
          Benhmark: this.Benchmark,
          Portfolios: this.Portfolios,
          StockID: this.StockID,
          part: this.part
        });
        const data = response.data;
      } catch (error) {
        console.error('Error fetching index:', error);
      }
    },
  },
  computed: {

  },
  mounted() {
    this.renderMath();
  }
}</script>
<style>
body {
  margin: 0;
  font-size: 1rem;
  font-weight: 400;
  line-height: 1.5;
  color: #fff;
  text-align: left;
  background-color: #fff;
}

.form-group {
  margin-top: 3%
}
</style>