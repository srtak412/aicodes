import copy
from heapq import heappush, heappop

n = 3  

rows = [1, 0, -1, 0]
cols = [0, -1, 0, 1]


class Nodes:

    def __init__(self, parent, mats, empty_tile_posi, costs, levels):
        self.parent = parent
        self.mats = mats
        self.empty_tile_posi = empty_tile_posi
        self.costs = costs
        self.levels = levels

    def __lt__(self, nxt):
        return self.costs < nxt.costs


def calculate_costs(mats, final) -> int:
    count = 0
    for i in range(n):
        for j in range(n):
            if mats[i][j] and mats[i][j] != final[i][j]:
                count += 1
    return count


def new_nodes(mats, empty_tile_posi, new_empty_tile_posi, levels, parent, final) -> Nodes:
    new_mats = copy.deepcopy(mats)

    # Moving the tile by 1 position
    x1 = empty_tile_posi[0]
    y1 = empty_tile_posi[1]
    x2 = new_empty_tile_posi[0]
    y2 = new_empty_tile_posi[1]
    new_mats[x1][y1], new_mats[x2][y2] = new_mats[x2][y2], new_mats[x1][y1]

    costs = calculate_costs(new_mats, final)

    new_nodes = Nodes(parent, new_mats, new_empty_tile_posi, costs, levels)
    return new_nodes


def print_matrix(mats):
    for i in range(n):
        for j in range(n):
            print("%d " % (mats[i][j]), end=" ")
        print()


def is_safe(x, y):
    return 0 <= x < n and 0 <= y < n


def print_path(root):
    if root is None:
        return
    print_path(root.parent)
    print_matrix(root.mats)
    print()


def solve(initial, empty_tile_posi, final):

    heap = []

    costs = calculate_costs(initial, final)
    root = Nodes(None, initial, empty_tile_posi, costs, 0)
    heappush(heap, root)

    while heap:
        minimum = heappop(heap)

        if minimum.costs == 0:
            print_path(minimum)
            return

        for i in range(n):
            new_tile_posi = [minimum.empty_tile_posi[0] + rows[i], minimum.empty_tile_posi[1] + cols[i]]
            if is_safe(new_tile_posi[0], new_tile_posi[1]):

                child = new_nodes(minimum.mats,
                                  minimum.empty_tile_posi,
                                  new_tile_posi,
                                  minimum.levels + 1,
                                  minimum, final)
                heappush(heap, child)


initial = [[1, 2, 3],
           [5, 6, 0],
           [7, 8, 4]]

final = [[1, 2, 3],
         [5, 8, 6],
         [0, 7, 4]]

empty_tile_posi = [1, 2]
solve(initial, empty_tile_posi, final)
