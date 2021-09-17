import time
import  sys
import random
from heapq import heapify, heappush, heappop;

def tiles_out_of_place(dim, grid, target):
    counter = 0
    for i in range (dim):
        for j in range (dim):
            if (grid [i][j] != target [i][j]):
                counter += 1
    return counter

def manhattan (dim, grid, target):
    result = 0
    for i in range (dim):
        for j in range (dim):
            if (target [i][j] == 0):
                continue
            for l in range (dim):
                for m in range (dim):
                    if (target [i][j] == grid [l][m]):
                        result += (abs (m - j) + abs (l - i))
                        break
    return result

def sum_of_inverse_permutations(dim, grid, target):
    count = 0
    aux=0
    vector = []
    for i in range(dim):
        for j in range(dim):
            vector.append(grid[i][j])
            aux += 1
    for i in vector:
        for j in range(i,len(vector)):
            if(vector[i] > vector[j]):
                count += 1
    return count 

def poroto(dim, grid, target):
    counter = 0
    for i in range (dim):
        for j in range (dim):
            if (grid [i][j] == target [i][j]):
                counter += random.randint(0, 1)
    return counter

def getNextStates (dim, current):
    nextStates = []
    empty = None
    for i in range (dim):
        try:
            empty = current [i].index (0)
        except  Exception as e:
            continue
        empty = (i, empty)
        break
    if (empty[1] < (dim - 1)):
        a = [i.copy() for i in current]
        a[empty[0]] [empty[1]], a[empty[0]] [empty[1] + 1] = a[empty[0]] [empty[1] + 1], a[empty[0]] [empty[1]]
        nextStates.append(('RIGHT', a, (empty[0], empty[1] + 1)))
    if (empty [1] > 0):
        b = [i.copy() for i in current]
        b[empty[0]] [empty[1]], b[empty[0]] [empty[1] - 1] = b[empty[0]] [empty[1] - 1], b[empty[0]] [empty[1]]
        nextStates.append (('LEFT', b,(empty [0], empty[1] - 1)))
    if (empty[0] > 0):
        c = [i.copy() for i in current]
        c[empty[0]] [empty[1]], c[empty[0] - 1] [empty[1]] = c[empty[0] - 1] [empty[1]], c[empty[0]] [empty[1]]
        nextStates.append (('UP', c, (empty[0] - 1, empty[1])))
    if (empty[0] < (dim - 1)):
        d = [i.copy() for i in current]
        d[empty[0]] [empty[1]], d[empty[0] + 1] [empty[1]] = d[empty[0] + 1] [empty[1]], d[empty[0]] [empty[1]]
        nextStates.append (('DOWN', d, (empty[0] + 1, empty [1])))
    return nextStates

def getSequenceInfo(dim, grid):
    count = -1
    target = [[j for j in range(i, i + dim)] for i in range(0, (dim * (dim - 1)) + 1, dim)]
    nodeSize = sys.getsizeof(grid)
    initialTime = time.time()
    current = (tiles_out_of_place(dim, grid, target), 0, [], grid)
    stateTree = [current]
    heapify(stateTree)
    while(not current [-1] == target):
        current = heappop(stateTree)
        for state in getNextStates(dim, current [-1]):
            heappush(stateTree, (tiles_out_of_place(dim, state[1], target) + current[1] + 1, current[1] + 1, current[2] + [state[0]], state[1]))
            count += 1
    finalTime = time.time()
    print("Total search time elapsed : " + str(finalTime - initialTime)+" seconds")
    print ("Number of nodes :" + str(count))
    print ("Use of memory : "+ str(((nodeSize* count)/1024)/1024)+" MB")
    return current[1], current[2]

def getSequenceInfo2(dim, grid):
    count = -1
    target = [[j for j in range(i, i + dim)] for i in range(0, (dim * (dim - 1)) + 1, dim)]
    nodeSize = sys.getsizeof(grid)
    initialTime = time.time()
    current = (manhattan(dim, grid, target), 0, [], grid)
    stateTree = [current]
    heapify(stateTree)
    while(not current [-1] == target):
        current = heappop(stateTree)
        for state in getNextStates(dim, current [-1]):
            heappush(stateTree, (manhattan(dim, state[1], target) + current[1] + 1, current[1] + 1, current[2] + [state[0]], state[1]))
            count += 1
    finalTime = time.time()
    print("Total search time elapsed : " + str(finalTime - initialTime)+" seconds")
    print ("Number of nodes :" + str(count))
    print ("Use of memory : "+ str(((nodeSize* count)/1024)/1024)+" MB")
    return current[1], current[2]

def getSequenceInfo3(dim, grid):
    count = -1
    target = [[j for j in range(i, i + dim)] for i in range(0, (dim * (dim - 1)) + 1, dim)]
    nodeSize = sys.getsizeof(grid)
    initialTime = time.time()
    current = (sum_of_inverse_permutations(dim, grid, target), 0, [], grid)
    stateTree = [current]
    heapify(stateTree)
    while(not current [-1] == target):
        current = heappop(stateTree)
        for state in getNextStates(dim, current [-1]):
            heappush(stateTree, (sum_of_inverse_permutations(dim, state[1], target) + current[1] + 1, current[1] + 1, current[2] + [state[0]], state[1]))
            count += 1
    finalTime = time.time()
    print("Total search time elapsed :" + str(finalTime - initialTime)+" seconds")
    print ("Number of nodes :" + str(count))
    print ("Use of memory : "+ str(((nodeSize* count)/1024)/1024)+" MB")
    return current[1], current[2]

def getSequenceInfoPoroto(dim, grid):
    count = -1
    target = [[j for j in range(i, i + dim)] for i in range(0, (dim * (dim - 1)) + 1, dim)]
    nodeSize = sys.getsizeof(grid)
    initialTime = time.time()
    current = (poroto(dim, grid, target), 0, [], grid)
    stateTree = [current]
    heapify(stateTree)
    while(not current [-1] == target):
        current = heappop(stateTree)
        for state in getNextStates(dim, current [-1]):
            heappush(stateTree, (poroto(dim, state[1], target) + current[1] + 1, current[1] + 1, current[2] + [state[0]], state[1]))
            count += 1
    finalTime = time.time()
    print("Total search time elapsed :" + str(finalTime - initialTime)+" seconds")
    print ("Number of nodes :" + str(count))
    print ("Use of memory : "+ str(((nodeSize* count)/1024)/1024)+" MB")
    return current[1], current[2]

if (__name__ == '__main__'):
    print("Enter the size of the puzzle: ")
    dim = int (input ())
    row = numCount = 0
    print("Enter the elements: ")
    grid = [[] for i in range (dim)]

    for i in range (dim ** 2):
        grid [row].append (int (input ()))
        numCount += 1
        if (numCount % dim == 0):
            row += 1
            numCount = 0
    option = 0
    while(option != 5):
        print("1. Use the number of tiles out of place")
        print("2. Use the Manhattan distance")
        print("3. Use the sum of inverse permutations")
        print("4. Use all the heuristics")
        print("5. Poroto")
        option = input()
        if option == '1':
            print("- Tiles out of place -")
            seqCount, sequence = getSequenceInfo (dim, grid)
            print ("Step: "+ str(seqCount))
        if option == '2':
            print("- Manhattan Distance -")
            seqCount, sequence = getSequenceInfo2 (dim, grid)
            print ("Step: "+ str(seqCount))
        if option == '3':
            print("- Sum of inverse permutations - ")
            seqCount, sequence = getSequenceInfo3 (dim, grid)
            print ("Step: "+ str(seqCount))
        if option == '4':
            print("- Tiles out of place -")
            seqCount, sequence = getSequenceInfo (dim, grid)
            print ("Step: "+ str(seqCount))
            print("- Manhattan Distance -")
            seqCount, sequence = getSequenceInfo2 (dim, grid)
            print ("Step: "+ str(seqCount))
            print("- Sum of inverse permutations - ")
            seqCount, sequence = getSequenceInfo3 (dim, grid)
            print ("Step: "+ str(seqCount))
        if option == '5':
            print("- Poroto - ")
            seqCount, sequence = getSequenceInfoPoroto(dim, grid)
            print ("Step: "+ str(seqCount))

