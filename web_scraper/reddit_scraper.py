```python
import scrapy
from scrapy.crawler import CrawlerProcess
from web_scraper.spiders.reddit_spider import RedditSpider
from web_scraper.visualization.graph import NetworkGraph

class RedditScraper:
    def __init__(self):
        self.process = CrawlerProcess(settings={
            'ITEM_PIPELINES': {'web_scraper.pipelines.JsonWriterPipeline': 1},
        })

    def scrape_reddit(self, subreddit):
        self.process.crawl(RedditSpider, subreddit=subreddit)
        self.process.start()  # the script will block here until the crawling is finished

    def visualize_data(self, json_file):
        graph = NetworkGraph(json_file)
        graph.create_graph()

if __name__ == "__main__":
    scraper = RedditScraper()
    scraper.scrape_reddit('python')
    scraper.visualize_data('output.json')
```