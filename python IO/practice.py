import os
import os.path
import configparser

class student_info(object):

    def __init__(self,recordfile):
        self.logfile=recordfile
        self.cfg=configparser.ConfigParser()

    def cfg_load(self):
        self.cfg.read(self.logfile)

    def cfg_dump(self):
        for se in self.cfg.sections():
            print(se)
            print(self.cfg.items(se))
        print('-----------------')

    def delete_item(self,section,key):
        self.cfg.remove_option(section,key)

    def delte_section(self,section):
        self.cfg.remove_section(section)

    def add_section(self,section):
        self.cfg.add_section(section)

    def set_item(self,section,key,value):
        self.cfg.set(section,key,value)#添加或覆盖原来item的值

    def save(self):
        fp=open(self.logfile,'w')
        self.cfg.write(fp)
        fp.close()

if __name__ == '__main__':#这里是双下划线
    #new一个对象
    info=student_info('imooc.txt')
    info.cfg_load()
    info.cfg_dump()
    #info.delete_item('userinfo','name')
    #info.cfg_dump()
    #info.delte_section('userinfo')
    #info.cfg_dump()
    #info.add_section('login')
    info.set_item('login','password','12345')
    info.cfg_dump()
    info.save()#无close()方法的话就无法立即生效，将缓存中的数据写入到文件中

