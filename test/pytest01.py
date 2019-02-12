from selenium import webdriver
import unittest
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import HTMLTestReportCN
import os
from TestLogin import TestLogin

class SearchTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Firefox()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()
        # self.driver.get("https://www.baidu.com")

    def test_baidu_searsh1(self):
        time.sleep(3)
        self.driver.get("https://www.baidu.com")
        self.wd= self.driver.find_element_by_name("wd")
        self.wd.send_keys("selenium")
        self.su=self.driver.find_element_by_id("su")
        self.su.click()

    def test_baidu_searsh2(self):
        time.sleep(3)
        self.driver.get("https://www.baidu.com")
        self.wd = self.driver.find_element_by_name("wd")
        self.wd.send_keys("python")
        self.su = self.driver.find_element_by_id("su")
        self.su.click()

    def test_baidu_searsh3(self):
        time.sleep(3)
        self.driver.get("https://www.baidu.com")
        self.wd = self.driver.find_element_by_name("wd")
        self.wd.send_keys("unittest")
        self.su = self.driver.find_element_by_id("su")
        self.su.click()

    def test_baidu_searsh4(self):
        time.sleep(3)
        self.driver.get("https://www.baidu.com")
        self.wd = self.driver.find_element_by_name("wd")
        self.wd.send_keys("jenkins")
        self.su = self.driver.find_element_by_id("su")
        self.su.click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()


if __name__ == '__main__':
    path = os.getcwd()
    report_path = path + 'result.html'
    # 如果路径不存在，创建路径
    if not os.path.exists(path):
        os.makedirs(path)
    else:
        pass
    suit = unittest.TestSuite()
    suit.addTest(SearchTests('test_baidu_searsh2'))
    suit.addTest(SearchTests('test_baidu_searsh3'))
    suit.addTest(SearchTests('test_baidu_searsh4'))
    suit.addTest(SearchTests('test_baidu_searsh1'))
    time.sleep(3)
    suit.addTest(TestLogin('test_alogin'))
    suit.addTest(TestLogin('test_bBewEasy'))
    suit.addTest(TestLogin('test_Quit'))
    suit.addTest(TestLogin('test_Tclose'))

    fp = open(report_path, 'wb')
    runner = HTMLTestReportCN.HTMLTestRunner(
        stream=fp,
        title='百度自动化搜索',
        description='报告中描述部分',
        tester='杨婷婷'
    )
    # 执行测试
    runner.run(suit)




# import unittest
# from selenium import webdriver
#
# class SearchTests(unittest.TestCase):
#     def setUp(self):
#         # create a new Firefox session
#         self.driver = webdriver.Firefox()
#         self.driver.implicitly_wait(30)
#         self.driver.maximize_window()
#
#         # navigate to the application home page
#         self.driver.get("http://192.168.6.51:8080/login.jsp")
#
#     def test_search_by_category(self):
#         # get the search textbox
#         self.search_field = self.driver.find_element_by_id("_easyui_textbox_input1")
#         self.search_field.clear()
#
#         # enter search keyword and submit
#         self.search_field.send_keys("admin")
#         self.search_field.submit()
#
#
#         products = self.driver.find_element_by_id ("_easyui_textbox_input2").send_keys("54321")
#         # self.assertEqual(2, len(products))
#         submit = self.driver.find_element_by_xpath("/html/body/div/div/form/p[3]/input").click()
#
#     def tearDown(self):
#         # close the browser window
#         self.driver.quit()
#
# if __name__ == '__main__':
#     unittest.main(verbosity=2)