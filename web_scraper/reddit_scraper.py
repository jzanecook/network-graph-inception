```python
import scrapy
from scrapy.crawler import CrawlerProcess
from .spiders.reddit_spider import RedditSpider
from .items import RedditItem

class RedditScraper:

    def __init__(self):
        self.process = CrawlerProcess(settings={
            'FEED_FORMAT': 'json',
            'FEED_URI': 'result.json'
        })

    def run_spider(self, subreddit):
        self.process.crawl(RedditSpider, subreddit=subreddit)
        self.process.start()

if __name__ == "__main__":
    scraper = RedditScraper()
    scraper.run_spider('python')
```