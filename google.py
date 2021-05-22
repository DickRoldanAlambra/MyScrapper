#imports here
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException

import csv
import time
chrome_path = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(chrome_path)
driver.get('https://www.google.com/')
#CSV Header
#with open(r'C:\Users\DK\Desktop\hospital_detail.csv', 'w') as file:
	#file.write("Hospital Number,Name,Address,Postal Code,Hour,Phone,URL Website, \n")

with open(r'C:\Users\DK\Desktop\hospitals1.csv', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for rows in reader:
        url = 'https://www.google.com/search?q='+str(rows['名前'])+'&source=hp&ei=GhuBYMDLMJv6wAPtgYtY&iflsig=AINFCbYAAAAAYIEpKtxvfa7AZ0aanwk980L1KKVsWWzq&oq=%E4%B8%8A%E6%A2%9D%E7%94%B2%E7%8A%B6%E8%85%BA%E3%82%AF%E3%83%AA%E3%83%8B%E3%83%83%E3%82%AF&gs_lcp=Cgdnd3Mtd2l6EAwyAggAMgIIADICCAAyAggAMgIIADICCAAyAggAUMwMWNwNYOISaABwAHgBgAGMAYgB8QOSAQMxLjOYAQCgAQGqAQdnd3Mtd2l6&sclient=gws-wiz&ved=0ahUKEwjAwNb-n5HwAhUbPXAKHe3AAgsQ4dUDCAg'
        driver.get(url)
        time.sleep(2)
        
        for element in driver.find_elements_by_xpath('//div[@class="site30 v-r container-fluid"]'):
            try:
                Name = element.find_element_by_xpath('.//h2[@data-local-attribute="d3bn"]/span').text
            except:
                Name = "No Institution Available"
            try:
                Website = driver.find_element_by_xpath('//div[@class="QqG1Sd"]/a').get_attribute('href')
            except:
                Website = "No Website Available"   
            try:
                Address = driver.find_element_by_xpath('//span[@class="LrzXr"]').text
            except:
                Address = "No Address Available"
            try:
                Hours = driver.find_element_by_xpath('//span[@class="JjSWRd"]/span/span').text
            except:
                Hours = "No Hours Available"
            try:
                Phone = driver.find_element_by_xpath('//span[@class="LrzXr zdqRlf kno-fv"]').text
            except:
                Phone = "No Phone Available"
            try:
                HospitalNumber = rows['郵便番号']
            except:
                HospitalNumber = "No Records Available"
            try:
                PostalCode = rows['Postal Code']
            except:
                PostalCode = "No Records Available"
            #Name = element.find_element_by_xpath('.//h2[@data-local-attribute="d3bn"]/span').text  
            #Website = driver.find_element_by_xpath('//div[@class="QqG1Sd"]/a').get_attribute('href')
            #Address = driver.find_element_by_xpath('//span[@class="LrzXr"]').text
            #try:
                #Hours = driver.find_element_by_xpath('//span[@class="JjSWRd"]/span/span').text
            #except:
                #Hours = "No Records Available"
            #try:
            #Phone = driver.find_element_by_xpath('//span[@class="LrzXr zdqRlf kno-fv"]').text
            #except:
                #Phone = "No Phone Available"
            #Name = element.find_element_by_xpath('.//h2[@data-local-attribute="d3bn"]/span').text  
            #Website = driver.find_element_by_xpath('//div[@class="QqG1Sd"]/a').get_attribute('href')
            #Address = driver.find_element_by_xpath('//span[@class="LrzXr"]').text
            #Hours = driver.find_element_by_xpath('//span[@class="JjSWRd"]/span/span').text
            #Phone = driver.find_element_by_xpath('//span[@class="LrzXr zdqRlf kno-fv"]').text
            
        #append csv  
            with open (r'C:\Users\DK\Desktop\hospital_detail.csv', 'a',newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                print(HospitalNumber)
                print(PostalCode)
                writer.writerow([Name,Address,Hours,Phone,Website,HospitalNumber,PostalCode])
