#!/bin/env python3
# -*- coding: utf-8 -*- 

#Python3 version

import xlrd
import xml.etree.ElementTree as ET
from xml.dom import minidom

def read_xls(filename):
    data = xlrd.open_workbook(filename)
    table = data.sheet_by_index(0)        
    nrows = table.nrows
    d = {}
    for i in range(nrows):
        d[str(i+1)] = table.row_values(i)[1:]  
    return d
 
def write_xml(d):
    doc = minidom.Document()
    root = doc.createElement("root")
    doc.appendChild(root)
    students = doc.createElement("students")
    root.appendChild(students)
    students.appendChild(doc.createComment('    学生信息表\n    "id" : [名字, 数学, 语文, 英文]\n'))
    string = ''
    for i in range(len(d)):
      string += str(i) + ' ' + ':' + ' ' + str(d[str(i+1)]) + '\n'
    content = doc.createTextNode(string)
    students.appendChild(content)
    with open('student.xml',mode='w',encoding='utf-8') as f:
      doc.writexml(f)

def main():
    d = read_xls('student.xls')
    write_xml(d)


if __name__ == '__main__':
    main()