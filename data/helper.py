# -*- coding: utf-8 -*-
# @Time     :2019/11/8 15:57
# @Author   :XiaoMa
# @File     :helper.py
import pandas as pd
pd.set_option('display.width',1000)
pd.set_option('display.max_column',1000)

dev=pd.read_csv('dev_set.csv',sep='\t')

# dev['question']=dev['question1'] + '\t' +dev['question2']
dev.drop(['qid'],axis=1,inplace=True)
dev.to_csv('predict.csv',index=None,sep='\t',header=None)
# print(dev.head())
