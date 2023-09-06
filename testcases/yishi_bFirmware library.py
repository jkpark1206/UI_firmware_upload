from common.browser import Browser
from config.config import *
import unittest
import time

class Yishi_firmware_library(Browser):
    _testMethodDoc = '固件库管理'

    # @unittest.skip
    def test_lib_upload_01(self):
        '''跳转固件库页面'''
        super().firmware_lib_page()
        try:
            self.assertIn('添加固件', self.driver.page_source)
        except Exception as e:
            print(self.test_lib_upload_01.__doc__ + '运行失败', e)
            self.driver.get_screenshot_as_file(image_dir + self.test_lib_upload_01.__doc__ + '.png')

    def test_firm_upload_02(self):
        super().firmware_lib_page()
        super().firm_upload_click()
        time.sleep(3)
        super().file_upload_click(r'C:\Users\anban\Desktop\gujianhuizong\jizhunceshi\libcurl_7.17.1-1_arm.ipk')
        time.sleep(5)
        # try:
        #     self.assertIn('添加任务', self.driver.page_source)
        # except Exception as e:
        #     print(self.test_lib_upload_01.__doc__ + '运行失败', e)
        #     self.driver.get_screenshot_as_file(image_dir + self.test_lib_upload_01.__doc__ + '.png')

if __name__ == '__main__':
    Yishi_firmware_library()