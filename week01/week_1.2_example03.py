# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/3/18 19:57
# 文件名：week_1.2_example03.py
# 开发工具：PyCharm
import requests
# 此次内容为关键词提交


def geturl(url):
    kv = {"wd": "Python"}
    r = requests.get(url, params=kv)  # 关键字为Python
    print(r.request.url)  # 查看提交的url连接
    print(r.status_code)
    print(len(r.text))  # 查看返回长度
    try:
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print(r.text)
    except:
        print("error")


if __name__ == "__main__":
    geturl("https://www.baidu.com/s")
