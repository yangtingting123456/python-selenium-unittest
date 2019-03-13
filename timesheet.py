import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.alert import Alert
import datetime
import Include
class TimeSheet(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get("http://timesheet.juneyaokc.com/auth/login")
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(30)
        # 输入用户名
        cls.driver.find_element_by_name('adminUsername').send_keys('杨婷婷')
        # 输入密码
        cls.driver.find_element_by_name('adminPassword').send_keys('ytt123456')
        # 点击登陆代码
        cls.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/form/div[4]/button').click()
        time.sleep(3)

    # def test_Login(self):
    #     self.driver.get("http://timesheet.juneyaokc.com/auth/login")
    #     #输入用户名
    #     time.sleep(3)
    #     self.driver.find_element_by_name('adminUsername').send_keys('杨婷婷')
    #     # 输入密码
    #     time.sleep(3)
    #     self.driver.find_element_by_name('adminPassword').send_keys('ytt123456')
    #     # 点击登陆代码
    #     self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/form/div[4]/button').click()

    def test_dd(self):
        # 获取当前时间
        t_date = datetime.date.today()
        print(t_date)
        # 获取星期几
        week_day = int(t_date.strftime("%w"))
        print(week_day)
        if week_day<=5:
            self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/table/tbody/tr[1]/td[1]/input').click()
            time.sleep(1.5)
            #选择需要填入工时的日期
            self.driver.find_element_by_css_selector('html body div#layui-laydate3.layui-laydate div.'
                                                'layui-laydate-main.laydate-main-list-0 div.layui-laydate-content table tbody tr td.layui-this').click()

            #选择项目
            self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/table/tbody/tr[1]/td[2]/select').click()
            time.sleep(1.5)
            self.driver.find_element_by_css_selector('.selectProduct > option:nth-child(2)').click()
            #分类
            self.driver.find_element_by_id('typeChoose').click()
            time.sleep(1.5)
            self.driver.find_element_by_css_selector('#typeChoose > option:nth-child(5)').click()
            #调研评估，选择调研某个项目
            self.driver.find_element_by_id('pointChoose').click()
            self.driver.find_element_by_css_selector('#pointChoose > option:nth-child(2)').click()
            #填写今天工作的工时
            self.driver.find_element_by_css_selector('.timeText').send_keys('8')
            #提交此次的记录
            self.driver.find_element_by_css_selector('.workTr > td:nth-child(5) > button:nth-child(1)').click()
            time.sleep(1.5)
            self.driver.switch_to_alert().accept()
            time.sleep(6)
            # self.driver.quit()

    # def test_ZDelete(self):
    #     time.sleep(6)
    #     self.driver.find_element_by_css_selector('#obj_table > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(5) > a:nth-child(1)').click()
    #     self.driver.switch_to_alert().accept()

    @classmethod
    def tearDownClass(cls):
        time.sleep(1.5)
        try:
            cls.driver.quit()
        except:
            print('e')


if __name__ == '__main__':
    unittest.main(verbosity=2)







































# driver = webdriver.Firefox()
# driver.get("http://timesheet.juneyaokc.com/auth/login")
# driver.maximize_window()
# driver.implicitly_wait(30)
#输入用户名
# driver.find_element_by_name('adminUsername').send_keys('杨婷婷')
#输入密码
# driver.find_element_by_name('adminPassword').send_keys('ytt123456')
#点击登陆代码
# driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/form/div[4]/button').click()
# time.sleep(1.5)
# driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/table/tbody/tr[1]/td[1]/input').click()
# time.sleep(1.5)
# #选择需要填入工时的日期
# driver.find_element_by_css_selector('html body div#layui-laydate3.layui-laydate div.'
#                                     'layui-laydate-main.laydate-main-list-0 div.layui-laydate-content table tbody tr td.layui-this').click()
#
# #选择项目
# driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/table/tbody/tr[1]/td[2]/select').click()
# time.sleep(1.5)
# driver.find_element_by_css_selector('.selectProduct > option:nth-child(2)').click()
# #分类
# driver.find_element_by_id('typeChoose').click()
# time.sleep(1.5)
# driver.find_element_by_css_selector('#typeChoose > option:nth-child(5)').click()
# #调研评估，选择调研某个项目
# driver.find_element_by_id('pointChoose').click()
# driver.find_element_by_css_selector('#pointChoose > option:nth-child(2)').click()
# #填写今天工作的工时
# driver.find_element_by_css_selector('.timeText').send_keys('8')
# #提交此次的记录
# driver.find_element_by_css_selector('.workTr > td:nth-child(5) > button:nth-child(1)').click()
# time.sleep(1.5)
# driver.switch_to_alert().accept()












