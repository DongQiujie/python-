
# coding: utf-8

# ### get类型的网页

# In[ ]:


import requests
import webbrowser

param={"wd":"莫烦python"}
r = requests.get('http://www.baidu.com/s',params=param)
print(r.url)
webbrowser.open(r.url)


# ### post类型的网页：测试网站  http://pythonscraping.com/pages/files/form.html

# In[ ]:


data = {'firstname':'董','lastname':'秋杰'}

r=requests.post('http://pythonscraping.com/pages/files/processing.php',data=data)
print(r.text)


# ### upload image by post:  模拟上传图片的网站 http://pythonscraping.com/files/form2.html

# In[ ]:


file = {'uploadFile':open('./image.png','rb')}
r=requests.post('http://pythonscraping.com/files/processing2.php',files=file)
print(r.text)


# ### login:  测试网站  http://pythonscraping.com/pages/cookies/login.html
# 网站登录过程是一个连续的过程，而python处理信息进行返回不是一个连续的过程，所以使用cookies来用python获取网站的连续信息

# In[ ]:


payload = {'username':'qiujie','password':'password'}
r=requests.post('http://pythonscraping.com/pages/cookies/welcome.php',data=payload)
print(r.cookies.get_dict())
r = requests.get('http://pythonscraping.com/pages/cookies/profile.php',cookies=r.cookies)

print(r.text)


# ### another general way to login  
# 为了方便处理这种登陆的连续信息，程序员使用了session来控制cookies的传递，而不是将coolies放入代码中

# In[ ]:


session = requests.session()
payload = {'username':'qiujie','password':'password'}
r=session.post('http://pythonscraping.com/pages/cookies/welcome.php',data=payload)
print(r.cookies.get_dict())
r = session.get('http://pythonscraping.com/pages/cookies/profile.php')

print(r.text)

