#-*- coding:utf-8 -*-
import os
#如何自由移动文件指针
'''python文件指针操作：
seek(offset[,whence]):移动文件指针
offset：偏移量，可以为负数
whence：偏移相对位置
f.seek(offset,os.SEE)
os.SEEK_CUR 重新设置指针的当前位置为offset
os.SEEK_END 重新设置指针的起始位置为文件末位开始第-offset位（offset一般为0或负数）
os.SEEK_SET 相对当前的文件指针，设置指针的起始位置向前进-offset位
'''

f=open('imooc.txt','r+')
print(f.tell()) #表示当前文件的指针

print(f.read(3))


print(f.tell())
f.seek(5,os.SEEK_SET)

print(f.tell())

print(f.read(3))

f.seek(2,os.SEEK_SET)
f.seek(0,os.SEEK_END)#python3.4不适用
print(f.tell())
'''
print(f.read(4))
f.seek(0,os.SEEK_END)
print(f.tell())
f.seek(-10,os.SEEK_CUR)
print(f.read(4))
print(f.tell())'''










