'''
import numpy as np
from scipy.cluster.vq import vq, kmeans, whiten
list1 = [88.0, 74.0, 96.0, 85.0]
list2 = [92.0, 99.0, 95.0, 94.0]
list3 = [91.0, 87.0, 99.0, 95.0]
list4 = [78.0, 99.0, 97.0, 81.0]
list5 = [88.0, 78.0, 98.0, 84.0]
list6 = [100.0, 95.0, 100.0, 92.0]
data = np.array([list1,list2,list3,list4,list5,list6])
whiten = whiten(data)
centroids,_ = kmeans(whiten, 2)
result,_= vq(whiten, centroids)
print(result)      # result可能是[0 1 1 1 0 1]或其他类似列表

'''

'''
import numpy as np
import matplotlib.pyplot as plt
t = np.arange(0., 4., 0.1)
plt.plot(t, t, t, t+2, t, t**2)
#我是图，我是图，我是图
plt.show()

n1,n2 = input("input 2 num:").split()


print("sum:",float(n1)+float(n2))
print("minus:",float(n1)-float(n2))
print("mul:",float(n1)*float(n2))
print("div:",float(n1)/float(n2))
'''
'''
import math
print(math.gcd(16,24))
print(math.gcd(24,16))
'''
'''
f_name = input("input f_name")
s_name = input("input s_name")

print("your f_name :",f_name)
print("your s_name :",s_name)
print("your name :", f_name, s_name)


print('''hello
world''')
'''