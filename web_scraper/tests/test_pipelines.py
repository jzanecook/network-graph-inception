```python
import unittest
import json
from web_scraper.pipelines import RedditScraperPipeline
from web_scraper.items import RedditItem

class TestPipelines(unittest.TestCase):

    def setUp(self):
        self.pipeline = RedditScraperPipeline()
        self.item = RedditItem()
        self.item['title'] = 'Test Title'
        self.item['url'] = 'https://www.reddit.com/r/test/'
        self.item['subreddit'] = 'test'
        self.item['upvotes'] = 1000

    def test_process_item(self):
        result = self.pipeline.process_item(self.item, None)
        self.assertEqual(result, self.item)

    def test_close_spider(self):
        self.pipeline.process_item(self.item, None)
        self.pipeline.close_spider(None)
        with open('reddit_data.json', 'r') as file:
            data = json.load(file)
            self.assertEqual(data[0]['title'], 'Test Title')
            self.assertEqual(data[0]['url'], 'https://www.reddit.com/r/test/')
            self.assertEqual(data[0]['subreddit'], 'test')
            self.assertEqual(data[0]['upvotes'], 1000)

if __name__ == '__main__':
    unittest.main()
```