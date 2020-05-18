import pygame
import random

White = (255, 255, 255)
Black = (0, 0, 0)
Aqua=( 0, 255, 255)
Blue=( 0, 0, 255)
Fuchsia=(255, 0, 255)
Gray=(128, 128, 128)
Green=( 0, 128, 0)
Lime=( 0, 255, 0)
Maroon=(128, 0, 0)
Olive=(128, 128, 0)
Purple=(128, 0, 128)
Red=(255, 0, 0)
Silver=(192, 192, 192)
Teal=( 0, 128, 128)
Yellow=(255, 255, 0)
points=0

pygame.init()

screen = pygame.display.set_mode([1000, 800])
 
pygame.display.set_caption('Catch Red Ball')
 
clock = pygame.time.Clock()

pygame.display.update()
 
background_position = [0, 0]
 
# colors=[Aqua,Blue,Fuchsia,Gray,Green,Lime,Maroon,Olive,Purple,Red,Silver,Teal,Yellow]  
colors=[Red,Blue]  

def new_ball():
    global xi,yi,ci
    screen.fill((0,0,0))
    xi=random.randint(0,1000-50)
    yi=random.randint(0,1000-50)
    ci= random.choice(colors)
    pygame.draw.circle(screen, ci,(xi,yi),25,25)
    font = pygame.font.SysFont('serif', 25, True, False)
    text = font.render("Score: "+str(points),True,White)
    screen.blit(text, (25, 25))  
    pygame.display.flip()
    clock.tick(1) 
 
done = False
 
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True  
         

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
          mouse_position = pygame.mouse.get_pos()
          x = mouse_position[0]
          y = mouse_position[1]
          if (xi-x)**2 + (yi-y)**2 <= 25**2 and ci==colors[0]:
            points+=1
            xi=-1000
    new_ball() 
        
pygame.quit()


