'''
import pandas as pd

music_data = [("the rolling stones", "Satisfaction"),
              ("Beatles", "Let It Be"),
              ("Guns N' Roses", "Don't Cry"),
              ("Metallica", "Nothing Else Matters")]

m = pd.DataFrame(music_data, index=range(1,5), columns=['singers', 'song_name'])

print(m)
'''

'''
def find_person(dict_users, strU):
    if strU in dict_users.keys():
        return dict_users[strU]
    else:
        return 'Not Found'


if __name__ == "__main__":
    dict_users = {'xiaoyun':88888,'xiaohong':5555555,'xiaoteng':11111,'xiaoyi':12341234,'xiaoyang':1212121}
    strU = input()
    print(find_person(dict_users, strU))

'''


def countfeq(s):
    tmp_list = s.lower().split(' ')
    res = {}
    for i in tmp_list:
        if i[-1] in ',.':
            j = i[0:-1]
        else:
            j = i

        if j in res.keys():
            res[j] += 1
        else:
            res[j] = 1
    return res


if __name__ == "__main__":
    s = "Not clumsy person in this world, only lazy people, only people can not hold out until the last."
    s_dict = countfeq(s.lower())
    word = input()
    if word in s_dict.keys():
        print(s_dict[word])
    else:
        print(0)
#    基于s_dict判断word的词频并输出（可能是0次）


