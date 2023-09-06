from common.browser import Browser
import time
from common.HTMLTestRunner import TestResult
from config.config import *
import unittest

class Yishi_Register(Browser):
    _testMethodDoc = '跳转修改密码页'

    # @unittest.skip
    def test_register_01(self):
        '''跳转修改密码页'''
        super().login_url()
        super().register_skip()
        time.sleep(wait_time)
        try:
           self.assertIn('返回登录',self.driver.page_source)
        except Exception as e:
           self.driver.get_screenshot_as_file(image_dir+self.test_register_01.__doc__+'.png')

    # @unittest.skip
    def test_register_02(self):
        '''成功修改密码'''
        super().register_url()
        super().register_input_data('root','1234567','安般')
        super().register_click()
        time.sleep(wait_time)
        try:
           self.assertIn('用户登录',self.driver.page_source)
        except Exception as e:
           self.driver.get_screenshot_as_file(image_dir+self.test_register_02.__doc__+'.png')

    # @unittest.skip
    def test_register_03(self):
        '''用户名错误'''
        super().register_url()
        super().register_input_data('roo','1234567','安般')
        super().register_click()
        time.sleep(wait_time)
        try:
           self.assertIn('用户或密保参数错误！',self.driver.page_source)
        except Exception as e:
           self.driver.get_screenshot_as_file(image_dir+self.test_register_03.__doc__+'.png')

    # @unittest.skip
    def test_register_04(self):
        '''密保密码错误'''
        super().register_url()
        super().register_input_data('root','1234567','安')
        super().register_click()
        time.sleep(wait_time)
        try:
           self.assertIn('用户或密保参数错误！',self.driver.page_source)
        except Exception as e:
           self.driver.get_screenshot_as_file(image_dir+self.test_register_04.__doc__+'.png')

    # @unittest.skip
    def test_register_05(self):
        '''用户名为空'''
        super().register_url()
        super().register_input_data('','1234567','安般')
        super().register_click()
        time.sleep(wait_time)
        try:
           self.assertIn('输入您的用户名',self.driver.page_source)
        except Exception as e:
           self.driver.get_screenshot_as_file(image_dir+self.test_register_05.__doc__+'.png')

    # @unittest.skip
    def test_register_06(self):
        '''新密码为空'''
        super().register_url()
        super().register_input_data('root','','安般')
        super().register_click()
        time.sleep(wait_time)
        try:
           self.assertIn('输入您的密码',self.driver.page_source)
        except Exception as e:
           self.driver.get_screenshot_as_file(image_dir+self.test_register_06.__doc__+'.png')

    # @unittest.skip
    def test_register_07(self):
        '''密保密码为空'''
        super().register_url()
        super().register_input_data('root','1234567','')
        super().register_click()
        time.sleep(wait_time)
        try:
           self.assertIn('请输入密保',self.driver.page_source)
        except Exception as e:
           self.driver.get_screenshot_as_file(image_dir+self.test_register_07.__doc__+'.png')

    # @unittest.skip
    def test_register_08(self):
        '''直接返回登录页面'''
        super().register_url()
        super().login_return_click()
        time.sleep(wait_time)
        try:
           self.assertIn('http://{}#/'.format(URL),self.driver.current_url)
        except Exception as e:
           self.driver.get_screenshot_as_file(image_dir+self.test_register_08.__doc__+'.png')


if __name__=='__main__':
    Yishi_Register()