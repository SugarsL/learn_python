'''
import numpy as np
from scipy.cluster.vq import vq,kmeans,whiten

list1 = [88.0, 74.0, 96.0, 85.0]
list2 = [92.0, 99.0, 95.0, 94.0]
list3 = [91.0, 87.0, 99.0, 95.0]
list4 = [78.0, 99.0, 97.0, 81.0]
list5 = [88.0, 78.0, 98.0, 84.0]
list6 = [100.0, 95.0, 100.0, 92.0]

data = np.array([list1,list2,list3,list4,list5,list6])
std = whiten(data) # calculate 标准差（均方差） of every list

res, _ = kmeans(std,3) #聚出3类

final, _ = vq(std, res)

print(final)

#聚出2类
#[0 1 1 0 0 1]

#聚出3类
#[2 0 0 1 2 0]
'''

''' sk-learn: kmeans'''

import numpy as np
from sklearn.cluster import KMeans

list1 = [88.0, 74.0, 96.0, 85.0]
list2 = [92.0, 99.0, 95.0, 94.0]
list3 = [91.0, 87.0, 99.0, 95.0]
list4 = [78.0, 99.0, 97.0, 81.0]
list5 = [88.0, 78.0, 98.0, 84.0]
list6 = [100.0, 95.0, 100.0, 92.0]

data = np.array([list1,list2,list3,list4,list5,list6])

result = KMeans(n_clusters=3).fit(data)

final = result.predict(data)
print(final)

#聚出3类
#[0 1 1 2 0 1]


