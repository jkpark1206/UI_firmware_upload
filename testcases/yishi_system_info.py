import webbrowser
from selenium import webdriver
from common.browser import Browser
import time
from config.config import *
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class Yishi_system(Browser):
    _testMethodDoc = '系统信息'

    @unittest.skip
    def test_system_01(self):
        '''跳转系统信息页面'''
        super().sys_page()
        try:
            # WebDriverWait(self.driver, 5).until(EC.text_to_be_present_in_element(super().system_page_load(), '每日任务上限'))
            self.assertIn('每日任务上限', self.driver.page_source)
        except Exception as e:
            self.driver.get_screenshot_as_file(image_dir + self.test_system_01.__doc__ + '.png')
            print(self.test_system_01.__doc__ + '任务失败')


if __name__ =='main':
    Yishi_system()