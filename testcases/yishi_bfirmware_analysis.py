from common.browser import Browser
import time
from config.config import *
import unittest
from selenium.webdriver.common.by import By


class Yishi_firmware_analysis(Browser):
    _testMethodDoc = '固件扫描分析'

    @unittest.skip
    def test_upload_01(self):
        '''跳转上传固件页面'''
        super().login_url()
        super().login_input(user_name,passwd)
        super().login_click()
        super().firmware_upload_click()

        try:
           self.assertIn('点击上传',self.driver.page_source)
        except Exception as e:
           print(self.test_upload_01.__doc__+'运行失败',e)
           self.driver.get_screenshot_as_file(image_dir+self.test_upload_01.__doc__+'.png')

    @unittest.skip
    def test_upload_02(self):
        '''成功上传固件任务-全选不关联固件库'''
        super().firmware_info_input(r'C:\Users\anban\Desktop\gujianhuizong\jizhunceshi\libcurl_7.17.1-1_arm.ipk','libcurl_7.17.1-1_arm.ipk','all','全选不关联固件库')
        super().plugin_check(6)
        super().upload_click()
        super().task_start()
        try:
           self.assertNotIn('将固件添加至固件库，漏洞库更新时自动提醒扫描该固件。',self.driver.page_source)
        except Exception as e:
           print(self.test_upload_02.__doc__+'运行失败',e)
           self.driver.get_screenshot_as_file(image_dir+self.test_upload_02.__doc__+'.png')

    @unittest.skip
    def test_upload_03(self):
        '''成功上传固件任务-关联固件库'''
        super().firmware_info_input(r'E:\易识\网关、采集器固件（含内蒙古电力项目）\内蒙古电科项目客户提供\安全测试用固件汇总\SCM6JIZHONG.hex','SCM6JIZHONG.hex','all','关联固件库')
        super().plugin_all()
        super().upload_click()
        super().task_start()
        try:
           self.assertNotIn('将固件添加至固件库，漏洞库更新时自动提醒扫描该固件。',self.driver.page_source)
        except Exception as e:
           print(self.test_upload_03.__doc__+'运行失败',e)
           self.driver.get_screenshot_as_file(image_dir+self.test_upload_03.__doc__+'.png')

    # @unittest.skip
    def test_upload_04(self):
        '''成功上传固件任务-不勾选 软件成分探测& CVE漏洞查找  插件'''
        super().firmware_info_input(r'E:\易识\网关、采集器固件（含内蒙古电力项目）\内蒙古电科项目客户提供\安全测试用固件汇总\SCM6JIZHONG.hex','SCM6JIZHONG.hex','soft/cve0','soft/cve0')
        super().plugin_check(1)
        super().plugin_check(6)
        super().upload_click()
        super().task_start()
        try:
           self.assertNotIn('将固件添加至固件库，漏洞库更新时自动提醒扫描该固件。',self.driver.page_source)
        except Exception as e:
           print(self.test_upload_04.__doc__+'运行失败',e)
           self.driver.get_screenshot_as_file(image_dir+self.test_upload_04.__doc__+'.png')

    @unittest.skip
    def test_upload_05(self):
        '''成功上传固件任务-不勾选  CVE漏洞查找  插件'''
        super().firmware_info_input(r'E:\易识\网关、采集器固件（含内蒙古电力项目）\内蒙古电科项目客户提供\安全测试用固件汇总\SCM6JIZHONG.hex','SCM6JIZHONG.hex','cve0','cve0')
        super().plugin_check(2)
        super().plugin_check(6)
        super().upload_click()
        super().task_start()
        time.sleep(wait_time)
        try:
           self.assertNotIn('将固件添加至固件库，漏洞库更新时自动提醒扫描该固件。',self.driver.page_source)
        except Exception as e:
           print(self.test_upload_05.__doc__+'运行失败',e)
           self.driver.get_screenshot_as_file(image_dir+self.test_upload_05.__doc__+'.png')

    @unittest.skip
    def test_upload_06(self):
        '''成功上传固件任务-不勾选 文件类型分析 / CPU架构分析 /CWE缺陷查找/ 文件哈希值分析 插件'''
        super().firmware_info_input(r'E:\易识\网关、采集器固件（含内蒙古电力项目）\内蒙古电科项目客户提供\安全测试用固件汇总\SCM6JIZHONG.hex','SCM6JIZHONG.hex','file/cpu/cwe/hash0','file/cpu/cwe/hash0')
        super().plugin_check(3)
        super().upload_click()
        super().task_start()
        time.sleep(wait_time)
        try:
           self.assertNotIn('将固件添加至固件库，漏洞库更新时自动提醒扫描该固件。',self.driver.page_source)
        except Exception as e:
           print(self.test_upload_06.__doc__+'运行失败',e)
           self.driver.get_screenshot_as_file(image_dir+self.test_upload_06.__doc__+'.png')

    @unittest.skip
    def test_upload_07(self):
        '''成功上传固件任务-不勾选 CPU架构分析 插件'''
        super().firmware_info_input(r'E:\易识\网关、采集器固件（含内蒙古电力项目）\内蒙古电科项目客户提供\安全测试用固件汇总\SCM6JIZHONG.hex','SCM6JIZHONG.hex','cpu0','cpu0')
        super().plugin_check(4)
        super().upload_click()
        super().task_start()
        time.sleep(wait_time)
        try:
           self.assertNotIn('将固件添加至固件库，漏洞库更新时自动提醒扫描该固件。',self.driver.page_source)
        except Exception as e:
           print(self.test_upload_07.__doc__+'运行失败',e)
           self.driver.get_screenshot_as_file(image_dir+self.test_upload_07.__doc__+'.png')

    @unittest.skip
    def test_upload_08(self):
        '''成功上传固件任务-不勾选 CWE缺陷查找 插件'''
        super().firmware_info_input(r'E:\易识\网关、采集器固件（含内蒙古电力项目）\内蒙古电科项目客户提供\安全测试用固件汇总\SCM6JIZHONG.hex','SCM6JIZHONG.hex','cwe0','cwe0')
        super().upload_click()
        super().task_start()
        time.sleep(wait_time)
        try:
           self.assertNotIn('将固件添加至固件库，漏洞库更新时自动提醒扫描该固件。',self.driver.page_source)
        except Exception as e:
           print(self.test_upload_08.__doc__+'运行失败',e)
           self.driver.get_screenshot_as_file(image_dir+self.test_upload_08.__doc__+'.png')

    @unittest.skip
    def test_upload_09(self):
        '''成功上传固件任务-不勾选 文件哈希值分析 插件'''
        super().firmware_info_input(r'E:\易识\网关、采集器固件（含内蒙古电力项目）\内蒙古电科项目客户提供\安全测试用固件汇总\SCM6JIZHONG.hex','SCM6JIZHONG.hex','hash0','hash0')
        super().plugin_check(8)
        super().plugin_check(6)
        super().upload_click()
        super().task_start()
        time.sleep(wait_time)
        try:
           self.assertNotIn('将固件添加至固件库，漏洞库更新时自动提醒扫描该固件。',self.driver.page_source)
        except Exception as e:
           print(self.test_upload_09.__doc__+'运行失败',e)
           self.driver.get_screenshot_as_file(image_dir+self.test_upload_09.__doc__+'.png')

    @unittest.skip
    def test_upload_10(self):
        '''成功上传固件任务-不勾选 签名分析 插件'''
        super().firmware_info_input(r'E:\易识\网关、采集器固件（含内蒙古电力项目）\内蒙古电科项目客户提供\安全测试用固件汇总\SCM6JIZHONG.hex','SCM6JIZHONG.hex','sign0','sign0')
        super().plugin_check(5)
        super().plugin_check(6)
        super().upload_click()
        super().task_start()
        time.sleep(wait_time)
        try:
           self.assertNotIn('将固件添加至固件库，漏洞库更新时自动提醒扫描该固件。',self.driver.page_source)
        except Exception as e:
           print(self.test_upload_10.__doc__+'运行失败',e)
           self.driver.get_screenshot_as_file(image_dir+self.test_upload_10.__doc__+'.png')

    @unittest.skip
    def test_upload_11(self):
        '''成功上传固件任务-不勾选 加密算法分析 插件'''
        super().firmware_info_input(r'E:\易识\网关、采集器固件（含内蒙古电力项目）\内蒙古电科项目客户提供\安全测试用固件汇总\SCM6JIZHONG.hex','SCM6JIZHONG.hex','jiami0','jiami0')
        super().plugin_check(7)
        super().plugin_check(6)
        super().upload_click()
        super().task_start()
        time.sleep(wait_time)
        try:
           self.assertNotIn('将固件添加至固件库，漏洞库更新时自动提醒扫描该固件。',self.driver.page_source)
        except Exception as e:
           print(self.test_upload_11.__doc__+'运行失败',e)
           self.driver.get_screenshot_as_file(image_dir+self.test_upload_11.__doc__+'.png')

    @unittest.skip
    def test_upload_12(self):
        '''成功上传固件任务-不勾选  ELF分析 插件'''
        super().firmware_info_input(r'E:\易识\网关、采集器固件（含内蒙古电力项目）\内蒙古电科项目客户提供\安全测试用固件汇总\SCM6JIZHONG.hex','SCM6JIZHONG.hex','elf0','elf0')
        super().plugin_check(9)
        super().plugin_check(6)
        super().upload_click()
        super().task_start()
        time.sleep(wait_time)
        try:
           self.assertNotIn('将固件添加至固件库，漏洞库更新时自动提醒扫描该固件。',self.driver.page_source)
        except Exception as e:
           print(self.test_upload_12.__doc__+'运行失败',e)
           self.driver.get_screenshot_as_file(image_dir+self.test_upload_12.__doc__+'.png')

    @unittest.skip
    def test_upload_13(self):
        '''成功上传固件任务-不勾选 IP地址URI和Email探测 插件'''
        super().firmware_info_input(r'E:\易识\网关、采集器固件（含内蒙古电力项目）\内蒙古电科项目客户提供\安全测试用固件汇总\SCM6JIZHONG.hex','SCM6JIZHONG.hex','ip0','ip0')
        super().plugin_check(10)
        super().plugin_check(6)
        super().upload_click()
        super().task_start()
        time.sleep(wait_time)
        try:
           self.assertNotIn('将固件添加至固件库，漏洞库更新时自动提醒扫描该固件。',self.driver.page_source)
        except Exception as e:
           print(self.test_upload_13.__doc__+'运行失败',e)
           self.driver.get_screenshot_as_file(image_dir+self.test_upload_13.__doc__+'.png')

    @unittest.skip
    def test_upload_14(self):
        '''成功上传固件任务-不勾选 用户名和密码探测 插件'''
        super().firmware_info_input(r'E:\易识\网关、采集器固件（含内蒙古电力项目）\内蒙古电科项目客户提供\安全测试用固件汇总\SCM6JIZHONG.hex','SCM6JIZHONG.hex','user0','user0')
        super().plugin_check(11)
        super().plugin_check(6)
        super().upload_click()
        super().task_start()
        time.sleep(wait_time)
        try:
           self.assertNotIn('将固件添加至固件库，漏洞库更新时自动提醒扫描该固件。',self.driver.page_source)
        except Exception as e:
           print(self.test_upload_14.__doc__+'运行失败',e)
           self.driver.get_screenshot_as_file(image_dir+self.test_upload_14.__doc__+'.png')

    @unittest.skip
    def test_upload_15(self):
        '''成功上传固件任务-不勾选 安全编译选项识别 插件'''
        super().firmware_info_input(r'E:\易识\网关、采集器固件（含内蒙古电力项目）\内蒙古电科项目客户提供\安全测试用固件汇总\SCM6JIZHONG.hex','SCM6JIZHONG.hex','safe0','safe0')
        super().plugin_check(12)
        super().plugin_check(6)
        super().upload_click()
        super().task_start()
        time.sleep(wait_time)
        try:
           self.assertNotIn('将固件添加至固件库，漏洞库更新时自动提醒扫描该固件。',self.driver.page_source)
        except Exception as e:
           print(self.test_upload_15.__doc__+'运行失败',e)
           self.driver.get_screenshot_as_file(image_dir+self.test_upload_15.__doc__+'.png')

    @unittest.skip
    def test_upload_16(self):
        '''上传固件任务失败-不勾选插件'''
        super().firmware_info_input(r'E:\易识\网关、采集器固件（含内蒙古电力项目）\内蒙古电科项目客户提供\安全测试用固件汇总\SCM6JIZHONG.hex','SCM6JIZHONG.hex','plugin0','plugin0')
        super().plugin_none()
        super().upload_click()
        time.sleep(wait_time)
        try:
           self.assertIn('将固件添加至固件库，漏洞库更新时自动提醒扫描该固件。',self.driver.page_source)
        except Exception as e:
           print(self.test_upload_16.__doc__+'运行失败',e)
           self.driver.get_screenshot_as_file(image_dir+self.test_upload_16.__doc__+'.png')

    @unittest.skip
    def test_upload_17(self):
        '''上传固件任务失败-不上传文件'''
        super().firmware_nofile('file','cwe0','cwe0')
        super().upload_click()
        time.sleep(wait_time)
        try:
           self.assertIn('将固件添加至固件库，漏洞库更新时自动提醒扫描该固件。',self.driver.page_source)
        except Exception as e:
           print(self.test_upload_17.__doc__+'运行失败',e)
           self.driver.get_screenshot_as_file(image_dir+self.test_upload_17.__doc__+'.png')

    @unittest.skip
    def test_upload_18(self):
        '''上传固件任务失败-不输入版本名称'''
        super().firmware_info_input(r'E:\易识\网关、采集器固件（含内蒙古电力项目）\内蒙古电科项目客户提供\安全测试用固件汇总\SCM6JIZHONG.hex','','','cwe0')
        super().upload_click()
        time.sleep(wait_time)
        try:
           self.assertIn('将固件添加至固件库，漏洞库更新时自动提醒扫描该固件。',self.driver.page_source)
        except Exception as e:
           print(e,self.test_upload_18.__doc__+'运行失败')
           self.driver.get_screenshot_as_file(image_dir+self.test_upload_18.__doc__+'.png')

    @unittest.skip
    def test_upload_19(self):
        '''上传固件任务失败-不输入厂商名称'''
        super().firmware_info_input(r'E:\易识\网关、采集器固件（含内蒙古电力项目）\内蒙古电科项目客户提供\安全测试用固件汇总\SCM6JIZHONG.hex','','cwe0','')
        super().upload_click()
        time.sleep(wait_time)
        try:
           self.assertIn('将固件添加至固件库，漏洞库更新时自动提醒扫描该固件。',self.driver.page_source)
        except Exception as e:
           print(e,self.test_upload_19.__doc__+'运行失败')
           self.driver.get_screenshot_as_file(image_dir+self.test_upload_19.__doc__+'.png')

    @unittest.skip
    def test_upload_20(self):
        '''上传固件任务失败-版本为空格'''
        super().firmware_info_input(r'E:\易识\网关、采集器固件（含内蒙古电力项目）\内蒙古电科项目客户提供\安全测试用固件汇总\SCM6JIZHONG.hex','','   ','cwe0')
        super().upload_click()
        time.sleep(wait_time)
        try:
           self.assertIn('版本号不能只包含空格',self.driver.page_source)
        except Exception as e:
           print(e,self.test_upload_20.__doc__+'运行失败')
           self.driver.get_screenshot_as_file(image_dir+self.test_upload_20.__doc__+'.png')

    @unittest.skip
    def test_upload_21(self):
        '''上传固件任务失败-厂商为空格'''
        super().firmware_info_input(r'E:\易识\网关、采集器固件（含内蒙古电力项目）\内蒙古电科项目客户提供\安全测试用固件汇总\SCM6JIZHONG.hex','','cwe0','  ')
        super().upload_click()
        time.sleep(wait_time)
        try:
           self.assertIn('厂商名称不能只包含空格',self.driver.page_source)
        except Exception as e:
           print(e,self.test_upload_21.__doc__+'运行失败')
           self.driver.get_screenshot_as_file(image_dir+self.test_upload_21.__doc__+'.png')

    @unittest.skip
    def test_upload_22(self):
        '''可取消上传固件任务'''
        super().firmware_info_input(r'E:\易识\网关、采集器固件（含内蒙古电力项目）\内蒙古电科项目客户提供\安全测试用固件汇总\SCM6JIZHONG.hex','','cwe0','cwe0')
        super().firmware_cancel_click()
        time.sleep(wait_time)
        try:
           self.assertNotIn('将固件添加至固件库，漏洞库更新时自动提醒扫描该固件。',self.driver.page_source)
        except Exception as e:
           print(e,self.test_upload_22.__doc__+'运行失败')
           self.driver.get_screenshot_as_file(image_dir+self.test_upload_22.__doc__+'.png')

    @unittest.skip
    def test_upload_23(self):
        '''覆盖相同任务'''
        super().firmware_info_input(r'E:\易识\网关、采集器固件（含内蒙古电力项目）\内蒙古电科项目客户提供\安全测试用固件汇总\SCM6JIZHONG.hex','','cwe0','cwe0')
        super().firmware_cancel_click()
        time.sleep(wait_time)
        try:
           self.assertNotIn('将固件添加至固件库，漏洞库更新时自动提醒扫描该固件。',self.driver.page_source)
        except Exception as e:
           print(e,self.test_upload_23.__doc__+'运行失败')
           self.driver.get_screenshot_as_file(image_dir+self.test_upload_23.__doc__+'.png')

    @unittest.skip
    def test_upload_24(self):
        '''任务名称筛选任务'''
        super().login_success()
        super().task_name_search('SCM6JIZHONG.hex')
        time.sleep(2)
        try:
            self.assertIn('SCM6JIZHONG.hex',self.driver.page_source)
        except Exception as e:
            print(e,self.test_upload_24.__doc__+'运行失败')
            self.driver.get_screenshot_as_file(image_dir+self.test_upload_24.__doc__+'.png')

    @unittest.skip
    def test_upload_25(self):
        '''时间筛选任务'''
        super().login_success()
        super().task_time_search('2022-12-29 00:28:46','2022-12-29 00:28:46')
        time.sleep(2)
        try:
            self.assertNotIn(' R6300-V1.0.2.76_1.0.57.chk ',self.driver.page_source)
        except Exception as e:
            print(e,self.test_upload_25.__doc__+'运行失败')
            self.driver.get_screenshot_as_file(image_dir+self.test_upload_25.__doc__+'.png')

    @unittest.skip
    def test_upload_26(self):
        '''输入厂商筛选任务'''
        super().login_success()
        super().task_firm_search('all')
        time.sleep(2)
        try:
            self.assertNotIn(' R6300-V1.0.2.76_1.0.57.chk ',self.driver.page_source)
        except Exception as e:
            print(e,self.test_upload_26.__doc__+'运行失败')
            self.driver.get_screenshot_as_file(image_dir+self.test_upload_26.__doc__+'.png')


if __name__ == '__main__':
    Yishi_firmware_analysis()
