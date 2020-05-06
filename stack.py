class Stack:
    def __init__(self,size):
        self.stack = [None]*size
        self.count = 0
    
    def size(self):
        return self.count

    def isEmpyt(self):
        if self.size() == 0:
            return True
        return False
    
    def push(self,elem):
        self.stack[self.size()] = elem
        self.count += 1
    
    def pop(self):
        if self.size() == 0:
            return -1
        elem = self.stack[self.size()-1]
        self.count -= 1
        return elem
    
    def print(self):
        aux = Stack(1000)
        while self.size() > 0:
            x = self.pop()
            print(x)
            aux.push(x)
        
        while aux.size()>0:
            self.push(aux.pop())

        #for i in range(self.size()-1,-1,-1):
        #    print(self.stack[i])



if __name__ == '__main__':
    pilha = Stack(1000)
    pilha.push(10)
    pilha.push(11)
    x = pilha.pop()
    x = pilha.push(12)
    
    pilha.print()
    #print(pilha.size())