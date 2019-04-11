# from selenium import webdriver
# import time
# driver =webdriver.Chrome()
# driver.get("http://192.168.6.51:8080/login.jsp")
# driver.find_element_by_id("_easyui_textbox_input1").send_keys("admin")
# driver.find_element_by_id("_easyui_textbox_input2").send_keys("54321")
# driver.find_element_by_xpath("/html/body/div/div/form/p[3]/input").click()
# driver.find_element_by_link_text("文章管理").click()
# driver.find_element_by_link_text("新增").click()
# driver.find_element_by_id("_easyui_textbox_input12").send_keys("文章标题111")
# driver.find_element_by_id("_easyui_textbox_input13").send_keys("文章副标题11")
# driver.find_element_by_id("_easyui_textbox_input17").send_keys("自动化测试1")
# driver.find_element_by_css_selector("#article_submit > span").click()
# driver.find_element_by_xpath("/html/body/div[12]/div[3]/a/span").click()
# time.sleep(3)
# d=driver.switch_to_alert()
# d.accept()
#
import requests

url = "http://192.168.1.127:8282/api/account/login"

payload = "deviceOs=%20ios&version=5.2.2&username=17765101413&password=111111&authToken=&client=uuid&undefined="
headers = {
    'Content-Type': "application/x-www-form-urlencoded",
    'cache-control': "no-cache",
    'Postman-Token': "60981d4b-e16c-4512-8222-f51a532c18b9"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)