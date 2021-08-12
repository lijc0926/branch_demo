#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/7 21:20
# @Author  : jingchen
# @File    : 爬虫.py


import requests
import re
import xlwt
import os
import shutil

class ReptilesNovel(object):
    """
    爬一本小说的内容
    """
    def __init__(self, url):
        """
        :param url: 为要爬取的小说的url地址
        """
        self.url = url

    def get_data(self):
        """
        获取整本小说的目录名和目录链接以及小说名
        :return:
        """
        res = requests.post(self.url)
        book_num = re.findall("https://www.xs4.cc/(.*?)/", self.url)[0]
        res.encoding = "GBK"
        res =res.text
        book_name = re.findall("<h1>(.*?)</h1>", res)[0] # 获取小说名
        mulu_list = re.findall('html">(.*?)</a>', res)[9:] # 获取小说的目录列表
        mulu_url = re.findall(f'<a href="/{book_num}/(.*?).html">', res)[9:] # 获取本小说每个章节的uri
        mulu_url_list = []
        # 拼接小说的每个章节的url地址
        for i in mulu_url:
            mulu_url_list.append(f"{self.url}{i}.html")
        # 将小说的章节名和链接地址一一对应起来存成一个字典
        mulu_dict = {}
        for i in range(len(mulu_list)):
            mulu_dict[mulu_list[i]] = mulu_url_list[i]
        # return mulu_url_list, mulu_dict
        self.mulu_url_list = mulu_url_list
        self.mulu_dict = mulu_dict
        self.book_name = book_name

    def write_txt(self):
        """
        将小说每个章节的内容写入一个txt文件内，并且将txt文件在本地的地址保存
        :return:
        """
        # 判断存放小说信息的目录是否存在，存在删除并创建，不存在创建
        self.get_data()
        if os.path.exists(f"D:/python_demo_folder/{self.book_name}"):
            shutil.rmtree(f"D:/python_demo_folder/{self.book_name}")
            os.mkdir(f"D:/python_demo_folder/{self.book_name}")
        else:
            os.mkdir(f"D:/python_demo_folder/{self.book_name}")
        data_path = f"D:/python_demo_folder/{self.book_name}"
        txt_file_path_list = []
        # 根据每个章节小说的链接，下载小说的内容并且写入对应的txt文件中
        for k, v in self.mulu_dict.items():
            txtfile_pata = f"{data_path}/{k}.txt"
            txt_file_path_list.append(txtfile_pata)
            res = requests.get(v)
            res.encoding = "GBK"
            res = res.text
            data = re.findall('<div id="content">(.*?)</div>', res, re.S)[0]
            data_list = re.findall('&nbsp;&nbsp;&nbsp;&nbsp;(.*)', data)
            with open(txtfile_pata, "w") as f:
                for i in data_list:
                    data_ever = i.replace("<br />", "")
                    f.write(data_ever)
        self.txt_file_path_list = txt_file_path_list
        self.data_path = data_path

    def wirte_data_to_excel(self):
        """
        将小说的信息写入xls文件中
        :return:
        """
        self.get_data()
        self.write_txt()
        # 将小说的目录名，链接地址和章节的内容所在的txt文件的路径写入excel中
        excel = xlwt.Workbook(encoding='utf-8')
        sheet = excel.add_sheet("book_name", cell_overwrite_ok=True)
        sheet.write(0, 0, "目录名")
        sheet.write(0, 1, "链接")
        sheet.write(0, 2, "文件内容txt文件地址")
        row = 1
        for k,v in self.mulu_dict.items():
            sheet.write(row, 0, k)
            sheet.write(row, 1, v)
            sheet.write(row, 2, self.txt_file_path_list[row-1])
            row += 1
        excel.save(f"{self.data_path}/{self.book_name}.xls")
        print(f"数据已经爬取完成，爬取的数据存放的地址是{self.data_path}")


if __name__ == '__main__':
    a = ReptilesNovel("https://www.xs4.cc/0_812/")
    a.wirte_data_to_excel()





