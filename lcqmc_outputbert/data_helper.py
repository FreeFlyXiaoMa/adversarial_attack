# -*- coding: utf-8 -*-
# @Time     :2019/11/11 20:09
# @Author   :XiaoMa
# @File     :data_helper.py
import re

"""
######################################################################################
#   1. tensorflow 版本bert_wwm_ext                                   --0.7796
#   2. tensorflow版本，训练集和验证集样本不交叉                          --0.7808
#   3. 使用pytorch框架，bert_wwm_ext，                                 --0.8156
#   4. pytorch框架，训练集和验证集样本不交叉                              --0.8502
#   5. pytorch框架，扩充训练集和验证集                                   --0.8664
#   6. roberta_wwm_ext                                                --0.8634
#   7. bert_wwm_ext  10折_7epoch                                      --0.8806
#######################################################################################
"""

with open('test_prediction.txt','r') as file:
    label_list=[]
    lines=file.readlines()
    for line in lines:
        label_list.append(line.replace('\n',''))

import pandas as pd
df=pd.DataFrame()

df['label']=label_list
df.to_csv('roberta_large_predict.csv',header=None,sep='\t')

