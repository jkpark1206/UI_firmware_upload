# import lib
import csv


# url地址
URL = '192.168.5.193:8011/'

# 测试用例的路径
test_dir = 'C:/Tools/UI_firmware_upload/testcases/'

# 测试报告的路径
report_dir = 'C:/Tools/UI_firmware_upload/reports/'

# 图片的存放路径
image_dir = 'C:/Tools/UI_firmware_upload/images/'

# 浏览器的类型
# firefox -- 火狐  ie--ie 浏览器  edge- miscrosoft edge浏览器
browser = 'chrome'

# 等待的时间
wait_time = 5

#用户名密码
user_name='wwh'
passwd='Test123456'

#对比任务筛选时间
compare_start_time = '2022-11-24 00:00:00'
compare_end_time = '2023-12-12 23:59:59'


#

#基准测试固件路径
filename = 'C:/Users/anban/Desktop/gujianhuizong/firmware_list.csv'

'''class upload():
    def csv_file(self):
        filename = 'C:/Users/anban/Desktop/firmware_list.csv'
        fp = open(filename, 'r', encoding='utf-8')
        c_data = csv.reader(fp)
        data = []
        for i in c_data:
            data.append(i)
            print(data)
        fp.close()
#         for n in range(0, len(data)):
#             A = data[n][0]
#             super().firmware_info_input(r'{}'.format(A), '', 'all', '关联固件库')


if __name__=='main':
    upload().csv_file()'''


