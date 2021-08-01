import pygame, sys, random, time
from pygame.locals import *



pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Bouncing Balls')
pygame.mouse.set_visible(False)

colors = [pygame.Color('black'),
 pygame.Color('white'),
 pygame.Color('red'),
 pygame.Color('green'),
 pygame.Color('blue'),
 pygame.Color('yellow'),
 pygame.Color('orange'),
 pygame.Color('purple'),
]

background = pygame.image.load('background.png').convert_alpha()
ball = pygame.image.load('ball.png').convert_alpha()
ball = pygame.transform.scale(ball, (40, 40))
ball_rect = ball.get_rect()
ball_speed = [10, 10]

ball1 = pygame.image.load('ball1.png').convert_alpha()
ball1 = pygame.transform.scale(ball1, (30, 30))
ball1_rect = ball1.get_rect()
ball1_speed = [8, 8]

ball2 = pygame.image.load('ball2.png').convert_alpha()
ball2 = pygame.transform.scale(ball2, (30, 30))
ball2_rect = ball2.get_rect()
ball2_speed = [6, 6]












clock = pygame.time.Clock()
FPS = 30

def terminate():
    pygame.quit()
    sys.exit()


running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
            terminate()


    ball_rect = ball_rect.move(ball_speed)
    if ball_rect.left < 0 or ball_rect.right > WIDTH:
        ball_speed[0] = - ball_speed[0]
    if ball_rect.top < 0 or ball_rect.bottom > HEIGHT:
        ball_speed[1] = - ball_speed[1]

    ball1_rect = ball1_rect.move(ball1_speed)
    if ball1_rect.left < 0 or ball1_rect.right > WIDTH:
        ball1_speed[0] = - ball1_speed[0]
    if ball1_rect.top < 0 or ball1_rect.bottom > HEIGHT:
        ball1_speed[1] = - ball1_speed[1]

    ball2_rect = ball2_rect.move(ball2_speed)
    if ball2_rect.left < 0 or ball2_rect.right > WIDTH:
        ball2_speed[0] = - ball2_speed[0]
    if ball2_rect.top < 0 or ball2_rect.bottom > HEIGHT:
        ball2_speed[1] = - ball2_speed[1]





    screen.fill(colors[1])
    screen.blit(background, (0, 0))
    screen.blit(ball, ball_rect)
    screen.blit(ball1, ball1_rect)
    screen.blit(ball2, ball2_rect)
    pygame.display.flip()
    clock.tick(FPS)
