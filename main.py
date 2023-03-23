from data.centralizedGraph import CentralizedGraph
from data.decentralizedGraph import DecentralizedGraph

graph = CentralizedGraph(5)
graph.addEdge(0, 1, 10)
graph.addEdge(0, 2, 5)
graph.addEdge(1, 3, 1)
graph.addEdge(1, 2, 2)
graph.addEdge(2, 1, 3)
graph.addEdge(2, 3, 9)
graph.addEdge(2, 4, 2)
graph.addEdge(3, 4, 4)
graph.addEdge(4, 3, 6)
graph.addEdge(4, 0, 7)
graph.printEdges()
# graph.minPathFind(0)

# graph.minPathFindIterative(0)
# graph.minPathFindIterative(0)
# graph.minPathFindIterative(0)
# graph.minPathFindIterative(0)

graph2 = DecentralizedGraph(["A", "B", "C", "D"])
graph2.add_edge("A", "B", 1)
graph2.add_edge("B", "C", 2)
graph2.add_edge("B", "D", 3)
graph2.printCostFromNode("D")
