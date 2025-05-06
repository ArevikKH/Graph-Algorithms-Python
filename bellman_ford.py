import networkx as nx

g = {
    0:[(1,1),(2,1)],
    1:[(3,4)],
    2:[(1,1)],
    3:[(2,-6),(4,1),(5,1)],
    4:[(5,1),(6,1)],
    5:[(6,1)],
    6:[]
}

n = len(g)

G =nx.DiGraph(g)
print(G)
print(list(G.edges()))
# print(list(G.edges())[0][1][1])
# print(G[list(G.edges())[0][0]])
def bellman_ford(G,n,s):
    D = [100]*n
    D[s] = 0

    for i in range(n-1):
        for edge in list(G.edges()):
            if D[edge[0]] + edge[1][1] < D[edge[1][0]]:
                D[edge[1][0]] = D[edge[0]] + edge[1][1]

    for i in range(n-1):
        for edge in list(G.edges()):
            if D[edge[0]] + edge[1][1] < D[edge[1][0]]:
                D[edge[1][0]]=-1000

    return D


print(bellman_ford(G,n,0))

g1 = {
    0:[(1,5)],
    1:[(2,20),(5,30),(6,60)],
    2:[(3,10),(4,75)],
    3:[(2,-15)],
    4:[(9,100)],
    5:[(4,25),(6,5),(8,50)],
    6:[(7,-50)],
    7:[(8,-10)],
    8:[],
    9:[]
}
n1 = len(g1)

G1 =nx.DiGraph(g1)

print(bellman_ford(G1,n1,0))