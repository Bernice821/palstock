<template>
  <div style="margin-left:3%;">
    <h4 class="text-2xl font-bold py-2" style="color:#1B3C73;text-align:left;font-size: 30px">首頁</h4>
    <div>
      <b-tabs content-class="mt-3">
        <b-tab title="台股">
          <h3 class="text-xl font-bold text-left py-2" style="color:#1B3C73">近期熱銷</h3>
          <div class="row">
            <div v-for="(stock, index) in stocks" :key="index" class="col">
              <div class="card1" :style="{ color: '#1B3C73', textAlign: 'left', fontSize: '18px', fontWeight: '600' }">
                {{ stock.name }}
                <h3 class="text-3xl font-bold text-left py-2" :style="{ color: '#40A578' }">{{ stock.change }}</h3>
                <div>
                  <apexchart :width="270" type="area" :options="getChartOptions(stock)"
                    :series="[{ name: stock.name, data: stock.StocksChart }]"></apexchart>
                </div>
              </div>
            </div>
          </div>
          <h3 class="text-xl font-bold text-left pt-8" style="color:#1B3C73;margin-top:3%;margin-bottom:3%">所有策略</h3>
          <div class="row">
            <div id="right_panel">
              <div class="wrap-table">
                <table>
                  <thead>
                    <tr>
                      <th scope="col"></th>
                      <th scope="col">年化報酬</th>
                      <th scope="col">最大虧損</th>
                      <th scope="col">夏普值</th>
                      <th scope="col">大盤比較</th>
                      <th scope="col">近期報酬</th>
                      <th scope="col">重要日期</th>
                      <th scope="col" class="sticky-col sticky-col-right">Actions</th>
                    </tr>
                  </thead>

                  <tbody>
                    <tr>
                      <td>
                        <div class="user__info">
                          <p style="font-size:16px;padding-top:2%;padding-left:10%;text-align:center;font-weight:500;">
                            合約負債建築工VIP</p>
                        </div>
                      </td>
                      <td data-label="Status">
                        <div class="user__badge user__badge_unpaid">+36.2%</div>
                      </td>
                      <td data-label="Status">
                        <div class="user__badge">-31.1%</div>
                      </td>
                      <td data-label="Status">
                        <div class="user__badge_1">1.8</div>
                      </td>
                      <td data-label="Course">
                        <div>
                          <div class="user__name">週 月 季</div>
                          <div class="user__email" style="color:red">勝 勝 勝</div>
                        </div>
                      </td>
                      <td data-label="Enrolled">
                        <div>
                          <div class="user__name">月 +19.1%</div>
                          <div class="user__email">季 +19.1%</div>
                        </div>
                      </td>
                      <td data-label="Date">
                        <div>
                          <div class="user__name">近期換股：2024-06-30</div>
                          <div class="user__email">策略更新：2024-04-18</div>
                        </div>
                      </td>
                      <td data-label="Actions" class="sticky-col sticky-col-right">
                        <a href="#" class="user__edit">Edit</a>
                      </td>
                    </tr>
                    <tr>
                      <td>
                        <div class="user__info">
                          <p style="font-size:16px;padding-top:2%;padding-left:10%;text-align:center;font-weight:500;">
                            合約負債建築工VIP</p>
                        </div>
                      </td>
                      <td data-label="Status">
                        <div class="user__badge user__badge_unpaid">+36.2%</div>
                      </td>
                      <td data-label="Status">
                        <div class="user__badge">-31.1%</div>
                      </td>
                      <td data-label="Status">
                        <div class="user__badge_1">1.8</div>
                      </td>
                      <td data-label="Course">
                        <div>
                          <div class="user__name">週 月 季</div>
                          <div class="user__email" style="color:red">勝 勝 勝</div>
                        </div>
                      </td>
                      <td data-label="Enrolled">
                        <div>
                          <div class="user__name">月 +19.1%</div>
                          <div class="user__email">季 +19.1%</div>
                        </div>
                      </td>
                      <td data-label="Date">
                        <div>
                          <div class="user__name">近期換股：2024-06-30</div>
                          <div class="user__email">策略更新：2024-04-18</div>
                        </div>
                      </td>
                      <td data-label="Actions" class="sticky-col sticky-col-right">
                        <a href="#" class="user__edit">Edit</a>
                      </td>
                    </tr>
                    <tr>
                      <td>
                        <div class="user__info">
                          <p style="font-size:16px;padding-top:2%;padding-left:10%;text-align:center;font-weight:500;">
                            合約負債建築工VIP</p>
                        </div>
                      </td>
                      <td data-label="Status">
                        <div class="user__badge user__badge_unpaid">+36.2%</div>
                      </td>
                      <td data-label="Status">
                        <div class="user__badge">-31.1%</div>
                      </td>
                      <td data-label="Status">
                        <div class="user__badge_1">1.8</div>
                      </td>
                      <td data-label="Course">
                        <div>
                          <div class="user__name">週 月 季</div>
                          <div class="user__email" style="color:red">勝 勝 勝</div>
                        </div>
                      </td>
                      <td data-label="Enrolled">
                        <div>
                          <div class="user__name">月 +19.1%</div>
                          <div class="user__email">季 +19.1%</div>
                        </div>
                      </td>
                      <td data-label="Date">
                        <div>
                          <div class="user__name">近期換股：2024-06-30</div>
                          <div class="user__email">策略更新：2024-04-18</div>
                        </div>
                      </td>
                      <td data-label="Actions" class="sticky-col sticky-col-right">
                        <a href="#" class="user__edit">Edit</a>
                      </td>
                    </tr>
                    <tr>
                      <td>
                        <div class="user__info">
                          <p style="font-size:16px;padding-top:2%;padding-left:10%;text-align:center;font-weight:500;">
                            合約負債建築工VIP</p>
                        </div>
                      </td>
                      <td data-label="Status">
                        <div class="user__badge user__badge_unpaid">+36.2%</div>
                      </td>
                      <td data-label="Status">
                        <div class="user__badge">-31.1%</div>
                      </td>
                      <td data-label="Status">
                        <div class="user__badge_1">1.8</div>
                      </td>
                      <td data-label="Course">
                        <div>
                          <div class="user__name">週 月 季</div>
                          <div class="user__email" style="color:red">勝 勝 勝</div>
                        </div>
                      </td>
                      <td data-label="Enrolled">
                        <div>
                          <div class="user__name">月 +19.1%</div>
                          <div class="user__email">季 +19.1%</div>
                        </div>
                      </td>
                      <td data-label="Date">
                        <div>
                          <div class="user__name">近期換股：2024-06-30</div>
                          <div class="user__email">策略更新：2024-04-18</div>
                        </div>
                      </td>
                      <td data-label="Actions" class="sticky-col sticky-col-right">
                        <a href="#" class="user__edit">Edit</a>
                      </td>
                    </tr>
                    <tr>
                      <td>
                        <div class="user__info">
                          <p style="font-size:16px;padding-top:2%;padding-left:10%;text-align:center;font-weight:500;">
                            合約負債建築工VIP</p>
                        </div>
                      </td>
                      <td data-label="Status">
                        <div class="user__badge user__badge_unpaid">+36.2%</div>
                      </td>
                      <td data-label="Status">
                        <div class="user__badge">-31.1%</div>
                      </td>
                      <td data-label="Status">
                        <div class="user__badge_1">1.8</div>
                      </td>
                      <td data-label="Course">
                        <div>
                          <div class="user__name">週 月 季</div>
                          <div class="user__email" style="color:red">勝 勝 勝</div>
                        </div>
                      </td>
                      <td data-label="Enrolled">
                        <div>
                          <div class="user__name">月 +19.1%</div>
                          <div class="user__email">季 +19.1%</div>
                        </div>
                      </td>
                      <td data-label="Date">
                        <div>
                          <div class="user__name">近期換股：2024-06-30</div>
                          <div class="user__email">策略更新：2024-04-18</div>
                        </div>
                      </td>
                      <td data-label="Actions" class="sticky-col sticky-col-right">
                        <a href="#" class="user__edit">Edit</a>
                      </td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
          </div>
          <h3 class="text-xl font-bold text-left pt-6" style="color:#1B3C73">股票新聞</h3>
          <div>
            <div class="row" style="padding-left:3%;">
              <div v-for="(newsItem, index) in news" :key="index" class="col-3" style="margin-right:7%">
                <div class="blog">
                  <div class="container1" style="width:500px">
                    <div class="row" style="width:95%;">
                      <div class="col-md-4 col-lg-9">
                        <div class="item">
                          <div class="img">
                            <img :src="newsItem.ImgUrl" alt="">
                          </div>
                          <div class="info">
                            <div class="date">
                              <span>{{ formatDate(newsItem.Time) }} <br> {{ formatMonth(newsItem.Time) }}</span>
                            </div>
                            <a :href="newsItem.Url">
                              <h5 style="color:#0C2D57;font-weight: 500;font-size: 20px;margin-bottom:12px">
                                {{ newsItem.Title}}
                              </h5>
                            </a>
                            <p>{{ newsItem.summary }}</p>
                            <a :href="newsItem.Url" class="more">
                              <svg viewBox="0 0 10 10" fill="currentColor" strokeWidth="2" class="w-6 h-5">
                                <path fill-rule="evenodd"
                                  d="M12.293 5.293a1 1 0 011.414 0l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-2.293-2.293a1 1 0 010-1.414z"
                                  clip-rule="evenodd"></path>
                              </svg>
                            </a>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </b-tab>
        <b-tab title="美股">
          <h3 class="text-xl font-bold text-left py-2" style="color:#1B3C73">近期熱銷</h3>
          <div class="row">
            <div class="col">
              <div class="card1" style="color:#1B3C73;text-align: left;font-size: 18px;font-weight: 600;">小資族首選-0050
                <h3 class="text-3xl font-bold text-left py-2" style="color:#D24545">+0.57%</h3>
                <div>
                  <apexchart width="270" type="area" :options="chartOptions" :series="chartSeries"></apexchart>
                </div>
              </div>
            </div>
            <div class="col">
              <div class="card1" style="color:#1B3C73;text-align: left;font-size: 18px;font-weight: 600;">小蝦米跟大鯨魚
                <h3 class="text-3xl font-bold text-left py-2" style="color:#D24545">+0.17%</h3>
                <div>
                  <apexchart width="270" type="area" :options="chartOptions1" :series="chartSeries1"></apexchart>
                </div>
              </div>
            </div>
            <div class="col">
              <div class="card1" style="color:#1B3C73;text-align: left;font-size: 18px;font-weight: 600;">小資族首選
                <h3 class="text-3xl font-bold text-left py-2" style="color:#D24545">+9.32%</h3>
                <div>
                  <apexchart width="270" type="area" :options="chartOptions2" :series="chartSeries2"></apexchart>
                </div>
              </div>
            </div>
          </div>
          <h3 class="text-xl font-bold text-left pt-8" style="color:#1B3C73">所有策略</h3>
          <div style="float:left;padding-top: 8px; width:100%; padding-right: 20%">
            <div class="row" style="padding-top:2%;float: left;width:100%;padding-right: 40%;">
              <div class="col">
                <p style="font-size: 17px;color:black;font-weight: 400;padding-top: 6px; text-align: left">類別：</p>
              </div>
              <div class="col"><b-button pill variant="outline-secondary" style="width:80px">全部</b-button></div>
              <div class="col"><b-button pill variant="outline-secondary" style="width:80px">台股</b-button></div>
              <div class="col"><b-button pill variant="outline-secondary" style="width:80px">ETF</b-button></div>
              <div class="col"><b-button pill variant="outline-secondary" style="width:80px">低波動</b-button></div>
            </div>
            <div class="row" style="padding-top:2%;float: left;width:100%;padding-right: 40%;padding-bottom: 3%;">
              <div class="col">
                <p style="font-size: 17px;color:black;font-weight: 400;padding-top: 6px;text-align: left">排序：</p>
              </div>
              <div class="col"><b-button pill variant="outline-info" style="width:80px">名稱</b-button></div>
              <div class="col"><b-button pill variant="outline-info" style="width:80px">季報酬</b-button></div>
              <div class="col"><b-button pill variant="outline-info" style="width:80px">月報酬</b-button></div>
              <div class="col"><b-button pill variant="outline-info" style="width:80px">週報酬</b-button></div>
            </div>
          </div>
          <div class="row">
            <div class="flex flex-col" style="margin-left:1%">
              <div class="-my-2 py-2 overflow-x-auto sm:-mx-6 sm:px-6 lg:-mx-8 lg:px-8">
                <div class="align-middle inline-block min-w-full overflow-hidden sm:rounded-lg border-b border-gray-200"
                  style="background-color:#e1ecf4">
                  <table class="min-w-full">
                    <thead>
                      <tr>
                        <th
                          class="px-6 py-3   text-left text-xs leading-4 font-medium text-gray-500 uppercase tracking-wider">
                        </th>
                        <th class="px-6 py-3  text-left text-xs leading-4 font-medium uppercase tracking-wider">
                          年化報酬
                        </th>
                        <th class="px-6 py-3  text-left text-xs leading-4 font-medium uppercase tracking-wider">
                          最大虧損
                        </th>
                        <th class="px-8 py-3 text-left text-xs leading-4 font-medium uppercase tracking-wider">
                          夏普值
                        </th>
                        <th class="px-12 py-3 text-left text-xs leading-4 font-medium tracking-wider">
                          大盤比較
                        </th>
                        <th class="px-12 py-3 text-left text-xs leading-4 font-medium tracking-wider">
                          近期報酬
                        </th>
                        <th class="px-24 py-3 text-left text-xs leading-4 font-medium tracking-wider">
                          重要日期
                        </th>
                        <th class="px-6 py-3"></th>
                      </tr>
                    </thead>
                    <tbody class="bg-white">
                      <tr>
                        <td class="px-6 py-4 whitespace-no-wrap border-b border-gray-200">合約負債建築工 VIP</td>
                        <td class="px-6 py-4 whitespace-no-wrap border-b border-gray-200">
                          <span
                            class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-red-100 text-red-800">
                            +36.2%
                          </span>
                        </td>
                        <td class="px-6 py-4 whitespace-no-wrap border-b border-gray-200">
                          <span
                            class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-green-100 text-green-800">
                            -31.1%
                          </span>
                        </td>
                        <td class="px-6 py-4 whitespace-no-wrap border-b border-gray-200">
                          <span
                            class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-gray-100 text-gray-800">
                            1.8
                          </span>
                        </td>
                        <td class="px-6 py-4 whitespace-no-wrap border-b border-gray-200">
                          <div class="flex items-center">
                            <div class="ml-4">
                              <div class="text-sm leading-5 font-medium text-gray-900"> 週 月 季 </div>
                              <div class="text-sm leading-5 text-red-500">勝 勝 勝</div>
                            </div>
                          </div>
                        </td>
                        <td class="px-6 py-4 whitespace-no-wrap border-b border-gray-200">
                          <div class="flex items-center">
                            <div class="ml-4">
                              <div class="text-sm leading-5 font-medium text-gray-900">月 +19.1 %</div>
                              <div class="text-sm leading-5 text-gray-500">季 +43.5 %</div>
                            </div>
                          </div>
                        </td>
                        <td class="px-6 py-4 whitespace-no-wrap border-b border-gray-200">
                          <div class="flex items-center">
                            <div class="ml-4">
                              <div class="text-sm leading-5 font-medium text-gray-900">近期換股： 2024-06-30</div>
                              <div class="text-sm leading-5 text-gray-500">策略更新： 2024-4-18</div>
                            </div>
                          </div>
                        </td>
                        <td
                          class="px-6 py-4 whitespace-no-wrap text-right border-b border-gray-200 text-sm leading-5 font-medium">
                          <a href="#"
                            class="text-indigo-600 hover:text-indigo-900 focus:outline-none focus:underline">Edit</a>
                        </td>
                      </tr>
                      <tr>
                        <td class="px-6 py-4 whitespace-no-wrap border-b border-gray-200">合約負債建築工 VIP</td>
                        <td class="px-6 py-4 whitespace-no-wrap border-b border-gray-200">
                          <span
                            class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-red-100 text-red-800">
                            +36.2%
                          </span>
                        </td>
                        <td class="px-6 py-4 whitespace-no-wrap border-b border-gray-200">
                          <span
                            class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-green-100 text-green-800">
                            -31.1%
                          </span>
                        </td>
                        <td class="px-6 py-4 whitespace-no-wrap border-b border-gray-200">
                          <span
                            class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-gray-100 text-gray-800">
                            1.8
                          </span>
                        </td>
                        <td class="px-6 py-4 whitespace-no-wrap border-b border-gray-200">
                          <div class="flex items-center">
                            <div class="ml-4">
                              <div class="text-sm leading-5 font-medium text-gray-900"> 週 月 季 </div>
                              <div class="text-sm leading-5 text-red-500">勝 勝 勝</div>
                            </div>
                          </div>
                        </td>
                        <td class="px-6 py-4 whitespace-no-wrap border-b border-gray-200">
                          <div class="flex items-center">
                            <div class="ml-4">
                              <div class="text-sm leading-5 font-medium text-gray-900">月 +19.1 %</div>
                              <div class="text-sm leading-5 text-gray-500">季 +43.5 %</div>
                            </div>
                          </div>
                        </td>
                        <td class="px-6 py-4 whitespace-no-wrap border-b border-gray-200">
                          <div class="flex items-center">
                            <div class="ml-4">
                              <div class="text-sm leading-5 font-medium text-gray-900">近期換股： 2024-06-30</div>
                              <div class="text-sm leading-5 text-gray-500">策略更新： 2024-4-18</div>
                            </div>
                          </div>
                        </td>
                        <td
                          class="px-6 py-4 whitespace-no-wrap text-right border-b border-gray-200 text-sm leading-5 font-medium">
                          <a href="#"
                            class="text-indigo-600 hover:text-indigo-900 focus:outline-none focus:underline">Edit</a>
                        </td>
                      </tr>
                      <tr>
                        <td class="px-6 py-4 whitespace-no-wrap border-b border-gray-200">合約負債建築工 VIP</td>
                        <td class="px-6 py-4 whitespace-no-wrap border-b border-gray-200">
                          <span
                            class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-red-100 text-red-800">
                            +36.2%
                          </span>
                        </td>
                        <td class="px-6 py-4 whitespace-no-wrap border-b border-gray-200">
                          <span
                            class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-green-100 text-green-800">
                            -31.1%
                          </span>
                        </td>
                        <td class="px-6 py-4 whitespace-no-wrap border-b border-gray-200">
                          <span
                            class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-gray-100 text-gray-800">
                            1.8
                          </span>
                        </td>
                        <td class="px-6 py-4 whitespace-no-wrap border-b border-gray-200">
                          <div class="flex items-center">
                            <div class="ml-4">
                              <div class="text-sm leading-5 font-medium text-gray-900"> 週 月 季 </div>
                              <div class="text-sm leading-5 text-red-500">勝 勝 勝</div>
                            </div>
                          </div>
                        </td>
                        <td class="px-6 py-4 whitespace-no-wrap border-b border-gray-200">
                          <div class="flex items-center">
                            <div class="ml-4">
                              <div class="text-sm leading-5 font-medium text-gray-900">月 +19.1 %</div>
                              <div class="text-sm leading-5 text-gray-500">季 +43.5 %</div>
                            </div>
                          </div>
                        </td>
                        <td class="px-6 py-4 whitespace-no-wrap border-b border-gray-200">
                          <div class="flex items-center">
                            <div class="ml-4">
                              <div class="text-sm leading-5 font-medium text-gray-900">近期換股： 2024-06-30</div>
                              <div class="text-sm leading-5 text-gray-500">策略更新： 2024-4-18</div>
                            </div>
                          </div>
                        </td>
                        <td
                          class="px-6 py-4 whitespace-no-wrap text-right border-b border-gray-200 text-sm leading-5 font-medium">
                          <a href="#"
                            class="text-indigo-600 hover:text-indigo-900 focus:outline-none focus:underline">Edit</a>
                        </td>
                      </tr>
                      <tr>
                        <td class="px-6 py-4 whitespace-no-wrap border-b border-gray-200">合約負債建築工 VIP</td>
                        <td class="px-6 py-4 whitespace-no-wrap border-b border-gray-200">
                          <span
                            class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-red-100 text-red-800">
                            +36.2%
                          </span>
                        </td>
                        <td class="px-6 py-4 whitespace-no-wrap border-b border-gray-200">
                          <span
                            class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-green-100 text-green-800">
                            -31.1%
                          </span>
                        </td>
                        <td class="px-6 py-4 whitespace-no-wrap border-b border-gray-200">
                          <span
                            class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-gray-100 text-gray-800">
                            1.8
                          </span>
                        </td>
                        <td class="px-6 py-4 whitespace-no-wrap border-b border-gray-200">
                          <div class="flex items-center">
                            <div class="ml-4">
                              <div class="text-sm leading-5 font-medium text-gray-900"> 週 月 季 </div>
                              <div class="text-sm leading-5 text-red-500">勝 勝 勝</div>
                            </div>
                          </div>
                        </td>
                        <td class="px-6 py-4 whitespace-no-wrap border-b border-gray-200">
                          <div class="flex items-center">
                            <div class="ml-4">
                              <div class="text-sm leading-5 font-medium text-gray-900">月 +19.1 %</div>
                              <div class="text-sm leading-5 text-gray-500">季 +43.5 %</div>
                            </div>
                          </div>
                        </td>
                        <td class="px-6 py-4 whitespace-no-wrap border-b border-gray-200">
                          <div class="flex items-center">
                            <div class="ml-4">
                              <div class="text-sm leading-5 font-medium text-gray-900">近期換股： 2024-06-30</div>
                              <div class="text-sm leading-5 text-gray-500">策略更新： 2024-4-18</div>
                            </div>
                          </div>
                        </td>
                        <td
                          class="px-6 py-4 whitespace-no-wrap text-right border-b border-gray-200 text-sm leading-5 font-medium">
                          <a href="#"
                            class="text-indigo-600 hover:text-indigo-900 focus:outline-none focus:underline">Edit</a>
                        </td>
                      </tr>
                      <tr>
                        <td class="px-6 py-4 whitespace-no-wrap border-b border-gray-200">合約負債建築工 VIP</td>
                        <td class="px-6 py-4 whitespace-no-wrap border-b border-gray-200">
                          <span
                            class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-red-100 text-red-800">
                            +36.2%
                          </span>
                        </td>
                        <td class="px-6 py-4 whitespace-no-wrap border-b border-gray-200">
                          <span
                            class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-green-100 text-green-800">
                            -31.1%
                          </span>
                        </td>
                        <td class="px-6 py-4 whitespace-no-wrap border-b border-gray-200">
                          <span
                            class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-gray-100 text-gray-800">
                            1.8
                          </span>
                        </td>
                        <td class="px-6 py-4 whitespace-no-wrap border-b border-gray-200">
                          <div class="flex items-center">
                            <div class="ml-4">
                              <div class="text-sm leading-5 font-medium text-gray-900"> 週 月 季 </div>
                              <div class="text-sm leading-5 text-red-500">勝 勝 勝</div>
                            </div>
                          </div>
                        </td>
                        <td class="px-6 py-4 whitespace-no-wrap border-b border-gray-200">
                          <div class="flex items-center">
                            <div class="ml-4">
                              <div class="text-sm leading-5 font-medium text-gray-900">月 +19.1 %</div>
                              <div class="text-sm leading-5 text-gray-500">季 +43.5 %</div>
                            </div>
                          </div>
                        </td>
                        <td class="px-6 py-4 whitespace-no-wrap border-b border-gray-200">
                          <div class="flex items-center">
                            <div class="ml-4">
                              <div class="text-sm leading-5 font-medium text-gray-900">近期換股： 2024-06-30</div>
                              <div class="text-sm leading-5 text-gray-500">策略更新： 2024-4-18</div>
                            </div>
                          </div>
                        </td>
                        <td
                          class="px-6 py-4 whitespace-no-wrap text-right border-b border-gray-200 text-sm leading-5 font-medium">
                          <a href="#"
                            class="text-indigo-600 hover:text-indigo-900 focus:outline-none focus:underline">Edit</a>
                        </td>
                      </tr>
                    </tbody>
                  </table>
                </div>
              </div>
            </div>
          </div>
          <h3 class="text-xl font-bold text-left pt-6" style="color:#1B3C73">股票新聞</h3>
          <div>
            <div class="row" style="padding-left:3%;">
              <div v-for="(newsItem, index) in news" :key="index" class="col-3" style="margin-right:7%">
                <div class="blog">
                  <div class="container1" style="width:500px">
                    <div class="row" style="width:95%;">
                      <div class="col-md-4 col-lg-9">
                        <div class="item">
                          <div class="img">
                            <img :src="newsItem.ImgUrl" alt="">
                          </div>
                          <div class="info">
                            <div class="date">
                              <span>{{ formatDate(newsItem.Time) }} <br> {{ formatMonth(newsItem.Time) }}</span>
                            </div>
                            <a :href="newsItem.urlrl">
                              <h5 style="color:#0C2D57;font-weight: 500;font-size: 20px;margin-bottom:12px">
                                {{ newsItem.title }}
                              </h5>
                            </a>
                            <p>{{ newsItem.summary }}</p>
                            <a :href="newsItem.Url" class="more">
                              <svg viewBox="0 0 10 10" fill="currentColor" strokeWidth="2" class="w-6 h-5">
                                <path fill-rule="evenodd"
                                  d="M12.293 5.293a1 1 0 011.414 0l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-2.293-2.293a1 1 0 010-1.414z"
                                  clip-rule="evenodd"></path>
                              </svg>
                            </a>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </b-tab>
      </b-tabs>
    </div>
    <div id="app">
      <go-top :size="50" bg-color="#1e3d73" :bottom="25"></go-top>
    </div>
  </div>
</template>
<script>
import axios from 'axios';
import VueApexCharts from 'vue-apexcharts';

export default {
  components: {
    apexchart: VueApexCharts
  },
  data() {
    return {
      stocks: [],
      timestamp: '',
      compatConfig: { MODE: 3 },
      news:[]
    };
  },
  created() {
    this.updateTimestamp();
    setInterval(this.updateTimestamp, 1000);
    this.fetchNews();
  },
  methods: {
    async fetchIndex() {
      try {
        const response = await axios.post('http://127.0.0.1:12000/api/indexStocks', {
          StocksNum: 3,
          StocksID: ["0050", "2330", "00940"],
          time: this.timestamp
        });
        const data = response.data;
        console.log(data)
        this.stocks = data.map((stock) => {
          const change = this.calculateChange(stock.StocksChart);
          return {
            StocksChart: stock.StocksChart,
            name: stock.StocksTitle,
            change
          };
        });
      } catch (error) {
        console.error('Error fetching index:', error);
      }
    },
    calculateChange(stocksChart) {
      if (stocksChart.length < 2) return 'N/A';
      const initialPrice = stocksChart[0];
      const finalPrice = stocksChart[stocksChart.length - 1];
      const change = ((finalPrice - initialPrice) / initialPrice) * 100;
      return change.toFixed(2) + '%';
    },
    async fetchNews() {
      try {
        const response = await axios.post('http://127.0.0.1:12000/api/newsStocks', {
          newsNum: 3
        });
        this.news = response.data;
        console.log(this.news)
      } catch (error) {
        console.error('Error fetching news:', error);
      }
    },
    getChartOptions(stock) {
      return {
        chart: {
          type: 'area',
          height: 150
        },
        xaxis: {
          categories: stock.StocksChart.map((_, index) => index + 1) // 示例x轴
        },
        stroke: {
          curve: 'smooth'
        },
        dataLabels: {
          enabled: false
        },
        fill: {
          type: 'gradient',
          gradient: {
            shadeIntensity: 1,
            opacityFrom: 0.7,
            opacityTo: 0.9,
            stops: [0, 100]
          }
        },
        tooltip: {
          x: {
            show: true
          }
        }
      };
    },
    updateTimestamp() {
      const today = new Date();
      const dateTime = today.getFullYear() + '/' +
        String(today.getMonth() + 1).padStart(2, '0') + '/' +
        String(today.getDate()).padStart(2, '0') + ' ' +
        String(today.getHours()).padStart(2, '0') + ':' +
        String(today.getMinutes()).padStart(2, '0') + ':' +
        String(today.getSeconds()).padStart(2, '0');
      this.timestamp = dateTime;
    },
    formatDate(timestamp) {
      const date = new Date(timestamp);
      return date.getDate();
    },
    formatMonth(timestamp) {
      const date = new Date(timestamp);
      return date.toLocaleString('default', { month: 'short' });
    }
  },
  mounted() {
    this.fetchIndex();
    this.fetchNews();
    this.updateTimestamp();
  }
};
</script>

<style lang="scss" scoped>
.card1 {
  margin-top: 2%;
  border-radius: 8px;
  background-color: #e1ecf4;
  padding: 20px;
  overflow: hidden;
  box-shadow: 0 4px 8px 0 rgba(182, 182, 182, 0.8);
  transition: 0.3s;
  margin-left: 3%
}

@media only screen and (max-width: 600px) {
  .card {
    border-radius: 12px;
    background-color: #fff;
    padding: 16px;
    border-color: #1e3d73;
    overflow: hidden;
  }
}

@media (min-width: 1200px) {
  .dasboard-content {
    margin-right: 280px
  }
}

span,
a,
a:hover {
  display: inline-block;
  text-decoration: none;
  color: inherit;
}

.blog img {
  max-width: 100%;
  min-height: 30vh;
}

.blog-head {
  margin-bottom: 70px;
}

.blog-head h6 {
  color: #f05907;
  position: relative;
  display: inline-block;
  text-transform: capitalize;
}

.wrap-table {
  border: 1px solid #e5e7eb;
  border-radius: 12px;
  overflow-x: auto;
  container-type: inline-size;
  container-name: table;
}

table {
  border-collapse: collapse;
  width: 100%;
  font-size: 14px;
}

th {
  font-weight: 700;
  color: #374151;
  font-size: 14px;
  padding: 12px 10px;
  text-align: center;
  background: #e1ecf4;
  border-bottom: 1px solid #e5e7eb;
}

td {
  padding: 12px 14px;
  border-bottom: 1px solid #e5e7eb;
  background: #fff;
  text-align: center;
}

.user__photo {
  width: 48px;
  height: 48px;
  object-fit: cover;
  border-radius: 100px;
}

.user__name {
  font-size: 14px;
  font-weight: 600;
  color: #111827;
}

.user__email {
  font-size: 12px;
  color: #4b5563;
}

.user__badge {
  width: max-content;
  background: #dcfce7;
  border-radius: 6px;
  border: 1px solid #40c370;
  color: #15803d;
  padding: 4px 12px;
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 12px;
  font-weight: 500;
}

.user__badge_1 {
  width: max-content;
  background: #dcfce7;
  border-radius: 6px;
  border: 1px solid #e6e8e7;
  color: #060606ea;
  padding: 4px 12px;
  display: flex;
  background: #d1d5db;
  align-items: center;
  gap: 8px;
  font-size: 12px;
  font-weight: 500;
}

.user__badge_1:before {
  content: "";
  width: 4px;
  height: 4px;
  border-radius: 100px;
  background: #929392;
  display: block;
}

.user__badge:before {
  content: "";
  width: 4px;
  height: 4px;
  border-radius: 100px;
  background: #15803d;
  display: block;
}

.user__badge_pending {
  background: #fefce8;
  color: #8a551c;
  border-color: #f4e7c5;
}

.user__badge_pending:before {
  background: #8a551c;
}

.user__badge_unpaid {
  background: #fef2f2;
  color: #b91c1c;
  border-color: #fbe0e0;
  list-style: none
}

.user__badge_unpaid:before {
  background: #b91c1c;
}

.user__edit {
  display: block;
  padding: 4px 12px;
  text-decoration: none;
}

input {
  display: none;
}

input+span {
  display: block;
  width: 16px;
  height: 16px;
  border: 2px solid #d1d5db;
  border-radius: 4px;
  transition: .3s;
  cursor: pointer;
}

input+span>svg {
  opacity: 0;
}

input:checked+span {
  background: #dcfce7;
  border: 2px solid #15803d;
  color: #15803d;
}

input:checked+span>svg {
  opacity: 1;
}

progress {
  display: block;
  width: 100px;
  height: 7px;
  -webkit-appearance: none;
  border-radius: 10px;
}

progress::-webkit-progress-bar {
  background-color: #eee;
  border-radius: 10px;
}

progress::-webkit-progress-value {
  background-color: #10b981;
  border-radius: 10px;
}

.user__edit {
  padding: 8px 12px;
  border-radius: 6px;
  background: #1e3d73;
  color: #fff;
  text-align: center;
  font-weight: 500;
}

.user__edit:hover {
  padding: 8px 12px;
  border-radius: 6px;
  background: #c5c5c7;
  color: #fff;
  text-align: center;
  font-weight: 500;
}

@container table (min-width: 400px) {
  .sticky-col {
    position: sticky;
    left: 0;
  }

  .sticky-col-right {
    right: 0;
  }
}

@container table (max-width: 400px) {
  td::before {
    content: attr(data-label);
    font-weight: 700;
    color: #374151;
    font-size: 14px;
  }

  label {
    display: none;
  }

  td {
    display: flex;
    align-items: center;
    justify-content: space-between;
    border-bottom: none;
  }

  td:first-child {
    background: #f9fafb;
  }

  th {
    display: none;
  }
}

#btn_resize {
  cursor: ew-resize;
  width: 14px;
  height: 100%;
  position: absolute;
  top: 0;
  left: calc(100% + 3px);
  background: #fff;
  display: flex;
  align-items: start;
  justify-content: center;
  border: none;
  padding: 0;
}

#btn_resize span {
  background: #94a3b8;
  height: 32px;
  width: 4px;
  display: block;
  border-radius: 10px;
}

.blog-head h6:after,
.blog-head h6:before {
  position: absolute;
  content: "";
  width: 50px;
  height: 3px;
  background: #e1ecf4;
  top: 50%;
}

.blog-head h6:after {
  right: 120%;
}

.blog-head h6:before {
  left: 120%;
}

.overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  z-index: 0;
}

.blog {
  margin-top: 50px;
  height: 40vh;
}

.blog .item {
  background-color: #fff;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
  border-radius: 10px;
  overflow: hidden;
  position: relative;
  height: 100%
}

.blog .item .more {
  position: absolute;
  right: 30px;
  bottom: 20px;
  box-shadow: 0 0 30px rgba(0, 0, 0, 0.1);
  color: #1e3d73;
  font-size: 19px;
  width: 40px;
  height: 40px;
  border-radius: 50%;
  line-height: 40px;
  text-align: center;
  transform: translate(0, 100px);
  transition: all 0.3s ease-in-out;
}

.blog .item:hover .more {
  transform: translate(0, 0)
}

h3 {
  text-align: left;
  margin-top: 3%
}

.blog .item:hover .img img {
  transition: all 0.4s ease;
}

.blog .item:hover .img img {
  transform: rotate(-5deg) scale(1.2, 1.2);
}

.blog .item .img {
  clip-path: polygon(0 0, 100% 0, 100% 70%, 0 100%, 0 75%);
}

.blog .item .info {
  padding: 30px;
  position: relative;
}

.blog .item .info .date {
  position: absolute;
  left: calc(50% - 25px);
  top: -54px;
  width: 50px;
  height: 50px;
  line-height: 20px;
  text-align: center;
  background-color: #1e3d73;
  color: #fff;
  padding: 5px;
  transform: rotate(45deg);
}

.blog .item .info .date span {
  transform: rotate(-45deg);
  display: inline-block;
}

.blog .item .info h5:hover {
  color: #1e3d73;
}

.blog .item .info .user {
  margin-top: 20px;
  color: #1e3d73;
}

.container1 {
  margin-right: 10px;
}
</style>
