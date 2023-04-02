class CentralizedGraph:
    """
    Represents a graph with centralized control.

    :param int nodes: Number of nodes in the graph.

    :ivar int nodes: Number of nodes in the graph.
    :ivar list edges: List of edges in the graph.
    :ivar list cost: List of costs of each node from source.
    :ivar list visited: List of booleans indicating whether a node has been visited or not.
    """

    def __init__(self, nodes):
        """
        Initializes a new instance of the CentralizedGraph class.

        :param int nodes: Number of nodes in the graph.
        """

        self.nodes = nodes
        self.edges = [[0 for _ in range(nodes)] for _ in range(nodes)]
        self.cost = [9999999] * nodes
        self.visited = [False] * nodes

    def getNumberOfNodes(self):
        """
        Returns the number of nodes in the graph.

        :return: Number of nodes in the graph.
        :rtype: int
        """

        return self.nodes

    def addEdge(self, source, destination, cost):
        """
        Adds an edge to the graph.

        :param int source: Source node of the edge.
        :param int destination: Destination node of the edge.
        :param int cost: Cost of the edge.
        """

        self.edges[source][destination] = cost
        self.edges[destination][source] = cost

    def getEdge(self, source, destination):
        """
        Returns the cost of the edge between the source and destination nodes.

        :param int source: Source node of the edge.
        :param int destination: Destination node of the edge.
        :return: Cost of the edge.
        :rtype: int
        """

        return self.edges[source][destination]

    def getCost(self, node):
        """
        Returns the cost of the node.

        :param int node: Node to get the cost from.
        :return: Cost of the node.
        :rtype: int
        """

        return self.cost[node]

    def getVisited(self, node):
        """
        Returns whether the node has been visited or not.

        :param int node: Node to check if it has been visited.
        :return: True if the node has been visited, False otherwise.
        :rtype: bool
        """

        return self.visited[node]

    def nextMinCostNode(self):
        """
        Returns the index of the next node with the minimum cost.

        :return: Index of the next node with the minimum cost.
        :rtype: int
        """

        minCostIndex = -1
        minCost = 9999999

        for i in range(self.nodes):
            if minCost > self.cost[i] and self.visited[i] == False:
                minCost = self.cost[i]
                minCostIndex = i

        return minCostIndex

    def minPathFindIterative(self, source):
        """
        Finds the minimum path from the source node to all other nodes in the graph using dijkstras shortest path algorithm.
        *Performs the algorithm iteratively in order to show the intermediate steps*

        :param int source: Source node.
        """

        self.cost[source] = 0

        minCostIndex = self.nextMinCostNode()
        self.visited[minCostIndex] = True

        for j in range(self.nodes):
            if self.edges[minCostIndex][j] != 0 and self.visited[j] == False and (self.cost[j] > self.cost[minCostIndex] + self.edges[minCostIndex][j]):
                self.cost[j] = self.cost[minCostIndex] + \
                    self.edges[minCostIndex][j]

        self.printCost()

    def minPathFind(self, source):
        """
        Finds the minimum path from the source node to all other nodes in the graph using dijkstras shortest path algorithm.

        :param int source: Source node.
        """

        self.cost[source] = 0

        for _ in range(self.nodes):
            minCostIndex = self.nextMinCostNode()
            self.visited[minCostIndex] = True

            for j in range(self.nodes):
                if self.edges[minCostIndex][j] != 0 and self.visited[j] == False and (self.cost[j] > self.cost[minCostIndex] + self.edges[minCostIndex][j]):
                    self.cost[j] = self.cost[minCostIndex] + \
                        self.edges[minCostIndex][j]

        self.printCost()

    def printEdges(self):
        """
        Prints all edges of the graph and their costs.
        """

        for i in range(self.nodes):
            print(self.edges[i])
        print()

    def printCost(self):
        """
        Prints the cost of each node from source.

        Output format:
            0  --- Cost: 0
            1  --- Cost: 2
            2  --- Cost: 1

        This indicates that cost from source (0) to itself is 0,
        cost from source (0) to 1 is 2,
        cost from source (0) to 2 is 1,
        etc.
        """

        for node in range(self.nodes):
            print(node, " --- Cost:", self.cost[node])
        print()
