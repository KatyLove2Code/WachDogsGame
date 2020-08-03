#################################
# ЕСЛИ ХОТИТЕ ЧТО-ТО ИЗМЕНИТЬ ПРЕДУПРЕДИТЕ МЕНЯ!!!!
#################################
import pygame
from classHero import Hero

## выясняем размер экрана пользователя
import ctypes
user32 = ctypes.windll.user32
USER_SCREEN_W, USER_SCREEN_H = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)


#настраиваем экран
pygame.init()
win = pygame.display.set_mode((USER_SCREEN_W, USER_SCREEN_H), pygame.FULLSCREEN)
pygame.display.set_caption("Mario")

bg = pygame.image.load('Tiles/bg/bg.png')
bg = pygame.transform.scale(bg, (USER_SCREEN_W, USER_SCREEN_H))


#Тамер и фпс
clock = pygame.time.Clock()
FPS = 60


hero = Hero(USER_SCREEN_H) #Создаём персонажа по шаблону из класса


def drawWindow():  # рисование всей карты
    win.blit(bg, (0, 0))
    win.blit(hero.image, hero.rect)

    pygame.display.update()


run = True
while run:
    clock.tick(FPS)

    ### ВСЁ УПРАВЛЕНИЕ ПЕРСОНАЖЕМ ВНУТРИ КЛАССА ПЕРСОНАЖА! НЕ ЗДЕСЬ
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_o and padOn == True:
        #         padOn = False
        #         keyboard = True
        #         print("False")
    hero.update()

    drawWindow()






pygame.quit()