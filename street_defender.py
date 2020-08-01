import pygame
from classHero import Hero
from class_menu import Menu
from level import level
from classPlatform import Platform
from classEnemy import Enemy

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

# Группы
all_sprites_group = pygame.sprite.Group()  # Группа вообще всех игровы объектов
platform_group = pygame.sprite.Group()  # Группа платформ
enemy_group = pygame.sprite.Group()  # Группа врагов

hero = Hero(all_sprites_group, USER_SCREEN_H)  # Создаём персонажа по шаблону из класса


# ФУНКЦИИ

def drawWindow():
    """
    функция занимается отрисовкой всех персонажей на карте
    :return:
    """
    win.blit(bg, (0, 0))  # фон
    platform_group.draw(win)  # Отрисвываем платформы
    enemy_group.draw(win)
    win.blit(hero.image, hero.rect)  # главный герой
    pygame.display.update()  # обновление экрана


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
                if event.key == 13:
                    if menu.activeButton == 0:  # Если выбрано "START GAME"
                        return
                    elif menu.activeButton == 2:
                        pygame.quit()

        menu.update()


GRASS = pygame.image.load("Tiles/Map/untitled - 2020-08-01T143755.478.png")  # трава

TREE1 = pygame.image.load("Tiles/Map/untitled - 2020-07-17T194613.279.png")  # дерево№1
TREE2 = pygame.image.load("Tiles/Map/untitled - 2020-07-17T195149.536.png")  # дерево№2
TREE3 = pygame.image.load("Tiles/Map/untitled - 2020-07-17T195540.200.png")  # дерево№3
TREE4 = pygame.image.load("Tiles/Map/untitled - 2020-07-17T194842.678.png")  # дерево№4

FLOWER1 = pygame.image.load("Tiles/Map/untitled - 2020-07-17T200113.601.png")  # цветок№1
FLOWER2 = pygame.image.load("Tiles/Map/untitled - 2020-07-17T200151.579.png")  # цветок№2

GRASS_sprite = pygame.transform.scale(GRASS, (650, 650))

TREE1_sprite = pygame.transform.scale(TREE1, (250, 250))
TREE2_sprite = pygame.transform.scale(TREE2, (450, 450))
TREE3_sprite = pygame.transform.scale(TREE3, (650, 650))
TREE4_sprite = pygame.transform.scale(TREE4, (465, 465))

FLOWER1_sprite = pygame.transform.scale(FLOWER1, (150, 150))
FLOWER2_sprite = pygame.transform.scale(FLOWER2, (125, 125))


def draw_level():
    """
    Отрисовываем статичный фон (цветочки, деревья, облака, вот это всё)
    :return:
    """
    bg.blit(TREE1_sprite, TREE1_sprite.get_rect(x=635, y=750))
    bg.blit(TREE2_sprite, TREE2_sprite.get_rect(x=65, y=550))
    bg.blit(TREE3_sprite, TREE3_sprite.get_rect(x=800, y=425))
    bg.blit(TREE4_sprite, TREE4_sprite.get_rect(x=1500, y=565))

    bg.blit(FLOWER1_sprite, FLOWER1_sprite.get_rect(x=1250, y=880))
    bg.blit(FLOWER2_sprite, FLOWER2_sprite.get_rect(x=120, y=890))

    bg.blit(GRASS_sprite, GRASS_sprite.get_rect(x=0, y=630))
    bg.blit(GRASS_sprite, GRASS_sprite.get_rect(x=635, y=630))
    bg.blit(GRASS_sprite, GRASS_sprite.get_rect(x=635*2, y=630))


def create_platforms():
    """
    Создание спрайтов
    :return:
    """
    platformSizeX = USER_SCREEN_W // len(level[0])
    platformSizeY = USER_SCREEN_H // len(level)

    x = 0
    y = 0

    for line in level:
        for b in line:
            if b == "H":
                hero.rect.x = x
                hero.rect.y = y
            elif b == 1:
                Platform((all_sprites_group, platform_group), x, y, platformSizeX, platformSizeY)
            elif b == 2:
                Enemy((all_sprites_group, enemy_group), x, y, platformSizeX, platformSizeY)

            x += platformSizeX
        x = 0
        y += platformSizeY


# НАЧАЛО ПРОГРАММЫ

showMenu()
create_platforms()
draw_level()

run = True
while run:
    clock.tick(FPS)  # ограничиваем ФПС

    ### ВСЁ УПРАВЛЕНИЕ ПЕРСОНАЖЕМ ВНУТРИ КЛАССА ПЕРСОНАЖА! НЕ ЗДЕСЬ
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Если нажали на крестикв углу (его не видно в фуллскрин)
            run = False

        if event.type == pygame.KEYDOWN:  #
            if event.key == pygame.K_ESCAPE:
                run = False

    hero.update(platform_group)  # Обновляем героя
    enemy_group.update()
    # all_sprites_group.update()
    drawWindow()  # обновляем экран

pygame.quit()
