import unittest
import sys
from io import StringIO
from decentralizedGraph import DecentralizedGraph


class TestDecentralizedGraph(unittest.TestCase):
    def test_init(self):
        graph = DecentralizedGraph(["A", "B", "C"])
        self.assertEqual(graph.nodes, ["A", "B", "C"])
        self.assertEqual(graph.graph, {"A": {}, "B": {}, "C": {}})

    def test_add_edge(self):
        graph = DecentralizedGraph(["A", "B", "C"])
        graph.add_edge("A", "B", 1)
        self.assertEqual(graph.graph, {"A": {"B": 1}, "B": {"A": 1}, "C": {}})

    def test_printEdges(self):
        graph = DecentralizedGraph(["A", "B", "C"])
        graph.add_edge("A", "B", 1)
        graph.add_edge("B", "C", 2)
        old_stdout = sys.stdout
        sys.stdout = fake_out = StringIO()
        graph.printEdges()
        sys.stdout = old_stdout
        self.assertEqual(fake_out.getvalue().strip(), "A: B(1)\nB: A(1), C(2)\nC: B(2)")

    def test_distance_vector(self):
        graph = DecentralizedGraph(["A", "B", "C", "D"])
        graph.add_edge("A", "B", 1)
        graph.add_edge("B", "C", 1)
        graph.add_edge("C", "D", 1)
        next_node = graph.distance_vector("A")
        self.assertEqual(next_node["A"], None)
        self.assertEqual(next_node["B"], "A")
        self.assertEqual(next_node["C"], "B")
        self.assertEqual(next_node["D"], "C")

    def test_printCostFromNode(self):
        graph = DecentralizedGraph(["A", "B", "C"])
        graph.add_edge("A", "B", 1)
        graph.add_edge("B", "C", 2)

        old_stdout = sys.stdout
        sys.stdout = fake_out = StringIO()
        graph.printCostFromNode("A")
        sys.stdout = old_stdout

        self.assertEqual(fake_out.getvalue().strip(), "Costs from A:\nA:0 , B:1 , C:3")


if __name__ == "__main__":
    unittest.main()
