
# coding: utf-8

# ## 这个程序不要用jupyter notebook运行，会卡死陷入死循环，可以使用spyder或者pycharm运行

# In[ ]:


import multiprocessing as mp
import time
from urllib.request import urlopen,urljoin
from bs4 import BeautifulSoup
import re


base_url = 'https://morvanzhou.github.io/'

if base_url == "https://morvanzhou.github.io/" :
    restricted_crawl = True
else:
    restricted_crawl = False


# In[ ]:


def crawl(url):
    response = urlopen(url)
    return response.read().decode()


# In[ ]:


def parse(html):
    soup = BeautifulSoup(html,'lxml')
    urls = soup.find_all('a',{"href" : re.compile('^/.+?/$')})
    title = soup.find('h1').get_text().strip()
    page_urls = set([urljoin(base_url, url['href']) for url in urls])
    url = soup.find('meta',{'property':"og:url"})['content']
    return title,page_urls,url


# In[ ]:


def main():
    unseen = set([base_url,])
    seen = set()

    pool = mp.Pool()
    count,t1=1,time.time()

    while len(unseen)!=0:
        if restricted_crawl and len(seen) > 20:
            break

        print('\nDistributed Crawling...')
    #    crawl_jobs=[]
    #    for url in unseen:
    #        crawl_jobs.append(pool.apply_async(crawl, args=(url,)))
    #注释掉的这三句可由下面一句完成
        crawl_jobs = [pool.apply_async(crawl, args=(url,)) for url in unseen]
    #    for j in crawl_jobs:
    #        htmls = j.get()
    #同理上面这两句可由下面一句完成
        htmls = [j.get() for j in crawl_jobs]

        print('\nDistributed Parsing...')
        parse_jobs = [pool.apply_async(parse, args=(html,)) for html in htmls]
        results = [j.get() for j in parse_jobs]

        print('\nAnalysing...')
        seen.update(unseen)
        unseen.clear()

        for title,page_urls,url in results:
            print(count,':', title, url)
            count += 1
            unseen.update(page_urls - seen)
    print('Total time: %.1f s' % (time.time()-t1,))


if __name__ == '__main__':
    main()


# 下面我们不使用多核（多进程）进行数据的运算处理，看一下需要多长时间

# In[1]:


unseen = set([base_url,])
seen = set()

count, t1 = 1, time.time()

while len(unseen) != 0:                 
    if restricted_crawl and len(seen) > 20:
            break
        
    print('\nDistributed Crawling...')
    htmls = [crawl(url) for url in unseen]

    print('\nDistributed Parsing...')
    results = [parse(html) for html in htmls]

    print('\nAnalysing...')
    seen.update(unseen)         
    unseen.clear()             

    for title, page_urls, url in results:
        print(count, title, url)
        count += 1
        unseen.update(page_urls - seen)    
print('Total time: %.1f s' % (time.time()-t1, ))   


# 经过对比可以看到，使用多核的确可以加速运算
