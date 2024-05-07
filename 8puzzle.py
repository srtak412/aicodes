import heapq
import copy
N = 3

class Node:
    def __init__(self, mat, x, y, newX, newY, level, parent):
        self.mat = copy.deepcopy(mat)
        self.x = x
        self.y = y
        self.cost = float('inf')
        self.parent = parent
        self.level = level
        
    def __lt__(self, other):
        return (self.cost + self.level) < (other.cost + other.level)
        
def newNode(mat, x, y, newX, newY, level, parent):
    node = Node(mat, x, y, newX, newY, level, parent)
    node.mat[x][y], node.mat[newX][newY] = node.mat[newX][newY], node.mat[x][y]
    return node
    
def calculateCost(initial, final):
    cost = 0
    for i in range(N):
        for j in range(N):
            if initial[i][j] and initial[i][j] != final[i][j]:
                cost+=1
    return cost
    
def isSafe(x, y):
    return x >= 0 and x < N and y >= 0 and y < N
    
def printMatrix(mat):
    for i in range(N):
        for j in range(N):
            print(mat[i][j], end = " ")
        print()

row = [1, 0, -1, 0]
col = [0, -1, 0, 1]

   
def solve(initial, x, y, final):
    pq = []
    path = []
    root = newNode(initial, x, y, x, y, 0, None)
    root.cost = calculateCost(root.mat, final)
    heapq.heappush(pq, root)
    
    while pq:
        min_node = heapq.heappop(pq)
        path.append(copy.deepcopy(min_node.mat))
        
        if min_node.mat == final:
            for state in path:
                printMatrix(state)
                print()
            return
        
        for i in range(4):
            if isSafe(min_node.x + row[i], min_node.y + col[i]):
                child = newNode(min_node.mat, min_node.x, min_node.y, min_node.x + row[i], min_node.y + col[i], min_node.level+1, min_node)
                child.cost = calculateCost(child.mat, final)
                heapq.heappush(pq, child)
                printMatrix(child.mat)
                print()
                
initial = [
        [1, 2, 3],
        [0, 6, 5],
        [7, 8, 4]
    ]
    
final = [
        [1, 2, 3],
        [5, 8, 6],
        [7, 0, 4]
    ]
x, y = 1, 0

solve(initial, x, y, final)