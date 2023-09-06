from common.browser import Browser
import time
from config.config import *
import csv
from get_file_path import file_name_list,path

class Yishi_firmware_analysis(Browser):
    _testMethodDoc = '固件扫描分析'

    def test_firmware_upload_01(self):
        '''成功上传固件任务-关联固件库'''
        # fp = open(filename, 'r', encoding='utf-8')
        # c_data = csv.reader(fp)
        # data = []
        # for i in c_data:
        #     data.append(i)
        # fp.close()

        for n in range(0, len(file_name_list )):
            file=path +'/'+ file_name_list [n]
            print(file)
            super().firmware_info_input(r'{}'.format(file), '' , 'all', '关联固件库')
            super().plugin_all()
            super().upload_click()
            time.sleep(wait_time)
            super().task_start()

        try:
            self.assertNotIn('将固件添加至固件库，漏洞库更新时自动提醒扫描该固件。', self.driver.page_source)
        except Exception as e:
            print(self.test_firmware_upload_01.__doc__ + '运行失败', e)
            self.driver.get_screenshot_as_file(image_dir + self.test_firmware_upload_01.__doc__ + '.png')


if __name__ == '__main__':
    Yishi_firmware_analysis().test_firmware_upload_01()


