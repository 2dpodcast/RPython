import urllib.request
import urllib.parse
import os
import re
import webbrowser
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys 
def Ngram(word,compare,n):
    baseurl='https://books.google.com/ngrams/graph?'
    url = baseurl + urllib.parse.urlencode({'content':word})+'%2'+compare+'&year_start=1900&year_end=2000'
    time.sleep(1)
    if n==1:
        script.get(url)
    else:
        script2.get(url)
    soup=BeautifulSoup(script.page_source,'html.parser')
    #print(soup.prettify())
    tag=soup.find("path",{"class":"line visible clickable main"})
    if tag is not None:
        return tag.get('d')
    else:
        return "NA"
def data(ngram):
    ls=re.findall(',([0-9]+)\\.',ngram)
    if len(ls)!=0:
        weight=sum(map(int,ls))/len(ls)
    else:
        weight=0
    return weight
f='C:\AMD\words.txt'
//Input with whom frequency will get judged
compare=input('')
file=open(f)
x=file.read()
file.close()
ls=re.findall('([a-z]+)\\n',x)
outdir=''
space="                "
count=0
total=0
curzero=0
script= webdriver.Chrome(r'C:\\chromedriver')
script2=webdriver.Chrome(r'C:\\chromedriver')
n=1
switch=0
out='C:\AMD\wordsmeaning.txt'
i=sum(1 for line in open('C:\AMD\wordsmeaning.txt')) -1
while i<len(ls):
    count=(count+1)%100
    if count==40:
        out='C:\AMD\wordsmeaning.txt'
        file=open(out,'a')
        file.write(outdir)
        file.close()
        
    if count==0:
        time.sleep(1)
        print('Total till now'+str(total))
    if switch==0:
        y=Ngram(ls[i],compare,1)
    else:
        y=Ngram(ls[i],compare,0)
    #print(y)
    x=str(data(y))
    if(x=='0'):
        time.sleep(3)
        switch=abs(1-switch)
        curzero=(curzero+1)%5
    else:
        total+=1
        outdir+=ls[i] + '  :  '+x
        outdir+="\n"
        print(space[len(str(total)):7]+str(total)+space[len(ls[i]):]+ls[i]+"   "+x)
    if curzero==4:
        i-=4
        curzero=0
    i=i+1
script.close()



