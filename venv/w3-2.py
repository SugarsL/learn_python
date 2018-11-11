'''test 1'''
'''
from bs4 import BeautifulSoup
import re
import requests

cnt = 0
comment_cnt = 0
score = []
for i in range(3):
    str = "https://movie.douban.com/subject/1300374/comments?start={:}&limit=20&sort=time&status=P".format(i*20)
    book = requests.get("https://movie.douban.com/subject/1300374/comments?start=20&limit=20&sort=time&status=P")
    soup = BeautifulSoup(book.text,'lxml')
    comment = soup.find_all('span','short')

    for j in comment:
        print(j)
        comment_cnt+=1
        if comment_cnt >= 50:
            break

    stars= re.compile('allstar(.*?) rating')
    res = re.findall(stars,book.text)
    for k in res:
        score.append(int(k))
        cnt += 1
        if cnt >= 50:
            break


print('avg score = {:.2f}'.format(sum(score)/50))
#print(comment_cnt)
#print(score)
#print(cnt)
'''

'''test 2'''

from bs4 import BeautifulSoup
import requests

msg = requests.get('https://money.cnn.com/data/dow30/')
msg_soup = BeautifulSoup(msg.text, 'lxml')
#title = msg_soup.find_all('span', '')
#print(title)

print(msg_soup)





