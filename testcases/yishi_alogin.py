from common.browser import Browser
import time
from common.HTMLTestRunner import TestResult
from config.config import *
import unittest

class Yishi_Login(Browser):
    _testMethodDoc = '登录测试'
    # @unittest.skip
    def test_Login_01(self):
        '''正确用户名，正确密码'''
        super().login_url()
        super().login_input(user_name,passwd)
        super().login_click()
        try:
           self.assertEqual('http://{}#/vulnerabilityScanTask'.format(URL),self.driver.current_url)
        except Exception as e:
           print(self.test_Login_01.__doc__,e)
           self.driver.get_screenshot_as_file(image_dir+self.test_Login_01.__doc__+'.png')

    @unittest.skip
    def test_Login_02(self):
        '''用户名错误'''
        super().login_url()
        super().login_input('roo','1234567')
        super().login_click()
        try:
           self.assertIn('用户[roo]登录失败，原因:用户名或密码错误', self.driver.page_source)
        except Exception as e:
           self.driver.get_screenshot_as_file(image_dir+self.test_Login_02.__doc__+'.png')

    @unittest.skip
    def test_Login_03(self):
        '''密码错误'''
        super().login_url()
        super().login_input('root','123456')
        super().login_click()
        try:
           self.assertIn('用户[root]登录失败，原因:用户名或密码错误', self.driver.page_source)
        except Exception as e:
           self.driver.get_screenshot_as_file(image_dir+self.test_Login_03.__doc__+'.png')

    @unittest.skip
    def test_Login_04(self):
        '''密码为空'''
        super().login_url()
        super().login_input('wwh', '')
        super().login_click()

        try:
            self.assertIn('输入您的密码', self.driver.page_source)
        except Exception as e:
            self.driver.get_screenshot_as_file(image_dir + self.test_Login_03.__doc__ + '.png')

    @unittest.skip
    def test_Login_05(self):
        '''用户名为空'''
        super().login_url()
        super().login_input('', '123456')
        super().login_click()

        try:
            self.assertIn('输入您的用户名', self.driver.page_source)
        except Exception as e:
            self.driver.get_screenshot_as_file(image_dir + self.test_Login_03.__doc__ + '.png')

    @unittest.skip
    def test_Login_06(self):
        '''用户名密码均为空'''
        super().login_url()
        super().login_input('', '')
        super().login_click()
        try:
            self.assertIn('输入您的用户名', self.driver.page_source)
            self.assertIn('输入您的密码', self.driver.page_source)
        except Exception as e:
            self.driver.get_screenshot_as_file(image_dir + self.test_Login_03.__doc__ + '.png')



if __name__=="__main__":
    Yishi_Login()