# -*- coding:utf-8 -*-
import socket
'''

接口自动化测试从基础到框架


#接口基础
HTTP接口熟悉

常见接口介绍

接口工具的使用

常见接口基础面试



#接口开发
django-->get/post



#Unittest与接口测试结合
Unittest的使用

HTMLTestRunner

断言

Case的管理

Requests的引入使用


#接口自动化测试框架从设计到开发
设计框架

工具类封装

基类封装

调试错误

数据处理

回写测试结果

解决数据依赖

结果统计

邮件服务

发送报告


#常见接口测试查漏补缺
操作数据库

操作Cookie


小结:所有代码均来自于慕课网接口

'''

'''
常见的接口类型有哪些:
-->get/post 
get:从指定的资源请求数据 pull
post:向指定的资源提交要被处理的数据 push


'''
#创建一个socket,默认使用ipv4/TCP协议,
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#建立连接,指定ip地址和端口号
s.connect(('www.sina.com.cn',80))
# 发送数据:
s.send(b'GET/HTTP/1.1\r\nHost:www.sina.com.cn\r\nConnection:close\r\n\r\n')
# receive data
buffer=[]
while True:
    d=s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = b''.join(buffer)
print(data)
#data=b".join(buffer)








