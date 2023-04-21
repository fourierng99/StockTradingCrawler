from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import sys
import ssl, os, codecs, re
from csv import writer
import re
import datetime

#Constant 
FILE_PATH = 'csv_files/vnindex.csv'
TIME_INTERVAL = 300

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

    def append_list_as_row(self,file_name, list_of_elem):
    # Open file in append mode
        with open(file_name, 'a+',encoding="UTF-8" ,newline='') as write_obj:
            # Create a writer object from csv module
            csv_writer = writer(write_obj)
            # Add contents of list as last row in the csv file
            if os.stat(file_name).st_size == 0:
                csv_writer.writerow(["date","time","value"])    

            csv_writer.writerow(list_of_elem)

    def check_valid_record(self, time_str):
        time_lst = time_str.split(":")
        num = int(time_lst[0])*60 + int(time_lst[1])
        if num in range(690,780) or num in range(871, 885) or (num < 540 or num > 900):
            return False
        return True

    def check_quit(self,time_str):
        time_lst = time_str.split(":")
        num = int(time_lst[0])*60 + int(time_lst[1])
        return num >= 900

    def crawl(self):
        while True:
            # time_now = self.driver.find_element(By.XPATH, '//div[@data-for="today"]').get_attribute('innerHTML')
            # date_now = self.driver.find_element(By.XPATH, '//div[@data-for="today"]').get_attribute('data-tip')
            current_time = datetime.datetime.now()
            date_now = current_time.strftime("%m/%d/%Y")
            time_now = current_time.strftime("%H:%M:%S")

            if(self.check_quit(time_now) == True):
                sys.exit("Time over!")
            if( self.check_valid_record(time_now) == True):
                index_elements = self.driver.find_elements(By.XPATH, '//div[@class="index-value"]/div')
                for e in index_elements:
                    x = re.search("VNINDEX", e.text)
                    if(x):
                        str_index = e.text.split()[1].replace(',', '')
                        try:
                            r_val = float(str_index)
                        except:
                            r_val = ""
                        print(r_val)
                self.append_list_as_row(FILE_PATH,[date_now, time_now, r_val] )
                time.sleep(TIME_INTERVAL)


if __name__ == "__main__":
    vn_index = VNIndexStock()
    vn_index.crawl()