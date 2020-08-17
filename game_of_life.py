import copy, random, time, turtle

cell_size = 15
board_size = 20
board_offset = -200
alive = 1
dead = 0
alive_color = 'yellow'
dead_color = 'gray'


def draw_cell(cell, x, y):
    turtle.goto(cell_size * x + board_offset, cell_size * y + board_offset)
    if cell == alive:
        color = alive_color
    if cell == dead:
        color = dead_color
    turtle.color(color)
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(cell_size)
        turtle.right(90)
    turtle.end_fill()


def draw_board(board):
    turtle.tracer(0, 0)
    for y in range(len(board)):
        row = board[y]
        for x in range(len(row)):
            cell = row[x]
            draw_cell(cell, x, y)
    turtle.update()


def living_neighbors(board, x, y):
    neighbors = 0
    for r in range(y - 1, y + 2):
        if r < 0 or r >= len(board): continue # skip out-of-bounds
        row = board[r]
        for c in range(x - 1, x + 2):
            if c < 0 or c >= len(row): continue # skip out-of-bounds
            if r == y and c == x: continue # skip the actual cell
            if row[c] == alive:
                neighbors += 1
    return neighbors


def iterate_board(board):
    new_board = copy.deepcopy(board)
    for y in range(len(board)):
        row = board[y]
        for x in range(len(row)):
            cell = row[x]
            neighbors = living_neighbors(board, x, y)
            if neighbors == 3:
                # new cell is born (even if not already alive)
                new_cell = alive
            elif neighbors == 2:
                # cell stays alive (if it was alive)
                new_cell = cell
            else:
                # too few or too many neighbors; cell dies
                new_cell = dead
            new_board[y][x] = new_cell
    return new_board
    

# Generate random board.
board = []
for y in range(board_size):
    board.append([])
    for x in range(board_size):
        board[y].append(random.randint(0, 1))

turtle.hideturtle()

# Run the game!
while True:
    draw_board(board)
    time.sleep(0.2)
    board = iterate_board(board)

#input("Press Enter to continue...")
