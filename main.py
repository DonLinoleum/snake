import pygame

FRAME_COLOR = (18, 27, 87)
BLUE = (195, 198, 219)
RED = (252, 130, 116)
SIZE_BLOCK = 20
COUNT_BLOCKS = 20
MARGIN = 2

size = [500, 600]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Супер Змейка")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.fill(FRAME_COLOR)
    for row in range(COUNT_BLOCKS):
        for column in range(COUNT_BLOCKS):
            if (column + row) % 2 == 0:
                color = RED
            else:
                color = BLUE
            pygame.draw.rect(screen, color,
                             [10 + column * SIZE_BLOCK + MARGIN * column, 20 + row * SIZE_BLOCK + MARGIN * row,
                              SIZE_BLOCK, SIZE_BLOCK])

    pygame.display.flip()
