import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.alert import Alert

class Test_BaiDu(unittest.TestCase):
    @classmethod
    def setUp(cls):
        # create a new Firefox session """
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()
        # navigate to the application home page """
        cls.driver.get("https://www.baidu.com/")

    def test_Regist(self):
        self.driver.get("https://www.baidu.com/")
        current_handle1=self.driver.current_window_handle
        print(current_handle1)
        self.driver.find_element_by_id("u1").find_element_by_name("tj_login").click()  # 登录 按钮
        # self.driver.find_element_by_id("TANGRAM__PSP_10__footerULoginBtn").click()  # 选择用户登录
        time.sleep(3)
        self.driver.find_element_by_link_text('立即注册').click()
        current_handle2 = self.driver.current_window_handle
        print('current_handle2：'+current_handle2)
        time.sleep(3)
        all_handles=self.driver.window_handles
        print(all_handles)
        for handle in all_handles:
            while handle != current_handle1:
                self.driver.switch_to_window(handle)
                print("now is not in current_handle")
                self.driver.find_element_by_id('TANGRAM__PSP_3__userName').send_keys('ytt05_091')
                self.driver.find_element_by_id('TANGRAM__PSP_3__phone').send_keys('17633710286')

                self.driver.find_element_by_id('').send_keys('ytt05_09')
                # self.driver.find_element_by_id('TANGRAM__PSP_3__verifyCodeSend').click()
                # a = input('请手动输入验证码')
                # self.driver.find_element_by_id('TANGRAM__PSP_3__verifyCode').send_keys(a)
                # self.driver.find_element_by_id('TANGRAM__PSP_3__isAgree').click()
                # self.driver.find_element_by_id('TANGRAM__PSP_3__submit').click()

            alert=self.driver.switch_to_alert()
            
            time.sleep(6)
            alert.accept()
            alert=self.driver.find_element_by_id("TANGRAM__PSP_22__confirm_continue").click()




    @classmethod
    def tearDownClass(cls):
        time.sleep(6)
        try:
            cls.driver.quit()
        except:
            print('e')


if __name__ == '__main__':
    unittest.main(verbosity=2)