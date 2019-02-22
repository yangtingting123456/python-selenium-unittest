#enconding =utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Firefox()
driver.get('https://www.baidu.com')
driver.implicitly_wait(30)
#将鼠标移动到‘设置’按钮上
mouse = driver.find_element_by_link_text('设置')
ActionChains(driver).move_to_element(mouse).perform()
driver.find_element_by_link_text('搜索设置').click()
driver.find_element_by_id('nr')
driver.find_element_by_id("nr").find_element_by_xpath("//option[@value='50']").click()