'''
n = eval(input("input a number"))
tmp = n
r = 0
m = 0
while n > 0:
        m = n % 10
        r = r * 10 + m
        n = n // 10
        print("m=",m)

print("input:{:d}\n output:{:d}".format(tmp,r))
'''
'''
num = eval(input("input a number"))
if num <= 2:
    print("num <= 2!")
else:
    print(num, "=", end="")
    while num > 1 :
        for i in range(2,num+1):
            if num % i == 0:
                num = num // i
                if num <= 1:
                    print(i,"\n")
                else:
                    print("{:d}*".format(i),end="")
                break

'''



while True:
    try:
        price = float(input("input price:"))
        num = int(input("input num:"))
        total = price * num
        print('total = ', total)
        break
    except Exception as err_msg:
        print('ljj:', err_msg)


