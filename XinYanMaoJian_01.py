#enconding =utf-8
from selenium import webdriver
import time
for i in range(1,10000):
       driver = webdriver.Firefox()
       driver.get('https://www.93goodtea.com/')
       driver.implicitly_wait(30)
       js = "var q=document.documentElement.scrollTop=10000"
       driver.execute_script(js)
       nowTime = time.strftime("%Y%m%d.%H.%M.%S")
       driver.get_screenshot_as_file('%s.png' % nowTime)
       print(driver.current_url)
       driver.quit()