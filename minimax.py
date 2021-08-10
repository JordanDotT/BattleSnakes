class Simulation:

    # assign values to the board 
    # food: -2
    # snake: (0-8 depending on the order that they're presented from the request)
    def __init__(self, data):
        self.board = [[-1] * 11 for _ in range(11)]
        self.directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        self.allSnakes = {data["snakes"][i]["name"]:i for i in range(len(data["snakes"]))}

        for i in range(len(data["snakes"])):
            for coords in data["snakes"][i]["body"]:
                self.board[10 - coords["y"]][coords["x"]] = i

        for coords in data["food"]:
            self.board[10 - coords["y"]][coords["x"]] = -2

    def isValid(self, x, y):
        if x < 0 or x >= len(self.board) or y < 0 or y >= len(self.board[0]):
            return False
        if self.board[x][y] != -1 and self.board[x][y] != -2:
            return False
        return True

    # check to see if we're the only one on the board = win (100)
    # to check to see if we're dead = loss
    # check to see if nobody is on the board = tie
    # empty: -1
    # food: -2
    def isEnd(self, data, currentSnake):
      index = self.allSnakes[currentSnake]
      # condition that we've won
      if len(data["board"]["snakes"]) == 1 and data["board"]["snakes"][index]["health"] > 0:
          return 100
      # condition that it's a tie
      elif len(data["board"]["snakes"]) == 0:
          return 50
      # condition that we lost
      elif data["board"]["snakes"][index]["health"] == 0:
          return -100
      return None



    def findMax(self, data):
        maxv = -101
        move = None

        result = self.isEnd(data, "hello")
        if result:
            return (result, None)

        x = 10 - data["you"]["head"]["y"]
        y = data["you"]["head"]["x"]

        for dirr in self.directions:
            if self.isValid(x + dirr[0], y + dirr[1]):
                self.board[x+dirr[0]][y+dirr[1]] = self.allSnakes["hello"]
                (m, move) = self.findMin(data)
                if m > maxv:
                    maxv = m
                    move = dirr
                self.board[x+dirr[0]][y+dirr[1]] = -1

        return (maxv, move)

    # # evaluate based on closeness to food and the center
    # # we also only want to get food when our health is low
    # def evaluateStrength(self, x, y, currentSnake):

    def findMin(self,data):
        minv = 101
        move = None

        result = self.isEnd(data, "Yung Snek V0")
        if result:
            return (result, None)

        x = 10 - data["board"]["snakes"][0]["head"]["y"]
        y = data["board"]["snakes"][0]["head"]["x"]

        for dirr in self.directions:
            if self.isValid(x + dirr[0], y + dirr[1]):
                self.board[x+dirr[0]][y+dirr[1]] = self.allSnakes["Yung Snek V0"]
                (m, move) = self.findMax(data)
                if m < minv:
                    minv = m
                    move = dirr
                self.board[x+dirr[0]][y+dirr[1]] = -1

        return (minv, move)
