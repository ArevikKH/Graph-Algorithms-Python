class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return "Queue is empty"

R, C = 5, 7
m = [
    ['S', '.', '.', '#', '.', '.', '.'],
    ['.', '#','.', '.', '.','#', '.'],
    ['.', '#','.', '.', '.','.', '.'],
    ['.', '.','#', '#', '.','.', '.'],
    ['#', '.','#', 'E', '.','#', '.']
]
sr, sc = (0,0)
rq, cq = Queue(), Queue()

move_count = 0
nodes_left_in_layer = 1
nodes_in_next_layer = 0

reached_end = False

visited = [[False for _ in range(C)] for _ in range(R)]

dr = [-1, +1, 0, 0]
dc = [0, 0, +1, -1]

def solve():

    global move_count, nodes_left_in_layer, nodes_in_next_layer

    rq.enqueue(sr)
    cq.enqueue(sc)

    visited[sr][sc] = True

    while rq.is_empty() == False:
        r = rq.dequeue()
        c = cq.dequeue()

        if m[r][c] == 'E':
            reached_end = True
            break

        explore_neighbours(r,c)

        nodes_left_in_layer -= 1

        if nodes_left_in_layer == 0:
            nodes_left_in_layer = nodes_in_next_layer
            nodes_in_next_layer = 0
            move_count += 1
            
    if reached_end:
        return move_count
    return -1

def explore_neighbours(r,c):

    global nodes_in_next_layer

    for i in range(4):
        rr = r + dr[i]
        cc = c + dc[i]

        if rr < 0 or cc < 0:
            continue
        if rr >= R or cc >= C:
            continue

        if visited[rr][cc]:
            continue
        if m[rr][cc] == "#":
            continue

        rq.enqueue(rr)
        cq.enqueue(cc)
        visited[rr][cc] = True
        nodes_in_next_layer += 1

print(solve())