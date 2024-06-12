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
    <div class="container" style="text-align: left;">
      <h4 style="color:#1B3C73;font-size:20px;font-weight:500;text-align:left">說明：</h4>
      <p>FinalBalance：最終餘額</p>
      <h2>CAGR</h2>
      <p>CAGR (Compound Annual Growth Rate)
        是一個用來衡量某項投資或業務在特定期間內平均每年的增長率的指標。它考慮了初始值和最終值之間的增長，而忽略了期間內的波動。這個指標特別適合用來比較不同投資的長期表現。CAGR 的公式如下：</p>
      <div id="formula-container">
        CAGR公式如下：
        <p>其中</p>
        <p>
          <strong>EV</strong> 代表最終價值（Ending Value）
          <br />
          <strong>BV</strong> 代表初始價值（Beginning Value）
          <br />
          <strong>n</strong> 代表期間的年數（Number of years）
        </p>
        <p>
          舉例來說，如果一項投資的初始價值是 1000 美元，五年後的最終價值是 2000 美元，那麼這項投資在這五年中的 CAGR 可以這樣計算：
        </p>
        <mathjax>
          \[\text{CAGR} = \left( \frac{2000}{1000} \right)^{\frac{1}{5}} - 1 = (2)^{\frac{1}{5}} - 1 \approx 0.1487\]
        </mathjax>
        <p>
          這意味著這項投資在五年期間內每年的平均增長率約為 14.87%。
        </p>
        <p>
          CAGR 的優點在於它能提供一個簡單明瞭的數字來反映長期的增長趨勢，使得不同的投資和業務表現之間更容易比較。然而，CAGR 也有其局限性，因為它忽略了期間內的波動，無法反映出每年的具體變化情況。
        </p>

        <h2>TWRR</h2>
        <p>
          TWRR (Time-Weighted Rate of Return)
          是一種用來衡量投資績效的指標，特別適合用來比較不同投資經理的績效，因為它消除了現金流入和流出對投資回報率的影響。這種方法強調的是投資本身的表現，而非投資者的資金投入或取出時間點。
        </p>
        <p>
          TWRR 的計算過程如下：
        </p>
        <ol>
          <li>
            <strong>分段回報計算</strong>：
            將整個投資期間分成若干段，每段期間因現金流動而分隔開來。計算每段期間的回報率。
            <br />
            假設投資在時間段 \( t_1, t_2, t_3, \ldots, t_n \) 發生了現金流動，每段期間的回報率為 \( r_1, r_2, r_3, \ldots, r_n \)。
          </li>
          <li>
            <strong>累積乘積</strong>：
            將每段期間的回報率進行累積乘積，得到總回報率。
            $TWRR = \left( (1 + r_1) \times (1 + r_2) \times \ldots \times (1 + r_n) \right) - 1 $
          </li>
        </ol>
      </div>
      <p>
        舉例說明：
      </p>
      <p>
        假設一位投資者在一段時間內進行了以下投資活動：
      </p>
      <ul>
        <li><strong>初始投資</strong>：$1000</li>
        <li><strong>期中現金流入</strong>：</li>
        <ul>
          <li>第一年末：額外投入 $500</li>
          <li>第二年末：額外投入 $300</li>
        </ul>
        <li><strong>期末總價值</strong>：$2500</li>
      </ul>
      <p>
        假設每段期間的回報率如下：
      </p>
      <ul>
        <li>第一年回報率 \( r_1 = 10\% \)（從 $1000 增加到 $1100）</li>
        <li>第二年回報率 \( r_2 = 5\% \)（從 $1600 增加到 $1680，考慮到第一年末投入 $500）</li>
        <li>第三年回報率 \( r_3 = 7\% \)（從 $1980 增加到 $2500，考慮到第二年末投入 $300）</li>
      </ul>
      <p>
        TWRR 的計算：
      </p>
      <div v-html="twrrFormula"></div>
      <p>
        所以，這段投資期間的 TWRR 約為 23.49%。
      </p>
      <p>
        TWRR 的優點在於，它能夠公平地反映出投資本身的績效，而不受投資者的資金流動影響，因此非常適合用來比較不同的投資策略和管理人的績效。
      </p>
      <div>
        <h2>MWRR</h2>
        <p>
          MWRR（Money-Weighted Rate of Return），也稱為 IRR（Internal Rate of
          Return），是一種考慮投資期間現金流動的投資回報率計算方法。它反映了投資者實際獲得的回報，因為它考慮了投資期間內的所有現金流入和流出。MWRR 適合用來衡量投資者實際的投資績效。
        </p>
        <p>
          MWRR 的計算方法是找出使得現金流現值為零的折現率。公式如下：
        </p>
        <div v-html="mwrrFormula"></div>
        <p>
          其中：
        </p>
        <ul>
          <li>𝐶<sub>𝑡</sub> 是第 𝑡 期的現金流（流入為正，流出為負）</li>
          <li>𝑟 是 MWRR（需要計算的回報率）</li>
          <li>𝑡 是時間（以年為單位）</li>
          <li>𝑛 是最後一個現金流的時間點</li>
        </ul>
        <p>
          舉例說明：
        </p>
        <ul>
          <li><strong>初始投資</strong>：$1000（現金流 *C*<sub>0</sub> = -1000）</li>
          <li><strong>第一年末</strong>：追加投入 $500（現金流 *C*<sub>1</sub> = -500）</li>
          <li><strong>第二年末</strong>：追加投入 $300（現金流 *C*<sub>2</sub> = -300）</li>
          <li><strong>第三年末</strong>：期末總值 $2500（現金流 *C*<sub>3</sub> = 2500）</li>
        </ul>
        <p>
          我們需要找出 <span class="formula">r</span> 使得以下方程成立：
          <span class="formula">−1000×(1+r)^0−500×(1+r)^1−300×(1+r)^2+2500×(1+r)^3=0</span>
        </p>
        <p>
          這是一個複雜的非線性方程，通常需要使用數值方法（如牛頓-拉夫森法）來求解。
        </p>
        <p>
          MWRR 的優點在於它能夠真實地反映投資者的實際回報，考慮了所有現金流的影響。然而，與 TWRR 不同的是，MWRR
          會受到現金流時機的影響，因此不適合作為比較不同投資經理績效的標準，但非常適合用來評估個人投資者的整體投資績效。
        </p>

        <h2>Stdev（標準差）</h2>
        <p>
          在投資策略的評估中，標準差（Standard Deviation，簡寫為 Stdev）是一個重要的指標，用於衡量投資回報的波動性和風險。以下是標準差在投資策略評估中的幾個應用：
        </p>
        <ul>
          <li>
            <strong>風險評估：</strong> 標準差用來衡量投資回報的變異性。較高的標準差表示回報波動較大，風險較高；較低的標準差表示回報較穩定，風險較低。
          </li>
          <li>
            <strong>例子：</strong> 假設有兩個投資策略A和B，在相同的期間內，它們的平均年回報率都是10%。策略A的回報標準差是5%，而策略B的回報標準差是15%。這意味著策略B的回報波動更大，風險更高。
          </li>
        </ul>

        <h2>BestYear（最佳年度回報率）</h2>
        <p>
          在投資策略評估中，“Best Year”指的是投資策略在特定期間內所獲得的最高年度回報率。這個指標有助於了解投資策略在最佳情況下的表現，並可以用來吸引投資者。然而，雖然“Best
          Year”是一個有用的指標，但它應該與其他指標一起使用來全面評估投資策略的績效和風險。
        </p>
        <p>
          <strong>如何使用 “Best Year” 進行投資策略評估</strong>
        </p>
        <h2>Best Year 的應用</h2>
        <h4>1. 瞭解策略的潛力</h4>
        <p>
          “Best Year” 可以幫助投資者瞭解投資策略在理想市場條件下的潛力。這有助於設置期望值，特別是對於風險承受能力較高的投資者而言。
        </p>

        <h4>2. 比較不同策略</h4>
        <p>
          在比較多個投資策略時，最佳年度回報率可以提供一個直觀的標準。投資者可以根據每個策略的最佳年度回報來篩選出表現最優異的策略。
        </p>

        <h2>具體應用</h2>
        <p>
          假設有三個投資策略，它們在過去五年中的最佳年度回報如下：
        </p>
        <ul>
          <li>策略A：30%</li>
          <li>策略B：25%</li>
          <li>策略C：35%</li>
        </ul>
        <p>
          從這些數據可以看出，策略C 在某一年中達到了最高的回報率，這可能表明它在特定市場條件下具有較高的增長潛力。
        </p>

        <h2>實際操作建議</h2>
        <h4>1. 與其他指標結合</h4>
        <p>
          單獨依靠“Best Year”來做出投資決策是有風險的。投資者應該將這個指標與其他指標（如標準差、夏普比率、最大回撤等）結合使用，以全面評估策略的風險和回報。
        </p>
        <h4>2. 長期表現考量</h4>
        <p>
          投資者應該考慮策略的長期表現，而不僅僅是單一年份的最佳表現。長期穩定的策略通常比僅在某一年表現突出的策略更值得信賴。
        </p>
        <h2>風險容忍度</h2>
        <p>
          在選擇投資策略時，應根據自己的風險容忍度來考慮“Best Year”指標。如果投資者能夠承受較高風險，那麼選擇過去有較高最佳年度回報的策略可能是合適的。
        </p>

        <h2>總結</h2>
        <p>
          “Best Year” 是投資策略評估中的一個有用指標，但應與其他風險和回報指標結合使用。它能幫助投資者瞭解策略的潛力，並在比較多個策略時提供參考。但單獨依賴這個指標是不夠的，全面的評估需要考慮策略的總體表現和風險特徵。
        </p>

        <h2>worst year</h2>
        <p>
          在投資策略的評估中，“Worst Year”指的是投資策略在特定期間內所遭遇的最差年度回報率。這個指標對於理解投資策略在不利市場條件下的表現至關重要，能夠幫助投資者評估策略的風險和最大回撤情況。
        </p>

        <h2>如何使用 “Worst Year” 進行投資策略評估</h2>
        <h4>1. 風險評估</h4>
        <p>
          “Worst Year” 提供了關於投資策略在極端不利條件下可能遭遇的最大損失的直觀認識。這有助於投資者了解在最壞情況下可能面臨的風險。
        </p>
        <h4>2. 投資者心理準備</h4>
        <p>
          通過了解“Worst Year”，投資者可以做好心理準備，避免在市場低迷時期因恐慌而做出不理性的投資決策。
        </p>
        <h4>3.策略穩定性比較</h4>
        <p>
          比較不同投資策略的最差年度回報，可以幫助投資者選擇更穩定、抗跌能力更強的策略。
        </p>

        <h2>具體應用</h2>
        <p>
          假設有三個投資策略，它們在過去五年中的最差年度回報如下：
        <ul>
          <li>策略A：-10%</li>
          <li>策略B：-15%</li>
          <li>策略C：-5%</li>
        </ul>
        從這些數據可以看出，策略C在最壞的一年中損失最小，這可能表明它在不利市場條件下的表現更穩定，風險較低。
        </p>

        <h2>實際操作建議</h2>
        <h4>1. 與其他指標結合</h4>
        <p>
          像“Best Year”一樣，單獨依賴“Worst Year”來做出投資決策是不夠的。應該將這個指標與其他風險和回報指標（如標準差、夏普比率、最大回撤等）結合使用，以全面評估策略的風險和回報。
        </p>
        <h4>2. 長期表現考量</h4>
        <p>
          考慮策略的長期表現，而不僅僅是單一年份的最差表現。長期穩定且抗跌能力強的策略通常更可靠。
        </p>
        <h4>3. 風險容忍度</h4>
        <p>
          根據自己的風險容忍度來考慮“Worst Year”指標。如果投資者風險承受能力較低，應該選擇在最差年份中回報相對較好的策略。
        </p>
        <h4>4. 市場條件分析</h4>
        <p>
          分析“Worst Year”發生的市場條件，有助於理解投資策略在特定市場環境下的表現。這可以幫助投資者在未來類似市場情況下做出更明智的決策。
        </p>
        <h4>總結</h4>
        <p>“Worst Year”
          是投資策略評估中的關鍵指標，能夠幫助投資者理解在最不利情況下策略的表現。它提供了關於策略風險的寶貴信息，有助於投資者在選擇和比較投資策略時做出更明智的決定。然而，與其他指標結合使用，才能全面評估策略的整體表現和風險特徵。
        </p>
        <h2>Max.Drawdown</h2>
        <p>最大回撤（Max Drawdown）是一個關鍵的風險指標，用於衡量投資策略或投資組合在特定期間內從峰值到谷值的最大跌幅。它反映了投資者在最壞情況下可能遭受的最大損失，對於風險管理和投資策略評估具有重要意義。</p>
        <h2>最大回撤的計算方法</h2>
        <p>最大回撤的計算包括以下步驟：</p>
        <ul>
          <li>識別峰值：找到投資期間內的最高點。</li>
          <li>識別谷值：找到從該峰值開始的最低點。</li>
          <li>計算回撤值：計算從峰值到谷值的百分比下降。</li>
        </ul>
        <p>公式如下：</p>
        <p>$\text{Max Drawdown} = \frac{\text{Peak Value} - \text{Trough Value}}{\text{Peak Value}}$</p>
        <h2>具體應用</h2>
        <p>假設某投資策略在一段時間內的資產價值如下（按月）：</p>
        <table>
          <thead>
            <tr>
              <th>月份</th>
              <th>資產價值（美元）</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(value, month) in assetData" :key="month">
              <td>{{ month }}</td>
              <td>{{ value }}</td>
            </tr>
          </tbody>
        </table>
        <p>
        <ol>
          <li><strong>識別峰值和谷值</strong>：
            <ul>
              <li>第一個峰值出現在第二個月（1200美元）。</li>
              <li>對應的谷值出現在第四個月（900美元）。</li>
            </ul>
          </li>
          <li><strong>計算回撤值</strong>：
            <span v-html="`Max Drawdown = \\frac{1200 - 900}{1200} = \\frac{300}{1200} = 0.25 = 25%`"></span>
            <br>在這個例子中，最大回撤是25%。
          </li>
        </ol>
        </p>

        <!-- 最大回撤在投資策略評估中的應用 -->
        <h3>最大回撤在投資策略評估中的應用</h3>
        <ol>
          <li><strong>風險管理</strong>：<br>
            最大回撤是風險管理中重要的指標。了解策略的最大回撤可以幫助投資者預測在極端市場情況下可能遭受的最大損失，從而更好地控制風險。
          </li>
          <li><strong>投資者心理準備</strong>：<br>
            通過了解最大回撤，投資者可以對潛在的最壞情況有心理準備，減少在市場下跌時的恐慌，從而保持理性決策。
          </li>
          <li><strong>策略穩定性比較</strong>：<br>
            最大回撤可以用來比較不同投資策略的穩定性。回撤較小的策略通常更穩定、風險較低，適合風險承受能力較低的投資者。
          </li>
          <li><strong>配置與調整</strong>：<br>
            在進行資產配置和調整時，最大回撤提供了重要參考。投資者可以根據最大回撤數據調整投資組合，以達到最佳風險回報平衡。
          </li>
        </ol>

        <!-- 與其他指標的結合 -->
        <h3>與其他指標的結合</h3>
        <ol>
          <li><strong>夏普比率（Sharpe Ratio）</strong>：<br>
            將最大回撤與夏普比率結合使用，可以更全面地評估策略的風險和回報。高夏普比率和低最大回撤的策略通常表現更好。
          </li>
          <li><strong>標準差（Standard Deviation）</strong>：<br>
            標準差衡量投資回報的波動性，與最大回撤結合使用，可以更全面地了解策略的風險特徵。
          </li>
          <li><strong>最差年份回報（Worst Year Return）</strong>：<br>
            最差年份回報和最大回撤都能提供策略在不利市場條件下的表現信息，二者結合可以提供更全面的風險評估。
          </li>
        </ol>

        <h3>總結</h3>


        <p>最大回撤是評估投資策略風險的重要指標，提供了關於投資策略在最不利市場情況下可能遭受的最大損失的信息。通過與其他指標結合使用，投資者可以更全面地了解策略的風險和回報特徵，從而做出更明智的投資決策。</p>

        <!-- SharpeRatio -->
        <h3>Sharpe Ratio</h3>
        <p>
          夏普比率（Sharpe Ratio）是一個衡量投資組合或投資策略風險調整後回報的指標，由諾貝爾經濟學獎得主威廉·夏普（William F. Sharpe）提出。它幫助投資者了解每單位風險所獲得的超額回報。
        </p>

        <h4>夏普比率的計算公式</h4>
        <p>
          $\text{Sharpe Ratio} = \frac{R_p - R_f}{\sigma_p}$
          <br>其中：
        <ul>
          <li>$R_p$ 是投資組合的平均回報率</li>
          <li>$R_f$ 是無風險利率（通常使用國債收益率作為代表）</li>
          <li>$\sigma_p$ 是投資組合回報的標準差（即波動性）</li>
        </ul>
        </p>

        <h4>計算步驟</h4>
        <ol>
          <li><strong>計算投資組合的平均回報率 $R_p$</strong>：</li>
          <li><strong>確定無風險利率 $R_f$</strong>：</li>
          <li><strong>計算投資組合回報的標準差 $\sigma_p$</strong>：</li>
          <li><strong>計算夏普比率</strong>：</li>
        </ol>

        <h4>例子</h4>
        <p>
          假設某投資組合在過去五年的年回報率分別為10%、15%、5%、20%和10%。無風險利率為2%。
          <br>1. 計算平均回報率 $R_p$：<br>
          2. 計算回報的標準差 $\sigma_p$：<br>
          3. 計算夏普比率：<br>
        </p>

        <h4>夏普比率的意義</h4>
        <ul>
          <li><strong>高夏普比率</strong>：表示每單位風險獲得了較高的超額回報，策略更為理想。</li>
          <li><strong>低夏普比率</strong>：表示每單位風險獲得的超額回報較低，策略風險較大且回報不高。</li>
        </ul>

        <h4>夏普比率的應用</h4>
        <ol>
          <li><strong>比較不同投資策略</strong>：</li>
          <li><strong>選擇最佳投資組合</strong>：</li>
          <li><strong>風險管理</strong>：</li>
        </ol>

        <h3>總結</h3>

        <p>夏普比率是衡量投資策略風險調整後回報的重要指標，有助於投資者在考慮風險的情況下做出更明智的投資決策。通過與其他風險和回報指標結合使用，投資者可以全面評估投資策略的績效和風險特徵。</p>


        <!-- SortinoRatio -->
        <h3>Sortino Ratio</h3>
        <p>
          Sortino比率（Sortino Ratio）是一個衡量投資策略風險調整後回報的指標，類似於夏普比率，但更專注於下行風險。由於Sortino比率只考慮負向波動，因此在評估風險和回報時，它被認為比夏普比率更準確。
        </p>

        <h4>Sortino比率的計算公式</h4>
        <p>
          $\text{Sortino Ratio} = \frac{R_p - R_f}{\sigma_d}$
          <br>其中：
        <ul>
          <li>$R_p$ 是投資組合的平均回報率</li>
          <li>$R_f$ 是無風險利率</li>
          <li>$\sigma_d$ 是下行標準差，即只考慮負回報的標準差</li>
        </ul>
        </p>

        <h4>計算步驟</h4>
        <ol>
          <li><strong>計算投資組合的平均回報率 $R_p$</strong>：</li>
          <li><strong>確定無風險利率 $R_f$</strong>：</li>
          <li><strong>計算下行標準差 $\sigma_d$</strong>：</li>
          <li><strong>計算Sortino比率</strong>：</li>
        </ol>

        <h4>例子</h4>
        <p>
          假設某投資組合在過去五年的年回報率分別為10%、15%、5%、20%和10%。無風險利率為2%。
          <br>1. 計算平均回報率 $R_p$：<br>
          2. 計算下行標準差 $\sigma_d$：<br>
          3. 計算Sortino比率：<br>
        </p>

        <h4>Sortino比率的意義</h4>
        <ul>
          <li><strong>高Sortino比率</strong>：表示每單位下行風險獲得的超額回報較高，策略較優。</li>
          <li><strong>低Sortino比率</strong>：表示每單位下行風險獲得的超額回報較低，策略風險較大且回報不高。</li>
        </ul>

        <h4>Sortino比率的應用</h4>
        <ol>
          <li><strong>比較不同投資策略</strong>：</li>
          <li><strong>選擇最佳投資組合</strong>：</li>
          <li><strong>風險管理</strong>：</li>
        </ol>

        <h3>總結</h3>
        <p>
          Sortino比率是衡量投資策略風險調整後回報的重要指標，專注於下行風險。它提供了一個更準確的風險調整後回報衡量方式，特別是對於那些關注下行風險的投資者。通過與其他風險和回報指標結合使用，投資者可以全面評估投資策略的績效和風險特徵。
        </p>
      </div>
    </div>
  </div>

</template>

<script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<script>
import axios from 'axios';
import {seriesData} from './data/buyandhold.js'
export default {
  components: {
  },
  data() {
    return {
      assetData: {
        1: 1000,
        2: 1200,
        3: 1150,
        4: 900,
        5: 950,
        6: 1100,
        7: 1050,
        8: 1000,
        9: 1200,
        10: 1150,
        11: 1300,
        12: 1250
      },
      seriesData: seriesData,
    };
  }, methods: {renderMath() {
      if (window.MathJax) {
        window.MathJax.typesetPromise();
      }
    },
    
  },
  computed: {

  },
  mounted() {
    this.renderMath();
  }
}</script>
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
