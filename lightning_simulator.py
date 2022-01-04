import random
import pygame


class Maze():

    # initalizes the maze with the following arguments
    # width -> width of the maze
    # height -> height of the maze
    # h_prob -> probability of any given horizontal edge being filled
    # v_prob -> probability of any given vertical edge being filled
    def __init__(self, width, height, h_prob, v_prob):
        self.horizontal_edges = \
            [[0 for _ in range(height + 1)] for _ in range(width)]
        self.vertical_edges = \
            [[0 for _ in range(height)] for _ in range(width + 1)]

        # randomly fills in horizontal edges
        for i in range(width):
            for j in range(height + 1):
                x = random.random()
                if x < p:
                    self.horizontal_edges[i][j] = 1

        # randomly fills in vertical edges
        for k in range(width + 1):
            for l in range(height):
                x = random.random()
                if x < q:
                    self.vertical_edges[k][l] = 1

        x = width // 2
        y = 0

        # makes sure the starting square has empty edges
        self.horizontal_edges[x][y] = 0
        self.horizontal_edges[x][y + 1] = 0
        self.vertical_edges[x][y] = 0
        self.vertical_edges[x + 1][y] = 0


# a breadth-first-search algorithm to find a path from the top-middle of the
# maze to the bottom of the maze
def bfs(path, maze, x, y, checked):
    if y == len(maze.horizontal_edges[0]) - 2:
        return [[x, y]]

    if x < len(maze.horizontal_edges) and y <= len(maze.vertical_edges[0]):
        if checked[x][y]:
            return
        else:
            checked[x][y] = 1
    else:
        return

    new_path = None

    # checks the edge below
    if not maze.horizontal_edges[x][y + 1]:
        down_result = bfs(new_path, maze, x, y + 1, checked)
        if down_result:
            result = [[x, y]]
            result += down_result
            return result

    # checks the edge to the left
    if x > 0 and not maze.vertical_edges[x][y]:
        left_result = bfs(new_path, maze, x - 1, y, checked)
        if left_result:
            result = [[x, y]]
            result += (left_result)
            return result

    # checks the edge to the right
    if x < len(maze.vertical_edges) - 1 and not maze.vertical_edges[x + 1][y]:
        right_result = bfs(new_path, maze, x + 1, y, checked)
        if right_result:
            result = [[x, y]]
            result += right_result
            return result

    return


# draws the given solution onto the screen
def draw_lightning(width, height, solution):
    black = 0, 0, 0
    white = 255, 255, 255

    size = width * 10, height * 10

    screen = pygame.display.set_mode(size)

    pygame.draw.rect(screen, black, (0, 0, width * 10, height * 10))

    for set in solution:
        pygame.draw.rect(screen, white, (set[0] * 10, set[1] * 10, 10, 10))


height = 40
width = 20

# probability of a singular horizontal edge being filled
p = .3

# probability of a singular vertical edge being filled
q = .7

checked = [[0 for _ in range(height)] for _ in range(width)]
x = width // 2
y = 0
lightning_maze = Maze(width, height, p, q)
solution = bfs([], lightning_maze, x, y, checked)

# makes sure that a real solution is found
while (solution == None):
    checked = [[0 for _ in range(height)] for _ in range(width)]
    lightning_maze = Maze(width, height, p, q)
    solution = bfs([], lightning_maze, x, y, checked)


if solution:

    pygame.init()

    draw_lightning(width, height, solution)

    while 1:

        # checks for quitting the tab and clicking
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        # if you hit enter you get a new lightning
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            checked = [[0 for _ in range(height)] for _ in range(width)]
            lightning_maze = Maze(width, height, p, q)
            solution = bfs([], lightning_maze, x, y, checked)

            while (solution == None):
                checked = [[0 for _ in range(height)] for _ in range(width)]
                lightning_maze = Maze(width, height, p, q)
                solution = bfs([], lightning_maze, x, y, checked)

            draw_lightning(width, height, solution)

        pygame.display.flip()
