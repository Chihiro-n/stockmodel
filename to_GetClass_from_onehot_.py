
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df_train_law = pd.read_csv('./data/label_difflog_2005-2018.csv' ,index_col=0)



np_diff = df_train_law.diff_log始値

sigma_p = df_train_law.diff_log始値.var()
sigma_m = sigma_p * -1

par_array = np_diff.quantile(q=[0, 0.1, 0.5, 0.9, 1])

m_10 = par_array.iat[1]
p_10 = par_array.iat[3]

print(df_train_law.head())

length = len(df_train_law.diff_log始値)
np_opendiff = df_train_law.diff_log始値.values

label_m1 = np.array([])
label_m0 = np.array([])
label_p0 = np.array([])
label_p1 = np.array([])
label_class = np.array([])

label_m1 = np.append(0,label_m1)
label_m0 = np.append(0,label_m0)
label_p0 = np.append(0,label_p0)
label_p1 = np.append(0,label_p1)
label_class = np.append(0,label_class)


for i in range(1,length):

    if np_opendiff[i] > p_10:
        label_m1 = np.append(label_m1,0)
        label_m0 = np.append(label_m0,0)
        label_p0 = np.append(label_p0,0)
        label_p1 = np.append(label_p1,1)
        label_class = np.append(label_class,4)


    elif 0 <= np_opendiff[i] < p_10:
        label_m1 = np.append(label_m1,0)
        label_m0 = np.append(label_m0,0)
        label_p0 = np.append(label_p0,1)
        label_p1 = np.append(label_p1,0)
        label_class = np.append(label_class,3)


    elif m_10 < np_opendiff[i] < 0:
        label_m1 = np.append(label_m1,0)
        label_m0 = np.append(label_m0,1)
        label_p0 = np.append(label_p0,0)
        label_p1 = np.append(label_p1,0)
        label_class = np.append(label_class,2)

    elif np_opendiff[i] < m_10:

        label_m1 = np.append(label_m1,1)
        label_m0 = np.append(label_m0,0)
        label_p0 = np.append(label_p0,0)
        label_p1 = np.append(label_p1,0)
        label_class = np.append(label_class,1)


df_label = df_train_law
df_label['label_m1'] = label_m1
df_label['label_m0'] = label_m0
df_label['label_p0'] = label_p0
df_label['label_p1'] = label_p1
df_label['label_class'] = label_class

print(df_label.head())

### データの可視化　重たいからコメントアウトしておく
"""
np_diff.hist(bins = 40,range=[-0.1, 0.1])
plt.vlines(x=p_10, ymin=0, ymax=500)
plt.vlines(x=m_10, ymin=0, ymax=500)

"""


sns.countplot(x="label_class", data=df_label)
plt.show()



df_label.to_csv('/Users/apple/python/stock/StockModelpytorch/data/class_label_difflog_2005-2018.csv')


