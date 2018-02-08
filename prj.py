import nltk
from nltk.corpus import wordnet
from nltk.corpus import stopwords
from collections import defaultdict
from nltk.tokenize import sent_tokenize,word_tokenize
from heapq import nlargest
from string import punctuation
import nltk
from nltk.corpus import brown
import nltk.tag
_POS_TAGGER = 'taggers/maxent_treebank_pos_tagger/english.pickle'
from nltk.tag import pos_tag # doctest: +SKIP
from nltk.stem.wordnet import WordNetLemmatizer

lmtzr = WordNetLemmatizer()
tg1=[]
node1=[]
def frequency():
 postag()   
 freq = defaultdict(int)
 f=open("e:output.txt",'r')
 post=f.read()
 text1=unicode(post,'utf-8')
 #print "text"
 #print text1
 sents = sent_tokenize(text1)
 word_sent = [s.lower().split(' ') for s in sents]
 _min_cut =0.1
 _max_cut =0.9
 stop = set(stopwords.words('english') + list(punctuation))
 freq = defaultdict(int)
 
 '''for s in word_sent:
   for word in s:
        if word not in stop:
            freq[word] += 1'''
 for s in word_sent:
   for word in s:
        tg1.append(lmtzr.lemmatize(word))  
 for wr in tg1:
    if wr not in stop:
        freq[wr] += 1
        
 m = float(max(freq.values()))
 #print m
 for w in freq.keys():
    freq[w] = freq[w]/m
    if freq[w] >= _max_cut or freq[w] <= _min_cut:
        del freq[w]     
 #print 'freq: '
 #print freq   
 node=nlargest(5, freq, key=freq.get)
 #print node 
 #print s
 return node

def postag():
  f=open("e:op1.txt",'r')
  post=f.read()
  text1=unicode(post,'utf-8')
  #essays = u"""information security is included in eight semester"""
  tokens = nltk.word_tokenize(text1)
  tagged = nltk.pos_tag(tokens)
  nouns = [word for word,pos in tagged \
	 if (pos == 'NNP'  or pos== 'NNPS' )]
  downcased = [x.lower() for x in nouns]
  joined = " ".join(downcased).encode('utf-8')
  into_string = str(nouns)

  output = open("e:output.txt", "w")
  output.write(joined)
  output.close()
  #print 'done'
   
#postag()
#node1 = frequency()
#print node1
