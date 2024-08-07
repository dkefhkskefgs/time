# from datetime import datetime
#
# # 获取当前时间对象
# now = datetime.now()
#
# # 获取当前时区信息
# local_timezone = now.astimezone().tzinfo
# print(f'当前系统的本地时区：{local_timezone}')
#
#
# import pytz
#
# # 打印所有支持的时区
# for tz in pytz.all_timezones:
#     print(tz)
# -*- coding: utf-8

import sys
import time
import requests

from datetime import datetime
now = datetime.now()

# 获取当前时区信息
local_timezone = now.astimezone().tzinfo
info = local_timezone.utcoffset(now)
print(info.seconds/3600)

prox = {'http': '192.168.100.127:8887', 'https': '192.168.100.127:8887'}
# 1、获取网络北京时间戳
def get_beijing_stamp_from_web(url):
    # 请求网络数据
    response = requests.get(url, proxies=prox)
    # 获取http头date部分
    ts = response.headers['date']
    # 将日期时间字符转化为数组对象
    gmt_time_obj = time.strptime(ts[5:25], "%d %b %Y %H:%M:%S")
    # 将时间数组对象转为时间戳
    gmt_ts = time.mktime(gmt_time_obj)  # 零时区时间戳
    # 将GMT时间转换成北京时间时间戳
    bj_internet_ts = int(gmt_ts + 8 * 3600)  # 北京时间戳

    # 返回东八区的北京时间戳
    return bj_internet_ts


# 2、获取网络北京日期字串
def get_beijing_date_from_web(url):
    # 请求网络数据
    # response = requests.get(url)
    response = requests.get(url, proxies=prox)
    # 获取http头date部分
    ts = response.headers['date']
    # 将日期时间字符转化为数组对象
    gmt_time_obj = time.strptime(ts[5:25], "%d %b %Y %H:%M:%S")  # GMT零时区
    # 将时间数组对象转为时间戳
    gmt_ts = time.mktime(gmt_time_obj)  # 零时区时间戳
    # 将GMT时间转换成北京时间时间戳
    bj_internet_ts = gmt_ts + info.seconds
    # 将北京时间戳转化为数组对象
    bj_local_time_obj = time.localtime(bj_internet_ts)
    # 构造日期字串
    str1 = "%u-%02u-%02u" % (bj_local_time_obj.tm_year,
                             bj_local_time_obj.tm_mon, bj_local_time_obj.tm_mday)
    str2 = "%02u:%02u:%02u" % (
        bj_local_time_obj.tm_hour, bj_local_time_obj.tm_min, bj_local_time_obj.tm_sec)
    bj_date_time_str = "%s %s" % (str1, str2)  # 日期字串

    # 返回东八区的北京时间戳
    return bj_date_time_str


# 3、获取网络GMT时间戳
def get_gmt_stamp_from_web(url):
    # 请求网络数据
    # response = requests.get(url)
    response = requests.get(url, proxies=prox)
    # 获取http头date部分
    ts = response.headers['date']
    # 将web日期时间字符转化为数组对象
    gmt_time = time.strptime(ts[5:25], "%d %b %Y %H:%M:%S")
    # 将数组对象时间转换成时间戳
    gmt_internet_ts = int(time.mktime(gmt_time))  # 零时区时间戳
    # 返回零时区时间戳
    return gmt_internet_ts


# 4、获取网络GMT日期字串
def get_gmt_date_from_web(url):
    # 请求网络数据
    # response = requests.get(url)
    response = requests.get(url, proxies=prox)
    # 获取http头date部分
    ts = response.headers['date']
    # 将web日期时间字符转化为数组对象
    gmt_time_boj = time.strptime(ts[5:25], "%d %b %Y %H:%M:%S")
    # 构建时间字符串
    str1 = "%u-%02u-%02u" % (gmt_time_boj.tm_year,
                             gmt_time_boj.tm_mon, gmt_time_boj.tm_mday)
    str2 = "%02u:%02u:%02u" % (
        gmt_time_boj.tm_hour, gmt_time_boj.tm_min, gmt_time_boj.tm_sec)
    gmt_date_time = "%s %s" % (str1, str2)
    # 返回零时区日期字串
    return gmt_date_time


def main():
    url = "https://www.google.com"
    # x = get_beijing_stamp_from_web(url)
    # print("北京时间戳：")
    # print(x)
    x = get_beijing_date_from_web(url)
    print("北京日期串：")
    print(x)
    # x = get_gmt_stamp_from_web(url)
    # print("GMT时间戳：")
    # print(x)
    # x = get_gmt_date_from_web(url)
    # print("GMT日期串：")
    # print(x)


if __name__ == '__main__':
    main()