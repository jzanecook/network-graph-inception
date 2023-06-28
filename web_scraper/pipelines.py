```python
import json
from scrapy.exporters import JsonItemExporter
from .items import RedditItem

class JsonWriterPipeline(object):

    def open_spider(self, spider):
        self.file = open('reddit_data.jl', 'w')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        if isinstance(item, RedditItem):
            line = json.dumps(dict(item)) + "\n"
            self.file.write(line)
        return item
```