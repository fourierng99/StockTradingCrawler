from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import sys
import ssl, os, codecs, re
from csv import writer

class VNIndexStock:
    def __init__(self):
        self.url = 'https://iboard.ssi.com.vn/'
        self.chrome_options = Options()
        self.chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.chrome_options.add_argument("--incognito")
        self.chrome_options.add_argument("--window-size=1920x1080")
        self.driver = webdriver.Chrome(chrome_options=self.chrome_options, executable_path="chromedriver.exe")
        self.driver.get(self.url)
        time.sleep(3)
    def crawl(self):
        while True:
            time_now = self.driver.find_element(By.XPATH, '//div[@data-for="today"]').get_attribute('innerHTML')
            print(time_now)
            time.sleep(5)


if __name__ == "__main__":
    vn_index = VNIndexStock()
    vn_index.crawl()