# # import csv
# # import nltk 
# # from nltk.tokenize import word_tokenize
# # import pandas as pd
# # #data exloration using pandas
# # dataset=pd.read_csv('SMSSpamCollection',sep="\t",header=None)

# # #Labelling the data
# # dataset.columns=['label','sms']

# # # print(dataset[0:5])

# # #Explore the data

# # #Shape the data: No of rows and columns in our dataset

# # print(f'Inpute data has {len(dataset)} rows,{len(dataset.columns)} columns')

# # #ham vs spam

# # print(f'ham={len(dataset[dataset["label"]=="ham"])}')
# # print(f'ham={len(dataset[dataset["label"]=="spam"])}')

# # #Missing data 

# # print(f"Numbers of missing label={dataset['label'].isnull().sum()}")


# # print(f"Numbers of missing msg={dataset['sms'].isnull().sum()}")

# #---->Removing the punctuations

# import re
# from tracemalloc import stop
# import pandas as pd
# import string
# import nltk

# data=pd.read_csv('SMSSpamCollection',sep="\t",header=None)
# data.columns=['label','msg']

# def remove_punc(txt):
#     txt_nopunc="".join([c for c in txt if c not in string.punctuation])
#     return txt_nopunc

# data['msg_clean']=data['msg'].apply(lambda x:remove_punc(x))

# # print(data[0:5])

# #--->Tokenisation using re inbuilt library


# def tokenize(txt):
#     t=re.split('\W+',txt)
#     return t

# data['msg_clean_tokenized']=data['msg_clean'].apply(lambda x:tokenize(x.lower()))

# # print(data[0:5])

# # Removing stop words

# stopwords=nltk.corpus.stopwords.words('english')


# def remove_stopwords(txt_tokenized):
#     txt_clean=[word for  word in txt_tokenized if word not in stopwords]
#     return txt_clean


# # data['msg_no_sw']=data['msg_clean_tokenized'].apply(lambda x:remove_stopwords(x))

# # print(data[0:5])

# #Lemmetization 

# # wn=nltk.WordNetLemmatizer()

# # def lem(token_txt):
# #     text=[wn.lemmatize(word) for word in token_txt]
# #     return text

# # data['msg_lem']=data['msg_no_sw'].apply(lambda x:lem(x))

# # print(data[0:5])

# # from sklearn.feature_extraction.text import TfidfVectorizer

# # tfidf_vect=TfidfVectorizer()

# # corupus=["This is a sentence is",
# #         "This is another sentence",
# #         "third document is here"]

# # X=tfidf_vect.fit(corupus)
# # print(X.vocabulary_)
# # print(tfidf_vect.get_feature_names_out())
# # X=tfidf_vect.transform(corupus)
# # print(X.shape)
# # print(X)
# # # print(X.totarray())
# # df=pd.DataFrame(X.toarray(),columns=tfidf_vect.get_feature_names_out())

# # print(df)

import os

for i in range(1,3374):
    file_path="p"+str(i)+"keyword.txt"
    if(os.stat(file_path).st_size==0):
        print(i)
