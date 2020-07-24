import pygame
import ctypes
user32 = ctypes.windll.user32
USER_SCREEN_W, USER_SCREEN_H = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
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
        pygame.image.load("Tiles/Character/Animations/Run/Armature_Run_05.png"),
        pygame.image.load("Tiles/Character/Animations/Run/Armature_Run_06.png"),
        pygame.image.load("Tiles/Character/Animations/Run/Armature_Run_07.png"),
        pygame.image.load("Tiles/Character/Animations/Run/Armature_Run_08.png"),
        pygame.image.load("Tiles/Character/Animations/Run/Armature_Run_09.png"),
        pygame.image.load("Tiles/Character/Animations/Run/Armature_Run_10.png"),
        pygame.image.load("Tiles/Character/Animations/Run/Armature_Run_11.png"),
        pygame.image.load("Tiles/Character/Animations/Run/Armature_Run_12.png"),
        pygame.image.load("Tiles/Character/Animations/Run/Armature_Run_13.png")]

HERO_W = 165
HERO_H = 165
SPEED = 10
runAnimation = []
for image in walk:
    runAnimation.append(pygame.transform.scale(image, (HERO_W, HERO_H)))




class Hero(pygame.sprite.Sprite):
    def __init__(self, screenH):
        super().__init__()
        self.animCount = 0
        self.image = runAnimation[self.animCount]

        self.rect = self.image.get_rect(x = 5, bottom = screenH)
        self.speedX = 0
        self.speedY = 0
        self.grav = 0 #гравитация - скорость движения вниз
        self.onGrond = True #Стоит на земле
        self.isJump = False #прыгает или нет
        self.padOn = True #использовать джойстик
        self.j_left = False
        self.j_right = False

    def update(self):
        #ТУТ ТОЛЬКО ФИЗИКА И УПРАВЛЕНИЕ, АНИМАЦИЯ В ФУНКЦИЮ АНИМАЦИИ
        keys = pygame.key.get_pressed()

        if padOn and self.padOn :
            self.joystick()


        self.speedX = 0
        if keys[pygame.K_a]  or self.j_left:
            if self.rect.left>0:
                self.speedX = -SPEED

        elif  keys[pygame.K_d]  or self.j_right:
            if self.rect.right<USER_SCREEN_W:

                self.speedX = SPEED


        self.rect.x+=self.speedX
        self.animation()

    def joystick(self):
        if my_joystick.get_hat(0) == (-1, 0):
            self.j_left = True
        else:
            self.j_left = False


        if  my_joystick.get_hat(0) == (1, 0):
            self.j_right = True
        else:
            self.j_right = False




    def animation(self):
        if self.speedX !=0:
            self.animCount +=1
            if self.animCount == len(runAnimation):
                self.animCount = 0
            self.image = runAnimation[self.animCount]
            if self.speedX>0:
                self.image = pygame.transform.flip(self.image, True, False)


