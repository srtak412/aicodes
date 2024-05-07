class Solution:
    
    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = []
        
    def addEdge(self, src, dst, wt):
        self.edges.append((wt, src, dst))
        
    def find(self, parent, v):
        if parent[v] == -1:
            return v
        parent[v] = self.find(parent, parent[v])
        return parent[v]
        
    def union(self, parent, rank, fromP, toP):
        fromP_root = self.find(parent, fromP)
        toP_root = self.find(parent, toP)
        
        if rank[fromP_root] > rank[toP_root]:
            parent[toP_root] = fromP_root
            
        elif rank[toP_root] > rank[fromP_root]:
            parent[fromP_root] = toP_root
            
        else:
            parent[fromP_root] = toP_root
            rank[toP_root] += 1
            
    def kruskals(self):
        parent = [-1] * self.vertices
        rank = [0] * self.vertices
        
        mst = []
        
        self.edges.sort()
        
        for wt, src, dest in self.edges:
            fromP = self.find(parent, src)
            toP = self.find(parent, dest)
            
            if fromP != toP:
                mst.append((src, dest, wt))
                self.union(parent, rank, fromP, toP)
                
        return mst
        
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

min_spanning_tree = solution.kruskals()
print("Minimum Spanning Tree (src, dst, wt):", min_spanning_tree)