# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/3/24 20:07
# 文件名：week_2_example.py
# 开发工具：PyCharm
import requests
from bs4 import BeautifulSoup as BS
import bs4
# 获取大学排名
# ①从网上获得网页内容
# ②提取信息到合适的数据结构
# ③输出结果


def getHtMLText(url):  # 得到文本信息

    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except r.status_code != 200:
        print("error")
        return ""


def fillUnivList(ulist, html):  # 填充list列表
    soup = BS(html, "html.parser")
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):  # 检测tr标签的类型，如果不是tag类型将过滤掉
            tds = tr("td")
            ulist.append([tds[0].string, tds[1].string, tds[3].string, tds[2].string])  # 填充大学名称 排名 得分
    pass


def printUnivList(ulist, num):  # 将列表信息打印 num代表想打印多少信息
    tplt = "{0:^10}\t{1:{4}^10}\t{2:^10}\t{3:^10}"
    print(tplt.format("排名", "学校名称", "总分", "地区", chr(12288)))
    for i in range(num):
        u = ulist[i]
        print(tplt.format(u[0], u[1], u[2], u[3], chr(12288)))  # 每个学校变量为u


if __name__ == "__main__":
    uinfo = []  # 存放信息
    url = "http://www.zuihaodaxue.com/zuihaodaxuepaiming2016.html"
    html = getHtMLText(url)
    fillUnivList(uinfo, html)
    printUnivList(uinfo, 20)  # 先列出前20所
