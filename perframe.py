import pygame

paddle_x=350
paddle_xspeed=1
paddle_y=500
player = pygame.Rect((paddle_x, paddle_y,100,15))


def update_player(screen):
    global paddle_x, paddle_y, paddle_xspeed
    player.x = paddle_x
    paddle_xspeed=0
    key = pygame.key.get_pressed() 

    pygame.draw.rect(screen,(0,255,0),player)
    if key[pygame.K_a] and paddle_x>0:
        paddle_x-=4
        paddle_xspeed=-1
         
    if key[pygame.K_d] and paddle_x<700:
         paddle_x+=4
         paddle_xspeed=1
    # pygame.display.update()
         
def update_ball(ball_obj,speed,screen,ball_hitbox,SCREEN_WIDTH,SCREEN_HEIGHT,paused):         
    ball_hitbox.center=ball_obj.center

    ball_obj.centerx=ball_obj.centerx+speed[0]*1.5
    ball_obj.centery=ball_obj.centery+speed[1]*1.5
    pygame.draw.circle(surface=screen, color=(255,255,255),center=ball_obj.center, radius=10)
    if ball_obj.left <= 0 :
        speed[0] = -speed[0]
        ball_obj.left = 0
    if ball_obj.right >= SCREEN_WIDTH:
        speed[0] = -speed[0]
        ball_obj.right = SCREEN_WIDTH
        
    if ball_obj.top <= 0 or ball_obj.bottom >= SCREEN_HEIGHT:
        speed[1] = -speed[1]
    if ball_hitbox.colliderect(player) and speed[1] > 0:
        speed[1] = -speed[1]
        speed[0] = speed[0]+paddle_xspeed/2
    
    if ball_obj.bottom>=500:
        paused = not paused
