import selenium
import os
from selenium import webdriver

driver = webdriver.Firefox()
driver.implicitly_wait(30)
# driver.maximize_window()
get_path = os.getcwd()
path = get_path + 'index.html'
driver.get(path)