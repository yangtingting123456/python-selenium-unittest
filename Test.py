from selenium import webdriver
import time
driver =webdriver.Chrome()
driver.get("http://192.168.6.51:8080/login.jsp")
driver.find_element_by_id("_easyui_textbox_input1").send_keys("admin")
driver.find_element_by_id("_easyui_textbox_input2").send_keys("54321")
driver.find_element_by_xpath("/html/body/div/div/form/p[3]/input").click()
driver.find_element_by_link_text("文章管理").click()
driver.find_element_by_link_text("新增").click()
driver.find_element_by_id("_easyui_textbox_input12").send_keys("文章标题111")
driver.find_element_by_id("_easyui_textbox_input13").send_keys("文章副标题11")
driver.find_element_by_id("_easyui_textbox_input17").send_keys("自动化测试1")
driver.find_element_by_css_selector("#article_submit > span").click()
driver.find_element_by_xpath("/html/body/div[12]/div[3]/a/span").click()
time.sleep(3)
d=driver.switch_to_alert()
d.accept()

