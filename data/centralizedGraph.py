class CentralizedGraph:
    def __init__(self, nodes):
        self.nodes = nodes
        self.edges = [[0 for _ in range(nodes)] for _ in range(nodes)]
        self.cost = [9999999] * nodes
        self.visited = [False] * nodes

    def getNumberOfNodes(self):
        return self.nodes

    def addEdge(self, source, destination, cost):
        self.edges[source][destination] = cost

    def getEdge(self, source, destination):
        return self.edges[source][destination]

    def getCost(self, node):
        return self.cost[node]

    def getVisited(self, node):
        return self.visited[node]

    def nextMinCostNode(self):
        minCostIndex = 0
        minCost = 9999999

        for i in range(self.nodes):
            if self.cost[i] < minCost and self.visited[i] == False:
                minCost = self.cost[i]
                minCostIndex = i

        return minCostIndex

    def minPathFindIterative(self, source):
        self.cost[source] = 0

        minCostIndex = self.nextMinCostNode()
        self.visited[minCostIndex] = True

        for j in range(self.nodes):
            if self.edges[minCostIndex][j] != 0 and self.visited[j] == False and self.cost[j] > self.cost[minCostIndex] + self.edges[minCostIndex][j]:
                self.cost[j] = self.cost[minCostIndex] + \
                    self.edges[minCostIndex][j]

        self.printCost()

    def minPathFind(self, source):
        self.cost[source] = 0

        for _ in range(self.nodes):
            minCostIndex = self.nextMinCostNode()
            self.visited[minCostIndex] = True

            for j in range(self.nodes):
                if self.edges[minCostIndex][j] != 0 and self.visited[j] == False and self.cost[j] > self.cost[minCostIndex] + self.edges[minCostIndex][j]:
                    self.cost[j] = self.cost[minCostIndex] + \
                        self.edges[minCostIndex][j]

        self.printCost()

    def printEdges(self):
        for i in range(self.nodes):
            print(self.edges[i])
        print()

    def printCost(self):
        for node in range(self.nodes):
            print(node, " --- Cost:", self.cost[node])
        print()
