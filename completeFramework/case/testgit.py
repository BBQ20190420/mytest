import time
import unittest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from completeFramework.config import readconf
import ddt
import os

user1=readconf.user1
pwd1=readconf.pwd1
user2=readconf.user2
pwd2=readconf.pwd2
user3=readconf.user3
pwd3=readconf.pwd3

#测试数据
testdata=[
    {"username":user1,"password":pwd1},
    {"username": user2, "password": pwd2},
    {"username": user3, "password": pwd3},

]

@ddt.ddt
class testlogin(unittest.TestCase):
    # @classmethod
    # # def setUpClass(cls):
    # #     """打开github"""
    # #     cls.driver = webdriver.Chrome()
    # #     cls.driver.get("https://github.com/login")
    # #     cls.driver.implicitly_wait(10)

    def setUp(self):
        """打开github"""
        self.option=webdriver.ChromeOptions()
        self.option.add_argument('headless')
        self.driver=webdriver.Chrome(chrome_options=self.option)
        self.driver.get("https://github.com/login")
        self.driver.implicitly_wait(5)



    def login_in(self, user, password):
        # 登录，输入用户名密码并点击登录
        self.driver.find_element_by_name("login").send_keys(user)
        self.driver.find_element_by_id("password").send_keys(password)
        time.sleep(2)
        self.driver.find_element_by_name("commit").click()
        time.sleep(2)

        # 判断是否登录成功
        # self.driver.find_element_by_css_selector(
        #     "body > div.position-relative.js-header-wrapper > header > div.Header-item.position-relative.mr-0.d-none.d-lg-flex > details > summary > img").click()
        # # name = self.driver.find_element_by_xpath("/html/body/div[1]/header/div[8]/details/details-menu/div[1]/a/strong").text
        # # print(name)
        # # if name == user:
        # #     print("登录成功！")
        # # else:
        # #     print("登录失败！")
        # self.assertEqual(name,user)

    def is_login_success(self):
        try:
            # 判断是否登录成功
            set = self.driver.find_element_by_css_selector(
                "body > div.position-relative.js-header-wrapper > header > div.Header-item.position-relative.mr-0.d-none.d-lg-flex > details > summary > img")
        except NoSuchElementException as msg:
            print(msg)
            print(type(msg))
            return False
        else:
            set.click()
            name = self.driver.find_element_by_xpath(
                "/html/body/div[1]/header/div[8]/details/details-menu/div[1]/a/strong").text
            print(name)
            return True

    @ddt.data(*testdata)
    def test_01(self,data):
        """测试github登录功能"""
        try:
            user = data['username']
            pwd = data['password']
            self.login_in(user, pwd)
            result = self.is_login_success()
            self.assertTrue(result)
            # self.login_out()
        except Exception as msg:
            print(msg)
            initpath = os.path.dirname(os.getcwd())
            reportpath = os.path.join(initpath, 'screen')
            print(reportpath)
            nowtime = time.strftime("%Y%m%d.%H.%M.%S")
            self.driver.get_screenshot_as_file(reportpath + "/" + "%s.png" % nowtime)
            raise




    # def test_02(self):
    #     user = "BBQ20190420"
    #     pwd = "youareapig2000"
    #     self.login_in(user,pwd)
    #     result=self.is_login_success()
    #     self.assertFalse(result)

    # def test_03(self):
    #     """验证登录用户名是否一致"""
    #     user = "BBQ20190420"
    #     pwd = "youareapig2012"
    #     self.login_in(user, pwd)
    #     location=("xpath","/html/body/div[1]/header/div[8]/details/details-menu/div[1]/a/strong")
    #     result=EC.text_to_be_present_in_element(location,user)(self.driver)
    #     self.assertTrue(result)

    def login_out(self):
        self.driver.refresh()
        time.sleep(2)
        self.driver.find_element_by_css_selector(
            "body > div.position-relative.js-header-wrapper > header > div.Header-item.position-relative.mr-0.d-none.d-lg-flex > details > summary > img").click()
        self.driver.find_element_by_css_selector(
            "body > div.position-relative.js-header-wrapper > header > div.Header-item.position-relative.mr-0.d-none.d-lg-flex > details > details-menu > form > button").click()
        time.sleep(2)
        # self.driver.refresh()
        # print("关闭浏览器")
        # driver.close()
        # driver.quit()

    # @classmethod
    # def tearDownClass(cls):
    #     """关闭浏览器"""
    #     cls.driver.quit()

    def tearDown(self):
        """关闭浏览器"""
        self.driver.quit()

    if __name__ == '__main__':
        unittest.main()

