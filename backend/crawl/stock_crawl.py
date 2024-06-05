from seleniumbase import Driver
from selenium.webdriver.common.by import By
from datetime import datetime
import requests
import os

#建立變數
driver= Driver(uc= True, incognito= False, headless= True)

driver.get('https://data.gov.tw/dataset/11549')
download_url= driver.find_element(By.CSS_SELECTOR,"#__nuxt > div > div > main > div > div > div > div > ul > li > a").get_attribute('href')
response= requests.get(download_url)       

if response.status_code == 200:
    cur_path  = os.path.abspath(__file__)
    cur_dir   = os.path.dirname(cur_path)
    cur_time  = datetime.now()
    file_name = f'stock_{cur_time.year}_{cur_time.month}_{cur_time.day}.csv'
    file_path = os.path.join(cur_dir, 'stocks_datas', file_name)
    with open(file_path, 'w') as f: #下載路徑依照需求更改，目前為預設路徑
        f.write(response.text)
else:   print(response.status_code)