def solveNqueens(n):
    cols = set()
    positives = set()
    negatives = set()
    
    res = []
    board = [["."]*n for i in range(n)]
    
    def backtrack(r):
        if r == n:
            copy = ["".join(row) for row in board]
            res.append(copy)
            
        for c in range(n):
            if c in cols or (r+c) in positives or (r-c) in negatives:
                continue
            
            cols.add(c)
            positives.add(r+c)
            negatives.add(r-c)
            board[r][c] = "Q"
            
            backtrack(r+1)
            
            cols.remove(c)
            positives.remove(r+c)
            negatives.remove(r-c)
            board[r][c] = "."
            
    backtrack(0)
    return res
    
n = int(input("Enter board size: "))
results = solveNqueens(n)

for res in results:
    for row in res:
        print(row)
    print()