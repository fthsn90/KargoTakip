##fthsn90##
#23.05.2020

from tkinter import *
from PIL import ImageTk,Image
import tkinter
from tkinter import messagebox
from selenium import webdriver
import time
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import pyautogui
from tkinter import messagebox

root = Tk()
root.geometry("890x365+200+150")
root.title("Kargo Takip")
img= ImageTk.PhotoImage(Image.open("pics/carg.png"))
yrt = ImageTk.PhotoImage(Image.open("pics/yurtici.png"))
mng = ImageTk.PhotoImage(Image.open("pics/mng.png"))
aras = ImageTk.PhotoImage(Image.open("pics/aras.png"))
ptt = ImageTk.PhotoImage(Image.open("pics/ptt.png"))
ups = ImageTk.PhotoImage(Image.open("pics/ups.png"))
yrts = ImageTk.PhotoImage(Image.open("pics/yrtsimge.jpg"))
mngs = ImageTk.PhotoImage(Image.open("pics/mngsimge.jpg"))
upss = ImageTk.PhotoImage(Image.open("pics/upssimge.png"))
arass = ImageTk.PhotoImage(Image.open("pics/arassimge.jpg"))
ptts = ImageTk.PhotoImage(Image.open("pics/pttsimge.png"))
root.tk.call('wm','iconphoto',root._w,img)

def show():
    root.update()
    root.deiconify()

def sorgula(deger):
    driver_path ="C:/Users/fthsn/Downloads/chromedriver.exe "

    if deger ==1 and yrtgir.get():
        browser = webdriver.Chrome(executable_path=driver_path)
        browser.get("https://www.yurticikargo.com/")
        time.sleep(5)
        browser.find_element_by_xpath("//*[@id='shipment-search-btn']").send_keys(f"{yrtgir.get()}",Keys.ENTER)

    elif deger ==2 and mnggir.get():

        browser = webdriver.Chrome(executable_path=driver_path)
        browser.get("https://www.mngkargo.com.tr/")
        browser.find_element_by_xpath("//*[@id='mm-0']/div[4]/div/div/div[1]/ul/li[1]/a").click()
        time.sleep(2)
        browser.find_element_by_xpath("//*[@id='gonderi_no']").send_keys(f"{mnggir.get()}",Keys.ENTER)

    elif deger ==3 and upsgir.get():
        browser.get("https://www.ups.com.tr/gonderi_takip.aspx")
        time.sleep(2)
        browser.find_element_by_xpath("//*[@id='ctl00_MainContent_text_yurtici2_takip']").send_keys(f"{upsgir.get()}",Keys.ENTER)

    elif deger ==4 and pttgir.get():
        browser.get(f"https://gonderitakip.ptt.gov.tr/Track/Verify?q={pttgir.get()}")
        time.sleep(2)
        pyautogui.leftClick(x=558,y=334)

    elif deger ==5 and arasgir.get():
        browser.get("https://www.araskargo.com.tr/tr/index.aspx?cargo=1")
        time.sleep(2)
        browser.find_element_by_xpath("//*[@id='InputCargo1']").send_keys(f"{arasgir.get()}",Keys.ENTER)
    else:
        messagebox.showwarning("Uyarı","Kutucuk boş bırakılamaz!")
def yurticikargo():
    global yrtgir
    root.withdraw()
    fram = Toplevel()
    fram.geometry("400x200+500+150")
    fram.title("Yurtiçi Kargo Takip")
    fram.tk.call('wm','iconphoto',fram._w,yrts)
    lbl = Label(fram,text="Kargo Takip Numarasını giriniz")
    lbl.pack()
    yrtgir = Entry(fram,bd=3)
    yrtgir.pack()
    btn = Button(fram,text="Sorgula",bd=5,command= lambda: sorgula(1) )
    btn.pack()
    btn2 = Button(fram,text="Ana Menü",bd=5,command= show)
    btn2.pack()
def mngkargo():
    global mnggir
    root.withdraw()
    fram = Toplevel()
    fram.geometry("400x200+500+150")
    fram.title("Mng Kargo Takip")
    fram.tk.call('wm','iconphoto',fram._w,mngs)
    lbl = Label(fram,text="Kargo Takip Numarasını giriniz")
    lbl.pack()
    mnggir = Entry(fram,bd=3)
    mnggir.pack()
    btn = Button(fram,text="Sorgula",bd=5,command= lambda: sorgula(2) )
    btn.pack()
    btn2 = Button(fram,text="Ana Menü",bd=5,command= show)
    btn2.pack()
def upskargo():
    global upsgir
    root.withdraw()
    fram = Toplevel()
    fram.geometry("400x200+500+150")
    fram.title("Ups Kargo Takip")
    fram.tk.call('wm','iconphoto',fram._w,upss)
    lbl = Label(fram,text="Kargo Takip Numarasını giriniz")
    lbl.pack()
    upsgir = Entry(fram,bd=3)
    upsgir.pack()
    btn = Button(fram,text="Sorgula",bd=5,command= lambda: sorgula(3) )
    btn.pack()
    btn2 = Button(fram,text="Ana Menü",bd=5,command= show)
    btn2.pack()
def pttkargo():
    global pttgir
    root.withdraw()
    fram = Toplevel()
    fram.geometry("400x200+500+150")
    fram.title("Ptt Kargo Takip")
    fram.tk.call('wm','iconphoto',fram._w,ptts)
    lbl = Label(fram,text="Kargo Takip Numarasını giriniz")
    lbl.pack()
    pttgir = Entry(fram,bd=3)
    pttgir.pack()
    btn = Button(fram,text="Sorgula",bd=5,command= lambda: sorgula(4) )
    btn.pack()
    btn2 = Button(fram,text="Ana Menü",bd=5,command= show)
    btn2.pack()
def araskargo():
    global arasgir
    root.withdraw()
    fram = Toplevel()
    fram.geometry("400x200+500+150")
    fram.title("Aras Kargo Takip")
    fram.tk.call('wm','iconphoto',fram._w,arass)
    lbl = Label(fram,text="Kargo Takip Numarasını giriniz")
    lbl.pack()
    arasgir = Entry(fram,bd=3)
    arasgir.pack()
    btn = Button(fram,text="Sorgula",bd=5,command= lambda: sorgula(5) )
    btn.pack()
    btn2 = Button(fram,text="Ana Menü",bd=5,command= show)
    btn2.pack()

btn1 = Button(root,text="Yurtici",image=yrt,command=yurticikargo)
btn1.grid(row=0,column=0)
btn2 = Button(root,text="Mng",image=mng,command=mngkargo)
btn2.grid(row=0,column=1)
btn3 = Button(root,text="Aras",image=aras,command=araskargo)
btn3.grid(row=1,column=0)
btn4 = Button(root,text="Ptt",image=ptt,command=pttkargo)
btn4.grid(row=1,column=1)
btn5 = Button(root,text="Ups",image=ups,command=upskargo)
btn5.grid()


root.mainloop()