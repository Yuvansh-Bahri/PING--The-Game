#setup
import pygame, sys
import random
import time

pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()

clock = pygame.time.Clock() #Event tick basically

# set custom game icon
image = pygame.image.load('pinglogo.png')
pygame.display.set_icon(image)

#show stuff
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('PING')

#Def function vars
ball_speed_x = 7 * random.choice((1, -1))
ball_speed_y = 7 * random.choice((1, -1))
speed_multiplier = 1
player_speed = 0
opponent_speed = 7
level = 1
tick_speed = 60

# Text vars
player_pong_score = 0
opponent_pong_score = 0
game_font = pygame.font.Font('Bareona-MVVBP.ttf', 50)
score_text_colour = pygame.Color('dodgerblue3')
popup_display_var = 0
effect_text_font = pygame.font.Font('Bareona-MVVBP.ttf', 35)

#Score lvl 1 timer
score_time = None

#BALL-ANIM function
def ball_anim():

    global ball_speed_x, ball_speed_y, player_pong_score, opponent_pong_score, score_time, level
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1

    if ball.left <= 0: 
        player_pong_score += 1
        score_time = pygame.time.get_ticks()
        pygame.mixer.Sound.play(ping_lvl_1_sound)

    if ball.right >= screen_width:
        opponent_pong_score += 1
        score_time = pygame.time.get_ticks()
        pygame.mixer.Sound.play(ping_lvl_1_sound)

    if ball.colliderect(player) or ball.colliderect(opponent):
        pygame.mixer.Sound.play(ping_lvl_1_sound)
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

# Sound
ping_lvl_1_sound = pygame.mixer.Sound('pingping.ogg')
score_lvl_1_sound = pygame.mixer.Sound('pingping.ogg')

#Defines Ball-Restart func
def ball_restart():
    global ball_speed_x, ball_speed_y, score_time, level

    if score_time is None:
        return

    current_time = pygame.time.get_ticks()
    ball.center = (screen_width/2, screen_height/2)

    if current_time - score_time < 700:
        number_three = game_font.render('3', False, line_colour)
        screen.blit(number_three, (screen_width/2 -10, screen_height/2 + 20))

    if 700 < current_time - score_time < 1400:
        number_two = game_font.render('2', False, line_colour)
        screen.blit(number_two, (screen_width/2 -10, screen_height/2 + 20))

    if 1400 < current_time - score_time < 2100:
        number_one = game_font.render('1', False, line_colour)
        screen.blit(number_one, (screen_width/2 -10, screen_height/2 + 20))

    if current_time - score_time < 2100:
        ball_speed_x, ball_speed_y = 0, 0
    else:    
        ball_speed_y = 7 * random.choice((1, -1))
        ball_speed_x = 7 * random.choice((1, -1))
        score_time = None

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

def main():
    global player_speed, level, opponent_speed, ball_speed_y, ball_speed_x, speed_multiplier, tick_speed, effect_level_text 
    while True:
        #Input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
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

        if score_time is not None:
            ball_restart()

        #Level Switcheroos + Time Dilation basic implementation
        if player_pong_score == 2 and level == 1: #switch pong score from 5 to 10 and so on, space it out a lil more ykwim?
            level += 1
            speed_multiplier += 1
            tick_speed += random.choice((30, -10))

         # Archived code. Full of unknown references. DO NOT UNHASH
            # - - - - -- - -- - - -- - - - - - - - - - - - - - - - - - - - - - --  - -- - - - - - - - - - -- - - - - - - - - --
            #player_speed *= random.choice((2, 3, 4, 5, 6, 7, 8, 9))
            #popup_display_var += 1
            #send_buff_message = True
            #event_buff_text = game_font.render(f"Ball speed increased!", True, score_text_colour) 
         #if send_buff_message == True and level == 2:
             #if popup_display_var == 1:
                #screen.blit(event_buff_text, (200, 200))
                #time.sleep(3)
                #popup_display_var = 0
            # - - - - -- - -- - - -- - - - - - - - - - - - - - - - - - - - - - --  - -- - - - - - - - - - -- - - - - - - - - --
        elif player_pong_score == 3 and level == 2:
            level += 1
            speed_multiplier += 1
            tick_speed += random.choice((30, -10))
        elif player_pong_score == 4 and level == 3:
            level += 1
            speed_multiplier += 1
            tick_speed += random.choice((30, -10))
        elif player_pong_score == 5 and level == 4:
            level += 1
            speed_multiplier += 1
            tick_speed += random.choice((30, -10))
        elif player_pong_score == 6 and level == 5:
            level += 1
            speed_multiplier += 1
            tick_speed += random.choice((30, -10))
        elif player_pong_score == 7 and level == 6:
            level += 1
            speed_multiplier += 1
            tick_speed += random.choice((30, -10))
        elif player_pong_score == 8 and level == 7:
            level += 1
            speed_multiplier += 1
            tick_speed += random.choice((30, -10))
        elif player_pong_score == 9 and level == 8:
            level += 1
            speed_multiplier += 1
            tick_speed += random.choice((30, -10))
        elif player_pong_score == 10 and level == 9:
            level += 1
            speed_multiplier += 1
            tick_speed += random.choice((30, -10))
        elif player_pong_score == 11 and level == 10:
            level += 1
            speed_multiplier += 1
            tick_speed += random.choice((30, -10))
        elif player_pong_score == 12 and level == 11:
            level += 1
            speed_multiplier += 1
            tick_speed += random.choice((30, -10))
        elif player_pong_score == 13 and level == 12:
            level += 1
            speed_multiplier += 1
            tick_speed += random.choice((30, -10))
        elif player_pong_score == 14 and level == 13:
            level += 1
            speed_multiplier += 1
            tick_speed += random.choice((30, -10))
        elif player_pong_score == 15 and level == 14:
            level += 1
            speed_multiplier += 1
            tick_speed += random.choice((30, -10))
        elif player_pong_score == 16 and level == 15:
            level += 1
            speed_multiplier += 1
            tick_speed += random.choice((30, -10))
        elif player_pong_score == 17 and level == 16:
            level += 1
            speed_multiplier += 1
            tick_speed += random.choice((30, -10))
        elif player_pong_score == 18 and level == 17:
            level += 1
            speed_multiplier += 1
            tick_speed += random.choice((30, -10))
        elif player_pong_score == 19 and level == 18:
            level += 1
            speed_multiplier += 1
            tick_speed += random.choice((30, -10))
        elif player_pong_score == 20 and level == 19:
            level += 1
            speed_multiplier += 1
            tick_speed += random.choice((30, -10))
        elif player_pong_score == 21 and level == 20:
            level += 1
            speed_multiplier += 1
            tick_speed += random.choice((30, -10))
        elif player_pong_score == 22 and level == 21:
            level += 1
            speed_multiplier += 1
            tick_speed += random.choice((30, -10))
        elif player_pong_score == 23 and level == 22:
            level += 1
            speed_multiplier += 1
            tick_speed += random.choice((30, -10))
        elif player_pong_score == 24 and level == 23:
            level += 1
            speed_multiplier += 1
            tick_speed += random.choice((30, -10))
        elif player_pong_score == 25 and level == 24:
            level += 1
            speed_multiplier += 1
            tick_speed += random.choice((30, -10))
        

        #player pong score.vis
        player_text = game_font.render(f"{player_pong_score}", False, score_text_colour)
        screen.blit(player_text, (430, 350))
        #opponent pong score.vis
        opponent_text = game_font.render(f"{opponent_pong_score}", False, score_text_colour)
        screen.blit(opponent_text, (350, 350))
        #level.vis
        Display_level_text = game_font.render(f"Lvl: {level}", False, score_text_colour)
        screen.blit(Display_level_text, (620, 25))
        #Effect.vis
        effect_level_text = effect_text_font.render(f"Speed: {tick_speed}", False, score_text_colour)
        screen.blit(effect_level_text, (600, 70))

        #Update window
        pygame.display.flip()
        clock.tick(tick_speed)
    pygame.quit() # hehe game go bye bye
main() # Run EVERYTHING
