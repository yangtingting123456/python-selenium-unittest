#encoding = utf-8
from selenium import webdriver
driver = webdriver.Firefox()
driver.get('file:///C:/Users/hongchao.yang/Desktop/checkandradio.html')
driver.implicitly_wait(30)
driver.find_element_by_id('boy').click()
driver.find_element_by_id('submit').click()
driver.find_element_by_id('c1').click()
driver.find_element_by_id('c2').click()

