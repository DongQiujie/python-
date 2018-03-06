
# coding: utf-8

# In[ ]:


from bs4 import BeautifulSoup
from urllib.request import urlopen

# if has Chinese, apply decode()
html=urlopen("file:///D:/Py_Workspace/webCrawler/webCrawler1.html").read().decode('utf-8')
print(html)


# In[ ]:


soup=BeautifulSoup(html,features='lxml')
print(soup.h1)
print('\n',soup.p)


# In[ ]:


#提取所有带a标签的单元。存入all_href
all_href=soup.find_all('a')
print(all_href)
print('\n------------\n')
#在提取的每个带a的单元中，寻找单元中的关键字href，即可提取出每个单元的link
for l in all_href:
    print(l['href'])
print('\n------------\n')
all_href=[l['href']for l in all_href]
print('\n',all_href)

