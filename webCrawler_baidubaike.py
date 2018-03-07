
# coding: utf-8

# In[ ]:


from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import random

base_url="https://baike.baidu.com"
his=["/item/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB/5162711"]
url=base_url+his[-1]

html=urlopen(url).read().decode('utf-8')
soup=BeautifulSoup(html,features='lxml')

h1=soup.find('h1')
print(h1.get_text(),'   url:',his[-1])


# In[ ]:


#find valid urls
sub_urls=soup.find_all("a",{"target":"_blank","href":re.compile("/item/(%.{2})+$")})

if len(sub_urls)!=0:
    his.append(random.sample(sub_urls,1)[0]['href'])
else:
    #no valid sub link found
    his.pop()
print(his)


# 下面这是一个整合的程序，可以爬取20次

# In[ ]:


from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import random

base_url="https://baike.baidu.com"
his=["/item/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB/5162711"]

for i in range(20):
    url=base_url+his[-1]

    html=urlopen(url).read().decode('utf-8')
    soup=BeautifulSoup(html,features='lxml')

    h1=soup.find('h1')
    print(i,":",h1.get_text(),'      url:',his[-1])
    #find valid urls
    sub_urls=soup.find_all("a",{"target":"_blank","href":re.compile("/item/(%.{2})+$")})

    if len(sub_urls)!=0:
        his.append(random.sample(sub_urls,1)[0]['href'])
    else:
        #no valid sub link found
        his.pop()

