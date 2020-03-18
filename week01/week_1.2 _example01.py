# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/3/18 19:27
# 文件名：week_1.2 _example01.py
# 开发工具：PyCharm

import requests


def geturl(url):
    r = requests.get(url, timeout=30)
    print(r.status_code)
    try:
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print(r.text)
    except:
        print("error")


if __name__ == "__main__":
    geturl("https://www.bilibili.com")
    geturl("https://www.google.com")  # 因为众所周知的原因，无法访问 建议注释掉不然会导致程序一直运行
