from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.edge.service import Service
from datetime import datetime
import time
import csv
import os

PATH = './crawl/driver/edgedriver_mac64_m1/msedgedriver'
edge_service = Service(PATH)
driver = webdriver.Edge(service=edge_service)
driver.implicitly_wait(20)
news = []
urls = ['https://money.udn.com/rank/pv/1001/5591/1', 'https://money.udn.com/rank/pv/1001/5590/1']

def crawl(news, news_url):        
    driver.get(news_url)
    driver.maximize_window() #最大化視窗防止無法操作


    holder = driver.find_element(By.CLASS_NAME, 'story-list-holder')
    wprs = holder.find_elements(By.CLASS_NAME, 'story-headline-wrapper')
    for i in range(len(wprs)):
        new = {}
        content = wprs[i].find_element(By.CLASS_NAME, 'story__content ')
        a = content.find_element(By.CSS_SELECTOR, 'a')
        date = content.find_element(By.CSS_SELECTOR, 'time').text
        title = a.get_attribute('title')
        url = a.get_attribute('href')
        pic_url = wprs[i].find_element(By.CLASS_NAME, 'story__image').find_element(By.CSS_SELECTOR, 'a > img').get_attribute('src')
        

        a.click()
        src = driver.find_element(By.CLASS_NAME, 'article-body__info').text
        driver.execute_script("window.history.go(-1)")
        print(f"{title}, {src}")

        new['title'] = title
        new['url'] = url
        new['pic_url'] = pic_url
        new['date'] = date
        new['src'] = src
        news.append(new)


        #避免 StaleReferenceElementException
        holder = driver.find_element(By.CLASS_NAME, 'story-list-holder')
        wprs = holder.find_elements(By.CLASS_NAME, 'story-headline-wrapper')
    return news

for url in urls:
    crawl(news, url)
driver.close()

fieldnames = set()
for item in news:
    fieldnames.update(item.keys())

cur_path  = os.path.abspath(__file__)
cur_dir   = os.path.dirname(cur_path)
cur_time  = datetime.now()
file_name = f'news_{cur_time.year}_{cur_time.month}_{cur_time.day}.csv'
file_path = os.path.join(cur_dir, 'news_datas', file_name)

with open(file_path, 'w') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(news)