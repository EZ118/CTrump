from tkinter import *
import warnings

warnings.filterwarnings("ignore")                                          #防止报错

def trans(url):
    url = url.replace("namespace std","trump_law instead")
    url = url.replace(";"," $ ")
    url = url.replace("cout","donate")
    url = url.replace("cin","earn")
    url = url.replace("return ","trump_gives_back ")
    url = url.replace("long long ","money ")
    url = url.replace("int ","pocket_money ")
    url = url.replace("void","rule")
    url = url.replace("bool","news")
    url = url.replace("false","fake")
    #通过替换语句，将指定字符替换为CTrump语法字符
    return url

def getCon():
    text_content = (codebox1.get('0.0','end')).split('\n')         #获取文本框的内容，并转换为列表类型
    text_content.pop() 
    return text_content

def submit():
    lst = getCon()                                                                     #调用函数，获取文本框内容
    length = len(lst) + 1                                                           #获取列表项目数
    for i in range(1,length):
        codebox2.insert(1.0, str(trans(lst[length-1-i]) + '\n')) #逐行替换并输出
    data = '''#include <iostream>
#include <bits/stdc++.h>

#define $ ;
#define donate cout
#define earn cin
#define trump_gives_back return
#define money long long
#define trump_law namespace
#define instead std
#define rule void
#define news bool
#define fake false
#define non_fiction true
#define pocket_money int
'''                                                                                              #Ctrump.h的内容
    codebox2.insert(1.0, str(data) + '\n')                                 #在文本框内加入CTrump库的语句

win = Tk()                                                                                #添加窗体
win.title('CTrump')                                                                  #设置窗体标题
win.geometry('500x320+100+100')                                    #设置窗体大小、起始位置

Button1 = Button(win, text='Go!', font=('等线', 11), command = submit)
Button1.place(y=15, x=258, width=222.5, height=25)      #放置按钮

codebox1 = Text(win, font=('等线', 11))
codebox1.place(y=15, x=15, width=222.5, height=290)   #负责输入的文本框

codebox2 = Text(win, font=('等线', 11))
codebox2.place(y=55, x=258, width=222.5, height=250) #负责输出代码的文本框

win.mainloop()


