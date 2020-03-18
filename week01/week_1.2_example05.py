# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/3/18 20:18
# 文件名：week_1.2_example05.py
# 开发工具：PyCharm
import requests
# ip地址归属地查询

url = "http://m.ip138.com/ip.asp?ip="
r = requests.get(url + '202.204.80.112')
print(r.status_code)

