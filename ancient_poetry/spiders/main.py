import os
import sys

from scrapy.cmdline import execute

if __name__ == '__main__':
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    # 执行爬虫程序
    execute(['scrapy', 'crawl', 'poems_spider'])

