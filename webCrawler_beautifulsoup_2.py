
# coding: utf-8

# In[ ]:


from bs4 import BeautifulSoup
from urllib.request import urlopen

# if has Chinese, apply decode()
html=urlopen("file:///D:/Py_Workspace/webCrawler/webCrawler2.html").read().decode('utf-8')
print(html)


# In[ ]:


soup=BeautifulSoup(html,features='lxml')
month=soup.find_all('li',{'class':'month'})
for m in month:
    print(m.get_text())


# In[ ]:


jan=soup.find('ul',{"class":"jan"})
day_jan=jan.find_all('li')
for d in day_jan:
    print(d.get_text())

