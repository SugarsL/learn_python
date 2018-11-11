''' test1
weight,height = eval(input("input your weight and height"))

bmi = weight/height ** 2
if bmi < 18.5:
    print("too thin")
elif bmi >18.5 and bmi < 23.9:
    print("normal")
elif bmi > 23.9 and bmi < 27.9:
    print("overweight")
elif bmi > 28:
    print("fat")
'''
''' test2 
for i in range(0,300,20):
    c = 5/9*(i-32)
    print('F:{:.2f} C:{:.2f}'.format(i,c))
'''

''' w2-exam 

def fac(x):
    for i in range(1,x+1):
        sum = 0
        for j in range(1,i):
            if i % j == 0:
                sum += j
        if sum != i:
            sum2 = 0
            for k in range(1,sum):
                if sum % k == 0:
                    sum2 += k
            if sum2 == i and sum > sum2:
                print("{}-{}".format(sum2,sum))





n = int(input())
fac(n)
'''
'''
import math

def prime(num):
    for i in range(2,int(math.sqrt(num))+1):
        if num % i == 0:
            return False

    return True



def monisen(no):
    n = 0
    i = 2
    while no > n:
        if prime(i):
            res = math.pow(2,i)-1
            if prime(res):
                n += 1
                if n == no:
                    return int(res)
        i += 1

print(monisen(int(input())))
'''

