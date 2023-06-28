```python
import scrapy
from scrapy.loader import ItemLoader
from web_scraper.items import RedditItem

class RedditSpider(scrapy.Spider):
    name = 'reddit_spider'
    allowed_domains = ['www.reddit.com']
    start_urls = ['https://www.reddit.com/']

    def parse(self, response):
        for post in response.css('div.thing'):
            loader = ItemLoader(item=RedditItem(), selector=post)
            loader.add_css('title', 'a.title::text')
            loader.add_css('url', 'a.title::attr(href)')
            loader.add_css('upvotes', 'div.score.unvoted::attr(title)')
            yield loader.load_item()

        next_page = response.css('span.next-button a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
```