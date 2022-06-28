from ast import keyword
import math
from cmath import log10
import pandas as pd
import string
import nltk
import re
import os
stopwords=nltk.corpus.stopwords.words('english')
wn=nltk.WordNetLemmatizer()

final_data=[]
freq={}
exclude=set(string.punctuation)
for i in range(1,3374):
    os.remove(f'p{i}keyword.txt')

final_data.sort()
final_data=list(dict.fromkeys(final_data))
final_data.remove('')
idfarr=[]

for d in final_data:
    idfarr.append(abs(1+log10(3373/freq[d])))

with open("keyword.txt","w+") as f:
     f.write("\n".join(final_data))

f=open("IDF.txt","w")

for d in idfarr:
    f.write(f"{d}\n")
f.close()
f1=open("TFIDF.txt","w")
mag={}
for i in range(0,len(final_data)):
    for j in range(1,3374):
       with open("p"+str(j)+"keyword.txt",'r') as f:
           keyword=f.read().splitlines()
       count=0
       for key in keyword:
           if(key==final_data[i]):
               count+=1
       if(count!=0):
           val=abs(idfarr[i]*(count/(len(keyword))))
           if(j in mag):
               mag[j]+=(val*val)
           else:
               mag[j]=val*val
           f1.write(f"{i+1}\n{j}\n{val}\n")
f1.close()
print(mag[1])
print(len(mag))
print(len(final_data))
f2=open("Magnitude.txt","w")
for i in range(1,3374):
    f2.write(f"{math.sqrt(mag[i])}\n")
f2.close()


# Below code is for verification
# mg=0
# with open("p"+str(1)+"keyword.txt",'r') as f:
#       keyword=f.read().splitlines()

# for key in keyword:
#     val=abs(1+log10(3373/freq[key]))
#     val/=12
#     if(key=="integer" or key=="target"):
#         mg+=(2*val*val)
#     else:
#         mg+=(val*val)

# print(mg)