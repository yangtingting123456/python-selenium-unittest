#enconding =utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
driver = webdriver.Firefox()
driver.get('https://www.baidu.com')
driver.implicitly_wait(30)
#将鼠标移动到‘设置’按钮上
mouse = driver.find_element_by_link_text('设置')
ActionChains(driver).move_to_element(mouse).perform()
driver.find_element_by_link_text('搜索设置').click()
driver.find_element_by_id('nr')
#定位下拉列表的方式1
driver.find_element_by_id("nr").find_element_by_xpath("//option[@value='50']").click()
#定位下拉列表的方式2
s=driver.find_element_by_id('nr')
Select(s).select_by_index(2)
Select(s).select_by_value('20')
Select(s).select_by_visible_text("每页显示50条")

