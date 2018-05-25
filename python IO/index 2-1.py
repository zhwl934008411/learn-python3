'''
文件概念
文件：Python中文件是对象

linux:一切设备均可以看做是文件，如：磁盘文件，管道，网络Socket（套接字），外设

文件属性：用户，读，写，执行权限

文件打开方式
文件打开方法：open(name[,mode[buf]])
//name：文件路径 mode:打开方式 buf：缓冲buffering大小
mode:'r',只读方式打开，文件必须存在
'w'（包括'a'）,只写方式，文件不存在创建文件，文件存在则清空文件内容
'a',追加方式，文件不存在创建文件
'r+'/'w+',读写方式打开
'r+',读写方式打开
'a+',追加和读写方式打开

文件读取
文件读取方式：read([size]):读取文件（读取size个字节，默认读取全部）
              readline([size]):读取一行的size个字节
              readlines([size]):读取完文件，返回每一行所组成的列表

文件写入
文件写入方式：
write(str):将字符串写入文件
writelines(sequence_of_strings):写多行到文件


文件指针
文件对象属性

linux文件系统
os模块文件操作
文件练习

f=open("hello.py")#默认以只读方式打开文件,表示打开当前目录下的hello.py文件
print(type(f))
print(f.read())
#f.write("test")
#g=open("1.txt")
g=open("1.txt",'w')
g.write("test write")
g.close()
g=open("1.txt","w")
g.close()#write方式写入文件做的就是以空的同名文件覆盖原文件

f=open("hello.py",'a')#与w方式的区别是不是覆盖，是在文件结尾处追加
#f.write("\nprint 'hello world test a'")
f=open("hello.py",'r+')
f.write("test r+")
f.close()#test r+依次替换首行前几个字符

f=open("hello.py",'w+')
print(f.read())#先清空原文件内容
f.write("test w+")
f.close()
f=open("hello.py",'r+')
print(f.read())

f=open("hello.py",'a+')#不清空，直接追加，且开放读权限
f.write("hello world")
f.close()
'''
#rb rb+ wb wb+ ab ab+
f=open("hello.py",'rb')
print(f.read())
