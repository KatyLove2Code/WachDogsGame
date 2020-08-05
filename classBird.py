import pygame
from settings import USER_SCREEN_H, USER_SCREEN_W

fly = [pygame.image.load("Tiles/Bird/Fly/Armature_fly_00.png"),
       pygame.image.load("Tiles/Bird/Fly/Armature_fly_01.png"),
       pygame.image.load("Tiles/Bird/Fly/Armature_fly_02.png"),
       pygame.image.load("Tiles/Bird/Fly/Armature_fly_03.png"),
       pygame.image.load("Tiles/Bird/Fly/Armature_fly_04.png"),
       pygame.image.load("Tiles/Bird/Fly/Armature_fly_05.png"),
       pygame.image.load("Tiles/Bird/Fly/Armature_fly_06.png"),
       pygame.image.load("Tiles/Bird/Fly/Armature_fly_07.png"),
       pygame.image.load("Tiles/Bird/Fly/Armature_fly_08.png"),
       pygame.image.load("Tiles/Bird/Fly/Armature_fly_09.png"),
       pygame.image.load("Tiles/Bird/Fly/Armature_fly_10.png"),
       pygame.image.load("Tiles/Bird/Fly/Armature_fly_11.png"),
       pygame.image.load("Tiles/Bird/Fly/Armature_fly_12.png"),
       pygame.image.load("Tiles/Bird/Fly/Armature_fly_13.png"),
       pygame.image.load("Tiles/Bird/Fly/Armature_fly_14.png"),
       pygame.image.load("Tiles/Bird/Fly/Armature_fly_15.png"),
       pygame.image.load("Tiles/Bird/Fly/Armature_fly_16.png"),
       pygame.image.load("Tiles/Bird/Fly/Armature_fly_17.png"),
       pygame.image.load("Tiles/Bird/Fly/Armature_fly_18.png"),
       pygame.image.load("Tiles/Bird/Fly/Armature_fly_19.png"),
       pygame.image.load("Tiles/Bird/Fly/Armature_fly_20.png")]

BIRD_W = 200
BIRD_H = 200
SPEED = 10
JUMP = 20

flyAnimation = []
for image in fly:
    flyAnimation.append(pygame.transform.scale(image, (BIRD_W, BIRD_H)))


class Bird(pygame.sprite.Sprite):
    def __init__(self, groups, x, y, width, height):
        super().__init__(groups)
        self.animCount = 0
        self.image = flyAnimation[self.animCount]
        self.rect = self.image.get_rect(x=x, bottom=y + height + 500)
        self.speedX = 0
        self.Left = False

    def update(self):
        """
        Функция запускается из главной программы постоянно(в цикле)
        :param platforms:
        :return:
        """

        # враг ходит от края я к краю

        if self.Left == False:
            self.speedX = SPEED
            if self.rect.right > USER_SCREEN_W:
                self.speedX = 0
                self.Left = True
        if self.Left == True:
            self.speedX = -SPEED
            if self.rect.right < 150:
                self.speedX = 0
                self.Left = False

        self.rect.x += self.speedX

        #
        # if keys[pygame.K_SPACE] and self.onGrond:
        #     self.speedY -= JUMP
        #     self.onGrond = False
        #
        # self.rect.x += self.speedX
        self.animation()
        #


    def animation(self):
        '''
        ВСЯ АНИМАЦИЯ ПЕРСОНАЖА
        :return:
        '''

        if self.speedX != 0:  # Если скорость по Х не нулевая, значит я иду
            self.animCount += 1  # Счётчик подсчитывает, какую картинку по счёту я должен показать
            if self.animCount == len(flyAnimation):  # если я дошёл до последней картинки в списке картинок
                self.animCount = 0  # то обнуляю счётчик, чтобы начать сначала

            self.image = flyAnimation[self.animCount]  # Достаю картинку с нужным номером из списка
            if self.speedX > 0:  # Если двигаюсь вправо,
                self.image = pygame.transform.flip(self.image, True, False)  # то отзеркаливаю картинку персонажа
