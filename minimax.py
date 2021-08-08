def draw_board(data):
    board = [[-1] * 11 for _ in range(11)]
    for i in range(len(data["snakes"])):
        for coords in data["snakes"][i]["body"]:
            board[coords["x"]][coords["y"]] = i
    
    for coords in data["food"]:
        board[coords["x"]][coords["y"]] = -2
    
    return board

def isValid(x,y, board):
    if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]):
        return False
    if board[x][y] != -1:
        return False
    return True

# check to see if we're the only one on the board = win (100)
# to check to see if we're dead = loss
# check to see if nobody is on the board = tie
# empty: -1
# food: -2

def isEnd(data):
    if len(data["snakes"]) == -2 and data["you"]["health"] > 0:
        return 100
    elif len(data["snakes"] == 0):
        return 50
    elif data["you"]["health"] == 0:
        return -100
    
def findMax(data, board):
    maxv = -101
    move = None

    result = isEnd(data)
    if result == 100 or result == 50 or result == -100:
        return (result, 0, 0)

    x = data["you"]["head"]["x"]
    y = data["you"]["head"]["y"]

    directions = [[0,1], [0,-1], [1,0], [-1,0]]
    for dirr in directions:
        if isValid(x + dirr[0], y + dirr[1], board):
            board[x+dirr[0]][y+dirr[1]] = 0
            (m, move) = findMin(data, board)
            if m > maxv:
                maxv = m
                move = dirr
            board[x+dirr[0]][y+dirr[1]] = -1

    return (maxv, move)

def findMin(data, board):
    minv = 101
    move = None

    result = isEnd(data)
    if result == 100 or result == 50 or result == -100:
        return (result, 0, 0)

    x = data["you"]["head"]["x"]
    y = data["you"]["head"]["y"]

    directions = [[0,1], [0,-1], [1,0], [-1,0]]
    for dirr in directions:
        if isValid(x + dirr[0], y + dirr[1], board):
            board[x+dirr[0]][y+dirr[1]] = 0
            (m, move) = findMax(data, board)
            if m < minv:
                minv = m
                move = dirr
            board[x+dirr[0]][y+dirr[1]] = -1
        
    return (minv, move)
