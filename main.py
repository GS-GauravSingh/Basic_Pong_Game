import pygame,pygame.mixer,sys, random
from pygame.locals import *
pygame.mixer.init()
pygame.init()

# Defining colors with RGB values
black = (0, 0, 0)
white = (255, 255, 255)
grey = (25, 25, 25)

# Setting Game Window
Screen_Width = 1280
Screen_Height = 720
Game_Window = pygame.display.set_mode([Screen_Width, Screen_Height])
pygame.display.set_caption("Pong")

# Game Variables
clock = pygame.time.Clock()
FPS = 60 
font = pygame.font.SysFont("footlight", 40) 
ball_speedx = 6
ball_speedy = 6 
player_speed = 0

# Rectangles
Game_over_png = pygame.image.load("over.png").convert_alpha()
Gameover_rect = Game_over_png.get_rect(center = (100, 100))
Ball = pygame.Rect(Screen_Width/2 - 10, Screen_Height/2 - 10, 20, 20)
Player = pygame.Rect(-15, Screen_Height/2 - 40, 20, 80)
Opponent = pygame.Rect( Screen_Width - 5, Screen_Height/2 - 40, 20, 80)


def main_game():
    speedx = 4
    speedy = 4
    global ball_speedx, ball_speedy, player_speed
    while True:
        Game_Window.fill(grey)
        pygame.draw.ellipse(Game_Window, white, Ball)
        pygame.draw.rect(Game_Window, white, Player)
        pygame.draw.rect(Game_Window, white, Opponent)
        pygame.draw.aaline(Game_Window, white, (Screen_Width/2, 0), (Screen_Width/2, Screen_Height))

        # Ball Speed
        Ball.x += ball_speedx
        Ball.y += ball_speedy

        # Ball Animation
        if Ball.bottom > Screen_Height or Ball.top < 0:
            ball_speedy *= -1

        if Ball.right > Screen_Width or Ball.left < 0:
            Game_Window.blit(Game_over_png, Gameover_rect)
            Gameover_rect.x += speedx
            Gameover_rect.y += speedy

        if Gameover_rect.bottom > Screen_Height or Gameover_rect.top < 0:
            speedy *= -1
        if Gameover_rect.right > Screen_Width or Gameover_rect.left < 0:
            speedx *= -1
        
        # Collision
        if Ball.colliderect(Player):
            pygame.mixer.Sound("3.wav").play()
            ball_speedx *= -1

        if Ball.colliderect(Opponent):
            pygame.mixer.Sound("3.wav").play()
            ball_speedx *= -1



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == K_UP:
                    player_speed -= 10
                if event.key == K_DOWN:
                    player_speed += 10

            if event.type == pygame.KEYUP:
                if event.key == K_UP:
                    player_speed = 0
                if event.key == K_DOWN:
                    player_speed = 0

        Player.y += player_speed

        # Player
        if Player.top < 0:
            Player.y = 0

        if Player.bottom > Screen_Height:
            Player.y = 640

        # Opponent
        if Ball.y > Opponent.y:
            Opponent.bottom += 7

        if Ball.y < Opponent.y:
            Opponent.top -= 7

        if Opponent.top < 0:
            Opponent.y = 0

        if Opponent.bottom > Screen_Height:
            Opponent.y = 640
        

        pygame.display.update()
        clock.tick(FPS)


main_game()
