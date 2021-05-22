#imports here
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import csv
import time
#CSV Header
with open(r'C:\Users\DK\Desktop\Honda Civic Fit.csv', 'w') as file:
	file.write("Image URL,Model & Grade, Location, LotNo, Auction, Year, Type & CC, Odo, ColorNo, Tm & Ac, Score, Start Price, Result \n")
	
chrome_path = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(chrome_path)
driver.get("https://www.iauc.co.jp/service/login")

#target the login button and click it
WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//a[@class='login-btn btn btn-info']"))).click()
time.sleep(5)
#target username
username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[class='form-control login_id']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[class='form-control login_password']")))

#enter username and password
username.clear()
username.send_keys("w60160201")
password.clear()
password.send_keys("TA6148")

#target the login button and click it
WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='button']"))).click()
time.sleep(2)
#target the login button and click it
WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
time.sleep(2)
#target the next button and click it
WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class='page-next-button col-md-2 col-xs-4']"))).click()
time.sleep(2)

#Japanese Language
#target the Check Box and click it
#WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class,'col-lg-8 col-md-8 col-sm-9 col-xs-8 search-maker-right') and contains(text(), '日産')]"))).click()
#time.sleep(2)
#target the Check Box and click it
#WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//div/span[contains(text(), 'ｴｸｽﾄﾚｲﾙ')]"))).click()
#time.sleep(2)

#English Language

#Change to English
WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//a[@id='toggle_lang']"))).click()
time.sleep(5)

#target the Check Box and click it
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class,'col-lg-8 col-md-8 col-sm-9 col-xs-8 search-maker-right') and contains(text(), 'HONDA')]"))).click()
time.sleep(5)
#target the Check Box and click it
WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//div/span[contains(text(), 'Grace')]"))).click()
time.sleep(2)

#target the next button and click it
WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class='page-next-button col-md-2 col-xs-4']"))).click()
time.sleep(2)

##Target Type Button
#WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//a[@class='narrow_button type ']"))).click()
#time.sleep(2)


#try:
  # WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//li/label/div[@class='zz '] and contains(text(), 'GM4')"))).click()
   #time.sleep(2)
#except:
  # WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//li/label/div[@class='zz '] and contains(text(), 'GM4')"))).click()
   #time.sleep(2)
#try:
#   WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//li/label/div[@class='zz '] and contains(text(), 'GM5')"))).click()
 #  time.sleep(2)
#except:
#   WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//li/label/div[@class='zz '] and contains(text(), 'GM5')"))).click()
#   time.sleep(2) 

#WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//a[@class='narrow_button button corner-radius col-xs-12']"))).click()
#time.sleep(2)


for k in range(1,132):
   url = 'https://www.iauc.co.jp/vehicle/carlist?page='+str(k)+'&sort_type=&limit=15&branch=&element=&mode=table&narrow_key=73802218660546bf7a7edc'
   driver.get(url)
   time.sleep(1)
   #get scrape data
   WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//img[@class = 'img-car lazy-table']"))).click()
   time.sleep(2)
   imageData = driver.find_elements_by_xpath('//img[@class = "img-car lazy-table"]')
   modelGrades = driver.find_elements_by_xpath('//td[@colspan= "7"][@class = "col3 open-detail"]')
   Locations = driver.find_elements_by_xpath('//td[@class = "col15 open-detail"]')
   LotNos = driver.find_elements_by_xpath('//td[@class = "col15 open-detail"]')
   Auctions = driver.find_elements_by_xpath('//td[@class = "col4 open-detail"]')
   Years = driver.find_elements_by_xpath('//td[@class = "col5 open-detail"]')
   TypeCCs = driver.find_elements_by_xpath('//td[@class = "col6 open-detail"]')
   Odos = driver.find_elements_by_xpath('//td[@class = "col7 open-detail"]')
   ColorNos = driver.find_elements_by_xpath('//td[@class = "col8 open-detail"]')
   TmAcs= driver.find_elements_by_xpath('//td[@class = "col9 open-detail"]')
   Scores = driver.find_elements_by_xpath('//td[@class = "col10 open-detail"]')
   StartPrices = driver.find_elements_by_xpath('//td[@class = "col11 open-detail"]')
   Results = driver.find_elements_by_xpath('//td[@class = "col12 open-detail"]')
   
   #append csv  
   with open (r'C:\Users\DK\Desktop\Honda Civic Fit.csv', 'a',newline='', encoding='utf-8') as file:
      writer = csv.writer(file)
      for i in range(len(imageData)):
         writer.writerow([imageData[i].get_attribute('data-original'),modelGrades[i].text,Locations[i].text,LotNos[i].text,Auctions[i].text,Years[i].text,TypeCCs[i].text,Odos[i].text,ColorNos[i].text,TmAcs[i].text,Scores[i].text,StartPrices[i].text,Results[i].text])
      #i=0
      #for modelGrade in modelGrades:
         #if modelGrade.text is not None:
            #file.write(imageData[i].get_attribute('data-original')+","+modelGrade.text+"\n\r")
            #i=i+1
   
   #for i in range(len(modelGrades)):
      #print(i)
         
            
      
      
            
