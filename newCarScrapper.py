#imports here
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import csv
import time
import shutil # to save it locally
import urllib.request


from selenium.webdriver.chrome.options import Options
op = webdriver.ChromeOptions()
op.add_argument
("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
+"AppleWebKit/537.36 (KHTML, like Gecko)"
+"Chrome/87.0.4280.141 Safari/537.36")


chrome_path = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(chrome_path, options=op)
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

#Change to English
WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//a[@id='toggle_lang']"))).click()
time.sleep(5)

#target the Check Box and click it
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class,'col-lg-8 col-md-8 col-sm-9 col-xs-8 search-maker-right') and contains(text(), 'HONDA')]"))).click()
time.sleep(5)
#target the Check Box and click it
WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//div/span[contains(text(), 'Civic')]"))).click()
time.sleep(2)

#target the next button and click it
WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class='page-next-button col-md-2 col-xs-4']"))).click()
time.sleep(2)

for k in range(1,132):
   url = 'https://www.iauc.co.jp/vehicle/carlist?page='+str(k)+'&sort_type=&limit=15&branch=&element=&mode=table&narrow_key=73802218660546bf7a7edc'
   driver.get(url)
   time.sleep(1)
   WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//img[@class = 'img-car lazy-table']"))).click()
   time.sleep(2)
   # get the image source
   img = driver.find_element_by_xpath('//figure[@class="col-md-12 col-xs-6"]/img')
   src = img.get_attribute('src')
   # download the image
   headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36'}
   session = request.Session()
   req = session.get(src, headers=headers)
   urllib.request.urlretrieve(src, "local-filename.jpg")
   
   
       
