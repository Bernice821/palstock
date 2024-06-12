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
      <div id="formula-container">
      <p>其中:</p>
      <ul>
        <li>EV 代表最終價值（Ending Value）</li>
        <li>BV 代表初始價值（Beginning Value）</li>
        <li>n 代表期間的年數（Number of years）</li> 
      </ul>
      <p>舉例說明：</p>
      <p>如果一項投資的初始價值是 1000 美元，五年後的最終價值是 2000 美元，那麼這項投資在這五年中的 CAGR 可以這樣計算：</p>
      <p>$$ \text{CAGR} = \left( \frac{2000}{1000} \right)^{\frac{1}{5}} - 1 = (2)^{\frac{1}{5}} - 1 \approx 0.1487 $$</p>
      <p>這意味著這項投資在五年期間內每年的平均增長率約為 14.87%。</p>
      <p>CAGR 的優點在於它能提供一個簡單明瞭的數字來反映長期的增長趨勢，使得不同的投資和業務表現之間更容易比較。然而，CAGR 也有其局限性，因為它忽略了期間內的波動，無法反映出每年的具體變化情況。</p>
      <p style="font-weight:600">TWRR</p>
      <p>TWRR (Time-Weighted Rate of Return) 是一種用來衡量投資績效的指標，特別適合用來比較不同投資經理的績效，因為它消除了現金流入和流出對投資回報率的影響。這種方法強調的是投資本身的表現，而非投資者的資金投入或取出時間點。</p>
      <p>舉例說明：</p>
      <p>假設一位投資者在一段時間內進行了以下投資活動：</p>
      <ul>
        <li>初始投資：$1000</li>
        <li>
          期中現金流入：
          <ul>
          <li>第一年末：額外投入 $500</li>
          <li>第二年末：額外投入 $300</li>
          </ul>
        </li>
        <li>期末總價值：$2500</li>
      </ul>
      <p>假設每段期間的回報率如下：</p>
      <ul>
        <li>第一年回報率  r_1 = 10% （從 $1000 增加到 $1100）</li>
        <li>第二年回報率  r_2 = 5% （從 $1600 增加到 $1680，考慮到第一年末投入 $500）</li>
        <li>第三年回報率  r_3 = 7% （從 $1980 增加到 $2500，考慮到第二年末投入 $300</li>
      </ul>
      <p>TWRR 的計算：</p>
      <p>$$ TWRR = (1 + 0.10) \times (1 + 0.05) \times (1 + 0.07) - 1 $$</p>
      <p>$$ TWRR = 1.10 \times 1.05 \times 1.07 - 1 $$</p>
      <p>$$ TWRR \approx 1.23485 - 1 $$</p> 
      <p>$$ TWRR \approx 0.23485  $$</p>
      <p>這段投資期間的 TWRR 約為 23.49%</p>
      <p>TWRR 的優點在於，它能夠公平地反映出投資本身的績效，而不受投資者的資金流動影響，因此非常適合用來比較不同的投資策略和管理人的績效。</p>
    </div>
    </div>
  </div>
</template>

<script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

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
      Benchmark: 0,  // Fixed typo
      Portfolios: {},
      StockID: 0,
      part: [],
      rowData: Array.from({ length: 3 }, () => ({
        name: '',
        FinalBalance: 0,
        CAGR: 0,
        TWRR: 0,
        MWRR: 0,
        Stdev: 0,
        BestYear: 0,
        WorstYear: 0,
        MaxDrawdown: 0,
        SharpeRatio: 0,
        SortinoRatio: 0
      })),
    };
  },
  methods: {
    loadMathJax() {
      if (!window.MathJax) {
        const script = document.createElement('script');
        script.src = 'https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js';
        script.async = true;
        document.head.appendChild(script);
        script.onload = () => {
          this.renderMath();
        };
      } else {
        this.renderMath();
      }
    },
    renderMath() {
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
        this.IncludeYTD === 0 || this.initialAmount === 0 || this.CashFlows === "" || this.Rebalancing === "" || this.ReinvestDividends === 0 || this.DisplayIncome === "" || this.Benchmark === 0) {
        alert('未完成填寫！');
        return; // 不執行分析操作
      }
      try {
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
          Benchmark: this.Benchmark,
          Portfolios: this.Portfolios,
          StockID: this.StockID,
          part: this.part
        });
        if (response.data && response.data.StatusCode === 200) {
          this.rowData = response.data.ReturnData.map((item, index) => ({
            name: `Portfolio ${index + 1}`,
            FinalBalance: item.FinalBalance,
            CAGR: item.CAGR,
            TWRR: item.TWRR,
            MWRR: item.MWRR,
            Stdev: item.Stdev,
            BestYear: item.BestYear,
            WorstYear: item.WorstYear,
            MaxDrawdown: item.MaxDrawdown,
            SharpeRatio: item.SharpeRatio,
            SortinoRatio: item.SortinoRatio
          }));
        }
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    }
  },
  computed: {

  },
  mounted() {
    this.loadMathJax();
  },
  updated() {
    this.renderMath();
  }
}
</script>

<style>
body {
  margin: 0;
  font-size: 1rem;
  font-weight: 400;
  line-height: 1.5;
  color: #000;  /* Changed text color to black for better readability */
  text-align: left;
  background-color: #fff;
}

.form-group {
  margin-top: 3%;
}
</style>
