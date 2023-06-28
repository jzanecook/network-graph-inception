```python
import unittest
from scrapy.http import Request, HtmlResponse
from web_scraper.spiders.reddit_spider import RedditSpider

class TestRedditSpider(unittest.TestCase):

    def setUp(self):
        self.spider = RedditSpider()

    def _test_item_results(self, results, expected_length):
        count = 0
        permalinks = set()
        for item in results:
            count += 1
            self.assertIsNotNone(item['title'])
            self.assertIsNotNone(item['url'])
            self.assertIsNotNone(item['upvotes'])
            self.assertIsNotNone(item['comments'])
            self.assertNotIn(item['url'], permalinks)
            permalinks.add(item['url'])
        self.assertEqual(count, expected_length)

    def test_parse(self):
        url = 'http://www.reddit.com'
        request = Request(url=url)
        response = HtmlResponse(url=url, request=request)
        results = self.spider.parse(response)
        self._test_item_results(results, 25)

if __name__ == '__main__':
    unittest.main()
```