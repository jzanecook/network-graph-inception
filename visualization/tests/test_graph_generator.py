```python
import unittest
from pyvis.network import Network
from visualization.graph_generator import GraphGenerator

class TestGraphGenerator(unittest.TestCase):

    def setUp(self):
        self.graph_generator = GraphGenerator()
        self.network = Network()

    def test_add_node(self):
        self.graph_generator.add_node(self.network, 'test_node')
        self.assertIn('test_node', self.network.nodes)

    def test_add_edge(self):
        self.graph_generator.add_node(self.network, 'node1')
        self.graph_generator.add_node(self.network, 'node2')
        self.graph_generator.add_edge(self.network, 'node1', 'node2')
        self.assertIn(('node1', 'node2'), self.network.edges)

    def test_generate_graph(self):
        data = {'node1': ['node2', 'node3'], 'node2': ['node3']}
        self.graph_generator.generate_graph(data)
        self.assertIn('node1', self.network.nodes)
        self.assertIn('node2', self.network.nodes)
        self.assertIn('node3', self.network.nodes)
        self.assertIn(('node1', 'node2'), self.network.edges)
        self.assertIn(('node1', 'node3'), self.network.edges)
        self.assertIn(('node2', 'node3'), self.network.edges)

if __name__ == '__main__':
    unittest.main()
```