
# coding: utf-8

# In[ ]:


from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

# if has Chinese, apply decode()
html=urlopen("file:///D:/Py_Workspace/webCrawler/webCrawler_3.html").read().decode('utf-8')
print(html)


# In[ ]:


soup=BeautifulSoup(html,features='lxml')

img_link=soup.find_all("img",{"src":re.compile('.*?\.jpg')})
for link in img_link:
    print(link["src"])


# In[ ]:


course_links=soup.find_all('a',{'href':re.compile('https://.*')})
for link in course_links:
    print(link["href"])

