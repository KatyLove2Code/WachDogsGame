import pygame
pygame.init()

maindisplay = pygame.display.set_mode((800, 600))


game = True
while game:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False
    maindisplay.fill((124,89, 194))
    pygame.draw.circle(maindisplay, (255, 255, 0))
    pygame.display.update()

pygame.quit()
print("Katy Divina")
print("Katy Divina from site")
print('Gorelik Savva from pycharm, у которого теперь все работает')
print("Artyom Shmavonyan")
print("Katy Divina from pyCharm")