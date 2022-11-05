import pygame
import sys
import random
import pygame_menu

pygame.init()

bg = pygame.image.load('bg.jpg')
FRAME_COLOR = (4, 17, 133)
BLUE = (195, 198, 219)
RED = (252, 130, 116)
WHITE = (255, 255, 255)
FOOD = (30, 23, 79)
SIZE_BLOCK = 20
COUNT_BLOCKS = 20
MARGIN = 2
HEADER_COLOR = (31, 22, 125)
HEADER_MARGIN = 100
SNAKE_COLOR = (6, 74, 5)

size = [SIZE_BLOCK * COUNT_BLOCKS + COUNT_BLOCKS * MARGIN + SIZE_BLOCK * 2,
        SIZE_BLOCK * COUNT_BLOCKS + COUNT_BLOCKS * MARGIN + 2 * SIZE_BLOCK + HEADER_MARGIN]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Супер Змейка")
timer = pygame.time.Clock()
courier = pygame.font.SysFont('courier', 36)
total = 0
speed = 1


class SnakeBlock:
    def __init__(self, x, y):
        self.x: int = x
        self.y: int = y

    def is_inside(self) -> bool:
        return 0 <= self.x < SIZE_BLOCK and 0 <= self.y < SIZE_BLOCK

    def __eq__(self, other):
        return isinstance(other, SnakeBlock) and self.x == other.x and self.y == other.y


def drawBlock(color, row, column):
    pygame.draw.rect(screen, color,
                     [SIZE_BLOCK + column * SIZE_BLOCK + MARGIN * column,
                      HEADER_MARGIN + SIZE_BLOCK + row * SIZE_BLOCK + MARGIN * row,
                      SIZE_BLOCK, SIZE_BLOCK])


def get_random_empty_block():
    x = random.randint(0, COUNT_BLOCKS - 1)
    y = random.randint(0, COUNT_BLOCKS - 1)
    empty_block = SnakeBlock(x, y)
    return empty_block


def draw_playing_field():
    for row in range(COUNT_BLOCKS):
        for column in range(COUNT_BLOCKS):
            if (column + row) % 2 == 0:
                color = RED
            else:
                color = BLUE
            drawBlock(color, row, column)


def draw_text():
    text_total = courier.render(f"Total: {total}", 0, WHITE)
    text_speed = courier.render(f"Speed: {speed}", 0, WHITE)
    screen.blit(text_total, (SIZE_BLOCK, SIZE_BLOCK))
    screen.blit(text_speed, (SIZE_BLOCK + 250, SIZE_BLOCK))


def start_the_game():
    global total, speed
    snake_blocks = [SnakeBlock(9, 8), SnakeBlock(9, 9), SnakeBlock(9, 10)]
    apple = get_random_empty_block()
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

        draw_text()
        draw_playing_field()
        drawBlock(FOOD, apple.x, apple.y)

        for block in snake_blocks:
            drawBlock(SNAKE_COLOR, block.x, block.y)

        head = snake_blocks[-1]
        if not head.is_inside():
            total = 0
            speed = 1
            print('exit')
            break

        if apple == head:
            total += 1
            speed = total // 3 + 1
            snake_blocks.append(apple)
            apple = get_random_empty_block()

        new_head = SnakeBlock(head.x + d_row, head.y + d_col)
        snake_blocks.append(new_head)
        snake_blocks.pop(0)

        if new_head in snake_blocks[0:-1]:
            total = 0
            speed = 1
            print('exit')
            break

        pygame.display.flip()
        timer.tick(3 + speed)




main_theme = pygame_menu.themes.THEME_DARK.copy()
main_theme.set_background_color_opacity(0.7)
menu = pygame_menu.Menu('', 300, 300, theme=main_theme)

menu.add.text_input('Name :', default='Player1')
menu.add.button('Play', start_the_game)
menu.add.button('Quit', pygame_menu.events.EXIT)

while True:
    screen.blit(bg, (0, 0))

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()

    if menu.is_enabled():
        menu.update(events)
        menu.draw(screen)

    pygame.display.update()
