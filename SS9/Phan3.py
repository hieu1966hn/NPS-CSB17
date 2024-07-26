class Game:
    def __init__(self):
        self.map = [['-' for _ in range(5)] for _ in range(5)]
        self.map[1][1] = 'P'
        self.map[3][3] = 'K'
        self.map[4][4] = 'D'
        self.player_pos = [1, 1]
        self.has_key = False

    def print_map(self):
        for row in self.map:
            print(' '.join(row))
        print()

    def move(self, direction):
        if direction == 'W':
            self.player_pos[0] -= 1
        elif direction == 'A':
            self.player_pos[1] -= 1
        elif direction == 'S':
            self.player_pos[0] += 1
        elif direction == 'D':
            self.player_pos[1] += 1

        self.player_pos[0] = max(0, min(self.player_pos[0], 4))
        self.player_pos[1] = max(0, min(self.player_pos[1], 4))

        if self.map[self.player_pos[0]][self.player_pos[1]] == 'K':
            self.has_key = True
            self.map[self.player_pos[0]][self.player_pos[1]] = '-'

        if self.map[self.player_pos[0]][self.player_pos[1]] == 'D':
            if self.has_key:
                return "You win!"
            else:
                return "You lose!"

        self.map = [['-' for _ in range(5)] for _ in range(5)]
        self.map[self.player_pos[0]][self.player_pos[1]] = 'P'
        self.map[3][3] = 'K' if not self.has_key else '-'
        self.map[4][4] = 'D'

        return "Keep going!"

game = Game()
while True:
    game.print_map()
    direction = input("Enter direction (W/A/S/D): ")
    result = game.move(direction)
    print(result)
    if result in ["You win!", "You lose!"]:
        break