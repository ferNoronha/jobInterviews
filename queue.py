#queue with predetermined len
class Queue:
    def __init__(self,size):
        self.queue = [None]*size
        self.count = 0

    def push(self,elem):
        self.queue[self.size()] = elem 
        self.count += 1
    
    def size(self):
        return self.count
    
    def pop(self):
        i=0
        if self.size() == 0:
            return -1
        elem = self.queue[0]
        for i in range(0,self.size()-1):
            y=i+1
            self.queue[i] = self.queue[y]
        
        self.count -= 1
        return elem

    def print(self):
        aux = Queue(1000)
        while self.size() > 0:
            x = self.pop()
            print(x)
            aux.push(x)
        
        while aux.size()>0:
            self.push(aux.pop())
        #for i in range(0,self.size()):
        #    print(self.queue[i])


if __name__ == '__main__':
    fila = Queue(1000)
    #teste = []
    #teste[0] =0
    
    fila.push(10)
    fila.push(20)
    fila.push(20)
    fila.push(30)
    r = fila.pop()
    fila.push(6)
    fila.print()
