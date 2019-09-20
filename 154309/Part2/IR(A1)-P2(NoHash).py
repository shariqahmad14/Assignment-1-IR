# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 13:28:00 2019

@author: Admin
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 14:58:47 2019

@author: Admin
"""


#fl=open("docids.txt","w")
#fl.close()



from bs4 import BeautifulSoup
from nltk.stem import PorterStemmer
import os
import re
from itertools import chain

path = 'S:\\9th Semmester\\Info Ret\\corpus'

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        files.append(os.path.join(r, file))

term_index=list()
doclist=list()
st='\n'
docidc=0
termidc=0
term_index=dict()
gdocid=0
docid=0

for fi in files:
    if fi in st or st in fi:
        print("File Already Read")
    else: 
        st=fi
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
        s = [ps.stem(word) for word in s]
        if docidc==131:
            print('')
        for i in range (len(s)):
            if s[i] not in chain(*term_index):
				try:
					s[i].encode(encoding='utf-8').decode('ascii')
					doc_index=list()
					docid=docidc-gdocid
					doc_info=[docid,i]
					doc_index.append([doc_info])
					term_index.append([termidc,1,1,doc_index])
					print(termidc,docidc)
					termidc+=1
				except UnicodeDecodeError:
                    print()
            else:
                print(termidc,docidc)
                docid=docidc-gdocid
                doc_info=[docid,i]
                for pair in term_index:
                    if pair[0]==termidc:
                        if docidc not in pair[3]:
                            pair[2]+=1
                            pair[3].append(doc_info)
                        else:
                            pair[3].append(doc_info)
                pair[1]=term_index[s[i]][1]+1
                
            
            if gdocid<docidc:
                gdocid=docidc
        
        docidc+=1

#fk.write(str(123456)+" "+str(1237896)+"\n")
#fk.write(str(123456)+" "+str(1237896)+"\n")
fk=open("term_index.txt","w")
for key in term_index:
    fk.write(str(term_index[key][0])+" "+str(term_index[key][1])+" "+str(term_index[key][2]))
    for kei in term_index[key][3]:
        for pair in term_index[key][3][kei]:
            fk.write(" "+str(pair[0])+","+str(pair[1]))
    fk.write("\n")
fk.close()