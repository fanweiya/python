#!/usr/bin/env python
# -*- coding:utf-8 -*-
import scrapy
import os
import urllib
from scrapy.selector import HtmlXPathSelector
class XiaoHuarSpider(scrapy.spiders.Spider):
    name = "xiaohuar"  # APP的名字，必须定义
    start_urls = [
        "http://www.xiaohuar.com/hua/",  # 起始URL
    ]
    def parse(self, response):  # 抓取start_urls页面，自动执行parse回调函数
        hxs = HtmlXPathSelector(response)  # 匹配查找
        items = hxs.select('//div[@class="item_list infinite_scroll"]/div')
        for i in range(len(items)):
            srcs = hxs.select(
                '//div[@class="item_list infinite_scroll"]/div[%d]//div[@class="img"]/a/img/@src' % i).extract()
            names = hxs.select(
                '//div[@class="item_list infinite_scroll"]/div[%d]//div[@class="img"]/span/text()' % i).extract()
            schools = hxs.select(
                '//div[@class="item_list infinite_scroll"]/div[%d]//div[@class="img"]/div[@class="btns"]/a/text()' % i).extract()
            if srcs and names and schools:
                # print(names, srcs, schools)
                # ['覃罗莹'] ['/d/file/20161018/5385b7113046ac9ae560da41a44b12af.jpg'] ['广西农业职业技术学院']
                try:
                    ab_src = "http://www.xiaohuar.com" + srcs[0]  # 文件路径
                    file_name = names[0] + "." + srcs[0].split(".")[-1]  # 保存的文件名
                    file_path = os.path.join("./pic", file_name)  # 保存的路径
                    # print(ab_src, file_name, file_path)
                    # http://www.xiaohuar.com/d/file/20161018/5385b7113046ac9ae560da41a44b12af.jpg 覃罗莹jpg ./pic/覃罗莹jpg
                    urllib.request.urlretrieve(ab_src, file_path)  # 下载文件
                except Exception as e:
                    print("错误》》", e)