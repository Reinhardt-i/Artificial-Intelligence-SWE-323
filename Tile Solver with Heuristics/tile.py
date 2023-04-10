class Puzzle:
    perfect_tiles = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, -1]
    ]

    def __init__(self, tiles):
        self.tiles = tiles
        self.blank_tile = self.find_blank_tile()
        self.g = 0

    def find_blank_tile(self):
        for i in range(len(self.tiles)):
            for j in range(len(self.tiles[i])):
                if self.tiles[i][j] == -1:
                    return (i, j)
        raise ValueError("No blank tile found")

    def H(self):
        differences = 0
        for i in range(len(self.tiles)):
            for j in range(len(self.tiles[i])):
                if self.tiles[i][j] != self.perfect_tiles[i][j]:
                    differences += 1
        return differences

    def f_n(self):
        return self.g + self.H()

    def valid_moves(self):
        moves = []
        i, j = self.blank_tile
        if i > 0:
            moves.append((i - 1, j))  # move up
        if i < len(self.tiles) - 1:
            moves.append((i + 1, j))  # move down
        if j > 0:
            moves.append((i, j - 1))  # move left
        if j < len(self.tiles[i]) - 1:
            moves.append((i, j + 1))  # move right
        return moves

    def apply_move(self, move):
        i, j = move
        blank_i, blank_j = self.blank_tile
        new_tiles = [row[:] for row in self.tiles]
        new_tiles[blank_i][blank_j], new_tiles[i][j] = new_tiles[i][j], new_tiles[blank_i][blank_j]
        return Puzzle(new_tiles), self.g + 1

    def a_star(self):
        frontier = [(self.f_n(), self)]
        explored = set()
        while frontier:
            _, current = frontier.pop(0)
            if current.H() == 0:
                return current.g
            explored.add(tuple(map(tuple, current.tiles)))
            for move in current.valid_moves():
                neighbor, cost = current.apply_move(move)
                if tuple(map(tuple, neighbor.tiles)) not in explored:
                    neighbor.g = cost
                    frontier.append((neighbor.f_n(), neighbor))
                    frontier.sort()
        return -1

if __name__ == '__main__':
    
    tile = [ [1, 2, 3],
             [-1, 4, 6],
             [7, 5, 8]
           ]

    puzzle = Puzzle(tile)
    print(puzzle.a_star())

