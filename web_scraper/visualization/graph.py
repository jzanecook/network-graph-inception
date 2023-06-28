```python
from pyvis.network import Network

class NetworkGraph:
    def __init__(self, data):
        self.data = data
        self.graph = Network(height="750px", width="100%", bgcolor="#222222", font_color="white")

    def create_graph(self):
        nodes = []
        edges = []

        for item in self.data:
            if item['parent'] not in nodes:
                nodes.append(item['parent'])
            if item['child'] not in nodes:
                nodes.append(item['child'])
            edges.append((item['parent'], item['child']))

        for node in nodes:
            self.graph.add_node(node)

        for edge in edges:
            self.graph.add_edge(edge[0], edge[1])

        return self.graph

    def show_graph(self):
        self.graph.show("reddit_network.html")
```