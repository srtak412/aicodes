import heapq

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjList = {i: {} for i in range(vertices)}

    def add_edge(self, u, v, weight):
        self.adjList[u][v] = weight

    def dijkstra(self, start):
        distances = {node: float('inf') for node in range(self.vertices)}
        distances[start] = 0
        minH = [[0, start]]

        while minH:
            current_distance, current_node = heapq.heappop(minH)

            if current_distance > distances[current_node]:
                continue

            for neighbor, weight in self.adjList[current_node].items():
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(minH, [distance, neighbor])

        return distances


g = Graph(5)
g.add_edge(0, 1, 10)
g.add_edge(0, 2, 5)
g.add_edge(1, 2, 2)
g.add_edge(1, 3, 1)
g.add_edge(2, 1, 3)
g.add_edge(2, 3, 9)
g.add_edge(2, 4, 2)
g.add_edge(3, 4, 4)

start_node = 0
print("Shortest distances from node", start_node, "to other nodes:")
print(g.dijkstra(start_node))
