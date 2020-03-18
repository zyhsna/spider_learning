# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/3/17 17:49
# 文件名：第一章.py
# 开发工具：PyCharm

import requests
import time as t

# 以下为入门先练手看看der  无中文行为代码
# -------------------------------------------------------------------------------↓

# r = requests.get("http://www.baidu.com")
# print(r.status_code)  # if status_code == 200 ,it means visit successfully,or 404  means wrong

# r.text url对应的页面内容
# r.encoding 从header中猜测的响应内容编码方式
# r.content HTTP响应内容的二进制形式
# r.apparent_encoding 从内容中分析出的响应的编码方式
# 流程 先用r.status_code确认访问是否成功，成功则解析返回内容
# print(r.text)
# print(r.apparent_encoding)
# print(r.encoding)  # 如果header中存在charset，默认编码为ISO-8859—1  ps: charset是类似于一种编码规范说明
# ---------------------------------------------------------------------------------↑
# requests库的异常
# requests.ConnectionError  网页链接错误
# requests.HTTPError HTTP错误异常
# requests.URLRequired  URL却是异常
# requests.TooManyRedirects 超过最大重定向次数，产生重定向异常
# requests.ConnectTimeout 链接远程服务器超时异常  （仅指链接服务器超时）
# requests.Timeout 请求URL超时，产生超时异常 （是整个过程的时间超时）

# r.raise_for_status()  如果不是200，则产生异常requests.HTTPError

# 爬取网页的通用代码框架
# -----------------------------------------------------------------------------------↓


def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        # print(r.status_code)
        r.raise_for_status()
        # 也会抛出异常
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "请求错误"


if __name__ == "__main__":
    start = t.perf_counter()
    url = "http://www.baidu.com"
    print(getHTMLText(url))
    # for i in range(100):
    # getHTMLText(url)
    end = t.perf_counter()
    print("100次用时"+str(end-start))
# --------------------------------------------------------------------------------------↑

# HTTP 协议 超文本传输协议
# URL格式 http://host[:port][path]   host 合法的Internet主机域名或IP地址  port 端口号，一般缺省为80  path 请求资源的路径
# URL 是通过HTTP协议存取资源的Internet路径，类似于电脑上的硬盘中存放的资源路径

# HTTP协议对资源的操作
# GET   请求获取资源
# HEAD  获得资源的头部信息
# POST  附加新数据
# PUT   用一个资源覆盖原位置资源
# PATCH 更新局部资源  ps:与put的区别在于如果想更改某一部分，patch只需提交想更改的部分  put是必须连同为更改的一并提交
# DELETE  删除资源

# requests库的方法与HTTP功能一致

