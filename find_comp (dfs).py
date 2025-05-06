#number of nodes
n = 9
comp = [0,0,0,0,0,0,0,0,0]
count_ = 0
# adjacency list
g = {
    0:[2,3,4,6],
    1:[5],
    2:[0,3,6],
    3:[0,2],
    4:[0,6],
    5:[1,7,8],
    6:[0,2,4],
    7:[5],
    8:[5]
}

visited =[False,False,False,False,False,False,False,False,False]

def find_comp():
    global count_
    global visited
    for i in range(n):
        if(visited[i]==False):
            count_ += 1 
            DFS(i)
    return(count_,comp) 

def DFS(i):
    global count_
    global visited
    global comp
    visited[i]=True
    comp[i]=count_ 
    for j in g[i]:
        if(visited[j]==False):
            DFS(j)

print(find_comp())
