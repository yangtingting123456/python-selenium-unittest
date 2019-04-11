import unittest
from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("https://www.baidu.com")
driver.find_element_by_name("wd").send_keys("selenium")
driver.find_element_by_id("su").click()
time.sleep(3)
driver.back()
time.sleep(3)
driver.forward()
print(driver.current_url)
print(driver.current_window_handle)
# print(driver.name)
# print(driver.orientation)
print(driver.page_source)
print(driver.title)
print(driver.window_handles)
time.sleep(6)
driver.close()