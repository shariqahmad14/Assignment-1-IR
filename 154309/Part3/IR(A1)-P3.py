# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 17:48:19 2019

@author: Admin
"""

from nltk.stem import PorterStemmer
import linecache

file=open("termids.txt","r")

termid=dict()

for line in file:
    fields=line.split("\t")
    fields[1]=fields[1].rstrip()
    termid[fields[1]]=fields[0]
    
file.close()

val = str(input("--term "))
ps=PorterStemmer()

while val!='':
    val=ps.stem(val)
    if val in termid.keys():
        desired_line_number = int(termid[val])
        f=linecache.getline("term_index.txt",desired_line_number+1)
        f=f.split(" ")
        print("Listing for term:",val)
        print("TERMID:",f[0])
        print("Number of documents containing term:",f[1])
        print("Term frequency in corpus:",f[2])
    else:
        print("Not Found")
    val = input("--term ")
f=linecache.clearcache()
#fp.close()