```python
from scrapy import Item, Field

class RedditItem(Item):
    # define the fields for your item here like:
    title = Field()
    url = Field()
    subreddit = Field()
    upvotes = Field()
    comments = Field()
    created_at = Field()
```