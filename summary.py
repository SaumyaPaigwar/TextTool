
import nltk
import Tkinter
from Tkinter import *
from PIL import ImageTk, Image
import os
import tkMessageBox
import tkFont
from tkFileDialog import askopenfilename
from nltk.tokenize import sent_tokenize,word_tokenize
from nltk.corpus import stopwords
from collections import defaultdict
from string import punctuation
from heapq import nlargest


text =""
res=""
num_of_line = ""
length = ""
ratio  =""

class FrequencySummarizer:

    def __init__(self, min_cut=0.1, max_cut=0.9):
        """
         Initilize the text summarizer.
         Words that have a frequency term lower than min_cut 
         or higer than max_cut will be ignored.
        """
        self._min_cut = min_cut
        self._max_cut = max_cut 
        self._stopwords = set(stopwords.words('english') + list(punctuation))

    def _compute_frequencies(self, word_sent):
        """ 
            Compute the frequency of each of word.
            Input: 
             word_sent, a list of sentences already tokenized.
            Output: 
             freq, a dictionary where freq[w] is the frequency of w.
        """
        freq = defaultdict(int)
        for s in word_sent:
            for word in s:
                if word not in self._stopwords:
                    freq[word] += 1
        # frequencies normalization and filtering
        #print freq.keys()
        m = float(max(freq.values()))
        for w in freq.keys():
            #print w,freq[w]
            freq[w] = freq[w]/m
            if freq[w] >= self._max_cut or freq[w] <= self._min_cut:
                del freq[w]
        return freq

    def summarize(self, text, n):
        """
            Return a list of n sentences 
            which represent the summary of text.
        """
        sents = sent_tokenize(text)
        #print sents

        if n >= len(sents):
          tkMessageBox.showinfo("WARNING","Number of lines is greater")
        assert n <= len(sents)
         
        word_sent = [word_tokenize(s.lower()) for s in sents]
        #print word_sent
        self._freq = self._compute_frequencies(word_sent)
        #print self._freq
        ranking = defaultdict(int)
        for i,sent in enumerate(word_sent):
            #print i,sent
            for w in sent:
                if w in self._freq:
                    #print w
                    ranking[i] += self._freq[w]
                    #print ranking[i]
        sents_idx = self._rank(ranking, n)
        #print sents_idx
        return [sents[j] for j in sents_idx]

    def _rank(self, ranking, n):
        #print ranking, n
        """ return the first n sentences with highest ranking """
        return nlargest(n, ranking, key=ranking.get)





def clear():
    text2.delete(1.0, END)
    text1.delete(1.0, END)
    E1.delete(0, 'end')
    E2.delete(0, 'end')
    E3.delete(0, 'end')

def summary():
    fs = FrequencySummarizer()
    global num_of_line
    n = E1.get()
    num_of_line=int(n)
    global text
    text = text1.get(1.0,END)
    x = sent_tokenize(text)
    print(text)
   
    if not text :
        tkMessageBox.showinfo("WARNING","No input given")

    length = len(x)
    E2.insert(INSERT,length)

    
    global res
    res = fs.summarize(text,num_of_line)
    res1=''
    for n in res:
        print n
        res1=res1+n+" "
    text2.insert(INSERT,res1)
    ratio = (100.0 * len(res))/length
    E3.insert(INSERT,ratio)
    

def summary_gui(txt,n):
    """
    summarizer gui
    """
    img = ImageTk.PhotoImage(Image.open("images\\textool.jpg"))
    panel = Label(root, image = img)
    
    L1 = Label(panel,bg="black",font=tkFont.Font(family="Times New Roman",size=12,weight="bold"),text=" Summarized statements required :",fg="yellow")
    L1.configure(background="black")
    L1.pack()
    L1.place(bordermode=INSIDE,x=30, y=80)
    global E1
    E1 = Entry(panel, bd =5)
    E1.pack()
    E1.place(bordermode=INSIDE,x=280, y=80)
    l4 = Label(panel,bg="black",font=tkFont.Font(family="Times New Roman",size=12,weight="bold"),text="Article statements entered: ",fg="yellow")
    l4.configure(background="black")
    l4.pack()
    l4.place(bordermode=OUTSIDE,x=500, y=80)
    global E2
    E2 = Entry(panel,bd=5)
    E2.pack()
    E2.place(bordermode=OUTSIDE,x=700, y=80)
    l5 = Label(panel,bg="black" ,font=tkFont.Font(family="Times New Roman",size=12,weight="bold"),text="Summary Ratio(%) : ",fg="yellow")
    l5.configure(background="black")
    l5.pack()
    l5.place(bordermode=OUTSIDE,x=900, y=80)
    global E3
    E3= Entry(panel,bd=5)
    E3.pack()
    E3.place(bordermode=OUTSIDE,x=1060, y=80)

    L2 = Label(panel,bg="black",font=tkFont.Font(family="Times New Roman",size=12,weight="bold"), text="---------Enter your text here :--------",fg="yellow")
    L2.configure(background="black")
    L2.pack()
    L2.place(bordermode=INSIDE,x=550,y=150)
    global text1
    text1 = Text(panel,height =13,width=120)
    if n==1:
        text1.insert(INSERT,txt)
    text1.pack()
    text1.place(bordermode=OUTSIDE,x=100,y=180)
    L3 = Label(panel,bg="black" ,font=tkFont.Font(family="Times New Roman",size=12,weight="bold"), text="--------Output : Top Ranked Sentences :--------",fg="yellow")
    L3.configure(background="black")
    L3.pack()
    L3.place(bordermode=INSIDE,x=550,y=415)
    global text2
    text2 = Text(panel,height =10,width=120)
    text2.pack()
    text2.place(bordermode=INSIDE,x=100,y=440)
      
    b1 = Button(panel,text="Rank", command = summary,height=2, width=20)
    b1.configure(bg= "#abddee")
    b1.pack()
    b1.place(bordermode=INSIDE,x=1100, y=200)
    
    
    b2 = Button(panel,text="clear", command = clear,height=2, width=20)
    b2.pack()
    b2.configure(bg= "#abddee")
    b2.place(bordermode=INSIDE,x=1100, y=300)
    panel.pack()
    root.mainloop()



def sel1():
    path= askopenfilename()
    file = open(path,"r")
    txt=file.read()
    print txt
    summary_gui(txt,1)
    
def sel2():
    summary_gui('',2)

def close_window (root): 
    root.destroy()
    
def main():
    """
    main gui
    """
    global root
    print "samk"
    root = Tkinter.Toplevel()
    root.configure(background="black")
    imag = ImageTk.PhotoImage(Image.open("images\\sum.jpg"))
    panel = Label(root, image = imag)
    w = root.winfo_screenwidth()
    h = root.winfo_screenheight()
    root.geometry("%dx%d+0+0"%(w,h))
    root.title("Get Summary")
    frame = Frame(root,height=0,width=556)
    frame.pack()
    space = Label(frame)
    heading = Label(root,font=tkFont.Font(family="AltamonteNF",size=55,weight="bold"),fg="yellow",text="Get Summary")
    heading.configure(background="black")
    heading.pack()
    global var
    var = StringVar()
    R1 = Button(root, font=tkFont.Font(family="Times New Roman",size=20,weight="bold"),text="From file",height=2, width=20, command=sel1)
    R1.pack( anchor = W )
    R1.place(bordermode=INSIDE,x=480, y=200)
    R1.configure(bg= "#abddee")
    
    R2 = Button(root, font=tkFont.Font(family="Times New Roman",size=20,weight="bold"),text="Direct Summary",height=2, width=20, command=sel2)
    R2.pack( anchor = W )
    R2.place(bordermode=INSIDE,x=480, y=400)
    R2.configure(bg= "#ead1dc")

    root.mainloop()


def __main__():
    main()

#__main__();

