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


class Yishi_compare(Browser):
    _testMethodDoc = '报告对比分析'

    # @unittest.skip
    def test_compare_01(self):
        '''跳转创建对比任务页面'''
        super().compare_task_change()
        try:
            WebDriverWait(self.driver, 5).until(EC.text_to_be_present_in_element(super().compare_task_end(), '已成功'))
            self.assertIn('新建报告对比',self.driver.page_source)
        except Exception as e:
            self.driver.get_screenshot_as_file(image_dir+self.test_compare_01.__doc__+'.png')
            print(self.test_compare_01.__doc__+'任务失败')

    # @unittest.skip
    def test_compare_02(self):
        '''跳转选择对比任务页面'''
        super().compare_task_change()
        super().compare_task_create_click()
        sleep(2)
        try:
            self.assertIn('厂商选择',self.driver.page_source)
        except Exception as e:
            self.driver.get_screenshot_as_file(image_dir+self.test_compare_02.__doc__+'.png')
            print(self.test_compare_02.__doc__+'任务失败')

    # @unittest.skip
    def test_compare_03(self):
        '''成功创建对比任务'''
        super().compare_task_change()
        super().compare_task_create_click()
        time.sleep(2)
        super().compare_task_choose(1)
        super().compare_task_choose(2)
        super().compare_task_confirm()
        try:
            WebDriverWait(self.driver, 5).until(EC.text_to_be_present_in_element(super().compare_task_end(), '已成功'))
            self.assertIn('创建对比分析任务成功',self.driver.page_source)
        except Exception as e:
            self.driver.get_screenshot_as_file(image_dir+self.test_compare_03.__doc__+'.png')
            print(e,self.test_compare_03.__doc__+'任务失败')


    # @unittest.skip
    def test_compare_04(self):
        '''全选创建对比任务'''
        super().compare_task_change()
        super().compare_task_create_click()
        time.sleep(2)
        super().compare_choose_all()
        super().compare_task_confirm()
        try:
            WebDriverWait(self.driver, 5).until(EC.text_to_be_present_in_element(super().compare_task_end(),'已成功') )
            self.assertIn('创建对比分析任务成功',self.driver.page_source)
        except Exception as e:
            self.driver.get_screenshot_as_file(image_dir+self.test_compare_04.__doc__+'.png')
            print(e,self.test_compare_04.__doc__+'任务失败')

    # @unittest.skip
    def test_compare_05(self):
        '''筛选任务创建对比任务'''
        super().compare_task_change()
        super().compare_task_create_click()
        # time.sleep(wait_time)
        super().choose_task('a')
        super().compare_task_choose(1)
        time.sleep(2)
        super().choose_task('b')
        super().compare_task_choose(1)
        super().compare_task_confirm()
        try:
            WebDriverWait(self.driver, 5).until(EC.text_to_be_present_in_element(super().compare_task_end(), '已成功'))
            self.assertIn('创建对比分析任务成功',self.driver.page_source)
        except Exception as e:
            self.driver.get_screenshot_as_file(image_dir+self.test_compare_05.__doc__+'.png')
            print(self.test_compare_05.__doc__+'任务失败')

    # @unittest.skip
    def test_compare_06(self):
        '''创建失败：只选择一个任务创建对比报告。'''
        super().compare_task_change()
        super().compare_task_create_click()
        super().choose_task('a')
        super().compare_task_choose(1)
        time.sleep(wait_time)
        super().compare_task_confirm()
        try:
           self.assertIn('需要2份报告执行对比分析，请确认选择的报告数量',self.driver.page_source)
        except Exception as e:
           self.driver.get_screenshot_as_file(image_dir+self.test_compare_06.__doc__+'.png')
           print(e,self.test_compare_06.__doc__+'任务失败')

    # @unittest.skip
    def test_compare_07(self):
        '''创建成功：筛选时间创建对比报告'''
        super().compare_task_change()
        super().compare_task_create_click()
        time.sleep(5)
        super().time_click(compare_start_time,compare_end_time)
        super().compare_choose_all()
        super().compare_task_confirm()

        try:
            WebDriverWait(self.driver, 5).until(EC.text_to_be_present_in_element(super().compare_task_end(), '已成功'))
            self.assertIn('创建对比分析任务成功',self.driver.page_source)
        except Exception as e:
            self.driver.get_screenshot_as_file(image_dir+self.test_compare_07.__doc__+'.png')
            print(self.test_compare_07.__doc__+'任务失败')

    # @unittest.skip
    def test_compare_08(self):
        '''创建成功：筛选厂商创建对比报告'''
        super().compare_task_change()
        super().compare_task_create_click()
        super().firm_click('a')
        super().compare_choose_all()
        super().compare_task_confirm()
        try:
            WebDriverWait(self.driver, 5).until(EC.text_to_be_present_in_element(super().compare_task_end(), '已成功'))
            self.assertIn('创建对比分析任务成功',self.driver.page_source)
        except Exception as e:
            self.driver.get_screenshot_as_file(image_dir+self.test_compare_08.__doc__+'.png')
            print(self.test_compare_08.__doc__+'任务失败')

    # @unittest.skip
    def test_compare_09(self):
        '''创建成功：厂商/任务名/时间组合筛选创建对比报告'''
        super().compare_task_change()
        super().compare_task_create_click()
        super().time_click('2022-11-24 00:00:00', '2023-12-12 23:59:59')
        super().choose_task('a')
        super().firm_click('a')
        super().compare_choose_all()
        super().compare_task_confirm()
        time.sleep(2)
        try:
            WebDriverWait(self.driver, 5).until(EC.text_to_be_present_in_element(super().compare_task_end(), '已成功'))
            self.assertIn('创建对比分析任务成功',self.driver.page_source)
        except Exception as e:
            self.driver.get_screenshot_as_file(image_dir+self.test_compare_09.__doc__+'.png')
            print(self.test_compare_09.__doc__+'任务失败')

    # @unittest.skip
    def test_compare_10(self):
        '''筛选任务：输入不存在的任务名'''
        super().compare_task_change()
        super().compare_task_create_click()
        super().choose_task('不存在的任务名')
        time.sleep(2)
        try:
            self.driver.implicitly_wait(10)
            self.assertIn('暂无数据',self.driver.page_source)
        except Exception as e:
            self.driver.get_screenshot_as_file(image_dir+self.test_compare_10.__doc__+'.png')
            print(e,self.test_compare_10.__doc__+'任务失败')

    # @unittest.skip
    def test_compare_11(self):
        '''筛选任务：输入不存在任务的时间段'''
        super().compare_task_change()
        super().compare_task_create_click()
        super().time_click('2023-11-24 00:00:00', '2023-12-12 23:59:59')
        time.sleep(2)
        try:
            self.assertIn('暂无数据',self.driver.page_source)
        except Exception as e:
            self.driver.get_screenshot_as_file(image_dir+self.test_compare_11.__doc__+'.png')
            print(e,self.test_compare_11.__doc__+'任务失败')

    # @unittest.skip
    def test_compare_12(self):
        '''筛选任务：输入不存在的厂商'''
        super().compare_task_change()
        super().compare_task_create_click()
        super().firm_click('不存在的厂商')
        time.sleep(2)      #等待筛选条件输入
        try:
           self.assertIn('暂无数据',self.driver.page_source)
        except Exception as e:
           self.driver.get_screenshot_as_file(image_dir+self.test_compare_12.__doc__+'.png')
           print(e,self.test_compare_12.__doc__+'任务失败')

    # @unittest.skip
    def test_compare_13(self):
        '''跳转页面'''
        super().compare_task_change()
        super().compare_task_create_click()
        super().page_skip(2)
        super().page_skip(3)
        super().page_skip(2)
        try:
            A = self.driver.find_element(By.XPATH,'//li[@class="number active"]').text
            self.assertIs('2',A)
        except Exception as e:
            self.driver.get_screenshot_as_file(image_dir+self.test_compare_13.__doc__+'.png')
            print(e,self.test_compare_13.__doc__+'任务失败')

    # @unittest.skip
    def test_compare_14(self):
        '''翻页'''
        super().compare_task_change()
        super().compare_task_create_click()
        super().page_right()    #
        super().page_left()
        super().page_right()
        try:
            A = self.driver.find_element(By.XPATH,'//li[@class="number active"]').text
            self.assertIs('2',A)
        except Exception as e:
            self.driver.get_screenshot_as_file(image_dir+self.test_compare_14.__doc__+'.png')
            print(e,self.test_compare_14.__doc__+'任务失败')

    # @unittest.skip
    def test_compare_15(self):
        '''查看对比报告'''
        super().compare_task_change()
        super().compare_task_report(1)
        self.driver.implicitly_wait(10)
        A = self.driver.window_handles
        self.driver.switch_to.window(A[-1])
        try:
            WebDriverWait(self.driver,10).until(EC.text_to_be_present_in_element(super().compare_report_load(),'固件对比分析报告'))
            self.assertIn('对于任务中没有勾选的功能',self.driver.page_source)
        except Exception as e:
            self.driver.get_screenshot_as_file(image_dir+self.test_compare_15.__doc__+'.png')
            print(e,self.test_compare_15.__doc__+'任务失败')



if __name__ == "__main__":
    Yishi_compare()