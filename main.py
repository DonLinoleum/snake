import pygame

FRAME_COLOR = (18, 27, 87)
BLUE = (195, 198, 219)
RED = (252, 130, 116)
SIZE_BLOCK = 20
COUNT_BLOCKS = 20
MARGIN = 2
HEADER_COLOR = (109, 126, 237)
HEADER_MARGIN = 100

size = [SIZE_BLOCK * COUNT_BLOCKS + COUNT_BLOCKS * MARGIN + SIZE_BLOCK * 2,
        SIZE_BLOCK * COUNT_BLOCKS + COUNT_BLOCKS * MARGIN + 2 * SIZE_BLOCK + HEADER_MARGIN]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Супер Змейка")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.fill(FRAME_COLOR)
    pygame.draw.rect(screen, HEADER_COLOR, [0, 0, size[0], HEADER_MARGIN])
    for row in range(COUNT_BLOCKS):
        for column in range(COUNT_BLOCKS):
            if (column + row) % 2 == 0:
                color = RED
            else:
                color = BLUE
            pygame.draw.rect(screen, color,
                             [SIZE_BLOCK + column * SIZE_BLOCK + MARGIN * column,
                              HEADER_MARGIN + SIZE_BLOCK + row * SIZE_BLOCK + MARGIN * row,
                              SIZE_BLOCK, SIZE_BLOCK])

    pygame.display.flip()
