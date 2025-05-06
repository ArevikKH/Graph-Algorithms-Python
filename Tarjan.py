class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return "pop from an empty stack"

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return "peek from an empty stack"

    def size(self):
        return len(self.items)

UNVISITED = -1
n = 8
g ={
    0 : [1],
    1 : [2],
    2 : [0],
    3 : [4, 7],
    4 : [5],
    5 : [0, 6],
    6 : [0, 2, 4],
    7 : [3, 5]
}

id = 0
sccCount = 0

ids = [-1] * n
low = [0] * n
onStack = [False] * n
stack = Stack()

def findSccs():
    for i in range(n):
        if(ids[i] == UNVISITED):
            dfs(i)
    return low
    
def dfs(at):
    global id
    stack.push(at)
    onStack[at] = True
    ids[at] = low[at] = id+1
    id += 1
    
    for to in g[at]:
        if ids[to] == UNVISITED:
            dfs(to)
        if onStack[to]:
            low[at] = min(low[at], low[to])

    if ids[at] == low[at]:
        while True:
            node = stack.pop()
            onStack[node] = False
            low[node] = ids[at]
            if node == at:
                break
        global sccCount
        sccCount += 1

findSccs()
print("Number of strongly connected components:", sccCount)    
    
    