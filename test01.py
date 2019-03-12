from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get("http://timesheet.juneyaokc.com/auth/login")
driver.maximize_window()
driver.implicitly_wait(30)
driver.find_element_by_name('adminUsername').send_keys('杨婷婷')
driver.find_element_by_name('adminPassword').send_keys('ytt123456')
driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/form/div[4]/button').click()
time.sleep(1.5)
driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/table/tbody/tr[1]/td[1]/input').click()
time.sleep(1.5)
#选择需要填入工时的日期
driver.find_element_by_css_selector('html body div#layui-laydate3.layui-laydate div.'
                                    'layui-laydate-main.laydate-main-list-0 div.layui-laydate-content table tbody tr td.layui-this').click()




