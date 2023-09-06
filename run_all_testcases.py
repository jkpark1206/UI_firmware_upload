import unittest
import time
from common import HTMLTestRunner
from config.config import test_dir,report_dir
def create_suite():   #创建对象
    # 测试用例的路径
    dir = test_dir
    discover = unittest.defaultTestLoader.discover(
        start_dir=dir,
        pattern='yishi_*.py',
        top_level_dir=None
    )
    suite = unittest.TestSuite()
    suite.addTests(discover)
    return suite

# 测试报告的路径
now = time.strftime('%Y-%m-%d-%H-%M-%S')  # 格式化显示时间
report_name = report_dir + now + '_yishi_ui_test.html'
fp = open(report_name, 'w+', encoding='utf-8')
runner = HTMLTestRunner.HTMLTestRunner(
    title='易识测试报告',
    description='易识测试结果说明',
    stream=fp
)
runner.run(create_suite())
fp.close()

# if __name__ == '__main__':
#     unittest.main(defaultTest='create_suite')

