import networkx as nx

g = {
    0:[2],
    1:[0,2,7],
    2:[5,6],
    3:[0,4],
    4:[2],
    5:[10],
    6:[9,10],
    7:[8,9],
    8:[9],
    9:[11,12],
    10:[11],
    11:[],
    12:[]
}

G =nx.DiGraph(g)
print(G)

def topsort(G):
    N = G.number_of_nodes()
    V = [False] * N
    ordering = [0] * N
    i = N-1

    for at in range(N):
        if V[at] == False:
            visited_nodes =[]
            DFS(at, V, visited_nodes, G)
            for node_id in visited_nodes:
                ordering[i] = node_id
                i -= 1
    return ordering

def DFS(at, V, visited_nodes, G):

    V[at] = True
    edges = list(G.edges())
    for edge in edges:
        if(V[edge[1]]==False):
            DFS(edge[1], V, visited_nodes, G)

    visited_nodes.append(at)

print(list(G.edges()))
print(topsort(G))