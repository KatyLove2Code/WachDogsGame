import pygame
from settings import USER_SCREEN_H, USER_SCREEN_W



pygame.joystick.init()
padOn = False
try:
    my_joystick = pygame.joystick.Joystick(0)
    my_joystick.init()
    joysticks = []
    for i in range(pygame.joystick.get_count()):
        joysticks.append(pygame.joystick.Joystick(i))
        joysticks[-1].init()
    padOn = True
except:
    print('Joystick not found')

walk = [pygame.image.load("Tiles/Character/Animations/Run/Armature_Run_00.png"),
        pygame.image.load("Tiles/Character/Animations/Run/Armature_Run_01.png"),
        pygame.image.load("Tiles/Character/Animations/Run/Armature_Run_02.png"),
        pygame.image.load("Tiles/Character/Animations/Run/Armature_Run_03.png"),
        pygame.image.load("Tiles/Character/Animations/Run/Armature_Run_04.png"),
        pygame.image.load("Tiles/Character/Animations/Run/Armature_Run_06.png"),
        pygame.image.load("Tiles/Character/Animations/Run/Armature_Run_07.png"),
        pygame.image.load("Tiles/Character/Animations/Run/Armature_Run_09.png"),
        pygame.image.load("Tiles/Character/Animations/Run/Armature_Run_10.png"),
        pygame.image.load("Tiles/Character/Animations/Run/Armature_Run_11.png"),
        pygame.image.load("Tiles/Character/Animations/Run/Armature_Run_13.png")]

idle = [pygame.image.load("Tiles/Character/Animations/Idle/Armature_Idle_00.png"),
        pygame.image.load("Tiles/Character/Animations/Idle/Armature_Idle_01.png"),
        pygame.image.load("Tiles/Character/Animations/Idle/Armature_Idle_02.png"),
        pygame.image.load("Tiles/Character/Animations/Idle/Armature_Idle_03.png"),
        pygame.image.load("Tiles/Character/Animations/Idle/Armature_Idle_04.png"),
        pygame.image.load("Tiles/Character/Animations/Idle/Armature_Idle_05.png"),
        pygame.image.load("Tiles/Character/Animations/Idle/Armature_Idle_06.png"),
        pygame.image.load("Tiles/Character/Animations/Idle/Armature_Idle_07.png"),
        pygame.image.load("Tiles/Character/Animations/Idle/Armature_Idle_08.png"),
        pygame.image.load("Tiles/Character/Animations/Idle/Armature_Idle_09.png"),
        pygame.image.load("Tiles/Character/Animations/Idle/Armature_Idle_10.png")]

attack = [pygame.image.load("Tiles/Character/Animations/Attack/Armature_Attack_00.png"),
          pygame.image.load("Tiles/Character/Animations/Attack/Armature_Attack_01.png"),
          pygame.image.load("Tiles/Character/Animations/Attack/Armature_Attack_02.png"),
          pygame.image.load("Tiles/Character/Animations/Attack/Armature_Attack_03.png"),
          pygame.image.load("Tiles/Character/Animations/Attack/Armature_Attack_04.png"),
          pygame.image.load("Tiles/Character/Animations/Attack/Armature_Attack_05.png"),
          pygame.image.load("Tiles/Character/Animations/Attack/Armature_Attack_06.png"),
          pygame.image.load("Tiles/Character/Animations/Attack/Armature_Attack_07.png"),
          pygame.image.load("Tiles/Character/Animations/Attack/Armature_Attack_08.png"),
          pygame.image.load("Tiles/Character/Animations/Attack/Armature_Attack_09.png"),
          pygame.image.load("Tiles/Character/Animations/Attack/Armature_Attack_10.png"),
          pygame.image.load("Tiles/Character/Animations/Attack/Armature_Attack_11.png"),
          pygame.image.load("Tiles/Character/Animations/Attack/Armature_Attack_12.png"),
          pygame.image.load("Tiles/Character/Animations/Attack/Armature_Attack_13.png"),
          pygame.image.load("Tiles/Character/Animations/Attack/Armature_Attack_14.png"),
          pygame.image.load("Tiles/Character/Animations/Attack/Armature_Attack_15.png")]

#HERO_W = 165
HERO_H = 165
SPEED = 15
JUMP = 20



def transform_image(list_image):
    transformed_image = []
    for image in list_image:
        w = image.get_width()
        scale =   image.get_height()  // HERO_H
        transformed_image.append(pygame.transform.scale(image, (w//scale, HERO_H)))
    return transformed_image

#RUN
runAnimation = transform_image(walk)

#STAND
idleAnimation = transform_image(idle)

#ATTAC
attackAnimation = transform_image(attack)



class Hero(pygame.sprite.Sprite):
    def __init__(self, groups, screenH):
        super().__init__(groups)
        self.animCount = 0
        self.image = runAnimation[self.animCount]

        self.rect = self.image.get_rect(x=5, bottom=screenH)
        self.speedX = 0

        # Движение по Y
        self.speedY = 0
        self.grav = 2  # гравитация - скорость движения вниз
        self.onGrond = True  # Стоит на земле
        self.isJump = False  # прыгает или нет
        self.GROUND = screenH

        # Джойстик
        self.padOn = True  # использовать джойстик
        self.j_left = False
        self.j_right = False
        self.j_jump = False
        self.attack = True

        self.idleLeft = True
        # self.idleRight = False


        self.damage = 5 #Урон, который герой наносит врагам

    def update(self, platforms):
        """
        Функция запускается из главной программы постоянно(в цикле)
        :param platforms:
        :return:
        """
        # ТУТ ТОЛЬКО ФИЗИКА И УПРАВЛЕНИЕ, АНИМАЦИЯ В ФУНКЦИЮ АНИМАЦИИ
        keys = pygame.key.get_pressed()

        if padOn and self.padOn:
            self.joystick()

        self.speedX = 0
        if keys[pygame.K_a] or self.j_left: #ЛЕВО
            self.idleLeft = True
            # self.idleRight = False
            if self.rect.left > 0:
                self.speedX = -SPEED


        elif keys[pygame.K_d] or self.j_right: #ПРАВО
            self.idleLeft = False
            # self.idleRight = True
            if self.rect.right < USER_SCREEN_W:
                self.speedX = SPEED


        if keys[pygame.K_SPACE] and self.onGrond: #ПРЫЖОК
            self.speedY -= JUMP
            self.onGrond = False

        self.rect.x += self.speedX
        self.rect.y += self.speedY

        if not self.onGrond:
            self.speedY += self.grav

        if self.rect.bottom >= self.GROUND:
            self.rect.bottom = self.GROUND
            self.onGrond = True
            self.speedY = 0


        if keys[pygame.K_e] and self.speedX == 0: #атака
            if self.attack == False:
                self.animCount = 0
            self.attack = True
        else:
            self.attack = False

        self.check_collizion(platforms)
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
            self.onGrond = False

    def joystick(self):
        """
        Если подключен джойстик, проверяем его кнопки
        :return:
        """
        if my_joystick.get_button(0) == 1 and self.onGrond:
            self.speedY -= JUMP
            self.onGrond = False



        if my_joystick.get_hat(0) == (-1, 0):
            self.j_left = True
        else:
            self.j_left = False

        if my_joystick.get_hat(0) == (1, 0):
            self.j_right = True
        else:
            self.j_right = False

    def animation(self):
        '''
        ВСЯ АНИМАЦИЯ ПЕРСОНАЖА
        :return:
        '''



        #ATAKA
        if self.attack == True:
            self.animCount += 1   # Для ускоренной анимации атаки
            if self.animCount >= len(attackAnimation):    # если я дошёл до последней картинки в списке картинок
                self.animCount = 0        # то обнуляю счётчик, чтобы начать сначала
            self.image = attackAnimation[self.animCount]    # Достаю картинку с нужным номером из списка

        #БЕГ
        elif self.speedX != 0:  # Если скорость по Х не нулевая, значит я иду
            if self.animCount >= len(runAnimation):  # если я дошёл до последней картинки в списке картинок
                self.animCount = 0  # то обнуляю счётчик, чтобы начать сначала

            self.image = runAnimation[self.animCount]  # Достаю картинку с нужным номером из списка
            # if self.speedX > 0:  # Если двигаюсь вправо,
            #     self.image = pygame.transform.flip(self.image, True, False)  # то отзеркаливаю картинку персонажа

        #СТОИТ
        elif self.speedX == 0:  # иначе скорость = 0, значит стою на месте
            if self.animCount >= len(idleAnimation):
                self.animCount = 0
            self.image = idleAnimation[self.animCount]

        #Если направление вправо, то зеркалим картинку
        if self.idleLeft == False:
           self.image = pygame.transform.flip(self.image, True, False)

        self.animCount += 1  # Счётчик подсчитывает, какую картинку по счёту я должен показать






