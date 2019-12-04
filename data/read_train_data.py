# -*- coding: utf-8 -*-
# @Time     :2019/11/8 11:53
# @Author   :XiaoMa
# @File     :read_train_data.py

from xml.dom import minidom
import xml.etree.ElementTree as ET
import xmltodict
import json

with open('train_set.xml') as f:
    data=f.read()
    doc=xmltodict.parse(data)

    corpus_list=doc['TrainCorpus']['Questions']
    # print(corpus_list[0])
    eq_list_train=[]
    neq_list_train=[]

    eq_list_val=[]
    neq_list_eval=[]
    #训练集
    for i in range(len(corpus_list)-1000):
        number=corpus_list[i]['@number']
        eq=corpus_list[i]['EquivalenceQuestions']
        neq=corpus_list[i]['NotEquivalenceQuestions']
        eq_list_train.append(eq)
        neq_list_train.append(neq)
    #验证集
    for j in range(len(corpus_list)-1000,len(corpus_list)):
        number_=corpus_list[j]['@number']
        eq_=corpus_list[j]['EquivalenceQuestions']
        neq_=corpus_list[j]['NotEquivalenceQuestions']
        eq_list_val.append(eq_)
        neq_list_eval.append(neq_)


#数据的整合
# 1.训练集正样本
pos_list_train=[]
for item in eq_list_train:
    question_list=item['question']

    # 双指针法组合数据
    for i in range(len(question_list) -1 ):
        for j in range(i+1,len(question_list)):
            sample=question_list[i]  + '\t' +question_list[j]
            pos_list_train.append(sample)

            sample=question_list[j] + '\t' +question_list[i]
            pos_list_train.append(sample)

# 2.训练集负样本
neg_list_train=[]
for item in neq_list_train:
    question_list_=item['question']

    for it in question_list_:
        if not it:
            question_list_.pop(0)

    # 双指针法组合不等同问题样本
    for i in range(len(question_list_) -1):
        for j in range(i+1,len(question_list_)):
            # print(question_list_)
            sample=question_list_[i] + '\t' +question_list_[j]
            neg_list_train.append(sample)

            sample=question_list_[j] + '\t' + question_list_[i]
            neg_list_train.append(sample)

# 3.验证集正样本
pos_list_val=[]
for item in eq_list_val:
    question_list__=item['question']
    #双指针
    for i in range(len(question_list__)-1):
        for j in range(i+1,len(question_list__)):
            sample=question_list__[i] + '\t' +question_list__[j]
            pos_list_val.append(sample)

            sample=question_list__[j] + '\t' + question_list__[i]
            pos_list_val.append(sample)

# 4.验证集负样本
neg_list_val=[]
for item in neq_list_eval:
    question_list___=item['question']
    #
    for it in question_list___:
        if not it:
            question_list___.pop(0)

    for i in range(len(question_list___)-1):
        for j in range(i+1,len(question_list___)):
            sample=question_list___[i] + '\t' +question_list___[j]
            neg_list_val.append(sample)

            sample=question_list___[j] + '\t' + question_list___[i]
            neg_list_val.append(sample)

# print(len(pos_list_train),len(neg_list_train))

import pandas as pd
df=pd.DataFrame()
df['text']=pos_list_train
li=['1' for _ in range(len(pos_list_train))]
df['label']=li

df2=pd.DataFrame()
df2['text']=neg_list_train
li_=['0' for _ in range(len(neg_list_train))]
df2['label']=li_

train=pd.concat([df,df2])
train=train.sample(frac=1.0,random_state=10)

train=train.reset_index()
train.drop('index',axis=1,inplace=True)

df3=pd.DataFrame()
df3['text']=pos_list_val
li__=['1' for _ in range(len(pos_list_val))]
df3['label']=li__

df4=pd.DataFrame()
df4['text']=neg_list_val
li___=['0' for _ in range(len(neg_list_val))]
df4['label']=li___

val=pd.concat([df3,df4])
val=val.sample(frac=1.0,random_state=100)
val=val.reset_index()
val.drop('index',axis=1,inplace=True)

train.to_csv('trian.csv',header=None,index=None,sep='\t')
val.to_csv('valid.csv',header=None,index=None,sep='\t')

# print(len(train),len(val))