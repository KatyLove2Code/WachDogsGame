import pygame
from settings import USER_SCREEN_H, USER_SCREEN_W

walk = [pygame.image.load("Tiles/Bots/Bot1/Run/Armature_run_00.png"),
        pygame.image.load("Tiles/Bots/Bot1/Run/Armature_run_01.png"),
        pygame.image.load("Tiles/Bots/Bot1/Run/Armature_run_02.png"),
        pygame.image.load("Tiles/Bots/Bot1/Run/Armature_run_03.png"),
        pygame.image.load("Tiles/Bots/Bot1/Run/Armature_run_04.png"),
        pygame.image.load("Tiles/Bots/Bot1/Run/Armature_run_05.png"),
        pygame.image.load("Tiles/Bots/Bot1/Run/Armature_run_06.png"),
        pygame.image.load("Tiles/Bots/Bot1/Run/Armature_run_07.png"),
        pygame.image.load("Tiles/Bots/Bot1/Run/Armature_run_08.png"),
        pygame.image.load("Tiles/Bots/Bot1/Run/Armature_run_09.png"),
        pygame.image.load("Tiles/Bots/Bot1/Run/Armature_run_10.png")]

damage = [pygame.image.load("Tiles/Bots/Bot1/Damage/Armature_hurt_00.png"),
          pygame.image.load("Tiles/Bots/Bot1/Damage/Armature_hurt_01.png"),
          pygame.image.load("Tiles/Bots/Bot1/Damage/Armature_hurt_02.png"),
          pygame.image.load("Tiles/Bots/Bot1/Damage/Armature_hurt_03.png"),
          pygame.image.load("Tiles/Bots/Bot1/Damage/Armature_hurt_04.png"),
          pygame.image.load("Tiles/Bots/Bot1/Damage/Armature_hurt_05.png"),
          pygame.image.load("Tiles/Bots/Bot1/Damage/Armature_hurt_06.png"),
          pygame.image.load("Tiles/Bots/Bot1/Damage/Armature_hurt_07.png"),
          pygame.image.load("Tiles/Bots/Bot1/Damage/Armature_hurt_08.png"),
          pygame.image.load("Tiles/Bots/Bot1/Damage/Armature_hurt_09.png"),
          pygame.image.load("Tiles/Bots/Bot1/Damage/Armature_hurt_10.png")]

die = [pygame.image.load("Tiles/Bots/Bot1/Die/Armature_die_00.png"),
       pygame.image.load("Tiles/Bots/Bot1/Die/Armature_die_01.png"),
       pygame.image.load("Tiles/Bots/Bot1/Die/Armature_die_02.png"),
       pygame.image.load("Tiles/Bots/Bot1/Die/Armature_die_03.png"),
       pygame.image.load("Tiles/Bots/Bot1/Die/Armature_die_04.png"),
       pygame.image.load("Tiles/Bots/Bot1/Die/Armature_die_05.png"),
       pygame.image.load("Tiles/Bots/Bot1/Die/Armature_die_06.png"),
       pygame.image.load("Tiles/Bots/Bot1/Die/Armature_die_07.png"),
       pygame.image.load("Tiles/Bots/Bot1/Die/Armature_die_08.png"),
       pygame.image.load("Tiles/Bots/Bot1/Die/Armature_die_09.png"),
       pygame.image.load("Tiles/Bots/Bot1/Die/Armature_die_10.png"),
       pygame.image.load("Tiles/Bots/Bot1/Die/Armature_die_11.png"),
       pygame.image.load("Tiles/Bots/Bot1/Die/Armature_die_12.png"),
       pygame.image.load("Tiles/Bots/Bot1/Die/Armature_die_13.png")]

ENEMY_W = 200
ENEMY_H = 200
SPEED = 10


def transform_image(list_image):
    transformed_image = []
    for image in list_image:
        w = image.get_width()
        scale = image.get_height() // ENEMY_H
        transformed_image.append(pygame.transform.scale(image, (w // scale, ENEMY_H)))
    return transformed_image


runAnimation = transform_image(walk)
damageAnimation = transform_image(damage)
dieAnimation = transform_image(die)


class Enemy(pygame.sprite.Sprite):
    def __init__(self, groups, x, y, width, height):
        super().__init__(groups)
        self.animCount = 0
        self.image = runAnimation[self.animCount]
        self.rect = self.image.get_rect(x=x, bottom=USER_SCREEN_H - 50)

        self.speedX = SPEED
        self.Left = False

        self.gettingDamage = False
        self.dying = False
        self.heals = 100
        self.damage = True

    def update(self, hero):
        """
        Функция запускается из главной программы постоянно(в цикле)
        :return:
        """

        # враг ходит от края я к краю
        if self.rect.right > USER_SCREEN_W or self.rect.left < 0:
            self.speedX *= -1
            self.damage = True

        if not self.gettingDamage and not self.dying:
            self.rect.x += self.speedX
            self.damage = True

        self.check_damage(hero)
        self.animation()

    def animation(self):
        '''
        ВСЯ АНИМАЦИЯ ПЕРСОНАЖА
        :return:
        '''

        if self.dying:
            if self.animCount == len(dieAnimation):  # если я дошёл до последней картинки в списке картинок
                self.kill()
            else:
                self.image = dieAnimation[self.animCount]


        elif self.gettingDamage:

            if self.animCount == len(damageAnimation):  # если я дошёл до последней картинки в списке картинок
                self.animCount = 0  # то обнуляю счётчик, чтобы начать сначала
                self.gettingDamage = False
            if self.damage == True:
                self.image = pygame.transform.flip(self.image, True, False)
            self.image = damageAnimation[self.animCount]



        else:
            if self.animCount == len(runAnimation):  # если я дошёл до последней картинки в списке картинок
                self.animCount = 0  # то обнуляю счётчик, чтобы начать сначала

            self.image = runAnimation[self.animCount]  # Достаю картинку с нужным номером из списка

            if self.speedX > 0:  # Если двигаюсь вправо,
                self.image = pygame.transform.flip(self.image, True, False)  # то отзеркаливаю картинку персонажа

        self.animCount += 1  # Увеличиваю счётчик

    def check_damage(self, hero):
        if self.rect.colliderect(hero.rect) and hero.attack:
            if not self.gettingDamage:
                self.animCount = 0
                self.gettingDamage = True
            else:
                self.heals -= hero.damage

        if self.heals <= 0:
            self.dying = True
