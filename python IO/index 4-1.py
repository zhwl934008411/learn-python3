import configparser
'''
Python文件练习
练习内容：使用Python管理ini文件：实现查询，添加，删除，保存
练习目的：1.掌握文件基本操作
2.认识ini文件
3.了解ConfigParser
ini配置文件格式：
节:      [session]
参数：    name=value

'''
cfg=configparser.ConfigParser()#创建对象
cfg.read('imooc.txt')
print(cfg.sections()[1])
for se in cfg.sections():
    print(se)
    print(cfg.items(se))
print(cfg.get('userinfo','name'))#传入session和key
cfg.set('userinfo','name','lisi')
print(cfg.get('userinfo','name'))
cfg.set('userinfo','email','934008411@qq.com')
print(cfg.get('userinfo','email'))
cfg.remove_option('userinfo','email')
#print(cfg.get('userinfo','email'))
cfg.remove_section('userinfo')
print(cfg.sections())