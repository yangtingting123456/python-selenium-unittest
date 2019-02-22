# coding:utf-8
from selenium import webdriver
import time,unittest
from selenium.webdriver.support import expected_conditions as EC
class Login(unittest.TestCase):
    def setUp(self):
        url_login = "https://passport.cnblogs.com/user/signin"
        self.driver = webdriver.Firefox()
        self.driver.get(url_login)

    def test_01(self):
        '''前面输入账号密码，让正确运行到assert这一步，断言故意设置为False不成功'''
        try:
            self.driver.find_element_by_id("input1").send_keys("yangtingting1")
            self.driver.find_element_by_id("input2").send_keys("ytt123456.")
            # 登录id是错的，定位会抛异常
            self.driver.find_element_by_id("signin").click()
            #　判断登录成功页面是否有账号："上海-悠悠"
            time.sleep(6)
            locator = ("id", "lnk_current_user")
            result = EC.text_to_be_present_in_element(locator,"皓空星辰")(self.driver)
            self.assertTrue(result)
        except Exception as msg:
            print(u"异常原因%s"%msg)
            # 图片名称可以加个时间戳
            nowTime = time.strftime("%Y%m%d.%H.%M.%S")
            self.driver.get_screenshot_as_file('%s.jpg' % nowTime)
            raise

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()