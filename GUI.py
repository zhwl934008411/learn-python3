#Python支持多种图形界面的第三方库,包括
'''
TK,wxWidgets,Qt,GTK
'''
#编写的Python代码会调用内置的Tkinter，Tkinter封装了访问Tk的接口；
#Tk是一个图形库，支持多个操作系统，使用Tcl语言开发；

#Tk会调用操作系统提供的本地GUI接口，完成最终的GUI

#from tkinter import *
import tkinter
#表示导入tkinter包的所有内容,相当于import tkinter

#从Frame派生一个Application类，这是所有Widget的父容器：
class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets() #创建窗口小部件

    def createWidgets(self):
        self.helloLabel = Label(self, text='Hello, world!')
        self.helloLabel.pack()
        self.quitButton = Button(self, text='Quit', command=self.quit)
        self.quitButton.pack()

#在GUI中，每个Button、Label、输入框等，都是一个Widget
if __name__ == '__main__':
    app = Application()
    # 设置窗口标题:
    app.master.title('Hello World')
    # 主消息循环:
    app.mainloop()









