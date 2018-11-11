
'''
database={'ljj':123,'dst':321}

def newusers(name):

    if name  in database:
        print('name is repeated,input new name again')
        return 1
    else:
        pwd = int(input('your pwd'))
        database[name] = pwd
        print("new users ok")
        return 0

def oldusers(name,pwd):
    if database[name] == pwd:
        print(name, 'welcome back ')
    else:
        print('login incorrect')

def login():
''''''    option = input('''
#    (N)ew User Login
#    (O)ld User Login
#    (E)xit
# ''')
'''
    if option=='N':
        r = 1
        while r > 0:
            name = input('input name')
            r = newusers(name)

    elif option=='O':
        name2 = input('input name-2')
        pwd2 = int(input('input pwd-2'))
        oldusers(name2,pwd2)

    else:
        print('exit')


if __name__ == '__main__':
    login()
    print(database)
    
'''

import math
import time
import numpy as np
x=np.arange(0,1000,0.1)
tm1=time.clock()
for i,t in enumerate(x):
    x[i]=math.pow(math.cos(t),3)
tm2=time.clock()
y=np.arange(0,1000,0.1)
tn1=time.clock()
y=np.power(np.cos(y),3)
tn2=time.clock()
print('running time of math:',tm2-tm1)
print('running time of numpy:',tn2-tn1)











