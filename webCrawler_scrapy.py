
# coding: utf-8

# ### 爬虫高级库
# 
# scrapy的官网中文文档：https://scrapy-chs.readthedocs.io/zh_CN/0.24/

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
#上面这句是运行此脚本的命令，需在terminal里进行运行，scrapy runspider 是运行命令，webCrawler_scrapy是运行的文件名，-o是输出命令
#将程序运行结果输出到res.json文件中

#注意：运行此程序时，只需要将python的Scripts加入环境变量即可（不然会出现scrapy不是内部命令的提示），当然，如果你把python的路径也加入了也不会有影响

