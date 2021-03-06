#!/usr/bin/env python
# coding: utf-8

# In[80]:


import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
import warnings
warnings.filterwarnings(action='ignore')


# ## raw data 와 valid data 개요

# In[81]:


raw_data = pd.read_csv("../data/sea/sea_managing_raw.csv", encoding='cp949')
print(raw_data.shape)
raw_data.head()


# In[82]:


df = pd.DataFrame(raw_data, columns=raw_data.columns)


# In[83]:


#검색식을 통해 수집한 유효특허 후보 데이터
val_data = pd.read_csv("../data/sea/sea_managing_val.csv", encoding = "cp949")
print(val_data.shape)
val_data.head()


# In[84]:


#미국 특허 확인
val_data.tail()


# ## raw data 필요없는 column 제거
# * 미국 특허만 활용
# * 일본 특허 정보 x  
# ex) 'Original FI[JP]', 'Original F-term[JP]', 'Original Theme Code [JP]', '출원인 식별기호[JP]'

# In[85]:


df.columns


# In[86]:


df = raw_data.dropna(axis=1, how='all')
df.head()


# In[87]:


df.columns


# ## valid data에서 US data 외 데이터 drop

# In[88]:


val_data = val_data[val_data.국가 == "US"]
val_data = val_data.drop_duplicates(val_data.columns)
val_data.shape
# val_data.to_csv("1.csv", encoding='cp949')


# ## raw data와 valid data의 공개/등록 번호 form 맞춰주기

# In[89]:


print("<valid> \n", val_data['공개(등록)번호'].head())
print("\n<raw> \n", raw_data['공개번호/공표/재공표 '].head(), "\n", raw_data['등록번호'].head())


# In[90]:


df.loc[:, '공개번호/공표/재공표 '] = (df.loc[:, '공개번호/공표/재공표 '].str.split('-')).str.join('')
df.loc[:, '공개번호/공표/재공표 '].fillna(value = 0, inplace=True)


# In[91]:


# 8자리 맞추기 ex)8704653 -> 08704653
# 00000000 -> 0

df.loc[:, '등록번호'] = df.loc[:, '등록번호'].apply(lambda x:'{0:0>8}'.format(x) if(np.all(pd.notnull(x))) else x).fillna(0)
for idx, i in enumerate(df['등록번호']):
    if str(i).isdigit() != True:
        df['등록번호'][idx] = 0


# In[92]:


df['등록번호'].head(10)


# ## valid patent 확인
# US 유효특허 : 86개

# In[93]:


#raw_data 중에서 val_data
y_idx_list = []
for idx, raw in enumerate(df["공개번호/공표/재공표 "]):
    for val in val_data["공개(등록)번호"]:
        if raw == val and idx not in y_idx_list:
            y_idx_list.append(idx)

for idx, raw in enumerate(df["등록번호"]):
    for val in val_data["공개(등록)번호"]:
        if raw == val and idx not in y_idx_list:
            y_idx_list.append(idx)

for idx, raw in enumerate(df["발명의 명칭"]):
    for val in val_data["발명의 명칭"]:
        if raw.lower() == val.lower() and idx not in y_idx_list:
            y_idx_list.append(idx)
y_data_list = [int(1) for i in range(len(y_idx_list))]
print(len(y_idx_list), len(y_data_list))


# In[94]:


y_values = pd.Series(data=y_data_list, index=y_idx_list)
df.loc[:, "유효특허 여부"] = y_values
df["유효특허 여부"].fillna(0, inplace=True)


# In[95]:


df['유효특허 여부'].value_counts()


# <hr>

# ## IPC Digitization

# In[96]:


df.loc[:, 'Original IPC Main'] = df.loc[:, 'Original IPC Main'].astype('str').str.slice(0,4)
df['Original IPC Main'].head()


# In[97]:


# |로 묶인 IPC 처리
ipc_idx_list = []
ipc_all = []
for idx, i in enumerate(df['Original IPC All']):
    i = i.split('|')
    if len(i) != 1: # 여러 개 있으면
        ipc_list = []
        for ipc in i:
            ipc_list.append((ipc.strip())[:4])
        ipc_all.append(('|').join(ipc_list))
        ipc_idx_list.append(idx)
    else:
        ipc_all.append((i[0].strip())[0:4])
        ipc_idx_list.append(idx)


# In[98]:


ipc_values = pd.Series(data = ipc_all, index=ipc_idx_list)
df.loc[:, 'Original IPC All'] = ipc_values
df['Original IPC All'].head()


# ## fillna

# In[99]:


df.loc[:, '출원인'] = df.loc[:, '출원인'].fillna(value='UKN')
df[['출원인']][60:70]


# ## including dash/slash data preprocessing

# In[100]:


df.loc[:, '출원일'] = (df.loc[:, '출원일'].str.split('-')).str.join('')
df.loc[:, '출원일'] = df.loc[:, '출원일'].fillna(0)

df.loc[:, '공개일'] = (df.loc[:, '공개일'].str.split('-')).str.join('')
df.loc[:, '공개일'] = df.loc[:, '공개일'].fillna(0)

df.loc[:, '등록일'] = (df.loc[:, '등록일'].str.split('-')).str.join('')
df.loc[:, '등록일'] = df.loc[:, '등록일'].fillna(0)

df.loc[:, '국제 공개번호'] = (df.loc[:, '국제 공개번호'].str.split('-')).str.join('').str.slice(2,-1)
df.loc[:, '국제 공개번호'] = (df.loc[:, '국제 공개번호'].str.split('/')).str.join('')
df.loc[:, '국제 공개번호'] = df.loc[:, '국제 공개번호'].fillna(value=int(0))


# ## Label Encoding

# In[101]:


application_id = list(df['출원번호'])
le = LabelEncoder()
le.fit(application_id)

application_id_le = le.transform(application_id)
df['출원번호'] = application_id_le


# In[102]:


patent_kind = list(df['문헌종류 코드'])
le = LabelEncoder()
le.fit(patent_kind)

patent_kind_le = le.transform(patent_kind)
df['문헌종류 코드'] = patent_kind_le


# In[103]:


priority_id = list(df['우선권 번호'])
le = LabelEncoder()
le.fit(priority_id)

priority_id_le = le.transform(priority_id)
df['우선권 번호'] = priority_id_le


# In[104]:


df = df.astype('str')


# In[105]:


df.to_csv('../data/sea/data_sea_1.csv', encoding='cp949')


# ---------

# In[106]:


df['patent index'] = [i for i in range(df.shape[0])]


# ## ipc main to EdgeList

# In[107]:


# ipc 한 개
main_ipc_dict = {}
main_ipc_dict['patent'] = df['patent index']
main_ipc_dict['ipc'] = df['Original IPC Main']

main_ipc_edge = pd.DataFrame(main_ipc_dict)
main_ipc_edge.to_csv("../data/sea/sea_main_ipc_edge.tsv", sep='\t', index=False, header=True)


# ## ipc all to EdgeList

# In[108]:


# ipc 여러 개
ipc_index = []
ipc = []
for idx, i in enumerate(df['Original IPC All']):
    i = i.split('|')
    if len(i) != 1:
        for j in range(len(i)):
            ipc_index.append(idx)
            ipc.append(i[j])
    else:
        ipc_index.append(idx)
        ipc.append(i[0])


# In[109]:


ipc_idx_values = pd.Series(data=ipc_index)
ipc_values = pd.Series(data=ipc)

all_ipc_dict = {}
all_ipc_dict['ipc'] = ipc_values
all_ipc_dict['patent'] = ipc_idx_values

all_ipc_edge = pd.DataFrame(all_ipc_dict)
all_ipc_edge.to_csv("../data/sea/sea_all_ipc_edge.tsv", sep='\t', index=False, header=True)


# ## US Class main to EdgeList

# In[110]:


# 한 개
main_usclass_dict = {}
main_usclass_dict['patent'] = df['patent index']
main_usclass_dict['us_class'] = df['Original US Class Main[US]']

main_usclass_edge = pd.DataFrame(main_usclass_dict)
main_usclass_edge.to_csv("../data/sea/sea_main_usclass_edge.tsv", sep='\t', index=False, header=True)


# ## US Class all to EdgeList

# In[111]:


# 여러 개
usclass_index = []
usclass = []
for idx, i in enumerate(df['Original US Class All[US]']):
    i = i.split('|')
    if len(i) != 1:
        for j in range(len(i)):
            usclass_index.append(idx)
            usclass.append(i[j].strip())
    else:
        usclass_index.append(idx)
        usclass.append(i[0])


# In[112]:


usclass_idx_values = pd.Series(data=usclass_index)
usclass_values = pd.Series(data=usclass)

all_usclass_dict = {}
all_usclass_dict['us_class'] = usclass_values
all_usclass_dict['patent'] = usclass_idx_values

all_usclass_edge = pd.DataFrame(all_usclass_dict)
all_usclass_edge.to_csv("../data/sea/sea_all_usclass_edge.tsv", sep='\t', index=False, header=True)


# ## assignee to EdgeList

# In[113]:


assignee = pd.read_csv('../data/sea/assignee.tsv', sep='\t', encoding='utf-8')
assignee = assignee.drop('Unnamed: 0', axis=1)


# In[114]:


# patent id 와 assignee id 리스트 생성
patent_id =[]
assignee_id_list = []
for i in range(len(assignee)):
    ids = assignee.fillna('0').iloc[[i]].values
    for j in ids[0]:
        patent_assignee = j.replace("(","").replace(")","").replace("'","").split(",")
        if len(patent_assignee) != 1:
            patent_id.append(patent_assignee[0].strip())
            assignee_id_list.append(patent_assignee[1].strip())


# In[115]:


patent_values = pd.Series(data=patent_id)
assignee_values = pd.Series(data=assignee_id_list)

patent_assignee_dict= {}
patent_assignee_dict['patent_id'] = patent_id
patent_assignee_dict['assignee_id'] = assignee_id_list

patent_assignee_edge = pd.DataFrame(patent_assignee_dict)
patent_assignee_edge.to_csv('../data/sea/sea_assignee_edge.tsv', sep='\t', header=True)


# ## application citation to EdgeList

# In[116]:


application_citation = pd.read_csv('../data/sea/application_citation.tsv', sep='\t', encoding='utf-8')
application_citation = application_citation.drop('Unnamed: 0', axis=1)
application_citation = application_citation.dropna(how='all')


# In[117]:


patent_id =[]
application_citation_id_list = []
for i in range(len(application_citation)):
    ids = application_citation.fillna('0').iloc[[i]].values
    for j in ids[0]:
        patent_application_citation = j.replace("(","").replace(")","").replace("'","").split(",")
        if len(patent_application_citation) != 1:
            patent_id.append(patent_application_citation[0].strip())
            application_citation_id_list.append(patent_application_citation[1].strip())


# In[118]:


patent_values = pd.Series(data=patent_id)
application_citation_values = pd.Series(data=application_citation_id_list)

patent_application_citation_dict= {}
patent_application_citation_dict['patent_id'] = patent_id
patent_application_citation_dict['application_citation_id'] = application_citation_id_list

patent_application_citation_edge = pd.DataFrame(patent_application_citation_dict)
patent_application_citation_edge.to_csv('../data/sea/sea_application_citation_edge.tsv', sep='\t', header=True)


# ## grant citation to EdgeList

# In[119]:


grant_citation = pd.read_csv('../data/sea/grant_citation.tsv', sep='\t', encoding='utf-8')
grant_citation = grant_citation.drop('Unnamed: 0', axis=1)
grant_citation = grant_citation.dropna(how='all')


# In[120]:


patent_id =[]
grant_citation_id_list = []
for i in range(len(grant_citation)):
    ids = grant_citation.fillna('0').iloc[[i]].values
    for j in ids[0]:
        patent_grant_citation = j.replace("(","").replace(")","").replace("'","").split(",")
        if len(patent_grant_citation) != 1:
            patent_id.append(patent_grant_citation[0].strip())
            grant_citation_id_list.append(patent_grant_citation[1].strip())


# In[121]:


patent_values = pd.Series(data=patent_id)
grant_citation_values = pd.Series(data=grant_citation_id_list)

patent_grant_citation_dict= {}
patent_grant_citation_dict['patent_id'] = patent_id
patent_grant_citation_dict['grant_citation_id'] = grant_citation_id_list

patent_grant_citation_edge = pd.DataFrame(patent_grant_citation_dict)
patent_grant_citation_edge.to_csv('../data/sea/sea_grant_citation_edge.tsv', sep='\t', header=True)


# ## inventor to EdgeList

# In[122]:


df.columns


# In[123]:


inventor_index = []
inventor = []
for idx, i in enumerate(df['발명자/고안자']):
    i = i.split('|')
    if len(i) != 1:
        for j in range(len(i)):
            inventor_index.append(idx)
            inventor.append(i[j].strip())
    else:
        inventor_index.append(idx)
        inventor.append(i[0])


# In[124]:


inventor_idx_values = pd.Series(data=inventor_index)
inventor_values = pd.Series(data=inventor)

inventor_dict = {}
inventor_dict['patent_id'] = inventor_idx_values
inventor_dict['inventor'] = inventor_values

inventor_edge = pd.DataFrame(inventor_dict)
inventor_edge.to_csv('../data/sea/sea_inventor_edge.tsv', sep='\t', encoding='utf-8', header=True)


# ## applicant

# In[125]:


applicant_index = []
applicant = []
for idx, i in enumerate(df['출원인']):
    i = i.split('|')
    if len(i) != 1:
        for j in range(len(i)):
            applicant_index.append(idx)
            applicant.append(i[j].strip().lower())
    else:
        applicant_index.append(idx)
        applicant.append(i[0].lower())


# In[126]:


applicant_idx_values = pd.Series(data=applicant_index)
applicant_values = pd.Series(data=applicant)

applicant_dict = {}
applicant_dict['patent_id'] = applicant_idx_values
applicant_dict['applicant'] = applicant_values

applicant_edge = pd.DataFrame(applicant_dict)
applicant_edge.to_csv('../data/sea/sea_applicant_edge.tsv', sep='\t', encoding='utf-8', header=True)


# ----------

# In[127]:


df = pd.read_csv("../data/sea/data_sea_1.csv", encoding='cp949')


# In[128]:


print(df.shape)
df.columns


# ## convert column's name to english & drop columns

# In[129]:


df = df.rename(index=str, 
               columns={'등록번호': 'grant_id','출원번호':'application_id', '공개번호/공표/재공표 ':'published_grant_id',
                        '발명의 명칭': "title", '대표청구항':'claim', '청구항 수':'n_claim', "발명자/고안자":"inventor",
                        '우선권 번호':'priority_id', '요약': 'abstract', 'Unnamed: 0' : 'index', '등록일':'grant_date',
                        '출원일':'application_date', '공개일':'published_date', '출원인':'applicant', 
                        '출원인 수':'n_applicant',
                        '출원인 대표명화 코드':'applicant_code', '국제 공개번호':'international_published_id', 
                        'Original IPC Main':'ipc_main', 'Original IPC All':'ipc_all',
                        'Original US Class Main[US]':'usclass_main', 'Original US Class All[US]':'usclass_all',
                        '유효특허 여부':'valid_patent', '문헌종류 코드':'patent_kind'})


# In[130]:


df = df.drop(['특허/실용 구분', 'DB종류', '국가코드', '출원인 대표명화 영문명', '국제 공개일', '우선권 주장일',
             'Original CPC Main', 'Original CPC All', 'WIPS ON key', '출원인 국적', '우선권 국가'], axis=1)


# In[131]:


df.shape


# ## merge edgelist to df

# ### assignee

# In[132]:


assignee_edge = pd.read_csv("../data/sea/sea_assignee_edge.tsv", sep='\t')
for i, j in enumerate(df.grant_id):
    if j in list(assignee_edge['patent_id']):
        x = assignee_edge.loc[assignee_edge['patent_id']==j]['Unnamed: 0']
        assignee_edge.at[x,'patent_id']= i


# In[133]:


cols = assignee_edge.columns.tolist()[::-1]
assignee_edge = assignee_edge[cols]

assignee_edge["value"] = 1
assignee_matrix = pd.pivot_table(assignee_edge, index=['patent_id', 'assignee_id'])

assignee_matrix_reidx = assignee_matrix.reset_index()
assignee_matrix_reidx = assignee_matrix_reidx.pivot(values= "value",index="patent_id",columns="assignee_id").fillna(0)

df.index = df['index']
df = df.drop_duplicates()
df = df.join(assignee_matrix_reidx, how='outer')
df.shape


# ### appication citation

# In[134]:


application_citation_edge = pd.read_csv("../data/sea/sea_application_citation_edge.tsv", sep='\t')

for i, j in enumerate(df.grant_id):
    if j in list(application_citation_edge['patent_id']):
        x = application_citation_edge.loc[application_citation_edge['patent_id']==j]['Unnamed: 0']
        application_citation_edge.at[x,'patent_id']= i


# In[135]:


cols = application_citation_edge.columns.tolist()[::-1]
application_citation_edge = application_citation_edge[cols]

application_citation_edge["value"] = 1
application_citation_matrix = pd.pivot_table(application_citation_edge, index=['patent_id', 'application_citation_id'])

application_citation_matrix_reidx = application_citation_matrix.reset_index()
application_citation_matrix_reidx = application_citation_matrix_reidx.pivot(values= "value",index="patent_id",columns="application_citation_id").fillna(0)

df.index = df['index']
df = df.drop_duplicates()
df = df.join(application_citation_matrix_reidx, how='outer')
df.shape


# ### grant citaion

# In[136]:


grant_citation_edge = pd.read_csv("../data/sea/sea_grant_citation_edge.tsv", sep='\t')

for i, j in enumerate(df.grant_id):
    if j in list(grant_citation_edge['patent_id']):
        x = grant_citation_edge.loc[grant_citation_edge['patent_id']==j]['Unnamed: 0']
        grant_citation_edge.at[x,'patent_id']= i


# In[137]:


cols = grant_citation_edge.columns.tolist()[::-1]
grant_citation_edge = grant_citation_edge[cols]
grant_citation_edge["value"] = 1
grant_citation_matrix = pd.pivot_table(grant_citation_edge, 
                                             index=['patent_id', 'grant_citation_id'])

grant_citation_matrix_reidx = grant_citation_matrix.reset_index()
grant_citation_matrix_reidx = grant_citation_matrix_reidx.pivot(values= "value",index="patent_id",columns="grant_citation_id").fillna(0)
df.index = df['index']
df = df.drop_duplicates()
df = df.join(grant_citation_matrix_reidx, how='outer')
df.shape


# ### ipc all

# In[138]:


all_ipc_edge = pd.read_csv("../data/night/night_all_ipc_edge.tsv", sep='\t')
cols = all_ipc_edge.columns.tolist()[::-1]


# In[139]:


all_ipc_edge = all_ipc_edge[cols]
all_ipc_edge["value"] = 1
all_ipc_matrix = pd.pivot_table(all_ipc_edge, index=['patent', 'ipc'])
all_ipc_matrix.head()


# In[140]:


all_ipc_matrix_reidx = all_ipc_matrix.reset_index()
all_ipc_matrix_reidx = all_ipc_matrix_reidx.pivot(index="patent",columns="ipc")["value"].fillna(0)
all_ipc_matrix_reidx.head()


# In[141]:


df = df.drop('ipc_all', axis=1)
df = df.drop('ipc_main', axis=1)

df.index = df['index']
df = df.drop_duplicates()
df = df.merge(all_ipc_matrix_reidx, left_index=True, right_index=True)
print(df.shape)


# ### usclass all

# In[142]:


all_usclass_edge = pd.read_csv("../data/night/night_all_usclass_edge.tsv", sep='\t')
cols = all_usclass_edge.columns.tolist()[::-1]

all_usclass_edge = all_usclass_edge[cols]
all_usclass_edge["value"] = 1
all_usclass_matrix = pd.pivot_table(all_usclass_edge, index=['patent', 'us_class'])

all_usclass_matrix_reidx = all_usclass_matrix.reset_index()
all_usclass_matrix_reidx = all_usclass_matrix_reidx.pivot(index="patent",columns="us_class")["value"].fillna(0)
df = df.drop('usclass_all', axis=1)
df = df.drop('usclass_main', axis=1)

df.index = df['index']
df = df.drop_duplicates()
df = df.merge(all_usclass_matrix_reidx, left_index=True, right_index=True)
print(df.shape)


# ### inventor

# In[143]:


inventor_edge = pd.read_csv("../data/night/night_inventor_edge.tsv", sep='\t')
cols = inventor_edge.columns.tolist()[::-1]

inventor_edge = inventor_edge[cols]
inventor_edge["value"] = 1
inventor_matrix = pd.pivot_table(inventor_edge, index=['patent_id', 'inventor'])

inventor_matrix_reidx = inventor_matrix.reset_index()
inventor_matrix_reidx = inventor_matrix_reidx.pivot(index="patent_id",columns="inventor")["value"].fillna(0)

df = df.drop('inventor', axis=1)
df.index = df['index']
df = df.drop_duplicates()
df = df.merge(inventor_matrix_reidx, left_index=True, right_index=True)
print(df.shape)


# ### applicant

# In[144]:


applicant_edge = pd.read_csv("../data/night/night_applicant_edge.tsv", sep='\t')
cols = applicant_edge.columns.tolist()[::-1]

applicant_edge = applicant_edge[cols]
applicant_edge["value"] = 1
applicant_matrix = pd.pivot_table(applicant_edge, index=['patent_id', 'applicant'])

applicant_matrix_reidx = applicant_matrix.reset_index()
applicant_matrix_reidx = applicant_matrix_reidx.pivot(index="patent_id",columns="applicant")["value"].fillna(0)

df = df.drop('applicant', axis=1)
df = df.drop('applicant_code', axis=1)

df.index = df['index']
df = df.drop_duplicates()
df = df.merge(applicant_matrix_reidx, left_index=True, right_index=True)
print(df.shape)


# In[145]:


df.to_csv("../data/night/night_dataset_1.csv", index=False, header=True)


# In[146]:


set(df.columns) - set(df.describe().columns)


# ----------

# In[153]:


from collections import Counter
from imblearn.over_sampling import SMOTE
from sklearn.model_selection import train_test_split


# In[159]:


df.drop(['title', 'abstract', 'claim'], axis=1, inplace=True)

x = df.loc[:, df.columns!='valid_patent'].astype(float)
y = df['valid_patent'].astype(int)


# ## Train/Test Split

# In[160]:


x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=50)


# ## SMOTE

# In[161]:


print('Original dataset shape {}'.format(Counter(y_train)))
sm = SMOTE(random_state=42)
x_res , y_res = sm.fit_resample(x_train, y_train)
print('Resampled dataset shape {}'.format(Counter(y_res)))
print('Y test dataset shpae {}'.format(Counter(y_test)))


# ## Model

# ### Logistic Regression

# In[162]:


from sklearn import linear_model, metrics
from sklearn.metrics import classification_report, confusion_matrix


# In[163]:


logreg = linear_model.LogisticRegression(fit_intercept=False)
logreg.fit(x_res, y_res)

result = logreg.predict(x_test)

print("This classification report of using threshold: \n",classification_report(y_test, result))
print ("This is accuracy score:",metrics.accuracy_score(y_test, result),"\n")


# In[164]:


prob = logreg.predict_proba(x_test)

y_pred = np.zeros(len(x_test))
y_pred[prob[:,1] > 0.35] = 1

print("This classification report of using threshold: \n",classification_report(y_test, y_pred))
print ("This is accuracy score:",metrics.accuracy_score(y_test, y_pred),"\n")


# ### Decision Tree

# In[165]:


from sklearn import tree

dt = tree.DecisionTreeClassifier(criterion='gini', max_depth=5, min_samples_leaf=5)
dt.fit(x_res, y_res)

result = dt.predict(x_test)

print("This classification report of using threshold: \n",classification_report(y_test, result))
print ("This is accuracy score:",metrics.accuracy_score(y_test, result),"\n")


# ### Random Forest

# In[171]:


from sklearn.ensemble import RandomForestClassifier

rf = RandomForestClassifier(random_state=42, max_depth=5)
rf.fit(x_res, y_res)

result = rf.predict(x_test)

print("This classification report of using threshold: \n",classification_report(y_test, result))
print ("This is accuracy score:",metrics.accuracy_score(y_test, result),"\n")


# In[ ]:




