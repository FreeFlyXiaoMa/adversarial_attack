# -*- coding: utf-8 -*-
# @Time     :2019/11/8 11:53
# @Author   :XiaoMa
# @File     :read_train_data.py

import pandas as pd
with open('train_data.csv','r',encoding='utf-8') as file:
    qe1_list=[]
    qe2_list=[]
    label_list=[]
    print('-----')
    lines=file.readlines()
    for index,line in enumerate(lines):
        line=line.replace('\n','')
        line_list=line.split('\t')
        # print(line_list)
        # print(len(line_list))
        # print(len(line_list))
        question1=line_list[0]
        question2=line_list[1]
        label=int(line_list[2])
#
        qe1_list.append(question1)
        qe2_list.append(question2)
        label_list.append(label)

df=pd.DataFrame()
df['question1']=qe1_list
df['question2']=qe2_list
df['label']=label_list
df.to_csv('train_data.csv',index=None)

