from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import nltk
import Tkinter
from Tkinter import *
from PIL import ImageTk, Image
import os
import tkMessageBox
import tkFont
from tkFileDialog import askopenfilename



def get_cloud():
    txt = text1.get(1.0,END)
    wordcloud = WordCloud(   stopwords=STOPWORDS,
                              background_color='pink',
                              width=1200,
                              height=1000
                             ).generate(txt)


    plt.imshow(wordcloud)
    plt.axis('off')
    plt.show()


def cloud_(txt,n):
    root = Tkinter.Toplevel()
    root.configure(background="black")
    #imag = ImageTk.PhotoImage(Image.open("sum.jpg"))
    #panel = Label(root, image = imag)
    #print "niki"
    w = root.winfo_screenwidth()
    h = root.winfo_screenheight()
    root.geometry("%dx%d+0+0"%(w,h))
    root.title("Get Cloud")
    heading = Label(root,font=tkFont.Font(family="AltamonteNF",size=35,weight="bold"),fg='yellow',text="Word Cloud")
    heading.configure(background="black")
    heading.pack()
    global text1
    text1 = Text(root,height =13,width=120)
    if n==1:
        text1.insert(INSERT,txt)
    text1.pack()
    text1.place(bordermode=OUTSIDE,x=100,y=180)
    R1 = Radiobutton(root, text="Get Cloud" ,height=2, width=20, variable=var,font=tkFont.Font(family="AltamonteNF",size=20,weight="bold"), command=get_cloud)        
    R1.pack( anchor = W )
    R1.place(bordermode=INSIDE,x=480, y=400)
    R1.configure(bg= "#abddee")
    #print "saumya:"
    panel.pack()
    root.mainloop()

    
def sel1():
    path= askopenfilename()
    file = open(path,"r")
    txt=file.read()
    cloud_(txt,1)
    
def sel2():
    cloud_('',0)

def close_window():
    print "sam"
    
def cloud_main():
    """
    main gui
    """
    global top
    global panel
    top = Tkinter.Toplevel()
    img1 = ImageTk.PhotoImage(Image.open("images\\textool.jpg"))
    top.title("word cloud")
    top.configure(background='black')
    
    panel = Label(top, image = img1)
    panel.pack()
    w = top.winfo_screenwidth()
    h = top.winfo_screenheight()
    top.geometry("%dx%d+0+0"%(w,h))
    top.title("Get Word Cloud")
    frame = Frame(top,height=0,width=556)
    frame.pack()
    space = Label(frame)
    heading = Label(top,font=tkFont.Font(family="AltamonteNF",size=35,weight="bold"),fg='yellow',text="Word Cloud")
    heading.configure(background='black')
    heading.pack()
    global var
    var = StringVar()
    R1 = Radiobutton(top, text="Text from file" ,height=2, width=20, variable=var,font=tkFont.Font(family="AltamonteNF",size=20,weight="bold"), command=sel1)        
    R1.pack( anchor = W )
    R1.place(bordermode=INSIDE,x=400, y=200)
    R1.configure(bg= "#abddee")
    
    R2 = Radiobutton(top, text="Input ",height=2, width=20,font=tkFont.Font(family="AltamonteNF",size=35,weight="bold"), variable=var, command=sel2)
    R2.pack( anchor = W )
    R2.place(bordermode=INSIDE,x=400, y=400)
    R2.configure(bg= "#ead1dc")

    button = Button (frame, text = "Good-bye.", command = close_window)
    button.pack()
    R1.configure(bg= "#abddee")
    top.mainloop()


def cloud_gui():
    cloud_main()

#cloud_main()
