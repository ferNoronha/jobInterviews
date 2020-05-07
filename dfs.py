#busca em profundidade

class Graph:

    def __init__(self,nV):
        self.graph = [[] for i in range(nV)]
        self.num = [-1 for i in range(nV)]
        self.count = 0
        self.nV = nV
    
    def aresta(self,x,y):
        self.graph[x].append(y)

def dfs(graph):
    for i in range(graph.nV):
        if graph.num[i] == -1:
            dfsRec(graph,i)

def dfsRec(graph,vertex):
    print(vertex)
    graph.num[vertex] = graph.count
    graph.count += 1
    for i in graph.graph[vertex]:
        if graph.num[i] == -1:
            dfsRec(graph,i)




if __name__=='__main__':
    g = Graph(6)
    g.aresta(0,1)
    g.aresta(1,2)
    g.aresta(1,3)
    g.aresta(2,4)
    g.aresta(2,5)
    dfs(g)


