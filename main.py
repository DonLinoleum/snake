import pygame

FRAME_COLOR = (18, 27, 87)
BLUE = (195, 198, 219)
RED = (252, 130, 116)
SIZE_BLOCK = 20
COUNT_BLOCKS = 20
MARGIN = 2
HEADER_COLOR = (109, 126, 237)
HEADER_MARGIN = 100
SNAKE_COLOR = (0, 102, 0)

size = [SIZE_BLOCK * COUNT_BLOCKS + COUNT_BLOCKS * MARGIN + SIZE_BLOCK * 2,
        SIZE_BLOCK * COUNT_BLOCKS + COUNT_BLOCKS * MARGIN + 2 * SIZE_BLOCK + HEADER_MARGIN]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Супер Змейка")


class SnakeBlock:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def drawBlock(color, row, column):
    pygame.draw.rect(screen, color,
                     [SIZE_BLOCK + column * SIZE_BLOCK + MARGIN * column,
                      HEADER_MARGIN + SIZE_BLOCK + row * SIZE_BLOCK + MARGIN * row,
                      SIZE_BLOCK, SIZE_BLOCK])


snake_block = [SnakeBlock(9, 9)]
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
            drawBlock(color, row, column)
    for block in snake_block:
        drawBlock(SNAKE_COLOR,block.x,block.y)

    pygame.display.flip()
