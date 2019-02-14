import unittest
from selenium import webdriver
import time
import HTMLTestReportCN
import os

class test_alert(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(30)
        # driver.maximize_window()
        get_path = os.getcwd()
        path = get_path + 'index.html'
        cls.driver.get('file:///E:/Python37/Scripts/TestL/index.html')

    #confirm对话框---点击确认按钮
    def test_confirm_accept(self):
        self.driver.find_element_by_xpath('/html/body/div/input[3]').click()
        self.alert = self.driver.switch_to_alert()
        self.alert.accept()

    # confirm对话框---点击取消按钮
    def test_confirm_dismiss(self):
        self.driver.find_element_by_xpath('/html/body/div/input[3]').click()
        alert = self.driver.switch_to_alert()
        alert.dismiss()

    #输入对话框框，输入1
    def test_prompt_accept(self):
        self.driver.find_element_by_xpath('/html/body/div/input[1]').click()
        alert = self.driver.switch_to_alert()
        alert.send_keys('1')
        alert.accept()
        # 输入对话框框，输入1

    # 输入对话框框，输入1
    def test_prompt_accept1(self):
        self.driver.find_element_by_xpath('/html/body/div/input[1]').click()
        alert = self.driver.switch_to_alert()
        alert.send_keys('2')
        alert.accept()

    # 输入对话框框，输入1,取消
    def test_prompt_accept2(self):
        self.driver.find_element_by_xpath('/html/body/div/input[1]').click()
        alert = self.driver.switch_to_alert()
        alert.send_keys('1')
        alert.accept()

    def test_prompt_dismiss(self):
        self.driver.find_element_by_xpath('/html/body/div/input[1]').click()
        alert = self.driver.switch_to_alert()
        alert.send_keys('1')
        alert.dismiss()

    def test_alert_accetp(self):
        self.driver.find_element_by_xpath('/html/body/div/input[1]').click()
        alert = self.driver.switch_to_alert()
        alert.accept()

    def test_alert_dismiss(self):
        self.driver.find_element_by_xpath('/html/body/div/input[1]').click()
        alert = self.driver.switch_to_alert()
        alert.dismiss()

    @classmethod
    def tearDown(cls):
        cls.driver.quit()

if __name__ == '__main__':
    path = os.getcwd()
    report_path = path + 'Report.html'
    # 如果路径不存在，创建路径
    if not os.path.exists(path):
        os.makedirs(path)
    else:
        pass
    suit=unittest.TestSuite()
    suit.addTest(test_alert('test_confirm_accept'))
    suit.addTest(test_alert('test_confirm_dismiss'))
    suit.addTest(test_alert('test_prompt_accept1'))
    suit.addTest(test_alert('test_prompt_accept2'))
    suit.addTest(test_alert('test_prompt_dismiss'))
    suit.addTest(test_alert('test_alert_accetp'))
    suit.addTest(test_alert('test_alert_dismiss'))

    fp = open(report_path, 'wb')
    runner = HTMLTestReportCN.HTMLTestRunner(
        stream=fp,
        title='百度自动化搜索',
        description='报告中描述部分',
        tester='杨婷婷'
    )
    # 执行测试
    runner.run(suit)




