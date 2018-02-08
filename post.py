import nltk
from nltk.corpus import wordnet
from nltk.corpus import stopwords
from collections import defaultdict
from nltk.tokenize import sent_tokenize,word_tokenize
from heapq import nlargest
from string import punctuation
import plotly.plotly as py
from plotly.graph_objs import Scatter
import plotly.plotly as py
import plotly.graph_objs as go
import jpype

def __main__(domain):
    return __get_trends__(domain)
    



def __get_trends__(domain):
    '''__get_post__'''
    freq = defaultdict(int)
    if domain == "news":
        f=open("file\\fn.txt",'r')
    elif domain == "sports":
        f=open("file\\fs.txt",'r')
    elif domain == "entertainment":
        f=open("file\\fe.txt",'r')
    else:
        f=open("file\\ft.txt",'r')
    post=f.read()
    print post
    text1=unicode(post,'utf-8')
    print "text"
    print text1
    #sent2=str(post).splitlines()[0]
    #print sent2
    #sents = sent_tokenize(post)
    sents = sent_tokenize(text1)
    #word_sent = [word_tokenize(s.lower()) for s in sents]
    word_sent = [s.lower().split(' ') for s in sents]
    #print 'word:'
    #print word_sent
    #def _compute_frequencies(word_sent):
    _min_cut =0.1
    #_max_cut =0.9
    _max_cut =0.9
    stop = set(stopwords.words('english') + list(punctuation))
    freq = defaultdict(int)
    for s in word_sent:
        for word in s:
           if word not in stop:
               #print "word = %s" %word
               freq[word] += 1
    m = float(max(freq.values()))
    for w in freq.keys():
        freq[w] = freq[w]/m
        if freq[w] >= _max_cut or freq[w] <= _min_cut:
            del freq[w]
    #print 'freq: '
    #print freq
    node=nlargest(5, freq, key=freq.get)
    #print 'node '
    #print node
    trace0 = go.Scatter(
    x=[node[0],node[1],node[2],node[3],node[4]],
    y=[5,4,3,2,1],
    mode='line')
    data = [trace0]
    #plot_url = py.plot(data, filename='line-scatter')
    # return [word_sent[j] for j in node]"""
    #trace0 = Scatter(x=[1, 2, 3, 4, 5],
    #           y=node)
    return node


def __get_post__():
    
    jpype.startJVM("C:/Program Files/Java/jre7/bin/server/jvm.dll", "-ea")
    javaPackage = jpype.JPackage("use_facebook4j") 
    javaClass = javaPackage.Main
    javaObject = javaClass() 
    javaObject.main() 
    jpype.shutdownJVM()
