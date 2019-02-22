# import unittest
# from selenium import webdriver
# import time
#
# driver = webdriver.Firefox()
# driver.get("https://mail.126.com/")
# driver.maximize_window()
# driver.implicitly_wait(30)
# #获取当前窗口的句柄
# current_window = driver.current_window_handle
# driver.find_element_by_id("lbNormal").click()
#
# driver.switch_to.frame('x-URS-iframe1550023994130.7668')   #切换到iframe
#
#
# time.sleep(2)
# driver.find_element_by_id('changepage').click()
#
#
#
# time.sleep(2)
# all_windows = driver.window_handles
# #进入注册的窗口
# for handle in all_windows:
#     if handle!= current_window:
#         print('now is register window!')
#         time.sleep(2)


from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

# 浏览器驱动放在了c:\\Python36\\Scripts目录下，无需指定参数
driver = webdriver.Chrome()
driver.get("https://mail.126.com/")
time.sleep(3)
####登陆
driver.find_elements_by_id("x-URS-iframe")
driver.switch_to.frame("x-URS-iframe")
user_name = driver.find_element_by_xpath('//*[@name="email"]')
# 将xxxxxxx替换为自己的用户名
user_name.send_keys('xxxxxxx')
pass_word = driver.find_element_by_xpath('//*[@name="password"]')
# 将11111111111替换为自己的密码
pass_word.send_keys('11111111111')
button = driver.find_element_by_id("dologin")
button.click()
driver.switch_to.default_content()
time.sleep(3)


















# from selenium import webdriver
# from time import sleep
#
# driver = webdriver.Firefox()
# driver.implicitly_wait(10)
# driver.get("https://mail.126.com/")
#
# # 获得百度学术搜索窗口句柄
# search_windows = driver.current_window_handle
# sleep(2)
#
# driver.find_element_by_link_text('注册').click()
# sleep(2)
#
# # 获得当前所有打开的窗口的句柄
# all_handles = driver.window_handles
#



# # 进入注册窗口
# for handle in all_handles:
#     if handle!=search_windows:
#         print('now is register window!')
#         sleep(2)

# 回到学术搜索窗口
# for handle in all_handles:
#     if handle == search_windows:
#         driver.switch_to.window(search_windows)
#         sleep(2)
#         print("now is search window!")
#         driver.find_element_by_id('kw').send_keys('selenium')
#         driver.find_element_by_id('su').click()
#         sleep(2)
#
# driver.quit()