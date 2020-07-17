import pygame
pygame.init()

maindisplay = pygame.display.set_mode((800, 600))


game = True
while game:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False
    maindisplay.fill((124,89, 194))
    pygame.display.update()

pygame.quit()
print("Katy Divina")
print("Katy Divina from site")
print("Artyom Shmavonyan")