# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/3/24 10:46
# 文件名：week_2_01.py
# 开发工具：PyCharm

# 解析HTML页面的第三方库 BeautifulSoup4
from bs4 import BeautifulSoup as bs
import requests

url = "https://python123.io/ws/demo.html"
r = requests.get(url)
print(r.status_code)
print(r.text)
demo = r.text
soup = bs(demo, "html.parser")  # 不仅要给出demo(即HTML格式的信息)，也要给出解释器
print(soup.prettify())

# BeautifulSoup 的基本元素
# <p>..</p>:标签 Tag
# <p class = "title"> ...</p>
# 名称及两个p是成对出现的 中间为属性域(Attributes)大于等于0
# 将标签树转化为BeautifulSoup类
# 可以将一个BeautifulSoup类对应一个HTML/xml文档的全部内容 xml需安装第三方库lxml

# 获取tag标签的方法
print(soup.title)
tag = soup.a  # 即第一个跳转页面
print(tag)
# 但是soup.b是有多个重载
print(tag.name)  # 获得a标签的名字
print(tag.parent.name)  # 获得其父亲名字，即包含a标签的上一级标签
print(tag.parent.parent.name)  # 再上一层
print(tag.attrs)  # 查看其属性，返回字典
print(tag.attrs["class"])  # 获得class属性
print(tag.attrs["href"])  # 获得连接
print(tag.string)
print(soup.p.string)

# 基于bs4库的内容遍历方法
# 由于html的树型格式 便有从根节点进行的下行遍历  和从叶子节点进行的上行遍历以及平级节点中的平行遍历

# 下行遍历 .contents为子节点列表 .children子节点的迭代类型，用于循环遍历 .descendants子孙节点迭代类型，包含所有子孙节点
# ∑(っ°Д°;)っ卧槽，不见了
print(soup.head.contents)  # 返回列表
print(soup.body.contents)
print(len(soup.body.contents))  # 查看其儿子节点数量
print(soup.body.contents[1])  # 查看第二个

for child in soup.body.children:
    print(child)  # 遍历儿子节点
print("-----------------------")
for child in soup.body.descendants:
    print(child)  # 遍历子孙节点

# 上行遍历 .parent节点的父亲标签  .parents节点先辈标签的迭代类型，用于遍历先辈节点
print("----------上行遍历---------")
for parent in soup.a.parents:  # 如果先辈存在打印其名字，否则返回当前列表
    if parent is None:
        print(parent)
    else:
        print("-----------------")
        print(parent.name)

# 平行遍历  注意：必须在同一父节点下才能遍历
# .next_sibling 返回下一个平行节点标签 .previous_sibling 返回上一个平行节点标签
# .next_siblings 迭代类型              .previous_siblings 迭代类型
print("----------平行遍历----------")
print("----------遍历后续----------")
for sibling in soup.a.next_siblings:
    print(sibling)
print("----------遍历前续----------")
for sibling in soup.a.previous_siblings:
    print(sibling)

# 更友好的显示HTML
# prettify()方法会自动加\n换行
