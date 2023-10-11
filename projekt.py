import time

start = "X 1 2 3 4 5 6 7 8 9 10 11" 
end = "1 2 X 3 4 5 6 7 8 9 10 11"   
row=3
col=4

class Node: 
    def __init__(self, state, steps):
        self.state = state  
        self.steps = list(steps)

def movement(node, nodes):
    dir =  directions(node.state)
    for x in dir: 
        if (x == "Hore"): 
            childNode1 = Node(node.state, node.steps)
            moveUp(childNode1)
            childNode1.steps.append("Hore")
            nodes.append(childNode1)
        if (x == "Dole"): 
            childNode2 = Node(node.state, node.steps)
            moveDown(childNode2)
            childNode2.steps.append("Dole")
            nodes.append(childNode2)
        if (x == "Vpravo"): 
            childNode3 = Node(node.state, node.steps)
            moveRight(childNode3)
            childNode3.steps.append("Vpravo")
            nodes.append(childNode3)
        if (x == "Vlavo"): 
            childNode4 = Node(node.state, node.steps)
            moveLeft(childNode4)
            childNode4.steps.append("Vlavo")
            nodes.append(childNode4)    
    

def directions(state): 
    state = state.split(" ")
    possibleDirections = []
    xIndex = state.index("X")
    #movement up
    if ((xIndex - row) > 0 ):
        possibleDirections.append("Hore")
    #movement down
    if ((xIndex + row) < len(state)): 
        possibleDirections.append("Dole")
    #movement lef
    lavaStrana = 0
    for x in range(col):
        if (xIndex == row*x): 
            lavaStrana = lavaStrana + 1
    if (lavaStrana == 0): 
        possibleDirections.append("Vlavo")
    #movement right 
    pravaStrana = 0 
    for x in range(col):
        if (xIndex == (row*x)-1) or xIndex == (len(state) - 1):
            pravaStrana = pravaStrana + 1
    if (pravaStrana == 0): 
        possibleDirections.append("Vpravo")
    state = " ".join(state)
    return possibleDirections;  
    

def moveRight(node):     
    state = node.state.split(" ")
    indexOfX = state.index("X")
    tempNumber = state[indexOfX + 1]
    state[indexOfX + 1]  = state[indexOfX]
    state[indexOfX] = tempNumber
    node.state = " ".join(state)

def moveLeft(node): 
    state = node.state.split(" ")
    indexOfX = state.index("X")
    tempNumber = state[indexOfX - 1]
    state[indexOfX -1] = state[indexOfX]
    state[indexOfX] = tempNumber
    node.state = " ".join(state)

def moveUp(node): 
    state = node.state.split(" ")
    indexOfX = state.index("X")
    dif = indexOfX - row
    tempNumber = state[indexOfX - row]
    state[dif] = state[indexOfX]
    state[indexOfX] = tempNumber
    node.state = " ".join(state)

def moveDown(node): 
    state = node.state.split(" ")
    indexOfX = state.index("X")
    tempNumber = state[indexOfX + row]
    state[indexOfX + row] = state[indexOfX]
    state[indexOfX] = tempNumber
    node.state = " ".join(state)


startNode = Node(start, [])
endNode = Node(end, [])
startNodes = []
tempStartNodes = []
endNodes = []
tempEndNodes = []
success = 0
layers = 0
endSteps = []
startNodes.append(startNode)
endNodes.append(endNode)

start = time.time()
while (success == 0 or layers == 20):
    for x in startNodes: 
        movement(x, tempStartNodes)
        
    for y in endNodes: 
        movement(y, tempEndNodes)
    
    for x in tempStartNodes: 
        for y in tempEndNodes: 
            if (x.state == end and success == 0): 
                success = 1
                for j in x.steps: 
                    endSteps.append(j)
            if (x.state == y.state and success == 0): 
                success = 1
                for j in x.steps: 
                    endSteps.append(j)
                for i in reversed(y.steps): 
                    if (i == "Vlavo"):    
                        endSteps.append("Vpravo")     
                    elif (i == "Vpravo"): 
                        endSteps.append("Vlavo")
                    elif (i == "Hore"): 
                        endSteps.append("Dole")
                    elif (i == "Dole"): 
                        endSteps.append("Hore")
        for z in endNodes: 
            if (z.state == x.state and success == 0): 
                success = 1     
                for j in x.steps: 
                    endSteps.append(j)
                for i in reversed(z.steps): 
                    if (i == "Vlavo"):    
                        endSteps.append("Vpravo")     
                    elif (i == "Vpravo"): 
                        endSteps.append("Vlavo")
                    elif (i == "Hore"): 
                        endSteps.append("Dole")
                    elif (i == "Dole"): 
                        endSteps.append("Hore")       
                    
    startNodes = tempStartNodes
    endNodes = tempEndNodes
    tempStartNodes = []
    tempEndNodes = []
    layers = layers + 1 #Prevention of infinite loop
end = time.time()
print("Total time: ", end - start)
print(endSteps)