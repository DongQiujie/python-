
# coding: utf-8

# ### 加速爬虫：异步加载 Asyncio
# 这个原理时通过以通过单线程，可以减少等待时间

# 首先，我们先对Asyncio进行一个了解：
# 在不使用Asyncio时，我们使用单线程运行两次job函数

# In[ ]:


import time 

def job(t):
    print('Start job : ',t)
    time.sleep(t)
    print('Job',t ,'takes', t ,'s')
    
def main():
    [job(t) for t in range(1,3)]

t_start = time.time()
main()
print('No async total time :' , time.time() - t_start)


# 下面使用Asyncio运行两次job

# In[ ]:


import asyncio

async def job(t):
    print('Start job : ',t)
    await asyncio.sleep(t)
    print('Job',t,'takes',t,'s')

async def main(loop):
    tasks = [loop.create_task(job(t)) for t in range(1,3)]
    await asyncio.wait(tasks)                #等待所有的task完成

#   测试一下await asyncio.wait(tasks)语句的返回值是什么
#   finished, unfinished = await asyncio.wait(tasks)        
#   print(finished, unfinished)
#   通过运行我们发现，此句返回的是我们已经运行的job的信息的集合（set）——finished，
#       与没有运行的job的集合（set）——unfinished
#   在finished中我们可以获取已经运行的job的返回结果（result）
    
t_start = time.time()
loop = asyncio.get_event_loop()
loop.run_until_complete(main(loop))
#loop.close()
print('Asyncio total time :',time.time() - t_start)


# 由上面的运行结果可以看到，Asyncio的确可以加速程序的运行
# 
# 下面我们开始爬取网页，不使用异步加载情况如下,我们只使用简单的request

# In[ ]:


import requests

URL = 'https://morvanzhou.github.io/'

def normal():
    for i in range(2):    #只爬取两次
        r = requests.get(URL)
        url = r.url
        print(url)

t_start = time.time()
normal()
print('Normal total time :', time.time() - t_start)


# 在对网页进行异步加载时，我们使用的时基于Asyncio开发的专门针对网页设计的库aiohttp

# In[ ]:


import aiohttp

async def job(session):
    response = await session.get(URL)
    return str(response.url)

async def main(loop):
    async with aiohttp.ClientSession() as session:
        tasks = [loop.create_task(job(session)) for _ in range(2)] #这里的意思是，我们要进行两次
        finished, unfinished = await asyncio.wait(tasks)
        all_result = [r.result() for r in finished]
        print(all_result)
        
t_start = time.time()
loop = asyncio.get_event_loop()
loop.run_until_complete(main(loop))
#loop.close()
print('Asyncio total time :', time.time() - t_start)


# 下面我们同时使用asyncio 与 multiprocessing 会进一步加快程序运行

# In[ ]:


import aiohttp
import asyncio
import time
import re
import multiprocessing as mp
from bs4 import BeautifulSoup
from urllib.request import urljoin

base_url = 'https://morvanzhou.github.io/"'

if base_url == 'https://morvanzhou.github.io/':
    restricted_crawl = True
else:
    restricted_crawl = False

unseen = set([base_url,])
seen = set()

def parse(html):
    soup = BeautifulSoup(html,'lxml')
    urls = soup.find_all('a', {'href': re.compile('^/.+?/$')})
    title = soup.find('h1').get_text().strip()
    page_url = set([urljoin(base_url, url['href']) for url in urls])
    url = soup.find('meta',{'property':'og:url'})['content']
    return title,page_url,url

async def crawl(url, session):
    r = await session.get(url)
    html = await r.text()
    return html

async def main(loop):
    pool = mp.Pool()
    async with aiohttp.ClientSession() as session:
        count = 1
        while len(unseen) !=0:
            print('\nAsync Crawling...')
            tasks = [loop.create_task(crawl(url,session)) for url in unseen]
            finished, unfinished = await asyncio.wait(tasks)
            htmls = [f.result() for f in finished]
            
            print('\nDistributed Prasing...')
            parse_job = [pool.apply_async(parse, args=(html,)) for html in htmls]
            results = [p.get() for p in parse_job]
            
            print('\nAnalysing...')
            seen.update(unseen)
            unseen.clear()
            for title,page_url,url in results:
                print(count, title,':',url)
                unseen.update(page_url - seen)
                count += 1
                
if __name__ == '__main__':
    t_start = time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop))
    loop.close()
    print('Total time : ', time.time() - t_start)

