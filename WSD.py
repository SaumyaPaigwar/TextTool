from nltk.tokenize import sent_tokenize,word_tokenize
from nltk.corpus import stopwords
from collections import defaultdict
from string import punctuation
from heapq import nlargest
from nltk.wsd import lesk

import nltk
import Tkinter
from Tkinter import *
from PIL import ImageTk, Image
import os
import tkMessageBox
import tkFont

def clear():
    text1.delete(1.0, END)
    text2.delete(1.0, END)
    
def main():
    text2.delete(1.0, END)
    stopword = set(stopwords.words('english') + list(punctuation))
    sent=text1.get(1.0,END)
    word_sent = word_tokenize(sent)
    words=[]
    w=[]
    txt=""
    for word in word_sent:
        if word not in stopword:
            words.append(word)
    for word in words:
            w.append(word)
    for word in w:
        print word
        txt = txt + str(word)
        if not str.istitle(str(word)):
            txt = txt + " " + str(lesk(sent,word)) + " " + str(lesk(sent,word).definition()) + "\n"
            print lesk(sent,word)
            print lesk(sent,word).definition()
        else:
            txt = txt + "\n"
    text2.insert(INSERT, txt)


def wsd_gui_():
    global root
    global text1
    global text2
    root = Tkinter.Toplevel()
    root.configure(background='black')
    img = ImageTk.PhotoImage(Image.open("images\\textool.jpg"))
    w = root.winfo_screenwidth()
    h = root.winfo_screenheight()
    root.geometry("%dx%d+0+0"%(w,h))
    root.title("Ambiguity Resolver")
    frame = Frame(root,height=0,width=556)
    frame.pack()
    space = Label(frame)
    heading = Label(root,font=tkFont.Font(family="Times New Roman",size=55,weight="bold"),fg='yellow',text="Resolve Ambiguity")
    heading.configure(background='black')
    heading.pack()
    panel = Label(root,image = img)
    panel.pack()
    L1 = Label(root,bg="black",fg="white" ,font=tkFont.Font(family="Times New Roman",size=12,weight="bold"),text=" Enter sentence to be disambiguated:")
    L1.pack()
    L1.place(bordermode=INSIDE,x=50, y=100)
    text1 = Text(root,height =5,width=160)
    text1.pack()
    text1.place(bordermode=OUTSIDE,x=100,y=180)
    L2 = Label(root,bg="black",fg="white" ,font=tkFont.Font(family="Times New Roman",size=12,weight="bold"),text="Ambigous words and their meanings")
    L2.pack()
    L2.place(bordermode=INSIDE,x=50, y=450)
    text2 = Text(root,height =5,width=160)
    text2.pack()
    text2.place(bordermode=OUTSIDE,x=100,y=500)
    b1 = Button(root,text="resolve", command = main,height=2, width=20)
    b1.configure(bg= "#abddee")
    b1.pack()
    b1.place(bordermode=INSIDE,x=490, y=610)
    b2 = Button(root,text="Clear", command = clear,height=2, width=20)
    b2.configure(bg= "#abddee")
    b2.pack()
    b2.place(bordermode=INSIDE,x=650, y=610)
    root.mainloop()

#wsd_gui_()
