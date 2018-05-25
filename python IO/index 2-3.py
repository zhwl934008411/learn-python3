#-*- coding:utf-8 -*-
#文件读取方式;
#write(str):将字符串写入文件
#writelines(sequence_of_strings):
#写多行到文件，参数为可迭代对象(字符串、字符串组成的元组、列表、字符串所组成的迭代器)
'''
f=open('2.txt','w')
f.write('test write')
f.writelines('1,34,5')
f.writelines(('1','dd','22'))
f.writelines(['ff','ff','ee'])
score={
    'apa':33,
    'fff':33,
    'fdd':33
}
f.writelines(score)
#writelines方法只接受字符串及其衍生的各种元组等作为参数
f.close()
f=open('2.txt','w')
f.write('111111111')
f.flush()#flush()方法可以清空缓存，将write写入的数据写入到文件中
f.close()#文件在写入操作完成以后需调用close()方法，写入才会生效
'''
f=open('2.txt','w')
for i in range(1,9813):
    f.write('test write'+str(i)+'\n')#str()强转为字符串
f.flush()
#python文件为什么要关闭
'''
1.将写缓存同步到磁盘
2.linux系统中每个进程打开文件的个数是有限的
3.如果打开文件数到了系统限制，再打开就会失败
'''










