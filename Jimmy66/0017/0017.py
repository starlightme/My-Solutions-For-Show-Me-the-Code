#!/bin/env python
# -*- coding: utf-8 -*- 

#要填json坑，前面写的代码，json部分是网上找的，还没有完全理解，尤其是相关的字符串编码没有实践
#抽空了解下从xls文件读取数据的库
#xls -> json -> xml 是我的思路，当然也可以尝试下直接xls -> xml
#主要还是比较看重json的应用。有时候感觉看了别人的代码，不自己用另一种方式实现，（即使变得复杂啰嗦）还是别人的代码


import xlrd


def read_xls(filename):
    data = xlrd.open_workbook(filename)
    table = data.sheet_by_index(0)        #通过索引获取xls文件第0个sheet
    nrows = table.nrows
    d = {}
    for i in range(nrows):
        d[str(i)] = table.row_values(i)[1:]  #取编号后的数据，以列表形式存在字典对应的值中
    return d


def main():
    print read_xls('student.xls')


if __name__ == '__main__':
    main()
