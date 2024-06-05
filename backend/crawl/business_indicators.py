from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.edge.service import Service
import time
import csv

PATH = './crawl/driver/edgedriver_mac64_m1/msedgedriver'
edge_service = Service(PATH)
driver = webdriver.Edge(service=edge_service)
url = 'https://index.ndc.gov.tw/n/zh_tw/data/eco#/'
indicators = []

def crawl(url):
    driver.get(url)
    driver.maximize_window() #最大化視窗防止無法操作
    month_btn = driver.find_element(By.CSS_SELECTOR, '#search > div.search_chart > div.month_l > ul > li:nth-child(3) > a')
    table_btn = driver.find_element(By.CSS_SELECTOR, '#table__view')
    month_btn.click()
    table_btn.click()
    driver.implicitly_wait(20)
    table = driver.find_element(By.CSS_SELECTOR, '#search > div.search_chart > div.display > div.ng-scope > div.table_style > table')
    datas = table.find_elements(By.CSS_SELECTOR, 'tbody > tr')
    for data in datas:
        indicator = {}
        date = data.text.split('\n')[0]
        score = data.text.split('\n')[1]
        indicator['date'] = date
        indicator['score'] = score
        # print(indicator)
        indicators.append(indicator)


crawl(url)
print(indicators)

fieldnames = set()
for item in indicators:
    fieldnames.update(item.keys())

with open('./crawl/indicators.csv', 'w') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(indicators)