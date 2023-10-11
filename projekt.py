start = "12345678X"  #1 2 3  4 5 6 7 8 X 
end = "7865432X1"   #7 6 8 5 4 3 2 X 1
row=3
col=3

class Node: 
    def __init__(self, state):
        self.state = state  
        self.left = None 
        self.right = None
        self.up = None 
        self.down = None 

def search(): 
    startNode = Node(start)
    endNode = Node(end)
    movement(startNode, endNode)

def movement(node1, node2):
    new1State = node1.state
    new2State = node2.state
    success = 0
    while (success == 0):  
        dir1 =  directions(new1State)
        dir2 = directions(new2State)
        for x in dir1: 
            if (x == "Hore"): 
                moveUp(new1State)
                node1.up = Node(new1State)
            if (x == "Dole"): 
                moveDown(new1State)
                node1.down = Node(new1State)
            if (x == "Vpravo"): 
                moveRight(new1State)
                node1.right = Node(new1State)
            if (x == "Vlavo"): 
                moveLeft(new1State)
                node1.left = Node(new1State)
        for x in dir2: 
            if (x == "Hore"): 
                moveUp(new2State)
                node2.up = Node(new2State)
            if (x == "Dole"): 
                moveDown(new2State)
                node2.down = Node(new2State)
            if (x == "Vpravo"): 
                moveRight(new2State)
                node2.right = Node(new2State)
            if (x == "Vlavo"): 
                moveLeft(new2State)
                node2.left = Node(new2State)
        success = 1
    
    

def directions(state): 
    possibleDirections = []
    xIndex = state.find("X")
    #movement up
    if ((xIndex - 3) > 0 ):
        possibleDirections.append("Hore")
    #movement down
    if ((xIndex + 3) < len(state) - 1): 
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
    for x in range (col):
        if (xIndex == (row*x)-1) or xIndex == len(state) - 1:
            pravaStrana = pravaStrana + 1
    if (pravaStrana == 0): 
        possibleDirections.append("Vpravo")

    return possibleDirections;  
    

def moveLeft(state):     
    indexOfX = state.find("X")
    tempNumber = state[indexOfX + 1]
    state[indexOfX + 1]  = state[indexOfX]
    state[indexOfX] = tempNumber

def moveRight(state): 
    indexOfX = state.find("X")
    tempNumber = state[indexOfX - 1]
    state[indexOfX -1] = state[indexOfX]
    state[indexOfX] = tempNumber

def moveUp(state): 
    indexOfX = state.find("X")
    tempNumber = state[indexOfX - row]
    state[indexOfX - row] = state[indexOfX]
    state[indexOfX] = tempNumber

def moveDown(state): 
    indexOfX = state.find("X")
    tempNumber = state[indexOfX + row]
    state[indexOfX + row] = state[indexOfX]
    state[indexOfX] = tempNumber


search()