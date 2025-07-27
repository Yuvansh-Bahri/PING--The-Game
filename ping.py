#setup

import pygame, sys
import random

pygame.init()
clock = pygame.time.Clock() #Event tick basically

#show stuff
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('PING')

#Def function vars
ball_speed_x = 7 * random.choice((1, -1))
ball_speed_y = 7 * random.choice((1, -1))
player_speed = 0
opponent_speed = 9

#BALL-ANIM function
def ball_anim():

    global ball_speed_x, ball_speed_y
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= screen_width:
        ball_restart()

    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1

# Game Rectangles
ball = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15, 30, 30) 
player = pygame.Rect(screen_width - 20, screen_height/2 - 70, 10, 140) 
opponent = pygame.Rect(10, screen_height/2 - 70, 10, 140)

# Define some vars
bg_colour = pygame.Color('cornflowerblue')
player_colour = pygame.Color('dodgerblue4')
opp_colour = pygame.Color('dodgerblue4')
ball_colour = pygame.Color('dodgerblue4')
line_colour = pygame.Color('dodgerblue4')

#Defines Ball-Restart func
def ball_restart():
    global ball_speed_x, ball_speed_y
    ball.center = (screen_width/2, screen_height/2)
    ball_speed_y *= random.choice((1, -1))
    ball_speed_x *= random.choice((1, -1))

# Defines player-collision func
def player_collision():
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height

# Opponent-move func
def opponent_move():
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed

    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height

# Game loop
while True:
    #Input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 7
            if event.key == pygame.K_UP:
                player_speed -= 7

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 7
            if event.key == pygame.K_UP:
                player_speed += 7


    ball_anim()
    player_collision()
    opponent_move()

    #Visuals
    screen.fill(bg_colour)
    pygame.draw.rect(screen, player_colour, player)
    pygame.draw.rect(screen, opp_colour, opponent)
    pygame.draw.ellipse(screen, ball_colour, ball)
    pygame.draw.aaline(screen, line_colour, (screen_width/2, 0), (screen_width/2, screen_height))

    #Update window
    pygame.display.flip()
    clock.tick(60)
