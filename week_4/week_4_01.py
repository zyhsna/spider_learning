# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/4/8 18:21
# 文件名：week_4_01.py
# 开发工具：PyCharm

# scrapy框架的使用
import scrapy
# 5+2模式
# ENGINE  (ITEM PIPELINES)  SPIDERS DOWNLOADER SCHEDULER 5个模块
# engine 和 spiders 以及Downloader之间有middleware结构
# 当然具体内容仍需自己学习，这里只是简介
import scrapy

# 先建立目录
# cmd命令行输入 scrapy startproject python123demo
# 由于cmd死活建立不来project,只能作罢
