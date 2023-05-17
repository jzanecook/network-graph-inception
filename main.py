```python
from scrapy.crawler import CrawlerProcess
from web_scraper.spiders.reddit_spider import RedditSpider
from web_scraper.pipelines import JsonWriterPipeline
from visualization.graph_generator import GraphGenerator

def main():
    process = CrawlerProcess(settings={
        'ITEM_PIPELINES': {'web_scraper.pipelines.JsonWriterPipeline': 1},
    })

    process.crawl(RedditSpider)
    process.start()  # the script will block here until the crawling is finished

    graph_generator = GraphGenerator('output.json')
    graph_generator.generate_graph()

if __name__ == "__main__":
    main()
```