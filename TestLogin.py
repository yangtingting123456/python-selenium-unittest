import unittest
from selenium import webdriver
import time
import HTMLTestReportCN
import os
from Email_Fu import Email_Fu

class TestLogin(unittest.TestCase):
    driver = webdriver.Chrome()
    base_url = "http://192.168.6.51:8080"
    def setUp(self):
        self.driver=self.driver
        self.driver.implicitly_wait(30)
        base_url = "http://192.168.6.51:8080"
        verificationErrors = []
        accept_next_alert = True

    #oms登录
    def test_login(self):
        try:
            driver = self.driver
            driver.get(self.base_url+"/login.jsp")
            driver.find_element_by_id("_easyui_textbox_input1").send_keys("admin")
            driver.find_element_by_id("_easyui_textbox_input2").send_keys("54321")
            driver.find_element_by_xpath("/html/body/div/div/form/p[3]/input").click()
        except:
            print("登录失败")

    def test_Quit(self):
        try:
            driver = self.driver
            driver.find_element_by_class_name("iconfont icon-tuichu font-red").click()
        except:
            print("退出失败")


    def tearDown(self):
        time.sleep(3)
        self.driver.quit()

if __name__ == '__main__':
    # 定义测试报告的地址
    path = 'D:\\result\\'
    report_path = path + 'result.html'
    # 如果路径不存在，创建路径
    if not os.path.exists(path):
        os.makedirs(path)
    else:
        pass
    suit = unittest.TestSuite()
    suit.addTest(TestLogin('test_login'))
    # suit.addTest(TestLogin('test_Quit'))
    fp = open(report_path, 'wb')
    runner = HTMLTestReportCN.HTMLTestRunner(
        stream=fp,
        title='sish的UI自动化测试报告',
        description='报告中描述部分',
        tester='ytt'
    )
    # 执行测试
    runner.run(suit)
    fp.close()
    Email_Fu.mail(2)


