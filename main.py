import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def load_url():
    with open('url.json', 'r') as f:
        return json.load(f)

def execute_purchase(driver, url, wait_time):
    driver.get(url)
    
    # 等 "直接購買" available 後點選
    WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class='btn btn-solid-primary btn--l rvHxix']"))).click()
    print('------do')

    # 等 "去買單" available 後點選，需強制睡一秒最順
    time.sleep(1)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class='shopee-button-solid shopee-button-solid--primary']"))).click()
    print('-----do2')

    # 等 "貨到付款" available 後點選
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label='貨到付款']"))).click()
    print('-----do3')

    # 等 "下訂單" available 後點選 (如需下單，取消註解)
    # WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class='stardust-button stardust-button--primary stardust-button--large _1qSlAe']"))).click()
    # print('-----do4')

def init_driver():
    options = Options()
    #driver_path = './chrome-mac-arm64/Google Chrome for Testing.app/Contents/MacOS/Google Chrome for Testing'  # 指定你的 chromedriver 路徑
    driver_path  = '/opt/homebrew/bin/chromedriver'
    options.add_experimental_option("debuggerAddress", "127.0.0.1:9527")
    return webdriver.Chrome(executable_path=driver_path, options=options)  # 使用 executable_path


if __name__ == '__main__':
    config = load_url()
    driver = init_driver()

    for page in config['pages']:
        url = page['url']
        wait_time = page['wait_time']
        execute_purchase(driver, url, wait_time)
    
    driver.quit()
