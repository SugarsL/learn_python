import pandas as pd
'''
l1 = ['The rolling stones', 'Beatles', 'Guns N\' Roses', 'Metallica']
l2 = ['Satisfaction', 'Let It Be', 'Dont\' Cry', 'Nothing Else Matters']

s1 = pd.Series(l1)
s2 = pd.Series(l2)
df = pd.DataFrame(list(zip(s1,s2)),columns=('Singer', 'Song'))

df.to_csv('a.csv',index=False)
#print(df)


songs = pd.read_csv('a.csv', sep=',')

print(songs)

print(len(songs))

'''
df2 = pd.DataFrame()

df_tmp = pd.read_excel('w6-3-2.xlsx')

df2 = pd.concat([df2,df_tmp])

df2['sum'] = df2['Python'] + df2['Math']

print(df2)

df2.to_excel('students.xlsx',sheet_name='scores')









