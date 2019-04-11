import unittest
from selenium import webdriver
import time
import os
from selenium.webdriver import ActionChains

driver = webdriver.Firefox()
driver.implicitly_wait(30)
driver.maximize_window()
driver.get("https://www.baidu.com/")
current_handle1 = driver.current_window_handle
print(current_handle1)
driver.find_element_by_id("u1").find_element_by_name("tj_login").click()  # 登录 按钮
# self.driver.find_element_by_id("TANGRAM__PSP_10__footerULoginBtn").click()  # 选择用户登录
time.sleep(3)
driver.find_element_by_link_text('立即注册').click()
current_handle2 = driver.current_window_handle
print('current_handle2：' + current_handle2)
time.sleep(3)
all_handles = driver.window_handles
print(all_handles)
for handle in all_handles:
    if handle != current_handle1:
        driver.switch_to_window(handle)
        print("now is not in current_handle")
        driver.find_element_by_id('TANGRAM__PSP_3__userName').send_keys('ytt05_091')
        driver.find_element_by_id('TANGRAM__PSP_3__phone').send_keys('17633710286')

        driver.find_element_by_id('TANGRAM__PSP_3__password').send_keys('ytt05_09')
        # self.driver.find_element_by_id('TANGRAM__PSP_3__verifyCodeSend').click()
        # a = input('请手动输入验证码')
        # self.driver.find_element_by_id('TANGRAM__PSP_3__verifyCode').send_keys(a)
        # self.driver.find_element_by_id('TANGRAM__PSP_3__isAgree').click()
        # self.driver.find_element_by_id('TANGRAM__PSP_3__submit').click()
        time.sleep(2)
        driver.find_element_by_id('TANGRAM__PSP_22__confirm_continue').click()
        driver.find_element_by_id('TANGRAM__PSP_3__footerULoginBtn').click()

# driver.find_element_by_link_text('忘记密码？').click()
# driver.find_element_by_id('account').send_keys('17633710286')
# driver.find_element_by_id('TANGRAM__PSP_3__userName').send_keys('17633710286')
driver.find_element_by_id('TANGRAM__PSP_3__password').send_keys('ytt123456.')
driver.find_element_by_id('TANGRAM__PSP_3__submit').click()
driver.find_element_by_id('pass-mobile-sure-btn').click()
time.sleep(3)
ActionChains(driver).move_to_element(driver.find_element_by_link_text('巨蟹和别的')).perform()
driver.find_element_by_link_text('退出').click()
time.sleep(3)
driver.find_element_by_link_text('确定').click()

time.sleep(6)

driver.quit()

