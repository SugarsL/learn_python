import os

print(os.path)
with open('a.txt', 'r') as f:

    msg = f.read()
    #print(msg)
    l1 = msg.split('\n')
   # print(l1)

    for i in range(len(l1)):
        #print(l1[i])
        l2 = l1[i].split('/')
        #print(len(l2))
        path = 'patch'
        for j in range(len(l2)-1):
            path += l2[j]+'/'
        path = path[:-1]
        print(path)
        if path != '':
            os.makedirs(path, mode=0o777,exist_ok=True)
