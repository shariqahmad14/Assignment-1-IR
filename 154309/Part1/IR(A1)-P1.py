# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 00:34:08 2019

@author: Admin
"""




from bs4 import BeautifulSoup
from nltk.stem import PorterStemmer
import os
import re
import ntpath

fl=open("docids.txt","w")
fk=open("termids.txt","w")
path = 'S:\\9th Semmester\\Info Ret\\corpus'

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        files.append(os.path.join(r, file))

termlist=dict()
doclist=list()
st='\n'
docidc=0
termidc=0
term_index=dict()

for fi in files:
    if fi in st or st in fi:
        print("File Already Read")
    else: 
        st=fi
        check=ntpath.basename(fi)
        fl.write(str(docidc)+"\t"+check+'\n')
        try:
            file=open(fi,"r", encoding="utf8")
            data = file.read()
        except ValueError:
            try:
                file=open(fi,"rb")
                data = file.read()
                data=data.decode("utf-8")
            except ValueError:
                pass
        file.close()
        data=str(data)
        try:
            data = data[data.index('<!DOCTYPE'):]#
        except ValueError:
            try:
                data = data[data.index('<html'):]
            except ValueError:
                try:
                    data = data[data.index('<HTML'):]
                except ValueError:
                    data = data[data.index('<'):]
        s=BeautifulSoup(data,'lxml').text
        while(s!=BeautifulSoup(s,'lxml').text):
            s=BeautifulSoup(s,'lxml').text
        s=re.split(r'[^\w]',s)
        thing=['[^\w]']
        for g in thing:
              while g in s: s.remove(g) 
        s = list(filter(None, s))
        s=[x.lower() for x in s]
        file1=open('stoplist.txt','r')
        stop=file1.read()
        file1.close()
        stop=stop.split()
        s=[word for word in s if word not in stop]
#        g=0
#        for g in range(len(s)):
#            if len(s[g])==1:
#                s.remove(s[g])
#                g-=1
        ps=PorterStemmer()
        h=ps.stem(s[0])
        s = [ps.stem(word) for word in s]
        for i in range (len(s)):
            c=i
            if s[i] not in termlist:
                    try:
                        s[i].encode(encoding='utf-8').decode('ascii')
                        fk.write(str(termidc)+"\t"+s[i]+"\n")
                        termlist[s[i]]=termidc
                        print(termidc)
                        termidc+=1
                    except UnicodeDecodeError:
                        print('')                    
        docidc+=1
fl.close()
fk.close()
