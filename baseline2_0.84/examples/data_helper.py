# -*- coding: utf-8 -*-
# @Time     :2019/12/4 17:01
# @Author   :XiaoMa
# @File     :data_helper.py
import pickle
import pandas as pd

pred=pickle.load(open('lcqmc_pred.pkl','rb'))
df=pd.DataFrame()
index=[i for i in range(5000)]
df['index']=index
# print(len(df))
df['label']=pred
print(df)
df.to_csv('zen_pred_epoch3.csv',header=None,sep='\t',index=None)

