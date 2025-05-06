g = {
    0:[(1,4),(2,1)],
    1:[(3,1)],
    2:[(1,2),(3,5)],
    3:[(4,3)],
    4:[]
}

n = len(g)

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


def dijkstra(g,n,s):
    vis = [False]*n
    dist = [100]*n
    dist[s] = 0
    pq = Queue()
    pq.enqueue((s,0))

    while pq.is_empty() == False:
        index, min_value = pq.dequeue()
        if dist[index] < min_value:
            continue
        vis[index] = True
        for edge in g[index]:
            new_dict = dist[index]+edge[1]
            if new_dict < dist[edge[0]]:
                dist[edge[0]] = new_dict
                pq.enqueue((edge[0],new_dict))

    return dist

print(dijkstra(g,n,0))

