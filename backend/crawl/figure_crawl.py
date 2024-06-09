from seleniumbase import Driver
from selenium.webdriver.common.by import By
from datetime import datetime
import csv
import os

def string_to_float(str):
    if str != '' and str != None:
        float_num = float(str.replace(',', ''))
        return float_num
    return str

# 建立變數
driver = Driver(uc=True, incognito=False, headless=True)
tiles_set = {"開盤", "最高", "最低", "昨收", "成交量(億)"}
urls = [
    'https://www.wantgoo.com/index/0000',
    'https://www.wantgoo.com/global/dji'
]

# 準備 CSV 檔案
cur_time = datetime.now()
cur_dir  = os.path.dirname(os.path.abspath(__file__))
file_name = f'figures_data_{cur_time.year}_{cur_time.month}_{cur_time.day}.csv'
file_path = os.path.join(cur_dir, 'figures_datas', file_name)

csv_file = open(file_path, mode='w', newline='', encoding='utf-8')
csv_writer = csv.writer(csv_file)

# 寫入標題列
csv_writer.writerow(["指標名稱", "開盤", "最高", "最低", "收盤", "成交量(億)"])

for url in urls:
    driver.get(url)
    row_data = [driver.find_element(By.CSS_SELECTOR, "#investrue-info-1 > h3").text]
    figures = driver.find_elements(By.CSS_SELECTOR, "body > div.page-wrap > main > div > div.quotes-wrap > div.quotes-info > div.lasty-detail > ul > li")
    
    for figure in figures:
        key = figure.find_element(By.CSS_SELECTOR, "i").text
        val = figure.find_element(By.CSS_SELECTOR, "span").text  
        if key in tiles_set: 
            row_data.append(val)
    
    # 檢查並補齊缺失的資料
    while len(row_data) < 6:
        row_data.append('0.')
    
    row_data[-1] = string_to_float(row_data[-1])
    csv_writer.writerow(row_data)

# 關閉 CSV 文件
csv_file.close()

# 關閉瀏覽器
driver.quit()
