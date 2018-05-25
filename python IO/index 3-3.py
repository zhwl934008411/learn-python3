#-*- coding:utf-8 -*-
import os
import os.path

#使用os模块打开文件
'''os.open(filename,flag[,mode])
flag:打开文件的方式
os.O_CREAT:创建文件
os.O_RDONLY:只读方式打开
os.O_WRONLY:只写方式打开
os.O_RDWR:读写方式打开
os.write(filename,string):写入文件
os.read(filename.buffersize):读取文件
os.lseek(filename,pos,how):文件指针操作
os.close(filename):关闭文件

fd=os.open('3.txt',os.O_CREAT | os.O_RDWR)
fe=os.write(fd,'I love imooc')
ff=os.lseek(fd,0,os.SEEK_SET)
print(ff)#(ff代表当前指针的位置)
print(os.read(fd,5))
os.close(fd)
fd=os.open('3.txt',os.O_CREAT | os.O_RDWR)
print(os.access('3.txt',os.F_OK))#判断文件是否存在
print(os.access('3.txt',os.W_OK))
#print(os.access('3.txt',os.))
#print(os.access('3.txt',os_R_OK))
#print(os.access('3.txt',os_X_OK))
print(os.listdir('D:\Eclipse\Python文件处理'))
#os.remove('arg.py')#无法删除不存在的文件
print(os.listdir('./'))#返回文件所在目录所有文件的列表
#os.rename('wuwuwu.txt','1.txt')#无法重命名不存在的文件
#os.mkdir('test1')#未指定路径，默认在本目录下创建
#os.makedirs('test1/test2/test3')#创建test1下的多级目录
#os.rmdir('test')#无法移除不存在的目录
#os.rmdir('test1')#无法移除一个非空目录
os.removedirs('test1/test2/test3')#移除多级目录'''
'''os.path模块方法介绍'''
#'./'表示当前目录
print(os.path.exists('imooc.txt'))
print(os.path.exists('imoo.txt'))
print(os.path.isdir('imooc.txt'))
print(os.path.isfile('imooc.txt'))
print(os.path.getsize('imooc.txt'))
print(os.path.basename('./imooc.txt'))#返回路径
print(os.path.dirname('./imooc.txt'))#返回路径所在目录












