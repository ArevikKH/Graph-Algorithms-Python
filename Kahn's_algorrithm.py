g = {
    0:[2, 3],
    1:[4],
    2:[6],
    3:[1,4],
    4:[5,8],
    5:[],
    6:[7,11],
    7:[4,12],
    8:[],
    9:[2,10],
    10:[6],
    11:[12],
    12:[8],
    13:[]
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

def find_topological_ordering(g):
    n = len(g)
    in_degree = [0]*n

    for i in g:
        for to in g[i]:
            in_degree[to] += 1
    
    q = Queue()

    for i in g:
        if in_degree[i] == 0:
            q.enqueue(i)

    index = 0
    order = []

    while q.is_empty() == False:
        at = q.dequeue()
        order.append(at)
        index += 1

        for to in g[at]:
            in_degree[to] -= 1

            if in_degree[to] == 0:
                q.enqueue(to)
    
    if index != n:
        return None
    
    return order

print(find_topological_ordering(g))