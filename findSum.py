import random

# Give an S element, find the first 2 elements in a list where the sum is the same as S, return True or false and +
# + the index's
# Ex: S = 8
# list = [1, 2, 4, 4]
# 4 + 4 = 8 so, result = True, index 2 and index 3
# Ex2: S= 8
# list = [1,2,3,9]
# result = False, index -1 and index -1


#return bool, index 0 and index 1 
def find(S, randomlist):
    sumlist = []
    sumlist.append(S-randomlist[0])
    for index,val in enumerate(randomlist):
        if index > 0:
            if val in sumlist:
                return (True,sumlist.index(val),index)
            else:
                sumlist.append(S-val)
    
    return (False,-1,-1)


if __name__ == '__main__':
    randomlist = random.sample(range(0,100),100)
    S=random.randint(0,200)
    print('list:',randomlist)
    result,ix0,ix1 = find(S,randomlist)
    print('sum:',S)
    print('result',result)
    print('index 0:',ix0)
    print('index 1:',ix1)
