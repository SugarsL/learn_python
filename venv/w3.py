import requests
import os
from bs4 import BeautifulSoup
import re
'''
rr = requests.get(r"https://www.baidu.com/img/bd_logo1.png")
f = open(r'/Users/lingjiajun/home/baidu-logo.png','wb')
f.write(rr.content)

f.close()

'''

book = requests.get(r"https://book.douban.com/subject/30278164/comments/")
soup = BeautifulSoup(book.text,'lxml')

# 网页源码部分内容截取如下：
# <p class="comment-content">
#   <span class="short">已经不爱了，一点都不爱了，这种情况下怎么办才好呢？也许应该和你分开，也许还有别的办法。时间是有限的，人是会后悔的动物，这些我应该都懂，却对身边最亲近的人缺乏诚意，这是怎么回事呢？</span>
# </p>

comments = soup.find_all('span','short')
for i in comments:
    print(i.string)


# 评分语段部分内容结构如下：
# <span class="user-stars allstar30 rating" title="还行"></span>
score = re.compile("user-stars allstar(.*?) rating")

ss = re.findall(score,book.text)
sum=0
for j in ss:
    sum += int(j)

print(sum)
