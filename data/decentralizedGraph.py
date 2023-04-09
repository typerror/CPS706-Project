from collections import defaultdict

class DecentralizedGraph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = []
        self.edges = defaultdict(list)

    # Adds edges to the graph
    def add_edge(self, u, v, weight):
        self.graph.append([u, v, weight])
        self.edges[u].append([v, weight])
        self.edges[v].append([u, weight])

    def bellmanFord(self, src):
        # Initializes distance from src to all other vertices
        # All vertices start at infinity, while source is 0
        dist = [float("Inf")] * self.vertices
        dist[src] = 0

        # Relaxes all edges |V| - 1 times
        for _ in range(self.vertices - 1):
            for u, v, weight in self.graph:
                if dist[u] != float("Inf") and dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight

        # Checks for negative-weight cycles
        for u, v, weight in self.graph:
            if dist[u] != float("Inf") and dist[u] + weight < dist[v]:
                print("Graph contains negative weight cycle")
                return

        # Prints the distances
        for i in range(self.vertices):
            print(f"Vertex {i}: distance from source = {dist[i]}")
            
 
if __name__ == "__main__":
    g = DecentralizedGraph(5)
    g.add_edge(0, 1, -1)
    g.add_edge(0, 2, 4)
    g.add_edge(1, 2, 3)
    g.add_edge(1, 3, 2)
    g.add_edge(1, 4, 2)
    g.add_edge(3, 2, 5)
    g.add_edge(3, 1, 1)
    g.add_edge(4, 3, -3)

    g.bellman_ford(0)

