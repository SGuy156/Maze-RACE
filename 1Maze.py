import pygame
import time

pygame.init()
screen = pygame.display.set_mode((1100,600))
done = False

x = 10 #player starting coords
y = 30

x1 = 50
y1 = 30

#time fo player 1
timer1 = time.time()
stopwatch1 = time.time()
timer1Updated = 0

#time fo player2
timer2 = time.time()
stopwatch2 = time.time()
timer2Updated = 0

clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


        screen.fill((0,0,0))
        Font = pygame.font.SysFont("impact", 70, False)
        Title = Font.render("Amazing Maze", True ,(255,255,255))
        screen.blit(Title,(180,180))


        pressed = pygame.key.get_pressed()

        # movement player one
        if pressed[pygame.K_w]: y = y - 5
        if pressed[pygame.K_s]: y = y + 5
        if pressed[pygame.K_a]: x = x - 5
        if pressed[pygame.K_d]: x = x + 5
        #movement player two
        if pressed[pygame.K_i]: y1 = y1 - 5
        if pressed[pygame.K_k]: y1 = y1 + 5
        if pressed[pygame.K_j]: x1 = x1 - 5
        if pressed[pygame.K_l]: x1 = x1 + 5

        player1 = pygame.draw.rect(screen, (150,69,200) , pygame.Rect(x, y, 15, 15))
        player2 = pygame.draw.rect(screen, (100,39,100) , pygame.Rect(x1, y1,15,15))

        wall1 = pygame.draw.rect(screen, (200,200,200) , pygame.Rect(0, 0, 10, 1100))
        wall2 = pygame.draw.rect(screen, (200,200,200) , pygame.Rect(0, 0, 1100, 10))
        wall3 = pygame.draw.rect(screen, (200,200,200) , pygame.Rect(1090, 0, 10, 1100))
        wall4 = pygame.draw.rect(screen, (200, 200, 200), pygame.Rect(0, 590, 1100, 10))

        mazewall1orizontios =  pygame.draw.rect(screen, (200, 200, 200), pygame.Rect(90,350,530,20))
        mazewall2kauetos = pygame.draw.rect(screen, (200, 200, 200), pygame.Rect(90, 0, 20, 480))
        mazewall3orizontios = pygame.draw.rect(screen, (200, 200, 200), pygame.Rect(110, 90, 500, 20))
        mazewall4kauetos = pygame.draw.rect(screen, (200, 200, 200), pygame.Rect(600, 90, 20, 260))
        mazewall5kauetos = pygame.draw.rect(screen, (200, 200, 200), pygame.Rect(339,444, 20, 200))
        final = pygame.draw.rect(screen, (50, 200, 200), pygame.Rect(130,25, 50, 50))

    if player1.colliderect(wall1) or player1.colliderect(wall2) or player1.colliderect(wall3) or player1.colliderect(wall4) or player1.colliderect(mazewall1orizontios) or player1.colliderect(mazewall2kauetos) or player1.colliderect(mazewall3orizontios) or player1.colliderect(mazewall4kauetos) or player1.colliderect(mazewall5kauetos):
        if pressed[pygame.K_w]: y = y + 3
        if pressed[pygame.K_s]: y = y - 3
        if pressed[pygame.K_a]: x = x + 3
        if pressed[pygame.K_d]: x = x - 3

    if player2.colliderect(wall1) or player2.colliderect(wall2) or player2.colliderect(wall3) or player2.colliderect(wall4) or player2.colliderect(mazewall1orizontios) or player2.colliderect(mazewall2kauetos) or player2.colliderect(mazewall3orizontios) or player2.colliderect(mazewall4kauetos) or player2.colliderect(mazewall5kauetos):
        if pressed[pygame.K_i]: y1 = y1 - 5
        if pressed[pygame.K_k]: y1 = y1 + 5
        if pressed[pygame.K_j]: x1 = x1 - 5
        if pressed[pygame.K_l]: x1 = x1 + 5

    if player1.colliderect(final):
        x = 30
        y = 30
        timer1 = time.time()
        timer1Updated = round(timer1 - stopwatch1,2)
        stopwatch1 = time.time()
        time.sleep(0.5)

    if player2.colliderect(final):
        x1 = 30
        y2 = 30
        timer2 = time.time()
        timer2Updated = round(timer2 - stopwatch2,2)
        stopwatch2 = time.time()
        time.sleep(0.5)

    Font1 = pygame.font.SysFont("comicsansms", 40, False)
    Timer1= Font1.render("PLAYER 1 TIME:" + str(timer1Updated), False, (255,255,255))
    screen.blit(Timer1,(125,130))

    Font1 = pygame.font.SysFont("comicsansms", 40, False)
    Timer2 = Font1.render("PLAYER 2 TIME:" + str(timer2Updated), False, (255, 255, 255))
    screen.blit(Timer2, (125, 270))

    if timer1Updated > timer2Updated:
        Font1 = pygame.font.SysFont("comicsansms", 40, False)
        Timer3 = Font1.render("PLAYER ONE WINS!!!", False, (255, 255 ,255))
        screen.blit(Timer3, (325, 330))

    if timer1Updated < timer2Updated:
        Font1 = pygame.font.SysFont("comicsansms", 40, False)
        Timer4 = Font1.render("PLAYER SECOND WINS!!!", False, (255, 255 ,255))
        screen.blit(Timer4, (325, 430))


     #---HIGH CORE UNDERNEATH NOT WORKING---#
    #highscore = str
    #highscore = 0

    #if timer1Updated < highscore:
        #Font1 = pygame.font.SysFont("comicsansms", 40, False)
        #Timer5 = Font1.render("NEW HIGH SCORE OF " + str(timer1Updated), False, (255, 255, 255))
        #screen.blit(Timer5, (525, 100))
        #highscore = timer1Updated

    pygame.display.flip()
    clock.tick(60)




