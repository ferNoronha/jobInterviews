#busca em largura
from collections import defaultdict #another method
from queue import Queue

class graph:

    def __init__(self,nV):
        self.graph = [[] for i in range(nV)]
        self.num = [-1 for i in range(nV)]
        self.count=0


    def print(self):
        string = ''
        for i in self.graph:
            for j in i:
                string += str(j) + '|'
            string+='\n'
        print(string)

    def aresta(self,x,y):
        self.graph[x].append(y)



def bfs(gr,start):
    # se existir start
    queue = Queue(7)
    print(gr.num)
    queue.push(start)
    gr.num[start] = gr.count
    gr.count+=1
    while not queue.isEmpty():
        elem = queue.pop()
        print(elem)
        allV = gr.graph[elem]
        for i in allV:
            if gr.num[i] == -1:
                gr.num[i] = gr.count
                gr.count+=1
                queue.push(i)
            




if __name__ == '__main__':
    #(0,1),(0,2),(1,0),(2,1),(2,3),(2,5),(3,5),(3,6),(3,4),(4,6),(4,5),(4,3),(5,3)
    g = graph(7)
    g.aresta(0,2)
    g.aresta(0,3)
    g.aresta(0,4)
    g.aresta(2,4)
    g.aresta(3,4)
    g.aresta(3,5)
    g.aresta(4,5)
    g.aresta(5,1)
    '''g.aresta(0,1)
    g.aresta(0,2)
    g.aresta(1,0)
    g.aresta(2,1)
    g.aresta(2,3)
    g.aresta(2,5)
    g.aresta(3,5)
    g.aresta(3,6)
    g.aresta(3,4)
    g.aresta(4,6)
    g.aresta(4,5)
    g.aresta(4,3)
    g.aresta(5,3)'''
    
    g.print()
    bfs(g,0)




