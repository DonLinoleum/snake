import pygame
import sys

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
timer = pygame.time.Clock()


class SnakeBlock:
    def __init__(self, x, y):
        self.x: int = x
        self.y: int = y

    def isInside(self) -> bool:
        return 0 <= self.x < SIZE_BLOCK and 0 <= self.y < SIZE_BLOCK


def drawBlock(color, row, column):
    pygame.draw.rect(screen, color,
                     [SIZE_BLOCK + column * SIZE_BLOCK + MARGIN * column,
                      HEADER_MARGIN + SIZE_BLOCK + row * SIZE_BLOCK + MARGIN * row,
                      SIZE_BLOCK, SIZE_BLOCK])


snake_blocks = [SnakeBlock(9, 8), SnakeBlock(9, 9), SnakeBlock(9, 10)]

d_row = 0
d_col = 1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and d_col != 0:
                d_row = -1
                d_col = 0
            elif event.key == pygame.K_DOWN and d_col != 0:
                d_row = 1
                d_col = 0
            elif event.key == pygame.K_LEFT and d_row != 0:
                d_row = 0
                d_col = -1
            elif event.key == pygame.K_RIGHT and d_row != 0:
                d_row = 0
                d_col = 1

    screen.fill(FRAME_COLOR)
    pygame.draw.rect(screen, HEADER_COLOR, [0, 0, size[0], HEADER_MARGIN])
    for row in range(COUNT_BLOCKS):
        for column in range(COUNT_BLOCKS):
            if (column + row) % 2 == 0:
                color = RED
            else:
                color = BLUE
            drawBlock(color, row, column)

    head = snake_blocks[-1]
    if not head.isInside():
        print('exit')
        pygame.quit()
        sys.exit()
    for block in snake_blocks:
        drawBlock(SNAKE_COLOR, block.x, block.y)

    new_head = SnakeBlock(head.x + d_row, head.y + d_col)
    snake_blocks.append(new_head)
    snake_blocks.pop(0)

    pygame.display.flip()
    timer.tick(2)
