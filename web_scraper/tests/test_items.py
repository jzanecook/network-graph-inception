```python
import unittest
from web_scraper.items import RedditItem

class TestRedditItem(unittest.TestCase):

    def setUp(self):
        self.item = RedditItem()

    def test_fields(self):
        self.assertEqual(set(self.item.fields.keys()), {'title', 'url', 'subreddit', 'upvotes', 'comments'})

    def test_set_and_get_item(self):
        self.item['title'] = 'Test Title'
        self.item['url'] = 'https://www.reddit.com/test'
        self.item['subreddit'] = 'r/test'
        self.item['upvotes'] = 100
        self.item['comments'] = 20

        self.assertEqual(self.item['title'], 'Test Title')
        self.assertEqual(self.item['url'], 'https://www.reddit.com/test')
        self.assertEqual(self.item['subreddit'], 'r/test')
        self.assertEqual(self.item['upvotes'], 100)
        self.assertEqual(self.item['comments'], 20)

if __name__ == '__main__':
    unittest.main()
```