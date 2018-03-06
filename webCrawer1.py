
# coding: utf-8

# In[ ]:


from urllib.request import urlopen

#if  the web has chinese ，then we should apply decode
html=urlopen("file:///D:/Py_Workspace/webCrawler/webCrawler1.html").read().decode('utf-8')
print(html)


# In[ ]:


import re
res_1=re.findall(r"<title>(.+?)</title>",html)
print("\nThe webCrawler's title is:",res_1[0])


# In[ ]:


res_2=re.findall(r"<p>(.*?)</p>",html,flags=re.DOTALL)
print("\nThe webCrawler's paragraph is:",res_2[0])


# In[ ]:


res_3=re.findall(r'href="(.*?)"',html)
print("\nThe webcrawler's all links:",res_3)

