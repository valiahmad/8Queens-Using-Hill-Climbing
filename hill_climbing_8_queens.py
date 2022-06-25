from numpy.random import permutation
from random import randrange

nQueens = 8

def possibility(solution, i):

    row = solution[i] - 1
    col = i - 1
    while row >= 0 and col >= 0:
        if solution[col] == row:
            return False
        else:
            row = row - 1
            col -= 1

    row = solution[i] + 1
    col = i - 1
    while row < nQueens and col >= 0:
        if solution[col] == row:
            return False
        else:
            row = row + 1
            col -= 1
    
    return True
    


def evaluation(solution):

    cost = 0
    for i in range(0,nQueens):
        if not possibility(solution, i):
            cost += 1
            
    return cost

def activation(currentSol):

    newSol = list(currentSol)
    #cross
    firstPlace = randrange(nQueens)
    secondPlace = randrange(nQueens)
    newSol[firstPlace],newSol[secondPlace] = newSol[secondPlace],newSol[firstPlace]

    return newSol


def solve():

    #first step by chance
    currentSol = list(permutation(nQueens))
    newSol = currentSol
    newCost = int()
    bestSol = list()
    bestCost = 28
    i = 0
    changeSpace = 0
    while True:

        newCost = evaluation(newSol)
        if newCost < bestCost:
            bestCost = newCost
            bestSol = newSol
        if not bestCost or i == 100:
            if bestCost == 0 or changeSpace == 50:
                #print('i is : %d  and changeSpace is : %d \n'%(i,changeSpace))
                break
            else:
                i = 0
                changeSpace += 1
                bestSol = list(permutation(nQueens))


        currentSol = bestSol
        newSol = activation(currentSol)
        i += 1
        
    return bestSol

solution = solve()
print('solution : ',solution)
print('cost : ',evaluation(solution))
for i in range(0, nQueens):
    row = [0] * nQueens
    row[solution.index(i)] = 1
    print(*row, sep= '  ')