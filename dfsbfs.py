from collections import deque

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjList = [[]*vertices for i in range(vertices)]
        
    def addEdge(self, src, dest):
        self.adjList[src].append(dest)
        self.adjList[dest].append(src)
        
    def BFS(self, start, key):
        visited = [False] * self.vertices
        q = deque()
        path = []
        
        q.append(start)
        visited[start] = True
        path.append(start)
        
        while q:
            v = q.popleft()
            
            for node in self.adjList[v]:
                if not visited[node]:
                    visited[node] = True
                    path.append(node)
                    q.append(node)
                    
                    if node == key:
                        print(path)
                        return True
        return False
        
    def recursiveDFS(self, source, visited, key, path):
        path.append(source)
        if source == key:
            print("Traversal path:", *path)
            return True
        visited[source] = True
        for node in self.adjList[source]:
            if not visited[node] and self.recursiveDFS(node, visited, key, path):
                return True
        path.pop()
        return False
        
vertices = 6
graph = Graph(vertices)

graph.addEdge(0, 1)
graph.addEdge(0, 2)
graph.addEdge(1, 3)
graph.addEdge(1, 4)
graph.addEdge(2, 4)
graph.addEdge(3, 5)
graph.addEdge(4, 5)

start = 0
key = 5

graph.BFS(start, key)        
        
                    
            
            
            
