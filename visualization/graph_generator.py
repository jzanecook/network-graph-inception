```python
import json
from pyvis.network import Network

class GraphGenerator:
    def __init__(self, json_file):
        self.json_file = json_file
        self.graph = Network()

    def load_data(self):
        with open(self.json_file, 'r') as file:
            self.data = json.load(file)

    def generate_graph(self):
        for item in self.data:
            self.graph.add_node(item['id'], label=item['title'])
            for comment in item['comments']:
                self.graph.add_node(comment['id'], label=comment['content'])
                self.graph.add_edge(item['id'], comment['id'])

    def show_graph(self):
        self.graph.show("reddit_network.html")

if __name__ == "__main__":
    graph_generator = GraphGenerator('web_scraper/reddit_data.json')
    graph_generator.load_data()
    graph_generator.generate_graph()
    graph_generator.show_graph()
```