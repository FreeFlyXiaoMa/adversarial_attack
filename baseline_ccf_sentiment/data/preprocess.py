import pandas as pd
import os
import random


train=pd.read_csv('trian.csv',sep='\t',header=None)
dev=pd.read_csv('valid.csv',sep='\t',header=None)

text_a_list=[]
text_b_list=[]
label_list=[]
with open('trian.csv') as file:
    lines=file.readlines()
    for line in lines:
        line=line.replace('\n','').replace('"','')
        line_list=line.split('\t')

        text_a_list.append(line_list[0])
        text_b_list.append(line_list[1])
        label_list.append(line_list[2])

with open('valid.csv') as f:
    lines=f.readlines()
    for line in lines:
        line=line.replace('\n','').replace('"','')
        line_list=line.split('\t')

        text_a_list.append(line_list[0])
        text_b_list.append(line_list[1])
        label_list.append(line_list[2])
train_df=pd.DataFrame()
id_list=[i for i in range(len(text_a_list))]

train_df['id']=id_list
train_df['content']=text_a_list
train_df['title']=text_b_list
train_df['label']=label_list


# train_df=pd.concat([train,dev],axis=0)
#
list1=[]
list2=[]
# list3=[]
with open('predict.csv') as f:
    lines=f.readlines()
    line = line.replace('\n', '').replace('"', '')
    line_list = line.split('\t')

    list1.append(line_list[0])
    list2.append(line_list[1])
list3=[i for i in range(len(list1))]

test_df=pd.DataFrame()
test_df['id']=list3
test_df['content']=list1
test_df['title']=list2

#
#
index=set(range(train_df.shape[0])) #第一个维度的长度
#
#
K_fold=[]
for i in range(5):
    if i == 4:
        tmp=index
    else:
        tmp=random.sample(index,int(1.0/5*train_df.shape[0]))
    index=index-set(tmp)
    print("Number:",len(tmp))
    K_fold.append(tmp)
#
#
for i in range(5):
    print("Fold",i)
    os.system("mkdir data_{}".format(i))
    dev_index=list(K_fold[i])
    train_index=[]
    for j in range(5):
        if j!=i:
            train_index+=K_fold[j]
    train_df.iloc[train_index].to_csv("data_{}/train.csv".format(i),index=None)
    train_df.iloc[dev_index].to_csv("data_{}/dev.csv".format(i),index=None)
    test_df.to_csv("data_{}/test.csv".format(i),index=None)
