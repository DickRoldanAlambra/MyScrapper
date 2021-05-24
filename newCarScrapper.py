#imports here
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import csv
import time
from selenium.webdriver.chrome.options import Options
import urllib.request

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
   trs =driver.find_elements_by_xpath('//table/tbody/tr/td[@class="col2 open-detail"]/img')
   count = 1
   for tr in trs:
      print([tr.get_attribute('data-original')])        
      src = tr.get_attribute('data-original')
      
      request = urllib.request.Request(src)
      request.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36')
      request.add_header('Cookie', '_ga=GA1.3.359263082.1621670361; _gid=GA1.3.1725556770.1621670361; fuelrid=pr0AfA8cqH6cZr3zithRrxXMmoZegcFW-UV_t_-SBR-Voe1XWrWsucn8B-PSInQuD6Cabt1nbcwMMxfhx5LW9GRSSWQwLXhPNU1qdWJYWTc1WHF3UzRNcnVUOHVGb0poWWRyZEx5MkJwaFU; iauc_rf=0; __ulfpc=202105221559473211; mqzvpxGmSEwD=0; iauc_limit_vehicle=15; __ulfps=27pNsVyg1z83q946; iauc_lang=en; _l_tm_stmp=2021-05-22+19%3A10%3A28')

      response = urllib.request.urlopen(request)
      data = response.read()
      with open("page"+str(k)+"_"+str(count)+"civic.jpg", "wb") as f:
         f.write(data)
      count +=1      
      time.sleep(5)

      
          

