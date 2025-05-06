n = 8
pq = []
g = {
    0:[(0,1,10),(0,2,1),(0,3,4)],
    1:[(1,0,10),(1,2,3),(1,4,0)],
    2:[(2,0,1),(2,1,3),(2,3,2),(2,5,8)],
    3:[(3,0,4),(3,2,2),(3,5,2),(3,6,7)],
    4:[(4,1,0),(4,5,1),(4,7,8)],
    5:[(5,2,8),(5,3,2),(5,4,1),(5,6,6)],
    6:[(6,3,7),(6,5,6),(6,7,12)],
    7:[(7,4,8),(7,5,9),(7,6,12)],
}
visited = [False] * n

def dequeue():
    min_obj = min(pq,key=lambda x: x[2])
    pq.remove(min_obj)
    return min_obj

def lazy_Prims(s=0):
    m = n-1
    edge_count = 0
    mst_cost = 0
    mst_edges = [None] * m

    add_edges(s)

    while(len(pq) != 0 and edge_count != m):
        edge = dequeue()
        node_index =edge[1] 

        if visited[node_index]:
            continue

        mst_edges[edge_count] = edge
        edge_count += 1
        mst_cost += edge[2]

        add_edges(node_index)

    if edge_count != m:
        return (None,None)

    return (mst_cost, mst_edges)

def add_edges(i):
    visited[i] = True
    edges = g[i]
    
    for edge in edges:
        if visited[edge[1]] == False:
            pq.append(edge)
        
print(lazy_Prims())