import pygame
pygame.init()

from perframe import update_ball,update_player
  
clock=pygame.time.Clock()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT));

ball_obj = pygame.draw.circle(surface=screen,color=(255,255,255),center=(350,400),radius=10)
ball_hitbox = pygame.Rect(350,400,20,20)

speed = [1,1]
run =True
paused = False

while run:
    screen.fill((0,0,0))

    update_player(screen)
    if not paused :
        update_ball(ball_obj,speed,screen,ball_hitbox,SCREEN_WIDTH,SCREEN_HEIGHT,paused)
    
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            run= False
    
    pygame.display.update()
    clock.tick(120)            
pygame.quit()