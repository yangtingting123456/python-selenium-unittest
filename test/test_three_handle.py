import unittest
from selenium import webdriver

class Test_More_handle(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(30)
        defaule_window = cls.driver.get("https://www.baidu.com")
        window2= cls.driver.get('http://www.jd.com')
        window3 = cls.driver.get('http://www.126.com')


