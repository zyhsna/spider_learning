# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/4/1 21:34
# 文件名：week_3_example01.py
# 开发工具：PyCharm


# 淘宝商品信息定向爬虫
# 目标：获取商品的名称和价格
# 注意！！！ 本实例仅用于学习 不可将其用于对淘宝性能影响的用途
# 注意！！！ 由于淘宝的反爬策略，需要修改search的headers才行
import requests
import re


def getHTMLText(url):
    try:
        kv = ""  # 登录信息因人而异
        r = requests.get(url, params=kv)
        print(r.status_code)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except r.status_code != 200:
        return ""


def parsePage(ilt, html):  # 获取商品名称和价格
    try:
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"', html)  # 首先检索view_price 然后获得价格，保存在plt列表
        tlt = re.findall(r'\"raw_title\"\:\".*?\"', html)  # .*? 最小匹配
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])  #  eval去掉双引号 split以:来分割字符串
            name = eval(tlt[i].split(':')[1])
            ilt.append([price, name])
    except:
        print("error")


def printGoodsList(ilt):
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format("序号", "价格", "商品名称"))
    count = 0
    for g in ilt:
        count += 1
        print(tplt.format(count, g[0], g[1]))


def main():
    goods = "书包"  # 搜索关键词
    depth = 2  # 爬取深度
    start_url = "https://s.taobao.com/search?q=" + goods  # url
    infolist = []  # 放信息
    for i in range(depth):
        try:
            url = start_url + "&s=" + str(44*i)  # 切换页面
            html = getHTMLText(url)
            parsePage(infolist, html)
        except:
            continue
    printGoodsList(infolist)


if __name__ == "__main__":
    main()




