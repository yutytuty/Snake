import pygame

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)

block_size = 35
grid_size = 16
screen = pygame.display.set_mode((grid_size * block_size, grid_size * block_size))


def draw_grid():
    for i in range(grid_size):
        pygame.draw.line(screen, black, (0, i * block_size), (grid_size * block_size, i * block_size))
        pygame.draw.line(screen, black, (i * block_size, 0), (i * block_size, grid_size * block_size))


while True:
    screen.fill(white)
    draw_grid()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    pygame.display.update()

