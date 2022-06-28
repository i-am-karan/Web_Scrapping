from audioop import ulaw2lin
import time
from traceback import print_tb
from turtle import ht
from selenium import webdriver
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())

all_ques=[]  #This stores titles and urls of all the problems
all_dif=[]   #This stores difficulty level of all the problems
all_accep_rate=[] #This stores the accepatance rate of all the problems
urls=[]    #This stores the url of alll the problems
title=[]   #This stores the title of all the problems

driver.get("https://leetcode.com/tag/array/")
time.sleep(20)
html=driver.page_source
soup=BeautifulSoup(html,'html.parser')
all_ques_row1=soup.findAll("div",{"class":"title-cell__ZGos"})
all_que_dif1=soup.findAll("span",{"class":"label"})
all_que_acc1=soup.findAll("td",{"label":"Acceptance"})
for i in range(0,len(all_ques_row1)):
    if(all_ques_row1[i].find("i")==None):
     all_ques.append(all_ques_row1[i].find("a"))
     all_dif.append(all_que_dif1[i].text)
     all_accep_rate.append(all_que_acc1[i].text)

driver.get("https://leetcode.com/tag/string/")
time.sleep(15)
html=driver.page_source
soup=BeautifulSoup(html,'html.parser')
all_ques_row2=soup.findAll("div",{"class":"title-cell__ZGos"})
all_que_dif2=soup.findAll("span",{"class":"label"})
all_que_acc2=soup.findAll("td",{"label":"Acceptance"})
for i in range(0,len(all_ques_row2)):
    if(all_ques_row2[i].find("i")==None):
     all_ques.append(all_ques_row2[i].find("a"))
     all_dif.append(all_que_dif2[i].text)
     all_accep_rate.append(all_que_acc2[i].text)


driver.get("https://leetcode.com/tag/hash-table/")
time.sleep(15)
html=driver.page_source
soup=BeautifulSoup(html,'html.parser')
all_ques_row3=soup.findAll("div",{"class":"title-cell__ZGos"})
all_que_dif3=soup.findAll("span",{"class":"label"})
all_que_acc3=soup.findAll("td",{"label":"Acceptance"})
for i in range(0,len(all_ques_row3)):
    if(all_ques_row3[i].find("i")==None):
     all_ques.append(all_ques_row3[i].find("a"))
     all_dif.append(all_que_dif3[i].text)
     all_accep_rate.append(all_que_acc3[i].text)

driver.get("https://leetcode.com/tag/dynamic-programming/")
time.sleep(15)
html=driver.page_source
soup=BeautifulSoup(html,'html.parser')
all_ques_row4=soup.findAll("div",{"class":"title-cell__ZGos"})
all_que_dif4=soup.findAll("span",{"class":"label"})
all_que_acc4=soup.findAll("td",{"label":"Acceptance"})
for i in range(0,len(all_ques_row4)):
    if(all_ques_row4[i].find("i")==None):
     all_ques.append(all_ques_row4[i].find("a"))
     all_dif.append(all_que_dif4[i].text)
     all_accep_rate.append(all_que_acc4[i].text)


driver.get("https://leetcode.com/tag/math/")
time.sleep(15)
html=driver.page_source
soup=BeautifulSoup(html,'html.parser')
all_ques_row5=soup.findAll("div",{"class":"title-cell__ZGos"})
all_que_dif5=soup.findAll("span",{"class":"label"})
all_que_acc5=soup.findAll("td",{"label":"Acceptance"})
for i in range(0,len(all_ques_row5)):
    if(all_ques_row5[i].find("i")==None):
     all_ques.append(all_ques_row5[i].find("a"))
     all_dif.append(all_que_dif5[i].text)
     all_accep_rate.append(all_que_acc5[i].text)




driver.get("https://leetcode.com/tag/depth-first-search/")
time.sleep(15)
html=driver.page_source
soup=BeautifulSoup(html,'html.parser')
all_ques_row6=soup.findAll("div",{"class":"title-cell__ZGos"})
all_que_dif6=soup.findAll("span",{"class":"label"})
all_que_acc6=soup.findAll("td",{"label":"Acceptance"})
for i in range(0,len(all_ques_row6)):
    if(all_ques_row6[i].find("i")==None):
     all_ques.append(all_ques_row6[i].find("a"))
     all_dif.append(all_que_dif6[i].text)
     all_accep_rate.append(all_que_acc6[i].text)



driver.get("https://leetcode.com/tag/greedy/")
time.sleep(15)
html=driver.page_source
soup=BeautifulSoup(html,'html.parser')
all_ques_row7=soup.findAll("div",{"class":"title-cell__ZGos"})
all_que_dif7=soup.findAll("span",{"class":"label"})
all_que_acc7=soup.findAll("td",{"label":"Acceptance"})
for i in range(0,len(all_ques_row7)):
    if(all_ques_row7[i].find("i")==None):
     all_ques.append(all_ques_row7[i].find("a"))
     all_dif.append(all_que_dif7[i].text)
     all_accep_rate.append(all_que_acc7[i].text)



driver.get("https://leetcode.com/tag/two-pointers/")
time.sleep(15)
html=driver.page_source
soup=BeautifulSoup(html,'html.parser')
all_ques_row8=soup.findAll("div",{"class":"title-cell__ZGos"})
all_que_dif8=soup.findAll("span",{"class":"label"})
all_que_acc8=soup.findAll("td",{"label":"Acceptance"})
for i in range(0,len(all_ques_row8)):
    if(all_ques_row8[i].find("i")==None):
     all_ques.append(all_ques_row8[i].find("a"))
     all_dif.append(all_que_dif8[i].text)
     all_accep_rate.append(all_que_acc8[i].text)



driver.get("https://leetcode.com/tag/bit-manipulation/")
time.sleep(15)
html=driver.page_source
soup=BeautifulSoup(html,'html.parser')
all_ques_row9=soup.findAll("div",{"class":"title-cell__ZGos"})
all_que_dif9=soup.findAll("span",{"class":"label"})
all_que_acc9=soup.findAll("td",{"label":"Acceptance"})
for i in range(0,len(all_ques_row9)):
    if(all_ques_row9[i].find("i")==None):
     all_ques.append(all_ques_row9[i].find("a"))
     all_dif.append(all_que_dif9[i].text)
     all_accep_rate.append(all_que_acc9[i].text)


driver.get("https://leetcode.com/tag/tree/")
time.sleep(15)
html=driver.page_source
soup=BeautifulSoup(html,'html.parser')
all_ques_row10=soup.findAll("div",{"class":"title-cell__ZGos"})
all_que_dif10=soup.findAll("span",{"class":"label"})
all_que_acc10=soup.findAll("td",{"label":"Acceptance"})
for i in range(0,len(all_ques_row10)):
    if(all_ques_row10[i].find("i")==None):
     all_ques.append(all_ques_row10[i].find("a"))
     all_dif.append(all_que_dif10[i].text)
     all_accep_rate.append(all_que_acc10[i].text)

driver.get("https://leetcode.com/tag/sorting/")
time.sleep(15)
html=driver.page_source
soup=BeautifulSoup(html,'html.parser')
all_ques_row11=soup.findAll("div",{"class":"title-cell__ZGos"})
all_que_dif11=soup.findAll("span",{"class":"label"})
all_que_acc11=soup.findAll("td",{"label":"Acceptance"})
for i in range(0,len(all_ques_row11)):
    if(all_ques_row11[i].find("i")==None):
     all_ques.append(all_ques_row11[i].find("a"))
     all_dif.append(all_que_dif11[i].text)
     all_accep_rate.append(all_que_acc11[i].text)


for ques in all_ques:
    urls.append("https://leetcode.com"+ques['href'])
    title.append(ques.text)


with open("problem_url.txt","w+") as f:
    f.write("\n".join(urls))
with open("problem_title.txt","w+") as f:
    f.write("\n".join(title))
with open("problem_difficulty.txt","w+") as f:
    f.write("\n".join(all_dif))
with open("problem_acceptance_rate.txt","w+") as f:
    f.write("\n".join(all_accep_rate))
