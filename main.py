import numpy as np
import random

'''
Naming Conventions:
class name : Pascal-casing
class methods name : Camel-casing
variables : Camel-casing
'''

#Node Class : for individual Elements on a graph
class Node:
    #Initial node number
    srCounter = 101

    def __init__(self,column,row):
        self.num = Node.srCounter
        self.weight = 0
        self.nRow = row
        self.nColumn = column
        Node.srCounter += 1

    def setWeight(self,weight):
        self.weight = weight

    def getNumber(self):
        return self.num

    def getWeight(self):
        return self.weight

    def getPosition(self):
        return self.nColumn,self.nRow


#Graph Class : to contain node elements
class Graph:
    #prefered row=column (Square Matrix)
    def __init__(self,row,column):
        self.row = row
        self.column = column
        self.size = row * column
        self.nodes = [[Node(i,j) for i in range(column)] for j in range(row)]
        self.startNode = self.nodes[0][0]
        self.finishNode = self.nodes[column-1][row-1]

    def getGraphSize(self):
        return self.size

    def printGraphNumber(self):
        for row in self.nodes:
            for element in row:
                print(element.getNumber(),end= ' ')
            print("")

    def setStart(self,row,column):
        self.startNode = self.nodes[row][column]

    def setFinish(self,row,column):
        self.finishNode = self.nodes[row][column]

    def getStartNode(self):
        return self.startNode

    def getFinishNode(self):
        return self.finishNode

    def getNextNode(self,cNode,move):
        #1 - upward cell
        #2 - right cell
        #3 - down cell
        #4 - left cell
        #exception : catch for top elements
        cPostion,rPosition = cNode.getPosition()
        
        if (move == 1 and rPosition>0):
            print("Move Up")
            return self.nodes[rPosition-1][cPostion]
        elif (move == 2 and cPostion<(self.column-1)):
            print("Move Right")
            return self.nodes[rPosition][cPostion+1]
        elif (move == 3 and rPosition<(self.row-1)):
            print("Move Down")
            return self.nodes[rPosition+1][cPostion]
        elif (move == 4 and cPostion>0):
            print("Move Left")
            return self.nodes[rPosition][cPostion-1]
        else:
            print("Not a Correct Move")
            return cNode

def qLearning(stateSize,actionSize):
    q = np.zeros((stateSize,actionSize))


#set row and Column number (Square Matrix)
row = column = 10

if __name__ == "__main__":
    #Creating Graph
    newGraph = Graph(row,column)
    print("Graph Size : {}\n".format(newGraph.getGraphSize()))
    
    #Printing Graph node's number
    print("Printing Nodes(number) : \n")
    newGraph.printGraphNumber()

    #Creating Random row.column for Start and Finish Nodes
    newStartRandomRow,newStartRandomColumn = (random.randint(0,row-1),random.randint(0,column-1))
    newFinishRandomRow,newFinishRandomColumn = (random.randint(0,row-1),random.randint(0,column-1))

    #Initializing random start and finish nodes
    newGraph.setStart(newStartRandomColumn,newStartRandomRow)
    newGraph.setFinish(newFinishRandomColumn,newFinishRandomRow)
    print("Start node number : {}\nFinish node number : {} ".format(newGraph.getStartNode().getNumber(),newGraph.getFinishNode().getNumber()))

    #Loop through next randomly generated nodes for 'loop' times
    loop =5
    nextNode = newGraph.getNextNode(newGraph.startNode,random.randint(1,4))
    for i in range(loop):
        print("Next Move Node Number : {} ".format(nextNode.getNumber()))
        nextNode = newGraph.getNextNode(nextNode,random.randint(1,4))
    print("Finish Node at : {}".format(nextNode.getNumber()))


"""
Code Written and Modified by : Nishant Pandey
Github :
email : unexme@gmail.com 

"""