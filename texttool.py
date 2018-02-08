import nltk
import Tkinter
from Tkinter import *
from PIL import ImageTk, Image
import tkMessageBox
import tkFont


from trendy_gui2 import trendy_main
from summary import __main__
from WSD import wsd_gui_
from word_cloud import cloud_gui
from gui_2k16 import main as m
def sel1():
    __main__()

def sel2():
    trendy_main()

def sel3():
    wsd_gui_()

def sel4():
    m()
    
def sel5():
    cloud_gui()
   
    

def main():
    global top
    top = Tkinter.Tk()
    top.configure(background='black')
    w = top.winfo_screenwidth()
    h = top.winfo_screenheight()
    top.geometry("%dx%d+0+0"%(w,h))
    img = ImageTk.PhotoImage(Image.open("images\\textool.jpg"))
    top.title("Text Tool")
    frame = Frame(top,height=0,width=556)
    frame.pack()
    space = Label(frame)
    heading = Label(top,font=tkFont.Font(family="AltamonteNF",size=55,weight="bold"),fg='yellow',text="Text Tool")
    heading.configure(background='black')
    heading.pack()
    panel = Label(top, image = img)
    panel.pack()
    global var
    var = StringVar()
    R1 = Button(top, font=tkFont.Font(family="Times New Roman",size=20,weight="bold"),text="Top 'n' Sentences",height=2, width=20, command=sel1)
        
    R1.pack( anchor = W )
    R1.place(bordermode=INSIDE,x=200, y=200)
    R1.configure(bg= "#abddee")
        
    R2 = Button(top,font=tkFont.Font(family="Times New Roman",size=20,weight="bold"), text="Get Trends",height=2, width=20, command=sel2)
    R2.pack( anchor = W )
    R2.place(bordermode=INSIDE,x=500, y=280)
    R2.configure(bg= "#ead1dc")

    R3 = Button(top, font=tkFont.Font(family="Times New Roman",size=20,weight="bold"),text="Ambiguity Resolver",height=2, width=20, command=sel3)
    R3.pack( anchor = W)
    R3.place(bordermode=INSIDE,x=800, y=360)
    R3.configure(bg= "#d9ead3")

    R4 = Button(top,font=tkFont.Font(family="Times New Roman",size=20,weight="bold"), text="Topographic News",height=2, width=20, command=sel4)
    R4.pack( anchor = W)
    R4.place(bordermode=INSIDE,x=500, y=440)
    R4.configure(bg= "#ffe599")
    
    R5 = Button(top,font=tkFont.Font(family="Times New Roman",size=20,weight="bold"), text="Word Cloud",height=2, width=20,   command=sel5)
    R5.pack( anchor = W)
    R5.place(bordermode=INSIDE,x=200, y=520)
    R5.configure(bg= "#f9cb9c")

    top.mainloop()
 

main();
