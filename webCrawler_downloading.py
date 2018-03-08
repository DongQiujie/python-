
# coding: utf-8

# ### downloading

# In[ ]:


from bs4 import BeautifulSoup
import requests

URL="http://www.nationalgeographic.com.cn/animals/"


# ### find list of image holder

# In[ ]:


html = requests.get(URL).text
soup = BeautifulSoup(html,'lxml')
img_ul = soup.find_all('ul',{"class":"img_list"})


# ### Create a folder for these pictures

# In[ ]:


import os

os.makedirs('./img/',exist_ok=True)


# ### download

# In[ ]:


for ul in img_ul:
    imgs = ul.find_all('img')
    for img in imgs:
        url = img['src']
        r = requests.get(url,stream=True)
        image_name = url.split('/')[-1]
        with open('./img/%s' % image_name, 'wb') as f:
            for chunk in r.iter_content(chunk_size=128):
                f.write(chunk)
        print('Save %s' % image_name)

