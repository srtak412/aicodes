import heapq

class Solution:
    def __init__(self, V):
        self.vertices = V
        self.adjList = {i: [] for i in range(V)}
        self.weights = [[float('inf')] * V for _ in range(V)]  
        
    def addEdge(self, source, dest, weight):
        self.adjList[source].append(dest)
        self.adjList[dest].append(source)
        self.weights[source][dest] = self.weights[dest][source] = weight 
    
    def prims(self):
        res = 0
        visit = set()
        minH = [[0, 0]]

        while len(visit) < self.vertices:
            cost, i = heapq.heappop(minH)
            
            if i in visit:
                continue

            res += cost
            visit.add(i)
            print(i)
            for nei in self.adjList[i]:
                if nei not in visit:
                    heapq.heappush(minH, [self.weights[i][nei], nei])

        return res


solution = Solution(5)

solution.addEdge(0, 1, 1)
solution.addEdge(0, 2, 9)
solution.addEdge(0, 3, 4)
solution.addEdge(0, 4, 7)
solution.addEdge(1, 2, 8)
solution.addEdge(1, 3, 3)
solution.addEdge(1, 4, 6)
solution.addEdge(2, 3, 6)
solution.addEdge(2, 4, 4)
solution.addEdge(3, 4, 5)

min_cost = solution.prims()
print(min_cost)
