import pygame

FRAME_COLOR = (0, 255, 204)
WHITE = (255, 255, 255)
BLUE = (204, 255, 255)
SIZE_BLOCK = 20
COUNT_BLOCKS = 20
MARGIN = 1

size = [400, 600]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Супер Змейка")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.fill(FRAME_COLOR)
    for row in range(COUNT_BLOCKS):
        for column in range(0, COUNT_BLOCKS):
            if column % 2 == 0:
                color = BLUE
            else:
                color = WHITE
            pygame.draw.rect(screen, color, [10 + column * SIZE_BLOCK + MARGIN * column, 20, SIZE_BLOCK, SIZE_BLOCK])

    pygame.display.flip()
