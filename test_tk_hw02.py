from tkinter import *
from tkinter import ttk #theme of tk
from tkinter import messagebox
from money import *
from info import *
from study import *

GUI = Tk()
GUI.title('โปรแกรมบันทึกข้อมูล')
GUI.geometry('500x400')

L1 = Label(GUI,text='Account Info',fg='blue')
L1.pack(ipadx=10,ipady=20)

def Info():
    text = '{} {}'.format(name,lastname)
    messagebox.showinfo('account name',text)

B1 = ttk.Button(GUI, text='ชื่อบัญชี',command=Info)
B1.pack(ipadx=10, ipady=10) #ให้ปุ่ม 'แสดงจำนวนเงิน' แสดงอยู่ยนกลาง
#ipad x,y ขยายขนาดปุ่มด้าน x y ไปอีก 10 pixel

#################################################

def Money_1():
    text = my_account1
    messagebox.showinfo('my account',text)

FB1 = Frame(GUI)#คล้ายกระดาน
FB1.place(x=100, y=150)
B2 = ttk.Button(FB1, text='แสดงจำนวนเงินบัญชีที่ 1',command=Money_1)
B2.pack(ipadx=10, ipady=10)
##################################################

def Money_2():
    text = my_account2
    messagebox.showinfo('my account',text)

FB1 = Frame(GUI)#คล้ายกระดาน
FB1.place(x=250, y=150)
B2 = ttk.Button(FB1, text='แสดงจำนวนเงินบัญชีที่ 2',command=Money_2)
B2.pack(ipadx=10, ipady=10)
##################################################

def Study():
    text = subject
    messagebox.showinfo('my subject',text)

FB1 = Frame(GUI)
FB1.place(x=200, y=250)
B2 = ttk.Button(FB1, text='subject',command=Study)
B2.pack(ipadx=10, ipady=10)
##################################################

GUI.mainloop()
