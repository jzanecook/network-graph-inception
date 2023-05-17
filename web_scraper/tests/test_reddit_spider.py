```python
import unittest
from scrapy.http import Request, HtmlResponse
from web_scraper.spiders.reddit_spider import RedditSpider

class TestRedditSpider(unittest.TestCase):

    def setUp(self):
        self.spider = RedditSpider()

    def test_parse(self):
        url = 'http://www.reddit.com'
        request = Request(url=url)
        response = HtmlResponse(url=url, request=request)
        results = self.spider.parse(response)
        self.assertIsNotNone(results)

    def test_parse_item(self):
        url = 'http://www.reddit.com/r/test'
        request = Request(url=url)
        response = HtmlResponse(url=url, request=request)
        results = self.spider.parse_item(response)
        self.assertIsNotNone(results)

    def test_handle_pagination(self):
        url = 'http://www.reddit.com'
        request = Request(url=url)
        response = HtmlResponse(url=url, request=request)
        results = self.spider.handle_pagination(response)
        self.assertIsNotNone(results)

if __name__ == '__main__':
    unittest.main()
```