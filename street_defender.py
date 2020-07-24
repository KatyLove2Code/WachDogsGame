
import pygame
from classHero import Hero
from class_menu import Menu

## выясняем размер экрана пользователя
import ctypes

user32 = ctypes.windll.user32
USER_SCREEN_W, USER_SCREEN_H = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

# настраиваем экран
pygame.init()
win = pygame.display.set_mode((USER_SCREEN_W, USER_SCREEN_H), pygame.FULLSCREEN)
pygame.display.set_caption("street defender")

bg = pygame.image.load('Tiles/bg/bg.png')
bg = pygame.transform.scale(bg, (USER_SCREEN_W, USER_SCREEN_H))

# Тамер и фпс
clock = pygame.time.Clock()
FPS = 60

hero = Hero(USER_SCREEN_H)  # Создаём персонажа по шаблону из класса

#ФУНКЦИИ

def drawWindow():
    """
    функция занимается отрисовкой всех персонажей на карте
    :return:
    """
    win.blit(bg, (0, 0)) # фон
    win.blit(hero.image, hero.rect) #главный герой
    pygame.display.update()  #обновление экрана


def showMenu():
    '''
    стартовое меню
    :return:
    '''
    menu = Menu(win)

    while True:

    ### ВСЁ УПРАВЛЕНИЕ ПЕРСОНАЖЕМ ВНУТРИ КЛАССА ПЕРСОНАЖА! НЕ ЗДЕСЬ
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

            if event.type == pygame.KEYDOWN:
                 if event.key == pygame.K_ESCAPE:
                     return
                 if event.key == pygame.K_UP:
                     menu.up()
                 if event.key == pygame.K_DOWN:
                     menu.down()
        menu.update()


#НАЧАЛО ПРОГРАММЫ

showMenu()

run = True
while run:
    clock.tick(FPS)

    ### ВСЁ УПРАВЛЕНИЕ ПЕРСОНАЖЕМ ВНУТРИ КЛАССА ПЕРСОНАЖА! НЕ ЗДЕСЬ
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False

    hero.update() #Обновляем героя

    drawWindow() #обновляем экран

pygame.quit()