# # Storing url of questions by extracting the it from the file and the iteraring through all the urls 
# from audioop import ulaw2lin
# import time
# from traceback import print_tb
# from turtle import ht
# from selenium import webdriver
# from bs4 import BeautifulSoup
# from webdriver_manager.chrome import ChromeDriverManager
# driver = webdriver.Chrome(ChromeDriverManager().install())

# urls=[]
# file1=open('problem_url.txt','r')
# Lines=file1.readlines()
# for line in Lines:
#     urls.append(format(line.strip()))

# file1.close()
# cnt=1518
# for i in range(1518,len(urls)):
#     driver.get(urls[i])
#     cnt+=1
#     time.sleep(5)
#     html=driver.page_source
#     soup=BeautifulSoup(html,'html.parser')  
#     problem_text=soup.find("div",{"class":"content__u3I1 question-content__JfgR"}).find("p").text
#     problem_text=str(problem_text)
#     with open("problem"+str(cnt)+".txt","w+") as f:
#         f.write(problem_text)

