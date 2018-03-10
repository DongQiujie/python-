
# coding: utf-8

# ### selenium是一个高级库
# 可以完成像人一样的点击网页链接的动作，而普通的爬取工作无法点击
# 
# selenium是python的一个包，可以自行安装上。
# 
# 要操控浏览器, 就要有浏览器的 driver. Selenium 针对几个主流的浏览器都有 driver：http://selenium-python.readthedocs.io/installation.html#downloading-python-bindings-for-selenium
# Linux 和 MacOS 用户下载好之后, 请将下载好的”geckodriver”文件放在你的计算机的 “/usr/bin” 或 “/usr/local/bin” 目录. 并赋予执行权限,Win用户将下载的文件解压，然后将获得的exe文件放到与python的目录下，或者是将你存放exe文件的位置加入到PATH路径里。
# 
# Selenium with Python：http://selenium-python.readthedocs.io/ 介绍许多selenium的使用方法

# In[ ]:


import os 
from selenium import webdriver

os.makedirs('./img/', exist_ok = True)

driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')
driver.find_element_by_link_text(u"新闻").click()
driver.find_element_by_link_text(u"习近平参加重庆代表团审议").click()

html = driver.page_source
driver.get_screenshot_as_file('./img/sreenshot1.png')
driver.close()
print(html[ :200])


# 如果我们想浏览器运行界面在后台，而不显示出来，那么只需要对driver加入参数即可。

# In[ ]:


from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')

driver = webdriver.Chrome(chrome_options = chrome_options)
driver.get('https://www.baidu.com/')
driver.find_element_by_link_text(u"新闻").click()
driver.find_element_by_link_text(u"习近平参加重庆代表团审议").click()

html = driver.page_source
driver.get_screenshot_as_file('./img/sreenshot2.png')
driver.close()
print(html[ :200])

