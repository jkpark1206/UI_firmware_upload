import time
from selenium.webdriver.common.by import By
import csv
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pickle

sleep = time.sleep
#步骤1：将固件上传到易识
#步骤2：将固件用CSV文件读取方式，循环上传所有文件
#大麦网主页
damai_url="https://www.damai.cn/"
#登录页
login_url = "https://passport.damai.cn/login?ru=https%3A%2F9%2Fwww.damai.cn%2F"
#抢票目标页
target_url = "https://detail.damai.cn/item.htm?spm=a2oeg.search_catoegory.0.0.77f24d15RWgT4o&id=654534889506&clicktitle=%E5%A4%A7%E4%"

from appium import webdriver
from time import sleep

desired_caps={
              "platformName":"Android",   #平台名字
              "platformVersion":"7.1.2",   #设备版本号 ： adb shell getprop ro.build.version.release
              "deviceName":"127.0.0.1:62025", #设备名 ： adb devices
              "appPackage":"com.mobivans.onestrokecharge", # app包名
              "appActivity":"com.mobivans.onestrokecharge.activitys.MainActivity",  # 主启动页
              "udid":"127.0.0.1:62025",   # 设备编号
              "unicodeKeyboard":True,    # 支持中文
              "deviceReadyTimeout":20000  # 20s
             }

class Yibijizhang:
    def __init__(self):
        self.awb=webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        sleep(0.5)

    def jiyibi_zhichu(self):
        self.awb.find_element("id", "com.mobivans.onestrokecharge:id/main_write1").click()  # 点击记一笔按钮
        sleep(0.5)
        self.awb.find_element("xpath", "//*[@text='日常']").click()  # 点击日常按钮
        sleep(0.5)
        self.awb.find_element("xpath", "//*[@text='2']").click()  # 点击键盘数字2按钮
        self.awb.find_element("xpath", "//*[@text='5']").click()  # 点击键盘数字5按钮
        sleep(0.5)
        self.awb.find_element("xpath", "//*[@text='完成']").click()  # 点击完成按钮

    def jiyibi_shouru(self):
        self.awb.find_element("id", "com.mobivans.onestrokecharge:id/main_write1").click()  # 点击记一笔按钮
        sleep(0.5)
        self.awb.find_element("xpath", "//*[@text='收入']").click()  # 点击收入按钮
        sleep(0.5)
        self.awb.find_element("xpath", "//*[@text='工资']").click()  # 点击工资按钮
        sleep(0.5)
        self.awb.find_element("xpath", "//*[@text='2']").click()  # 点击键盘数字2按钮
        self.awb.find_element("xpath", "//*[@text='5']").click()  # 点击键盘数字5按钮
        self.awb.find_element("xpath", "//*[@text='0']").click()  # 点击键盘数字0按钮
        self.awb.find_element("xpath", "//*[@text='0']").click()  # 点击键盘数字0按钮
        self.awb.find_element("xpath", "//*[@text='0']").click()  # 点击键盘数字0按钮
        self.awb.find_element("xpath", "//*[@text='0']").click()  # 点击键盘数字0按钮
        sleep(0.5)
        self.awb.find_element("xpath", "//*[@text='今天']").click()  # 点击键盘今天按钮
        sleep(0.5)
        self.awb.find_element("xpath", "//android.view.View[@content-desc='01 七月 2022']").click()  # 点击选择日期
        sleep(0.5)
        self.awb.find_element("id", "android:id/button1").click()  # 点击确定
        sleep(0.5)
        self.awb.find_element("xpath", "//*[@text='完成']").click()  # 点击完成按钮
        sleep(0.5)
        self.awb.find_element("id", "com.mobivans.onestrokecharge:id/guide_img_close").click()  # 取消弹窗

    def yibijizhang_zhichudemo(self, zhichu):
        for zc in zhichu:
            self.awb.find_element("id", "com.mobivans.onestrokecharge:id/main_write1").click()  # 点击记一笔按钮
            sleep(0.5)
            self.awb.find_element("xpath", f"//*[@text='{zc[0]}']").click()  # 点击类别标签按钮
            sleep(0.5)
            for i in zc[1]:
                self.awb.find_element("xpath", f"//*[@text='{i}']").click()  # 点击键盘数字按钮
            sleep(0.5)
            day = zc[2].split("-")[-1]
            self.awb.find_element("xpath", "//*[@text='今天']").click()  # 点击键盘今天按钮
            sleep(0.5)
            self.awb.find_element("xpath", f"//*[@text='{day}']").click()  # 点击选择日期
            sleep(0.5)
            self.awb.find_element("id", "android:id/button1").click()  # 点击确定按钮
            sleep(0.5)
            self.awb.find_element("xpath", "//*[@text='完成']").click()  # 点击完成按钮
            try:
                self.awb.find_element("id", "com.mobivans.onestrokecharge:id/guide_img_close").click()  # 取消弹窗
            except:
                pass


if __name__ == '__main__':
    jizhang = Yibijizhang()

    # jizhang.jiyibi_zhichu()

    # jizhang.jiyibi_shouru()

    # 依据 测试数据 连续记多笔账 支出
    zhichu = [("日常", "25", "2022-7-1"), ("餐饮", "268", "2022-7-2"),
              ("购物", "2000", "2022-7-3"), ("日用", "88", "2022-7-4")]
    jizhang.yibijizhang_zhichudemo(zhichu)



# class upload():#步骤1：定义上传固件方法
#
#     def __init__(self):
#         self.driver=webdriver.Chrome()
#         self.driver.maximize_window()
#         self.driver.implicitly_wait(120)
#
#     def firmware_info_input(self):
#         A = self.driver.get("https://perico.damai.cn")
#         return A
#
#
if __name__ == '__main__':
    Concert_1().set_cookie()
    # Concert_1().get_cookie()


