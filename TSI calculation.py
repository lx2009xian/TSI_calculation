#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np
import os
import re
import math


# In[9]:


#一层数据，计算TSI的各个部分,最终生成的结果为五列的数据
#分别为patent_id、列表元素数量、特定元素第一次出现的索引、特定元素出现的次数以及参考patents的引文总量
path = r"D:\2020国自然\3-专利引文标准化\数据下载\Dimensions\专利数据\6-用来计算TSI\3-将1中被引专利被引频次按施引专利的专利号合并\将1中被引专利被引频次按施引专利的专利号合并-被引专利被引频次为0"
files=os.listdir(path)
for file in files:
    index = file.rfind('.')
    filename = file[:index]
    f = open(path+"/"+file,"rb")
    patent_reference=pd.read_excel(f,header=0)
    Tsi_part=pd.DataFrame(np.zeros((len(patent_reference),5)), columns =['patent id','element_total','first_index','number','reference_citations'])
    for i in range(0,patent_reference.shape[0]):
        reference_citation=patent_reference['times_cited'][i]
        reference_citation=reference_citation.replace('[', '').replace(' ', '').replace(']', '')
        reference_citation=reference_citation.split(',')
        reference_citation = map(eval, reference_citation)#将字符串列表转为数字列表
        reference_citation=list(reference_citation)
        reference_citation.append(patent_reference['patent citations'][i])
        reference_citation.sort(reverse=True)
#         Tsi_part.iloc[i,0]=patent_reference['patent_id'][i]
#         Tsi_part.iloc[i,1]=len(reference_citation)
#         Tsi_part.iloc[i,2]=reference_citation.index(patent_reference['times_cited_x'][i])
#         Tsi_part.iloc[i,3]=reference_citation.count(patent_reference['times_cited_x'][i])
#         Tsi_part.iloc[i,4]=sum(reference_citation)-patent_reference['times_cited_x'][i]
        Tsi_part.iloc[i,:]=[patent_reference['patent id'][i],len(reference_citation),reference_citation.index(patent_reference['patent citations'][i]),reference_citation.count(patent_reference['patent citations'][i]),sum(reference_citation)-patent_reference['patent citations'][i]]
    Tsi_part.to_excel(r"D:\2020国自然\3-专利引文标准化\数据下载\Dimensions\专利数据\6-用来计算TSI\4-用来计算TSI的组件\计算TSI组件-被引专利的被引频次为0/"+str(filename)+".xlsx")
    print(str(filename)+":finish")


# In[11]:


#一层数据，通过上述计算出来的结果计算最终的OIp、TII和TSI
path = r"D:\2020国自然\3-专利引文标准化\数据下载\Dimensions\专利数据\6-用来计算TSI\4-用来计算TSI的组件\计算TSI组件-被引专利的被引频次为0"
files=os.listdir(path)
for file in files:
    index = file.rfind('.')
    filename = file[:index]
    f = open(path+"/"+file,"rb")
    patent_reference=pd.read_excel(f,header=0)
    Tsi=pd.DataFrame(np.zeros((len(patent_reference),4)), columns =['patent id','OIp','TII','TSI'])
    for i in range(0,patent_reference.shape[0]):
        rank=((patent_reference['first_index'][i]+1)+((patent_reference['number'][i]-1)/2))
        total_elements=patent_reference['element_total'][i]
        citations_of_references=patent_reference['reference_citations'][i]
        OIp=1-(rank/total_elements)
        TII=math.sqrt(citations_of_references)
        TSI=OIp*TII
        Tsi.iloc[i,:]=[patent_reference['patent id'][i],OIp,TII,TSI]
    Tsi.to_excel(r"D:\2020国自然\3-专利引文标准化\数据下载\Dimensions\专利数据\6-用来计算TSI\5-计算TSI的最终结果\TSI最终结果-被引专利的被引频次为0/"+str(filename)+".xlsx")
    print(str(filename)+":finish")


# In[112]:


# #利用文件夹创建新的文件夹
# path =r"D:\2020国自然\TR & social impact\1-医学或生理学—样本及对照抽样数据\有关合成生物学的研究\2-patent citation\10-计算TSI的各个部分\3-patent citation(2nd generation)"
# file_names=os.listdir(path)
# for file_name in file_names:
#     os.mkdir(r"D:\2020国自然\TR & social impact\1-医学或生理学—样本及对照抽样数据\有关合成生物学的研究\2-patent citation\11-计算最终的OIp、TII和TSI\3-patent citation(2nd generation)/"+file_name)


# In[ ]:


# #利用文件夹创建新的文件夹
# path =r"D:\2020国自然\TR & social impact\1-医学或生理学—样本及对照抽样数据\有关合成生物学的研究\2-patent citation\9-用来对照专利和其参考专利的引文数量\3-patent citation(2nd generation)包含专利引文"
# file_names=os.listdir(path)
# for file_name in file_names:
#     os.mkdir(r"D:\2020国自然\TR & social impact\1-医学或生理学—样本及对照抽样数据\有关合成生物学的研究\2-patent citation\10-计算TSI的各个部分\3-patent citation(2nd generation)/"+file_name)


# In[1]:


# #两层数据，通过上述计算出来的结果计算最终的OIp、TII和TSI
# path = r"D:\2020国自然\TR & social impact\1-医学或生理学—样本及对照抽样数据\有关合成生物学的研究\2-patent citation\10-计算TSI的各个部分\3-patent citation(2nd generation)"
# file_names=os.listdir(path)
# for file_name in file_names:
#     fullname=os.path.join(path,file_name)
#     files= os.listdir(fullname)
#     for file in files:
#         index = file.rfind('.')
#         filename = file[:index]
#         f = open(fullname+"/"+file,"rb")
#         patent_reference=pd.read_csv(f,header=0)
#         Tsi=pd.DataFrame(np.zeros((len(patent_reference),4)), columns =['patent_id','OIp','TII','TSI'])
#         for i in range(0,patent_reference.shape[0]):
#             rank=((patent_reference['first_index'][i]+1)+((patent_reference['number'][i]-1)/2))
#             total_elements=patent_reference['element_total'][i]
#             citations_of_references=patent_reference['reference_citations'][i]
#             OIp=1-(rank/total_elements)
#             TII=math.sqrt(citations_of_references)
#             TSI=OIp*TII
#             Tsi.iloc[i,:]=[patent_reference['patent_id'][i],OIp,TII,TSI]
#         Tsi.to_csv(r"D:\2020国自然\TR & social impact\1-医学或生理学—样本及对照抽样数据\有关合成生物学的研究\2-patent citation\11-计算最终的OIp、TII和TSI\3-patent citation(2nd generation)/"+str(file_name)+"/"+str(filename)+".csv")
#         print(str(filename)+":finish")


# In[2]:


# #两层数据，计算TSI的各个部分,最终生成的结果为五列的数据
# #分别为patent_id、列表元素数量、特定元素第一次出现的索引、特定元素出现的次数以及参考patents的引文总量
# path = r"D:\2020国自然\TR & social impact\1-医学或生理学—样本及对照抽样数据\有关合成生物学的研究\2-patent citation\9-用来对照专利和其参考专利的引文数量\3-patent citation(2nd generation)包含专利引文"
# file_names=os.listdir(path)
# for file_name in file_names:
#     fullname=os.path.join(path,file_name)
#     files= os.listdir(fullname)
#     for file in files:
#         index = file.rfind('.')
#         filename = file[:index]
#         f = open(fullname+"/"+file,"rb")
#         patent_reference=pd.read_csv(f,header=0)
#         Tsi_part=pd.DataFrame(np.zeros((len(patent_reference),5)), columns =['patent_id','element_total','first_index','number','reference_citations'])
#         for i in range(0,patent_reference.shape[0]):
#             reference_citation=patent_reference['times_cited_y'][i]
#             reference_citation=reference_citation.replace('[', '').replace(' ', '').replace(']', '')
#             reference_citation=reference_citation.split(',')
#             reference_citation = map(eval, reference_citation)#将字符串列表转为数字列表
#             reference_citation=list(reference_citation)
#             reference_citation.append(patent_reference['times_cited_x'][i])
#             reference_citation.sort(reverse=True)
#     #         Tsi_part.iloc[i,0]=patent_reference['patent_id'][i]
#     #         Tsi_part.iloc[i,1]=len(reference_citation)
#     #         Tsi_part.iloc[i,2]=reference_citation.index(patent_reference['times_cited_x'][i])
#     #         Tsi_part.iloc[i,3]=reference_citation.count(patent_reference['times_cited_x'][i])
#     #         Tsi_part.iloc[i,4]=sum(reference_citation)-patent_reference['times_cited_x'][i]
#             Tsi_part.iloc[i,:]=[patent_reference['patent_id'][i],len(reference_citation),reference_citation.index(patent_reference['times_cited_x'][i]),reference_citation.count(patent_reference['times_cited_x'][i]),sum(reference_citation)-patent_reference['times_cited_x'][i]]
#         Tsi_part.to_csv(r"D:\2020国自然\TR & social impact\1-医学或生理学—样本及对照抽样数据\有关合成生物学的研究\2-patent citation\10-计算TSI的各个部分\3-patent citation(2nd generation)/"+str(file_name)+"/"+str(filename)+".csv")
#         print(str(filename)+":finish")


# In[ ]:




