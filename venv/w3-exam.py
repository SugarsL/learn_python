'''
pattern = 'abcdefghijklmnopqrstuvwxyz'

def countchar(string):
    r = [0]*26
    for c in string:
        if c.lower() in pattern:
            r[ord(c.lower())-ord('a')] += 1

    return r

if __name__ == "__main__":
    string = input()
    print(countchar(string))
'''




''''''


def pandigital(nums):
    lst = []
    for i in nums:
        s = str(i)
        sum1 = 0
        sum2 = 0
        for j in range(len(s)):
            sum1 = sum1 + j + 1
            sum2 = sum2 + int(s[j])
        if sum1 == sum2:
            lst.append(i)

    return lst


if __name__ == "__main__":
    lst = pandigital(eval(input()))
    if len(lst) == 0:
        print("not found")
    else:
        for i in lst:
            print(i)


