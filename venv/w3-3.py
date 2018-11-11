import random

'''test 1
n = int(input('input a number'))

r = [x for x in range(1,101) if x%n != 0 and str(n) not in str(x)]

for i in range(len(r)):
    print(r[i],end=',')
    if (i+1) % 10 ==0:
        print('\n')
'''



'''test 2

cnt = [0]*101

with open('w3.txt','w+') as f:
    for i in range(500):
        n = random.randint(1,100)
        f.write(str(n))
        f.write('\n')

    f.seek(0)
    for i in range(500):
        num = f.readline()
        cnt[int(num)] +=1

print(cnt)
for i in range(len(cnt)):
    if cnt[i] == max(cnt):
    print(cnt[i])

'''



'''test 3'''


# name=['Jacky']
# score=[90]
# for i in range(1):
#     print('{:2d},{:8s}:{:3d}'.format(i, name[i], score[i]))


'''
my_list = [s.lower() for s in 'Life is short, you need Python.'.split(' ')]
print(my_list)
print('short' in my_list)
print(my_list[5])
'''

