# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/3/31 19:12
# 文件名：week_3_01.py
# 开发工具：PyCharm

# 正则表达式 regular expression(RE)
# 用来简洁表达字符串的方式
# . 表示任何单个字符
# [ ] 字符集，对单个字符给出取值范围 例如[abc]表示a、b、c,[a-z]表示a到z全部字符
# [^ ] 非字符集，对单个字符给出排除范围，就是除了这些字符
# * 代表前一个字符的0次或无限次扩展  abc* 表示ab或abc或abcc或abccc·····
# + 表示前一个字符的1次或无限次扩展  abc+ 表示 abc 或 abcc ·····
# ? 表示前一个字符的0次或1次扩展  abc?表示 ab或abc
# | 表示左右表达式任意一个  abc|def 表示abc或者def
# {m} 表示扩展前一个字符m次  ab{2}c表示abbc
# {m,n} 表示扩展前一个字符m至n次 ab{1,2}c表示abc或abbc
# ^ 表示匹配字符串开头 ^abc 表示以abc开头的字符串
# $ 表示匹配字符串结尾 abc$表示以abc结尾的字符串
# () 分组标记，内部只能使用 | 标识符 (abc)表示abc (abc|def)表示abc或者def
# \d 数字 等价于[0-9]
# \w  单词字符 等价于[A-Z a-z 0-9]

# 例如 P( Y|YT|YTH|YTHO)?N 对应 PN PYN PYTN PYTHN PYTHON
# PY[TH]ON 表示PYTON 或 PYHON
# ^[A-Za-z]+$ 代表由26个字母组成的字符串

import re
# 正则表示式采用raw string 类型 ，只需在字符串前加个r便可
# search() 在一个字符串中搜索匹配正则表达式的第一个位置，返回match对象
# match() 从一个字符串的开始位置起匹配正则表达式，返回match对象
# findall() 搜索字符串，以列表形式返回全部能匹配的字符串
# split() 将一个字符串按照正则表示式匹配结果进行分割，返回列表类型
# finditer() 搜索字符串，返回一个匹配结果的迭代类型，每个迭代类型均为match对象
# sub() 在一个字符串中替换所有匹配正则表达式的子串，返回替换后的字符串

# re.search(pattern, string, flags=0)
# pattern 正则表达式的字符串或原生字符串表示
# string 带匹配字符串
# flags 正则表达式使用时的标记 re.I 忽略大小写 re.M 操作符^将对字符串的每行当做匹配开始 re.S 操作符.能够匹配所有字符

match = re.search(r'[1-9]\d{5}', "BIT 100081")
if match:
    print(match.group(0))

match = re.match(r'[1-9]\d{5}', "BIT 100081")
# print(match.group(0))  # 会报错，因为未匹配到字符串，为None

match = re.match(r'[1-9]\d{5}', "100081 BIT")
print(match.group(0))

ls = re.findall(r'[1-9]\d{5}', "100081 BIT TSU100084")
print(ls)

# re.split(pattern, string, maxsplit=0, flags=0)
# maxsplit 最大分割数，剩余部分作为最后一个元素输出，就是一共输出多少个

ls = re.split(r'[1-9]\d{5}', "BIT100081 TSU100084", maxsplit=1)
print(ls)

ls = re.split(r'[1-9]\d{5}', "BIT100081 TSU100084")
print(ls)

for match in re.finditer(r'[1-9]\d{5}', "BIT100081 TSU100084"):
    if match:
        print(match.group(0))

# re.sub(pattern, repl, string, count=0, flags=0)
# repl 用来替换的字符串
# count 替换的最大次数

print(re.sub(r'[1-9]\d{5}',':zipcode', "BIT100081 TSU100084", count=1))

# re.compile(pattern, flags) 将正则表达式的字符串形式编译成正则表达式对象
pat = re.compile(r"[1-9]\d{5}")
rst = pat.search("BIT 100081")
print(rst.group(0))

# match 对象
# 属性 .string 带匹配文本 .re 匹配时使用的pattern对象  .pos 正则表达式搜索的开始位置 .endpos 搜索文本的结束位置
# 方法 .group(0) 获得匹配后的字符串 .start() .end() 匹配字符串在原始字符串的开始和结束位置 .span() 返回(.start(),.end())

match = re.search(r'[1-9]\d{5}', "BIT100081 TSU100084")
print(match.string)
print(match.re)
print(match.pos)
print(match.endpos)
print(match.span())

# 贪婪匹配和最小匹配
match = re.search(r"PY.*N", "PYANBNCNDN")
print(match.group(0))
# re库默认贪婪匹配，即输出最长匹配

match = re.search(r"PY.*?N", "PYANBNCNDN")  # 最小匹配
print(match.group(0))
# *?   ??   +?    {m,n}?  最小匹配操作符


