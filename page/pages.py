from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from common.browser import Browser
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver



# class Assert_page:
#
#     def __init__(self):
#         self.driver = webdriver.Chrome()
#         self.wait_time = 20
#         self.add_time = 1800
#
# # 判断对比任务创建成功
#     def compare_task_end(self):
#         try:
#             A = By.XPATH,'//tbody/tr[1]/td[4]/div/span'
#             WebDriverWait(self.driver, 5).until(EC.text_to_be_present_in_element(A,'已完成'))
#             self.assertIn('创建对比分析任务成功', self.driver.page_source)
#         except Exception as e:
#             print(e)

