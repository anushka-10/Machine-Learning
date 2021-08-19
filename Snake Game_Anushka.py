# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import sys
import random
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import pygame

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
small_font = pygame.font.SysFont('Courier New', 20, True)
medium_font = pygame.font.SysFont('Courier New', 25, True)
large_font = pygame.font.SysFont('Courier New', 40, True, True)
clock = pygame.time.Clock()
snake_block = 15
food_block = 10
speed = 10
dis = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Snakez')


def startGame():
    dis.fill(BLACK)
    font1 = large_font.render("Welcome to SNAKEz!", True, GREEN)
    font2 = medium_font.render("Play Game", True, BLUE, YELLOW)
    font3 = medium_font.render("Instructions", True, BLACK, YELLOW)
    font4 = medium_font.render("Quit", True, RED, YELLOW)

    font1_rect = font1.get_rect()
    font2_rect = font2.get_rect()
    font3_rect = font3.get_rect()
    font4_rect = font4.get_rect()
    font1_rect.center = (300, 200)
    font2_rect.center = (300, 300)
    font3_rect.center = (300, 350)
    font4_rect.center = (300, 400)

    dis.blit(font1, font1_rect)
    dis.blit(font2, font2_rect)
    dis.blit(font3, font3_rect)
    dis.blit(font4, font4_rect)
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    gameloop()
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if (x > font3_rect.left) and (x < font3_rect.right):
                    if (y > font3_rect.top) and (y < font3_rect.bottom):
                        instructions(font1, font1_rect)
                if (x > font2_rect.left) and (x < font2_rect.right):
                    if (y > font2_rect.top) and (y < font2_rect.bottom):
                        gameloop()
                if (x > font4_rect.left) and (x < font4_rect.right):
                    if (y > font4_rect.top) and (y < font4_rect.bottom):
                        pygame.quit()
                        sys.exit()
        pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


def score_count(points):
    score = medium_font.render("Score:" + str(points), True, GREEN)
    dis.blit(score, [10, 10])




def game_over(points):
    dis.fill(WHITE)
    lost = large_font.render("Game Over!", True, YELLOW)
    dis.blit(lost, [200, 200])
    marks = medium_font.render("Your Score:"+str(points), True, RED)
    dis.blit(marks, [200, 300])
    repeat = small_font.render("Type P to play again and Q to quit", True, BLUE)
    dis.blit(repeat, [100, 400])
    pygame.display.update()
    while True:
      for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
             if event.key == pygame.K_p:
                gameloop()
             if event.key == pygame.K_q:
                pygame.quit()
                sys.exit()
    pygame.display.update()
    Clock.tick(speed)


def gameloop():
    dis.fill(BLACK)
    snake_pos = [300, 300]
    snake_body = [[300, 300], [290, 300], [280, 300]]
    x_change = 0
    y_change = 0
    direc = 'right'
    score_count(0)
    pause = False
    your_score = 0
    food_x = random.randrange(0, 500, 10)
    food_y = random.randrange(50, 500, 10)
    food = True
    run = True
    while run == True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    direc = 'up'
                if event.key == pygame.K_DOWN:
                    direc = 'down'
                if event.key == pygame.K_LEFT:
                    direc = 'left'
                if event.key == pygame.K_RIGHT:
                    direc = 'right'
                if event.key == pygame.K_SPACE:
                    pause = True
                    run = False

        if direc == 'up':
            snake_pos[1] -= 10
        if direc == 'down':
            snake_pos[1] += 10
        if direc == 'left':
            snake_pos[0] -= 10
        if direc == 'right':
            snake_pos[0] += 10



        while pause:

            dis.fill(YELLOW)
            heading = medium_font.render("Paused!", True, RED)
            opt1 = small_font.render("Press R to resume game", True, BLUE)
            opt2 = small_font.render("Press N to start new game", True, BLUE)
            opt3 = small_font.render("Press Q to quit game", True, BLUE)
            dis.blit(heading, (300, 200))
            dis.blit(opt1, (50, 300))
            dis.blit(opt2, (50, 350))
            dis.blit(opt3, (50, 400))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        pause = False
                        run = True

                    if event.key == pygame.K_n:
                        startGame()
                    if event.key == pygame.K_q:
                        pygame.quit()
                        sys.exit()




        snake_body.insert(0, list(snake_pos))
        if snake_pos[0] == food_x and snake_pos[1] == food_y:
            your_score += 10
            food = False
        else:
            snake_body.pop()

        if food!= True:
            food_x = random.randrange(0, 500, 10)
            food_y = random.randrange(50, 500, 10)
        food = True

        dis.fill(BLACK)

        for pos in snake_body:
            pygame.draw.rect(dis, BLUE, pygame.Rect(pos[0], pos[1], 10, 10))
        pygame.draw.circle(dis, RED, (food_x, food_y), 8)
        score_count(your_score)
        if snake_pos[0] < 0 or snake_pos[0] > 600:
            game_over(your_score)
        if snake_pos[1] < 0 or snake_pos[1] > 600:
            game_over(your_score)
        for block in snake_body[1:]:
            if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
                game_over(your_score)

        pygame.display.update()
        clock.tick(speed)
    pygame.quit()
    sys.exit()


def instructions(font1, font1_rect):
    dis.fill(BLACK)
    dis.blit(font1, font1_rect)
    inst1 = small_font.render("Rule 1: If you cross edges, you will die", True, BLUE)
    inst2 = small_font.render("Rule 2: Eat red coloured food to gain score", True, BLUE)
    inst3 = small_font.render("Rule 3: Do not cross over yourself", True, BLUE)
    inst5 = small_font.render("Rule 4: Press Spacebar to pause the game", True, BLUE)
    inst4 = small_font.render("Back", True, RED)
    inst4_rect = inst4.get_rect()
    inst4_rect.center = (500, 500)
    dis.blit(inst1, [20, 300])
    dis.blit(inst2, [20, 330])
    dis.blit(inst3, [20, 360])
    dis.blit(inst5, [20, 390])
    dis.blit(inst4, inst4_rect)
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                p, q = event.pos
                if p >= inst4_rect.left and p <= inst4_rect.right:
                    if q >= inst4_rect.top and q <= inst4_rect.bottom:
                        startGame()
        pygame.display.update()


startGame()
gameloop()
