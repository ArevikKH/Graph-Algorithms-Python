#number of nodes
n = 13
# adjacency list
g = {
    0:[7,9,11],
    1:[8,10],
    2:[3,12],
    3:[2,4,7],
    4:[3],
    5:[6],
    6:[5,7],
    7:[0,3,6],
    8:[1,9,12],
    9:[0,8,10],
    10:[1,9],
    11:[0,7],
    12:[2,8]
}


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

    def size(self):
        return len(self.items)


def bfs(s,e):

    prev = solve(s)

    return reconstructPath(s,e,prev)

def solve(s):
    global n
    q = Queue()
    q.enqueue(s)

    visited = [False]*n
    visited[s] = True

    prev = [None]*n

    while q.is_empty() == False:
        node = q.dequeue()
        neighbours = g.get(node)

        for next in neighbours:
            if visited[next] == False:
                q.enqueue(next)
                visited[next] = True
                prev[next] = node
    return prev

def reconstructPath(s,e,prev):
    path = []
    at = e
    while at is not None:
        path.append(at)
        at = prev[at]
    
    path.reverse()

    if path[0] == s:
        return path

    return []

print(bfs(0,12))



