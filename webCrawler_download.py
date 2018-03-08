
# coding: utf-8

# ### download image
# 下载图片方法与下载电影(mp4)、PDF的方法一致

# In[ ]:


import os
os.makedirs('./img/',exist_ok=True)

IMAGE_URL = "https://morvanzhou.github.io/static/img/description/learning_step_flowchart.png"


# ### downloadmethod_1:   urlretrieve

# In[ ]:


from urllib.request import urlretrieve
urlretrieve(IMAGE_URL,'./img/image1.png')


# ### downloadmethod_2: requests

# In[ ]:


import requests
r = requests.get(IMAGE_URL)
with open('./img/image2.png','wb') as f:
    f.write(r.content)                     #whole document


# ### downloadmethod_3: chunck
# 这种方法可以对文件分块下载，适合下载大文件，前面两种方法下载时，需要先将下载的部分文件存于内存中，当全部下载好后，再存于本地

# In[ ]:


r=requests.get(IMAGE_URL,stream=True)  #stream loading

with open('./img/image3.png','wb') as f:
    for chunk in r.iter_content(chunk_size=32):   #chunk_size为每次写入文件是32个字节
        f.write(chunk)

