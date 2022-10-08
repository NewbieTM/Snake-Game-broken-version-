import time
import pygame

pygame.init()


def Iterations(argument, c, i=1):
    while i < argument:
        if c == 0:  # right
            pygame.draw.rect(screen, BLUE, ((x + 30 * i), y, 30, H_R))
        elif c == 1:  # up
            pygame.draw.rect(screen, BLUE, (x+120, y - 30 * i, 30, H_R))
        elif c == 2:  # left
            pygame.draw.rect(screen, BLUE, (x - 30 * i, y, 30, H_R))
        elif c == 3:  # down
            pygame.draw.rect(screen, BLUE, (x+120, y + 30 * i, 30, H_R))
        i += 1



def Move(argumentr, argumentl, argumentu, argumentd,x):
    c = 0
    Iterations(argumentr, c)
    c+=1
    Iterations(argumentu, c)
    c+=1
    Iterations(argumentl, c)
    c+=1
    Iterations(argumentd, c)
    pygame.display.update()


H = 600
W = 783
GREEN = (0, 255, 50)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)

screen = pygame.display.set_mode((W, H))
sc2 = screen
pygame.display.set_caption("Змейка")

pygame.display.update()

clock = pygame.time.Clock()
FPS = 60
run = True
x = 152
y = H // 2
move_direction = 'RIGHT'
W_R = 120
H_R = 30
j = 0

'''while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d and move_direction != 'LEFT':
                move_direction = 'RIGHT'
            elif event.key == pygame.K_a and move_direction != 'RIGHT':
                move_direction = 'LEFT'
            elif event.key == pygame.K_w and move_direction != 'DOWN':
                move_direction = 'UP'
            elif event.key == pygame.K_s and move_direction != 'UP':
                move_direction = 'DOWN'

    screen.fill(GREEN)
    argument = Move(move_direction, x, y, argument,c)
    if move_direction == 'RIGHT':
        x+=30
        if argument < 6:
            argument += 1
    elif move_direction == 'LEFT':
        x += 30
        if argument < 6:
            argument += 1
    elif move_direction == 'UP':
        c +=1
        ux +=30
    elif move_direction == 'DOWN':
        y += 30
        argument -= 1
        if argument == 5:
            x += 30
    # pygame.draw.rect(screen, BLUE, (x, y, W_R, H_R))
    for x_line in range(1, W, 30):
        pygame.draw.line(screen, YELLOW, (x_line, 0), (x_line, H), 3)
    for y_line in range(0, H, 30):
        pygame.draw.line(screen, YELLOW, (0, y_line), (W, y_line), 3)
    pygame.display.update()
    time.sleep(2)
    clock.tick(FPS)
'''

argument_right = 6
argument_left = 1
argument_up = 1
argument_down = 1

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d and move_direction != 'LEFT':
                move_direction = 'RIGHT'
            elif event.key == pygame.K_a and move_direction != 'RIGHT':
                move_direction = 'LEFT'
            elif event.key == pygame.K_w and move_direction != 'DOWN':
                move_direction = 'UP'
            elif event.key == pygame.K_s and move_direction != 'UP':
                move_direction = 'DOWN'

    screen.fill(GREEN)


    if move_direction == 'RIGHT':
        if argument_right < 6:
            argument_right += 1


        x += 30


        if argument_up > 1:
            argument_up-=1
        if argument_down > 1:
            argument_down -= 1

    elif move_direction == 'LEFT':
        if argument_left < 6:
            argument_left += 1

        x -= 30


        if argument_up > 1:
            argument_up -= 1
        if argument_down > 1:
            argument_down -= 1

    elif move_direction == 'UP':
        if argument_up < 6:
            argument_up += 1

        if j == 0:
            j = 1
            x+=30

        if argument_right > 1:
            argument_right -= 1
        if argument_left > 1:
            argument_left -= 1



    elif move_direction == 'DOWN':
        if argument_down < 6:
            argument_down += 1

        y += 30


        if argument_right > 1:
            argument_right -= 1
        if argument_left > 1:
            argument_left -= 1

    Move(argument_right, argument_left, argument_up, argument_down,x)


    for x_line in range(1, W, 30):
        pygame.draw.line(screen, YELLOW, (x_line, 0), (x_line, H), 3)
    for y_line in range(0, H, 30):
        pygame.draw.line(screen, YELLOW, (0, y_line), (W, y_line), 3)
    pygame.display.update()
    time.sleep(2)
    clock.tick(FPS)
