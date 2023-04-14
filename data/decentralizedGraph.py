from collections import defaultdict

class DecentralizedGraph:
    def __init__(self, nodes):
        self.nodes = nodes
        self.graph = []
        self.edges = defaultdict(list)
        self.cost = [9999999] * nodes
        self.cost[0] = 0
        self.currentNode = 0
        self.nextNode = 0
        self.finished = False

    # Adds edges to the graph
    def addEdge(self, u, v, weight):
        self.graph.append([u, v, weight])
        self.edges[u].append([v, weight])
        self.edges[v].append([u, weight])

    def getEdge(self, source, destination):
        for edge in self.edges[source]:
            if edge[0] == destination:
                return edge[1]
            
    def getCost(self, node):
        return self.cost[node]

    def minPathFindIterative(self):

        if (self.nextNode == self.nodes - 1):
            self.nextNode = 0

        if self.nextNode == 0:
            minCostIndex = self.nextMinCostNode()
            self.visited[minCostIndex] = True
            self.currentNode = self.nextNode

        temp = self.nextNode

        for j in range(temp, self.nodes, 1):
            u = self.graph[j][0]
            v = self.graph[j][1]
            weight = self.graph[j][2]
            if self.cost[u] != 9999999 and self.cost[u] + weight < self.cost[v]:
                self.cost[v] = self.cost[u] + weight
                self.nextNode = j
                break
            else:
                self.nextNode = j

        # Relaxes all edges |V| - 1 times
        # for _ in range(self.nodes - 1):
        #     for u, v, weight in self.graph:
        #         if self.cost[u] != 9999999 and self.cost[u] + weight < self.cost[v]:
        #             self.cost[v] = self.cost[u] + weight


        # temp = 1
        # for i in self.visited:
        #     if i == False:
        #         temp = 0
        #         break

        # if temp == 1:
        #     self.finished = True

    def bellmanFord(self, src):
        # Initializes costance from src to all other vertices
        # All vertices start at infinity, while source is 0
        cost = [9999999] * self.nodes
        cost[src] = 0

        # Relaxes all edges |V| - 1 times
        for _ in range(self.nodes - 1): 
            for u, v, weight in self.graph:
                if cost[u] != 9999999 and cost[u] + weight < cost[v]:
                    cost[v] = cost[u] + weight

        # Checks for negative-weight cycles
        for u, v, weight in self.graph:
            if cost[u] != 9999999 and cost[u] + weight < cost[v]:
                print("Graph contains negative weight cycle")
                return
            
    def printEdges(self):
        for edge in self.graph:
            print(edge)
        print()

    def printGraph(self):
        # Prints the distances
        for i in range(self.nodes):
            print(f"Vertex {i}: distance from source = {self.cost[i]}")

if __name__ == "__main__":
    graph = DecentralizedGraph(5)

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

    graph.minPathFindIterative()
    graph.minPathFindIterative()
    graph.minPathFindIterative()
    graph.printGraph()
