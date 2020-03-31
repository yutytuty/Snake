import pygame

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)

block_size = 35
grid_size = 16
screen = pygame.display.set_mode((grid_size * block_size, grid_size * block_size))


class Snake:
    def __init__(self, start):
        self.body = [start]
        self.direction_x = 0
        self.direction_y = 0
        self.size = block_size

    def show(self):
        for part in self.body:
            pygame.draw.rect(screen, black, (part[0], part[1], block_size, block_size))


def draw_grid():
    for i in range(grid_size):
        pygame.draw.line(screen, black, (0, i * block_size), (grid_size * block_size, i * block_size))
        pygame.draw.line(screen, black, (i * block_size, 0), (i * block_size, grid_size * block_size))


snake = Snake(((block_size * grid_size) / 2 - 1 * block_size, (block_size * grid_size) / 2 - 1 * block_size))

while True:
    screen.fill(white)
    draw_grid()
    snake.show()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    pygame.display.update()
