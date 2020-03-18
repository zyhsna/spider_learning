# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/3/18 20:05
# 文件名：week_1.2_example04.py
# 开发工具：PyCharm
import requests
# 网络图片爬取
# 图片格式 http://www.example.com/picture.jpg


def geturl(url, path):
    r = requests.get(url)  # 关键字为Python
    print(r.status_code)
    print(len(r.text))  # 查看返回长度

    r.raise_for_status()
    r.encoding = r.apparent_encoding
    with open(path, 'wb') as f:
        f.write(r.content)
    f.close()


if __name__ == "__main__":
    path = r"C:\Users\zyh\Desktop\1.jpg"  # 保存到桌面并命名为1.jpg
    geturl("https://iknow-pic.cdn.bcebos.com/6d81800a19d8bc3e45438732878ba61ea9d345fb", path)
