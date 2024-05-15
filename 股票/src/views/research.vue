<template>
  <div>
    <h3 class="text-2xl font-bold text-left py-2" style="color:#1B3C73;text-align:left;margin-left:2%">策略研究</h3>
    <h1
      style="margin-left:1%;color:#1B3C73;font-size:20px;font-weight:500;text-align: left;background-color: #e1ecf4;padding:15px;width:16%;border-radius: 10px;">
      Buy and Hold</h1>
    <div class="container" style="margin-top:3%">
      <div class="form-wrap">
        <form id="survey-form">
          <div class="row">
            <div class="col-md-12">
              <div class="form-group">
                <div class="row">
                  <div class="col-3"><label id="email-label" for="email"><b-button variant="light"
                        v-b-popover.hover.top="'I am popover directive content!'" title="Popover Title"
                        style="color:#1B3C73;margin-right:12px">
                        *</b-button>Time Periods</label></div>
                  <div class="col"><select id="dropdown" name="role" class="form-control" required>
                      <option disabled selected value>Year-To-Year</option>
                      <option value="student">Year-To-Year</option>
                      <option value="job">Year/Month-To-Year/Month</option>
                    </select>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <div class="row">
            <div class="col-md-12">
              <div class="form-group">
                <div class="row">
                  <div class="col-3"><label id="email-label" for="email"><b-button variant="light"
                        v-b-popover.hover.top="'I am popover directive content!'" title="Popover Title"
                        style="color:#1B3C73;margin-right:12px">
                        *</b-button>Include YTD</label></div>
                  <div class="col"><select id="dropdown" name="role" class="form-control" required>
                      <option disabled selected value>Yes</option>
                      <option value="student">Yes</option>
                      <option value="job">No</option>
                    </select>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="row">
            <div class="col-md-12">
              <div class="form-group">
                <div class="row">
                  <div class="col-3"><label id="email-label" for="email"><b-button variant="light"
                        v-b-popover.hover.top="'I am popover directive content!'" title="Popover Title"
                        style="color:#1B3C73;margin-right:12px">
                        *</b-button>Initial Amount</label></div>
                  <div class="col"><input type="number" min="100" max="2000" step="1" value="100"
                      placeholder="Enter your initial amount" class="form-control" required>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="row">
            <div class="col-md-12">
              <div class="form-group">
                <div class="row">
                  <div class="col-3"><label id="email-label" for="email"><b-button variant="light"
                        v-b-popover.hover.top="'I am popover directive content!'" title="Popover Title"
                        style="color:#1B3C73;margin-right:12px">
                        *</b-button>CashFlows</label></div>
                  <div class="col"><select id="dropdown" name="role" class="form-control" required>
                      <option disabled selected value>Yes</option>
                      <option value="student">固定投入</option>
                      <option value="job">固定領出</option>
                      <option value="job">不投入也不領出</option>
                    </select>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="row">
            <div class="col-md-12">
              <div class="form-group">
                <div class="row">
                  <div class="col-3"><label id="email-label" for="email"><b-button variant="light"
                        v-b-popover.hover.top="'I am popover directive content!'" title="Popover Title"
                        style="color:#1B3C73;margin-right:12px">
                        *</b-button>Rebalancing</label></div>
                  <div class="col"><select id="dropdown" name="role" class="form-control" required>
                      <option disabled selected value>No</option>
                      <option value="student">Yes</option>
                      <option value="job">No</option>
                    </select>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="row">
            <div class="col-md-12">
              <div class="form-group">
                <div class="row">
                  <div class="col-3"><label id="email-label" for="email"><b-button variant="light"
                        v-b-popover.hover.top="'I am popover directive content!'" title="Popover Title"
                        style="color:#1B3C73;margin-right:12px">
                        *</b-button>Rebalancing</label></div>
                  <div class="col"><select id="dropdown" name="role" class="form-control" required>
                      <option disabled selected value>Yes</option>
                      <option value="student">Yes</option>
                      <option value="job">No</option>
                    </select>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="row">
            <div class="col-md-12">
              <div class="form-group">
                <div class="row">
                  <div class="col-3"><label id="email-label" for="email"><b-button variant="light"
                        v-b-popover.hover.top="'I am popover directive content!'" title="Popover Title"
                        style="color:#1B3C73;margin-right:12px">
                        *</b-button>Reinvest Dividends</label></div>
                  <div class="col"><select id="dropdown" name="role" class="form-control" required>
                      <option disabled selected value>No</option>
                      <option value="student">Yes</option>
                      <option value="job">No</option>
                    </select>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="row">
            <div class="col-md-12">
              <div class="form-group">
                <div class="row">
                  <div class="col-3"><label id="email-label" for="email"><b-button variant="light"
                        v-b-popover.hover.top="'I am popover directive content*'" title="Popover Title"
                        style="color:#1B3C73;margin-right:12px;">
                        *</b-button>Display Income</label></div>
                  <div class="col"><select id="dropdown" name="role" class="form-control" required>
                      <option disabled selected value>Yes</option>
                      <option value="student">Yes</option>
                      <option value="job">No</option>
                    </select>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="row">
            <div class="col-md-12">
              <div class="form-group">
                <div class="row">
                  <div class="col-3"><label id="email-label" for="email"><b-button variant="light"
                        v-b-popover.hover.top="'I am popover directive content!'" title="Popover Title"
                        style="color:#1B3C73;margin-right:12px">
                        *</b-button>Benchmark</label></div>
                  <div class="col"><select id="dropdown" name="role" class="form-control" required>
                      <option disabled selected value>Benchmark</option>
                      <option value="student">Yes</option>
                      <option value="job">No</option>
                    </select>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="row mt-8" style="margin-top:5%">
            <div class="col-md-12">
              <div class="empty-input-table">
                <table class="table">
                  <thead>
                    <tr>
                      <th>#</th>
                      <th>Stock ID</th>
                      <th>Percentage of Total Assets</th>
                      <th>Second Allocation</th>
                      <th>Third Allocation</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr v-for="index in 5" :key="index">
                      <td>{{ index }}</td>
                      <td>
                        <div class="input-group mb-2">
                          <div class="input-group-prepend">
                            <div class="input-group-text">i</div>
                          </div>
                          <input type="number" class="form-control" placeholder="股票代碼"
                            v-model="rowData[index - 1].name">
                        </div>
                      </td>
                      <td>
                        <div class="input-group mb-2">
                          <input type="number" class="form-control" placeholder="佔總資產比例" min="0" max="100">
                          <div class="input-group-prepend">
                            <div class="input-group-text">%</div>
                          </div>
                        </div>
                      </td>
                      <td>
                        <div class="input-group mb-2">
                          <input type="number" class="form-control" placeholder="第二配置" min="0" max="100">
                          <div class="input-group-prepend">
                            <div class="input-group-text">%</div>
                          </div>
                        </div>
                      </td>
                      <td>
                        <div class="input-group mb-2">
                          <input type="number" class="form-control" placeholder="第三配置" min="0" max="100">
                          <div class="input-group-prepend">
                            <div class="input-group-text">%</div>
                          </div>
                        </div>
                      </td>
                    </tr>
                    <tr>
                      <td>
                        <h1 style="font-size:18px;font-weight:500">Total</h1>
                      </td>
                      <td></td>
                      <td>
                        <div class="input-group mb-2">
                          <input type="number" class="form-control" placeholder="0" min="0" max="100" disabled>
                          <div class="input-group-prepend">
                            <div class="input-group-text">%</div>
                          </div>
                        </div>
                      </td>
                      <td>
                        <div class="input-group mb-2">
                          <input type="number" class="form-control" placeholder="0" min="0" max="100" disabled>
                          <div class="input-group-prepend">
                            <div class="input-group-text">%</div>
                          </div>
                        </div>
                      </td>
                      <td>
                        <div class="input-group mb-2">
                          <input type="number" class="form-control" placeholder="0" min="0" max="100" disabled>
                          <div class="input-group-prepend">
                            <div class="input-group-text">%</div>
                          </div>
                        </div>
                      </td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
          </div>
          <div class="row">
            <div class="col-md-12">
              <b-button style="width:130px;float:right;margin:12px" pile type="submit" id="submit"
                variant="outline-primary">Analyze</b-button>
              <b-button style="width:130px;float:right;margin:12px" pile type="clear" id="submit"
                variant="outline-secondary">Cancel</b-button>
            </div>
          </div>

        </form>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  data() {
    return {
      rowData: [
        { name: '', quantity: '' },
        { name: '', quantity: '' },
        { name: '', quantity: '' },
        { name: '', quantity: '' },
        { name: '', quantity: '' },
      ]
    };
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
.form-group{
  margin-top:3%
}
</style>