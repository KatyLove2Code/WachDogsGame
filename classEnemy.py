import pygame
import ctypes

# pygame.joystick.init()
# padOn = False
# try:
#     my_joystick = pygame.joystick.Joystick(0)
#     my_joystick.init()
#     joysticks = []
#     for i in range(pygame.joystick.get_count()):
#         joysticks.append(pygame.joystick.Joystick(i))
#         joysticks[-1].init()
#     padOn = True
# except:
#     print('Joystick not found')
#
# user32 = ctypes.windll.user32
# USER_SCREEN_W, USER_SCREEN_H = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
# pygame.joystick.init()
# padOn = False

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

ENEMY_W = 165
ENEMY_H = 165
SPEED = 10
JUMP = 20

runAnimation = []
for image in walk:
    runAnimation.append(pygame.transform.scale(image, (ENEMY_W, ENEMY_H)))

class Enemy(pygame.sprite.Sprite):
    def __init__(self, groups, screenH):
        super().__init__(groups)
        self.animCount = 0
        self.image = runAnimation[self.animCount]

        self.rect = self.image.get_rect(x=5, bottom=screenH)
        self.speedX = 0

        # Движение по Y
        self.speedY = 0
        self.grav = 1  # гравитация - скорость движения вниз
        self.onGrond = True  # Стоит на земле
        self.isJump = False  # прыгает или нет
        self.GROUND = screenH

        #  # Джойстик
        # self.padOn = True  # использовать джойстик
        # self.j_left = False
        # self.j_right = False
        # self.j_jump = False

    def update(self, platforms):
        """
        Функция запускается из главной программы постоянно(в цикле)
        :param platforms:
        :return:
        """
        # # ТУТ ТОЛЬКО ФИЗИКА И УПРАВЛЕНИЕ, АНИМАЦИЯ В ФУНКЦИЮ АНИМАЦИИ
        # keys = pygame.key.get_pressed()
        #
        # if padOn and self.padOn:
        #     self.joystick()
        #
        # self.speedX = 0
        # if self.j_left:
        #     self.idleLeft = True
        #     self.idleRight = False
        #     if self.rect.left > 0:
        #         self.speedX = -SPEED
        #
        #
        #
        # elif self.j_right:
        #     self.idleLeft = False
        #     self.idleRight = True
        #     if self.rect.right < USER_SCREEN_W:
        #         self.speedX = SPEED
        #
        #
        # if keys[pygame.K_SPACE] and self.onGrond:
        #     self.speedY -= JUMP
        #     self.onGrond = False
        #
        # self.rect.x += self.speedX
        # self.rect.y += self.speedY
        #
        # if not self.onGrond:
        #     self.speedY += self.grav
        #
        # if self.rect.bottom >= self.GROUND:
        #     self.rect.bottom = self.GROUND
        #     self.onGrond = True
        #     self.speedY = 0

        #self.check_collizion(platforms)
        self.animation()

    def check_collizion(self, platforms):
        """
        Проверка на столкновение с платформами
        :return:
        """
        if pygame.sprite.spritecollideany(self, platforms):

            if self.speedY != 0:
                if self.speedY > 0:
                    self.onGrond = True
                self.speedY = 0
        else:
            self.speedY += self.grav

    # def joystick(self):
    #     """
    #     Если подключен джойстик, проверяем его кнопки
    #     :return:
    #     """
    #     if my_joystick.get_button(0) == 1 and self.onGrond:
    #         self.speedY -= JUMP
    #         self.onGrond = False
    #
    #
    #
    #     if my_joystick.get_hat(0) == (-1, 0):
    #         self.j_left = True
    #     else:
    #         self.j_left = False
    #
    #     if my_joystick.get_hat(0) == (1, 0):
    #         self.j_right = True
    #     else:
    #         self.j_right = False

    def animation(self):
        '''
        ВСЯ АНИМАЦИЯ ПЕРСОНАЖА
        :return:
        '''

        if self.speedX != 0:  # Если скорость по Х не нулевая, значит я иду
            self.animCount += 1  # Счётчик подсчитывает, какую картинку по счёту я должен показать
            if self.animCount == len(runAnimation):  # если я дошёл до последней картинки в списке картинок
                self.animCount = 0  # то обнуляю счётчик, чтобы начать сначала

            self.image = runAnimation[self.animCount]  # Достаю картинку с нужным номером из списка
            if self.speedX > 0:  # Если двигаюсь вправо,
                self.image = pygame.transform.flip(self.image, True, False)  # то отзеркаливаю картинку персонажа


