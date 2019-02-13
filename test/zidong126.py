#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
from selenium import webdriver
driver = webdriver.Chrome()
host = 'https://mail.126.com/'

def Register():#注册
    driver.get('http://reg.email.163.com/unireg/call.do?cmd=register.entrance&from=126mail')#打开主页
    time.sleep(0.5)

    regist_name = 'chouting888'
    regist_pass = 'chouting8888'
    mobile = '18621853784'
    code = '图形验证码'#验证码 手动识别输入
    duanxin_code = '短信验证码'#短信验证码

    driver.find_element_by_id('nameIpt').send_keys(regist_name) #邮件地址
    time.sleep(0.5)
    driver.find_element_by_id('mainPwdIpt').send_keys(regist_pass)#密码
    time.sleep(0.5)
    driver.find_element_by_id('mainCfmPwdIpt').send_keys(regist_pass)  #确认密码
    time.sleep(0.5)

    driver.find_element_by_id('mainMobileIpt').send_keys(mobile)  # 手机号码
    time.sleep(0.5)

    driver.find_element_by_id('vcodeIpt').send_keys(code)  # 验证码
    time.sleep(20)

    driver.find_element_by_id('sendMainAcodeStg').click() # 点击获取验证码
    time.sleep(20)

    driver.find_element_by_id('mainAcodeIpt').send_keys(duanxin_code)  # 点击获取验证码
    time.sleep(10)

    driver.find_element_by_id('mainRegA').click() #立即注册
    pass

def Login():#登录
    driver.get(host)#打开主页
    driver.implicitly_wait(30)
    time.sleep(1.5)
    driver.find_element_by_id('lbNormal').click()
    time.sleep(0.5)

    u_name = 'chouting888'
    u_pass = 'chouting8888'
    time.sleep(3)
    driver.find_element_by_class_name('dlemail').send_keys(u_name)
    time.sleep(0.5)
    driver.find_element_by_class_name('dlpwd').send_keys(u_pass)
    time.sleep(0.5)

    driver.find_element_by_id('dologin').click()#确定
    pass

#
# Register()
Login()