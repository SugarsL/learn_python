import tushare as ts
import pandas as pd
import numpy as np

zs = ts.get_hist_data('600036',start='2018-01-01',end='2018-07-01')


''' t1 '''
zs1 = zs.drop(zs.columns[5:],axis=1)
zs1 = zs1.sort_index()

''' t2 '''
zs2 = zs1.sort_values('volume',ascending=False)
zs2_1 = zs2.head(1)
print('The max volume day is {:},the volume = {:}' \
      .format(zs2_1.iloc[0].name,zs2_1.iloc[0].volume))
zs2_2 = zs2.tail(1)
print('The minimize volume day is {:},the min volume = {:}' \
      .format(zs2_2.iloc[0].name,zs2_2.iloc[0].volume))


''' t3 '''
zs3 = zs2[zs2.volume > 1000000]

''' t4 '''
zs4 = zs2[zs.close > zs.open]
print('The num of open > close = {:}'.format(len(zs4)))


''' t5 '''
r1 = np.diff(zs2.open)

r2 = np.sign(r1)


''' t6 '''
ll = []
for i in range(119):
    ll.append(zs2.index[i][5:7])

zs2['month'] = ll


def mean_ljj(df):
    return df.sum()/len(df) # or df.mean()

tmp = zs2.groupby('month').close.apply(mean_ljj)
#print(zs2.groupby('month').close.mean())
print(tmp)





