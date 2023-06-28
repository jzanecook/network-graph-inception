```python
import unittest
from pyvis.network import Network
from web_scraper.visualization.graph import NetworkGraph

class TestNetworkGraph(unittest.TestCase):

    def setUp(self):
        self.network_graph = NetworkGraph()

    def test_add_node(self):
        self.network_graph.add_node("test_node")
        self.assertIn("test_node", self.network_graph.graph.nodes)

    def test_add_edge(self):
        self.network_graph.add_node("node1")
        self.network_graph.add_node("node2")
        self.network_graph.add_edge("node1", "node2")
        self.assertIn(("node1", "node2"), self.network_graph.graph.edges)

    def test_visualize(self):
        self.network_graph.add_node("node1")
        self.network_graph.add_node("node2")
        self.network_graph.add_edge("node1", "node2")
        self.network_graph.visualize("test_graph.html")
        self.assertTrue(os.path.exists("test_graph.html"))

if __name__ == "__main__":
    unittest.main()
```