```python
import json
from reddit_scraper import scrape_reddit
from network_graph import create_network_graph

def main():
    # Scrape data from Reddit
    scraped_data = scrape_reddit()
    
    # Save scraped data to JSON file
    with open('data/scraped_data.json', 'w') as f:
        json.dump(scraped_data, f)
    
    # Load scraped data from JSON file
    with open('data/scraped_data.json', 'r') as f:
        data = json.load(f)
    
    # Create network graph from scraped data
    create_network_graph(data)

if __name__ == "__main__":
    main()
```