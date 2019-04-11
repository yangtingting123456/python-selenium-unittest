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

    #confirm对话框---点击确认按钮3
    def test_confirm_accept(self):
        self.driver.find_element_by_xpath('/html/body/div/input[3]').click()
        self.alert = self.driver.switch_to_alert()
        alert_text3=self.alert.text
        print(alert_text3)
        self.assertEqual('你是帅哥吗？',alert_text3)
        self.alert.accept()

    # confirm对话框---点击取消按钮3
    def test_confirm_dismiss(self):
        self.driver.find_element_by_xpath('/html/body/div/input[3]').click()
        alert = self.driver.switch_to_alert()
        alert.dismiss()
        dismiss_text=self.driver.find_element_by_xpath('//*[@id="textSpan"]/font').text
        print(dismiss_text)
        self.assertEqual('您为何如此谦虚？',dismiss_text)

    #输入对话框框，输入1    1
    def test_prompt_accept1(self):
        self.driver.find_element_by_xpath('/html/body/div/input[1]').click()
        alert = self.driver.switch_to_alert()
        alert.send_keys('1')
        alert.accept()
        accetp_test1 = self.driver.find_element_by_xpath('//*[@id="textSpan"]/font').text
        print(accetp_test1)
        self.assertEqual('强哥是真聪明啊', accetp_test1)
        # 输入对话框框，输入1

    # 输入对话框框，输入2    1    1
    def test_prompt_accept2(self):
        self.driver.find_element_by_xpath('/html/body/div/input[1]').click()
        alert = self.driver.switch_to_alert()
        alert.send_keys('2')
        alert.accept()
        accetp_test1 = self.driver.find_element_by_xpath('//*[@id="textSpan"]/font').text
        print(accetp_test1)
        self.assertEqual('左哥是真笨啊', accetp_test1)
        # 输入对话框框，输入1

    # 输入对话框框，输入1,取消
    def test_prompt_dismiss1(self):
        self.driver.find_element_by_xpath('/html/body/div/input[1]').click()
        alert = self.driver.switch_to_alert()
        alert.dismiss()
        accept_test2 = self.driver.find_element_by_xpath('//*[@id="textSpan"]/font').text
        print(accept_test2)
        self.assertEqual('您没有按要求输入，请重新输入', accept_test2)

    def test_prompt_dismiss2(self):
        self.driver.find_element_by_xpath('/html/body/div/input[1]').click()
        alert = self.driver.switch_to_alert()
        alert.send_keys('1')
        alert.dismiss()
        test_prompt_dismiss2 = self.driver.find_element_by_xpath('//*[@id="textSpan"]/font').text
        print(test_prompt_dismiss2)
        self.assertEqual('您没有按要求输入，请重新输入', test_prompt_dismiss2)

    def test_alert_accetp(self):
        self.driver.find_element_by_xpath('/html/body/div/input[2]').click()
        alert = self.driver.switch_to_alert()
        self.assertEqual('用我三世烟火，换你一世迷离', alert.text)
        alert.accept()

    # def test_alert_dismiss(self):
    #     self.driver.find_element_by_xpath('/html/body/div/input[2]').click()
    #     alert = self.driver.switch_to_alert()
    #     self.assertEqual('你用我三世烟火，换你一世迷离', alert.text)
    #     alert.dismiss()

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
    suit.addTest(test_alert('test_prompt_dismiss1'))
    suit.addTest(test_alert('test_prompt_dismiss2'))
    suit.addTest(test_alert('test_alert_accetp'))
    # suit.addTest(test_alert('test_alert_dismiss'))

    fp = open(report_path, 'wb')
    runner = HTMLTestReportCN.HTMLTestRunner(
        stream=fp,
        title='三种对话框的测试用例',
        description='报告中描述部分',
        tester='杨婷婷'
    )
    # 执行测试
    runner.run(suit)




