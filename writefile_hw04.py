from tkinter import *
from tkinter import ttk #theme of tk
from tkinter import messagebox
from datetime import datetime

##########################CSV#################################
import csv

def writecsv(datalist):
    with open('data.csv','a',encoding='utf-8',newline='') as file:
        fw = csv.writer(file)
        fw.writerow(datalist)

def readcsv():
    with open('data.csv',encoding='utf-8',newline='') as file:
        fr = csv.reader(file)
        data = list(fr)
    return data
###########################CSV##################################

GUI = Tk()
GUI.title('รายการของ')
GUI.geometry('500x800')

LF1 = ttk.LabelFrame(GUI,text='เพิ่มรายการ')
LF1.pack(ipadx=10,ipady=20)

v_data = StringVar() #ตัวแปรพิเศษที่ใช้กับข้อความใน GUI
E1 = ttk.Entry(LF1,textvariable=v_data)
E1.pack(ipadx=10,ipady=10)

def SaveData():
    t = datetime.now().strftime('%Y%m%d')
    data = v_data.get() #ดึงข้อมูลจากตัวแปร v_data มาใช้งาน
    text = [t,data]
    writecsv(text)
    v_data.set('') #เคลัยร์ข้อมูลในช่องกรอก

B1 = ttk.Button(GUI, text='บันทึก',command=SaveData)
B1.pack(ipadx=10, ipady=10)

def ShowData():
    data = readcsv()
    messagebox.showinfo('Show Data',data)

FB2 = Frame(GUI)
FB2.place(x=250, y=150)
B2 = ttk.Button(GUI, text='แสดงรายการ',command=ShowData)
B2.pack(ipadx=10, ipady=10)

