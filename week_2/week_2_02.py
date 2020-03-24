# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/3/24 19:20
# 文件名：week_2_02.py
# 开发工具：PyCharm

# 正则表达式
import re
import requests
from bs4 import BeautifulSoup as bs

url = "https://python123.io/ws/demo.html"
r = requests.get(url)
demo = r.text
soup = bs(demo, "html.parser")

for tag in soup.find_all(True):
    print(tag.name)

print("------------------")
for tag in soup.find_all(re.compile('b')):
    print(tag.name)  # 返回以b开头的所有信息

# find_all(name, attrs, recursive. string, **kwargs)
# name：对标签名称的检索字符串
# attrs:对标签属性的检索字符串
# recursive:是否对其子孙节点进行搜索
# string：对<>...</>中字符串区域的检索字符串
print("----------------")
print(soup.find_all(string=re.compile("python")))
# 检索有python的所有字符串
