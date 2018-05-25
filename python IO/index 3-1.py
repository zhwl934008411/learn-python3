#-*- coding:utf-8 -*-
import sys
import os
import codecs
'''文件对象属性
file.fileno():文件描述符
file.mode:文件打开权限
file.encoding:文件编码格式
file.closed:文件是否关闭
标准文件
文件标准输入：sys.stdin;
文件标准输出：sys.stdout;
文件标准错误：sys.stderr;
文件命令行参数


文件编码格式

f=open('imooc.txt','r')
print(f.fileno())
print(f.mode)
print(f.encoding)
print(f.closed)
print(f.name)
f.close()
print(f.closed)

f=sys.stdin
print(f.fileno())
print(f.closed)
print(f.encoding)
print(f.name)
print(f.mode)
#print(f.read(4))
g=sys.stdout
print(g.fileno())
print(g.name)
print(g.mode)
g.write('223444')
print(sys.stderr.name)
print(sys.stderr.mode)
sys.stderr.write('efhehu')
print(sys.stderr.fileno())


f=open('imooc.txt','r+')
a=unicode.encode(u'慕课','utf-8')#再传入一个参数表示编码格式
#f.write(u'慕课')
f.write(a)
#utf-8 英文或数字占一个字节 汉字占三个字节
f.seek(0,os.SEEK_SET)
print(f.read())'''
#如何创建一个utf-8或者其他编码格式的文件
#使用codecs模块提供方法创建指定编码格式文件

f=codecs.open('test.txt','w','utf-8')
f.write(u'慕课')
f.close()

