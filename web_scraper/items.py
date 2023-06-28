```python
from scrapy import Item, Field

class RedditItem(Item):
    title = Field()
    url = Field()
    comments = Field()
    upvotes = Field()
    subreddit = Field()
```