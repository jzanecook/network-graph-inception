```python
import scrapy
from scrapy.crawler import CrawlerProcess
from utils import handle_pagination, handle_dynamic_content, REDDIT_URL

class RedditSpider(scrapy.Spider):
    name = "reddit_scraper"
    start_urls = [REDDIT_URL]

    def parse(self, response):
        for post in response.css('div.thing'):
            yield {
                'title': post.css('p.title a::text').get(),
                'url': post.css('p.title a::attr(href)').get(),
                'upvotes': post.css('div.score.unvoted::attr(title)').get(),
                'comments': post.css('a.comments::text').get(),
            }

        next_page = handle_pagination(response)
        if next_page is not None:
            yield response.follow(next_page, self.parse)

def scrape_reddit():
    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
        'FEED_FORMAT': 'json',
        'FEED_URI': 'data/scraped_data.json'
    })

    process.crawl(RedditSpider)
    process.start()  # the script will block here until the crawling is finished
```
