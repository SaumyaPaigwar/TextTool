import Tkinter
from Tkinter import *
from PIL import ImageTk, Image
import tkMessageBox
import tkFont
import webbrowser
import plotly.plotly as py
import plotly.graph_objs as go
import CallJava_JPype as cj
from jpype import *
import jpype

from post import __main__



def sel():
       selection =  str(var.get())#topic
       #s= "https://www.google.co.in/?q="+"%s" %selection
       s= "https://www.google.co.in/search?q={}".format(selection)
       webbrowser.open_new_tab(s)
       label = Label(top)
       label.pack()
       label.config(text = selection)
       
       
       
def helloCallBack(domain):
        global node
        #print "calling main"
        #print "calling jpype"
        #root.destroy()
        tkMessageBox.showinfo("Info", "Retreiving Trends. Please wait a few seconds...")
        """cj.main(domain)"""
        node=__main__(domain)
        #print "node in gui"
        #print node
        print node[0]
        print node[1]
        print node[2]
        print node[3]
        print node[4]
        global var
        var = StringVar()
        #rad_img = ImageTk.PhotoImage(Image.open("but.png"))
        R1 = Radiobutton(top, text="%s" %node[0],height=2, width=20, variable=var, value="%s" %node[0],
                          command=sel)
        
        R1.pack( anchor = W )
        R1.place(bordermode=INSIDE,x=730, y=200)
        R1.configure(bg= "#abddee")
        
        R2 = Radiobutton(top, text="%s" %node[1],height=2, width=20, variable=var, value="%s" %node[1],
                          command=sel)
        R2.pack( anchor = W )
        R2.place(bordermode=INSIDE,x=730, y=240)
        R2.configure(bg= "#ead1dc")

        R3 = Radiobutton(top, text="%s" %node[2],height=2, width=20, variable=var, value="%s" %node[2],
                          command=sel)
        R3.pack( anchor = W)
        R3.place(bordermode=INSIDE,x=730, y=280)
        R3.configure(bg= "#d9ead3")

        R4 = Radiobutton(top, text="%s" %node[3],height=2, width=20, variable=var, value="%s" %node[3],
                          command=sel)
        R4.pack( anchor = W)
        R4.place(bordermode=INSIDE,x=730, y=320)
        R4.configure(bg= "#ffe599")
        R5 = Radiobutton(top, text="%s" %node[4],height=2, width=20, variable=var, value="%s" %node[4],
                          command=sel)
        R5.pack( anchor = W)
        R5.place(bordermode=INSIDE,x=730, y=360)
        R5.configure(bg= "#f9cb9c")


def chooseDomain():
       print "hello"
       global root
       root = Tkinter.Toplevel()
       root.title("Choose Domain")
       panel = Label(root, image = trend_img)
       panel.pack()
       b2 = Button(root,text ="News", command = lambda: helloCallBack("news"),font=tkFont.Font(family="Times New Roman",size=12,weight="bold"))
       b2.pack()
       b2.place(bordermode=INSIDE, x=710, y=200)
       b3 = Button(root,text ="Sports",  command = lambda: helloCallBack("sports"),font=tkFont.Font(family="Times New Roman",size=12,weight="bold"))
       b3.pack()
       b3.place(bordermode=INSIDE, x=710, y=250)
       b4 = Button(root,text ="Entertainment", command = lambda: helloCallBack("entertainment"),font=tkFont.Font(family="Times New Roman",size=12,weight="bold"))
       b4.pack()
       b4.place(bordermode=INSIDE, x=710, y=300)
       """b5 = Button(root,text ="Technology",  command = lambda: helloCallBack("technology"),font=tkFont.Font(family="Times New Roman",size=12,weight="bold"))
       b5.pack()
       b5.place(bordermode=INSIDE, x=710, y=350)"""
       root.mainloop()


def main():
    print "Main"
    
    global btn
    global top
    top = Tkinter.Toplevel()
    w = top.winfo_screenwidth()
    h = top.winfo_screenheight()
    top.geometry("%dx%d+0+0"%(w,h))
    #gui_img = ImageTk.PhotoImage(Image.open("UI1.jpg"))
    #gui_img=Image.open("gui_image.jpg")
    #gui_img=gui_img.resize((1000,w),Image.ANTIALIAS)
    global trend_img
    trend_img = ImageTk.PhotoImage(Image.open("images\\UI1.jpg"))
    #trend_img.resize(w,h)
    head_img = ImageTk.PhotoImage(Image.open("images\\UI1.jpg"))
    top.title("Trends")
    frame = Frame(top,height=0,width=556)
    frame.pack()
    space = Label(frame)
    heading = Label(top,font=tkFont.Font(family="Times New Roman",size=55,weight="bold"),text="Trend getter")
    heading.pack()
    panel = Label(top, image = head_img)
    panel.pack()
    btn = ImageTk.PhotoImage(Image.open("images\\button.png"))
    b1 = Button(top,text ="Get trends", image=btn, command = chooseDomain,font=tkFont.Font(family="Times New Roman",size=12,weight="bold"))
    b1.pack()
    b1.place(bordermode=INSIDE, x=710, y=560)
    #space = Label(frame)
    #space.pack()
    top.mainloop()
    
def trendy_main():
       main()
#trendy_main()
#button = Tk.Button(master=frame, text='press', command=action(someNumber))
#button = Tk.Button(master=frame, text='press', command= lambda: action(someNumber))
