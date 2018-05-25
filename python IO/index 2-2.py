import io
'''
#文件读取方式
#read([size]),读取size个字节，size为空默认读取全部内容，
#readline([size]):读取一行的size个字节,size为空默认读取一行全部内容
#readlines([size]):读取完文件，返回每一行数据组成的列表
f=open('1.txt')
print(f.readline())#先读取第一行全部数据
print(f.readline(3))#后读取第二行的前三个字符
print(f.readline(3))#后读取第二行的第四到第六个个字符
#当前行长度>size的值，返回size长度的字节
#当前行长度<size的值，返回整行的数据
#print(f.readlines())#读取完剩余未被读取的文件(最大不超过8192b)，并返回每一行数据组成的列表，缓存最大是8192b
f.close()
print(io.DEFAULT_BUFFER_SIZE)
'''
#iter:使用迭代器读取文件
f=open("1.txt")
iter_f=iter(f)
lines=0
for line in iter_f:
    print(f.read())#每次对f的每一行进行读取并输出
    lines = lines + 1#然后下一轮会自动清空，所以结果是1
print(lines)
#使用迭代器进行读取，每次从文件取出一行存入到buffer中进行读操作，
#可以节省内存



