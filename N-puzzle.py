from heapq import heapify, heappush, heappop;

def hamming (dim, grid, target):
    counter = 0
    for i in range (dim):
        for j in range (dim):
            if (not (grid [i][j] == target [i][j] or grid [i][j] == 0)):
                counter += 1
    return counter

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

def getSequenceInfo(dim, grid):
    count = -1
    target = [[j for j in range(i, i + dim)] for i in range(0, (dim * (dim - 1)) + 1, dim)]
    current = (sum_of_inverse_permutations(dim, grid, target), 0, [], grid)
    stateTree = [current]
    heapify(stateTree)
    while(not current [-1] == target):
        current = heappop(stateTree)
        for state in getNextStates(dim, current [-1]):
            heappush(stateTree, (sum_of_inverse_permutations(dim, state[1], target) + current[1] + 1, current[1] + 1, current[2] + [state[0]], state[1]))
            count += 1
    print ("numero de nodos")
    print (count)
    return current[1], current[2]



if (__name__ == '__main__'):
	dim = int (input ())
	row = numCount = 0
	grid = [[] for i in range (dim)]

	for i in range (dim ** 2):
		grid [row].append (int (input ()))
		numCount += 1

		if (numCount % dim == 0):
			row += 1
			numCount = 0

	seqCount, sequence = getSequenceInfo (dim, grid)
	print (seqCount)
	#print ('\n'.join (sequence))