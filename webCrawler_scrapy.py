
# coding: utf-8

# ### 爬虫高级库
# 
# scrapy的官网中文文档：https://scrapy-chs.readthedocs.io/zh_CN/0.24/
#运行此程序时，只需要将python的Scripts加入环境变量即可，当然，如果你把python的路径也加入了也不会有影响

# In[ ]:


import scrapy

class MofanSpider(scrapy.Spider):
    name = 'crawler'
    start_urls = [ 'https://morvanzhou.github.io/', ]
    
    def parse(self , response):
        yield{
            'title':response.css('h1::text').extract_first(default = 'Missing').strip().replace('"',''),
            'url':response.url,
        }
    
		urls = response.css('a::attr(href)').re(r'^/.+?/$')  #找到当前页面所有的网址
		for url in urls:
			yield response.follow(url, callback = self.parse) #继续进行运行，callback后面的是指示跳到哪个函数
        
# lastly, run this in terminal
# scrapy runspider webCrawler_scrapy.py -o res.json

