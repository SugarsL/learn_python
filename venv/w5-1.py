'''
import requests

films = requests.get('https://developers.douban.com/wiki/?title=movie_v2')

res = requests.findall(films.text,'1295644')

print(films.text)
print(res)

'''


'''
[['name', 'gender',  'age', 'taste of mooncake'],
['Liuzi',      'M',   21.   'Cantonese-style'],
['Huangqi',      'F',   32,         'Su-style'],
['Yuanyuan',      'F',  35,         'Su-style'],
['Duyue',      'F',   14,  'Cantonese-style'],
['Zhangtian',      'M',   33,   'Cantonese-style']]
'''
import pandas as pd
import numpy as np


col = ['name','gender','age','taste']

df = pd.DataFrame( \
[['Liuzi','M',21,'Cantonese-style'], \
['Huangqi','F',32,'Su-style'], \
['Yuanyuan','F',35,'Su-style'], \
['Duyue','F',14,'Cantonese-style'], \
['Zhangtian','M',33,'Cantonese-style']],columns=col)

#print(df)


#print(df.groupby('taste').age.count())

def f(df):
    return df.age.count()
#print(df.groupby('taste').apply(f))

def f2(df):
    return df.sort_values('age')

print(df.groupby('taste').apply(f2))