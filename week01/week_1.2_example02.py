# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/3/18 19:39
# 文件名：week_1.2_example02.py
# 开发工具：PyCharm
import requests


def geturl(url):
    r = requests.get(url, timeout=30)
    print(r.status_code)
    print(r.request.headers)
    kv = {"user-agent": "Mozilla/5.0"}
    r = requests.get(url, headers=kv)  # 修改headers
    print(r.status_code)
    print(r.request.headers)
    try:
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print(r.text)
    except:
        print("error")


if __name__ == "__main__":
    geturl("https://www.amazon.cn")
    # 这里会返回503错误 因为amazon会对个人的爬取进行限制，此时就要对request的header进行修改
    # 有个"python-requests/2.23.0" 代表就是个人爬取
    # 所以要模拟成浏览器访问
