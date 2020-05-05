import random


#binary search in recursive and iterative mode
#link for search: https://www.geeksforgeeks.org/binary-search/
# 0 1 2 3 4 5 6 7 8 9
#[1,2,3,4,5,6,7,8,9,10]

def recursiveBinarySearch(sortList,element,last,first):
    half = int((last+first)/2)
    if element == sortList[half]:
        return half
    elif element>sortList[half] and first<last:
        return recursiveBinarySearch(sortList,element,last,half+1)
    elif element<sortList[half] and first<last:
        return recursiveBinarySearch(sortList,element,half,first)
    return -1

def binarySearch(sortList,element):
    last = len(sortList)-1
    first = 0
    half = int(last/2)
    while element != sortList[half] and first < last:
        if element>sortList[half]:
            first = half+1
        else:
            last = half
        half = int((last+first)/2)
    
    if element == sortList[half]:
        return half
    else:
        return -1
    

if __name__ == '__main__':
    List = random.sample(range(1, 200), 100)
    List = sorted(List)
    print(List)
    
    findElement = random.randint(0,200)
    print(findElement)
    index = binarySearch(List,findElement)
    print(index)
    print('------------')
    index = recursiveBinarySearch(List,findElement,len(List)-1,0)
    print(index)

