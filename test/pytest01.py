from selenium import webdriver
import unittest

class SearchTests(unittest.TestCase):
        def setUp(self):
            self.driver=webdriver.Firefox()
            self.driver.implicitly_wait(30)
            self.driver.maximize_window()
            self.driver.get("https://www.baidu.com")

        def test_baidu_searsh1(self):
            self.wd= self.driver.find_element_by_name("wd")
            self.wd.send_keys("selenium")
            self.su=self.driver.find_element_by_id("su")
            self.su.click()

        def test_baidu_searsh2(self):
            self.wd = self.driver.find_element_by_name("wd")
            self.wd.send_keys("python")
            self.su = self.driver.find_element_by_id("su")
            self.su.click()

        def test_baidu_searsh3(self):
            self.wd = self.driver.find_element_by_name("wd")
            self.wd.send_keys("unittest")
            self.su = self.driver.find_element_by_id("su")
            self.su.click()

        def tearDown(self):
            self.driver.close()


if __name__ == '__main__':
    unittest.main(verbosity=2)



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