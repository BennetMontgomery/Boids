#allows me to recreate the output file without manually deleting it every time
import os

# creates the environment, prints the initial state, and returns it
def generateLife(inputFile, outputFile):
    dimensions = getFileSize(inputFile)# finds the size of the environment in the target file
    lines = filter(None, (line.rstrip() for line in open(inputFile)))# gets the lines with no blank lines
    arr = []
    i = 0
    for line in lines:# creates an array for every line
        arr.append([])
        for j in range(len(line)):# adds the 0s and 1s individually to each array created by the lines
            arr[i].append(line[j])
        i += 1
    printOutput(arr, outputFile, 0)# prints the initial state
    return arr

# returns the dimensions of the environment in the file
def getFileSize(file):
    f = open(file, "r")
    x = 0
    y = 0
    for line in f:# increases for the number of lines
        x += 1
        y = len(line)# increases for the size of the lines
    return [x,y]

# simulates the start and continuation of the algorithm
def simulateLife(inputFile, gens, outputFile):
    environment = generateLife(inputFile, outputFile)# handles initial creation of the environment
    i = 1
    indeces_to_change = []# initializes an array that tracks what indeces are born or die
    while i < gens:
        indeces_to_change = []# resets so that it is recalculated every turn
        for j in range(len(environment)):
            for k in range(len(environment[0])):# for every cell in the 2d array
                neighbors = getNeighborCount((j, k), environment)# find the number of neighbors
                if environment[j][k] == '1' and (1 >= neighbors or neighbors >= 4):# kill a cell for overcrowding/loneliness
                    indeces_to_change.append((j,k))# mark the cell to be changed so it doesnt influence this step
                if environment[j][k] == '0' and neighbors == 3:# make a child in a threesome
                    indeces_to_change.append([j, k])# mark the cell to be changed so it doesnt influence this step
        environment = changeStates(environment, indeces_to_change)# change all the cells once all change is determined
        printOutput(environment, outputFile, i)# print the environment at the current generation
        i += 1

#finds the number of neighbors to a cell taking the environment and current position
def getNeighborCount(pos, environment):
    neighbors = 0
    rows = len(environment)
    cols = len(environment[0])
    for j in range(max(0, pos[0] - 1), min(rows, pos[0] + 2)):# checks surrounding rows without going out of bounds
        for k in range(max(0, pos[1] - 1), min(cols, pos[1] + 2)):# checks surrounding columns without going out of bounds
            if (j, k) != pos and environment[j][k] == '1':# if the neighboring cell is alive
                neighbors += 1# increment the amount of neighbors the cell has
    return neighbors

# changes all the states of cells that were marked to change. Prevents cell changes effecting other cell changes in the same generation.
def changeStates(arr, indeces):
    for index in indeces:# for all marked cells
        i, j = index[0], index[1]
        if arr[i][j] == '0':# become alive if they are dead
            arr[i][j] = '1'
        else:
            arr[i][j] = '0'# or die if they are alive
    return arr# returns the new state of the environment

# prints the environment along with its generatino number
def printOutput(arr, outputFile, generation):
    string = "Generation " + str(generation) + "\n"# puts together the generation number string
    with open(outputFile, "a") as f_out:
        f_out.write(string)# print the generation number
        for line in arr:
            for element in range(0, len(arr[0])):
                f_out.write(str(line[element]))# print the environment
            f_out.write("\n")
        f_out.write("\n")

# self explanatory variables to change
def main():
    try:
        os.remove("outLife.txt")# used for my own testing, remakes the output file
    except OSError:
        pass
    number_of_generations = 3
    inputFile = "inLife.txt"
    outputFile = "outLife.txt"
    simulateLife(inputFile, number_of_generations, outputFile)


if __name__ == '__main__':
  main()
