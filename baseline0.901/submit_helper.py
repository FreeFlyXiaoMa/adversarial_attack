# -*- coding: utf-8 -*-
# @Time     :2019/11/14 17:49
# @Author   :XiaoMa
# @File     :submit_helper.py

import pandas as pd
pred=pd.read_csv('test_pred.csv')
re_list=[]
for index in pred.index:
    prob_0=pred['0'][index]
    prob_1=pred['1'][index]
    # print(type(prob_1))
    if prob_0 > prob_1:
        re_list.append(0)
    else:
        re_list.append(1)
df=pd.DataFrame()
df['resutl']=re_list
df.to_csv('submit_10-kfold_7-epoch.csv',header=None,sep='\t')



