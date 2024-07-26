# a = "anna" # len(a): n ky tu

# def is_palindrome(a):
#     flag = True
#     for i in range(len(a)): #4
#         if a[i] == a[len(a) - i - 1]:
#             flag = True
#         else:
#             flag = False
#             return False
#     if flag == True:
#         return True
        
# print(is_palindrome("anna213"))



### Gợi ý phần III
class Game: 
    ## print map
    def __init__(self):
        self.map = [["-" for _ in range(5)] for _ in range(5)]
        ## định vị vị trí các phần tử
        self.map[1][1] = "P"
        self.map[3][3] = "K"
        self.map[4][4] = "D"
        self.player_pos = [1, 1]
        self.has_key = False

    
    def print_map(self):
        for row in self.map:
            print(" ".join(row))
        print()
        
    ### hàm di chuyển
    def move(self, direction):
        if direction == "W":
            self.player_pos[0] -= 1 ### trừ đi một đơn vị.
        elif direction == "A":
            self.player_pos[1] -= 1 
        elif direction == "S":
            self.player_pos[0] += 1 
        elif direction == "D":
            self.player_pos[1] += 1 
    


game = Game()

while True:
    game.print_map()
    direction = input("Enter direction (W/A/S/D): ")
    result = game.move(direction)
    print(result)
    if result in ["You win", "You lose!"]:
        break