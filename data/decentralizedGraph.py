class DecentralizedGraph:
    def __init__(self, nodes):
        """
        Initializes a new instance of the DecentralizedGraph class.

        :param nodes: A list of node names.
        """
        self.nodes = nodes
        self.graph = {node: {} for node in nodes}

    def add_edge(self, u, v, w):
        """
        Adds an edge between two nodes with a specified weight.

        :param u: The name of the first node.
        :param v: The name of the second node.
        :param w: The weight of the edge.
        """
        self.graph[u][v] = w
        self.graph[v][u] = w

    def distance_vector(self, src):
        """
        Calculates the least-cost paths from a specific source node to all other nodes using the distance-vector algorithm.

        :param src: The name of the source node.

        :return: A dictionary containing the next node on the least-cost path from src to all other nodes.
                The keys are destination nodes and values are names of next nodes on least-cost path from src to destination.

                For example:

                {
                    'A': None,
                    'B': 'A',
                    'C': 'B'
                }

                This indicates that:

                - From src to itself there is no next node (None).
                - From src to B there is a direct link (next_node['B'] == 'A').
                - From src to C there is a link through B (next_node['C'] == 'B').

                And so on for all other destination nodes.
        """

        # Initialize dictionaries to store distances and next nodes
        dist = {n: float("inf") for n in self.nodes}
        next_node = {n: None for n in self.nodes}

        # Calculate least-cost paths using Bellman-Ford equation
        dist[src] = 0
        for i in range(len(self.nodes) - 1):
            for u in self.graph:
                for v in self.graph[u]:
                    if dist[v] > dist[u] + self.graph[u][v]:
                        dist[v] = dist[u] + self.graph[u][v]
                        next_node[v] = u

        return next_node

    def printEdges(self):
        """
        Prints all edges and their weights.
        """
        # Iterate over all edges sorted by their source and destination nodes
        for u in sorted(self.graph.keys()):
            print("{}: ".format(u), end="")
            edges = []
            # Append formatted string with edge information to list
            for v in sorted(self.graph[u].keys()):
                edges.append("{}({})".format(v, self.graph[u][v]))
            print(", ".join(edges))

    def printCostFromNode(self, src):
        """
        Prints costs from specific source node to every destination.

        Output format:

            Costs from A:
            A: 0, B: 1, C: 3

        This indicates that cost from source (A) to itself is 0,
        cost from source (A) to B is 1,
        cost from source (A) to C is 3,
        etc.

        :param src: The name of the source node.
        """

        # Calculate least-cost paths using distance-vector algorithm
        next_node = self.distance_vector(src)

        # Print costs header
        print("Costs from {}:".format(src))

        costs = []

        # Iterate over all destinations sorted by their names
        for dest in sorted(next_node.keys()):
            # Calculate cost by summing up weights along path from src to dest
            cost = 0
            current_node = dest
            while current_node != src:
                prev_node = next_node[current_node]
                cost += self.graph[current_node][prev_node]
                current_node = prev_node

            costs.append("{}:{} ".format(dest, cost))

        print(", ".join(costs))
