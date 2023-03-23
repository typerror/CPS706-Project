class CentralizedGraph:
    def __init__(self, nodes):
        self.nodes = nodes
        self.edges = [[0 for _ in range(nodes)] for _ in range(nodes)]
        self.cost = [9999999] * nodes
        self.visited = [False] * nodes

    def addEdge(self, source, destination, cost):
        self.edges[source][destination] = cost

    def getEdge(self, source, destination):
        return self.edges[source][destination]

    def getCost(self, node):
        return self.cost[node]

    def getVisited(self, node):
        return self.visited[node]

    def nextMinCost(self):
        minIndex = 0
        min = 9999999

        for i in range(self.nodes):
            if self.cost[i] < min and self.visited[i] == False:
                min = self.cost[i]
                minIndex = i

        return minIndex

    def minPathFindIterative(self, source):
        self.cost[source] = 0

        minIndex = self.nextMinCost()
        self.visited[minIndex] = True

        for j in range(self.nodes):
            if self.edges[minIndex][j] != 0 and self.visited[j] == False and self.cost[j] > self.cost[minIndex] + self.edges[minIndex][j]:
                self.cost[j] = self.cost[minIndex] + self.edges[minIndex][j]

        self.printCost()

    def minPathFind(self, source):
        self.cost[source] = 0

        for _ in range(self.nodes):
            minIndex = self.nextMinCost()
            self.visited[minIndex] = True

            for j in range(self.nodes):
                if self.edges[minIndex][j] != 0 and self.visited[j] == False and self.cost[j] > self.cost[minIndex] + self.edges[minIndex][j]:
                    self.cost[j] = self.cost[minIndex] + \
                        self.edges[minIndex][j]

        self.printCost()

    def printEdges(self):
        for i in range(self.nodes):
            print(self.edges[i])
        print()

    def printCost(self):
        for node in range(self.nodes):
            print(node, " --- Cost:", self.cost[node])
        print()
