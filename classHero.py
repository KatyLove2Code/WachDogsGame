import pygame

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
        self.padOn = False #использовать джойстик
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


        #
        # if padOn == True:
        #
        # #if my_joystick.get_hat(0) == (-1, -1) and x > 5 and y < 720 - height - 15:
        #     #x -= speed
        #     #y += speed
        # #if my_joystick.get_hat(0) == (1, 1) and x < 1024 - width - 5 and y > 5:
        #     #x += speed
        #     #y -= speed
        # #if my_joystick.get_hat(0) == (-1, 1) and x > 5 and y > 5:
        #     #x -= speed
        #     #y -= speed
        # #if my_joystick.get_hat(0) == (1, -1) and x < 1024 - width - 5 and y < 720 - height - 15:
        #     #x += speed
        #     #y += speed
        # if my_joystick.get_hat(0) == (-1, 0) and x > 5:
        #     x -= speed
        # if my_joystick.get_hat(0) == (1, 0) and x < 1024 - width - 5:
        #     x += speed
        # #if  my_joystick.get_hat(0) == (0, 1) and y > 5:
        #     #y -= speed
        # #if my_joystick.get_hat(0) == (0, -1) and y < 720 - height - 15:
        #     #y += speed
        # if event.type == pygame.JOYBUTTONDOWN:
        #     if not(isJump):
        #
        #         if event.button == 0:
        #             isJump = True
        #     else:
        #         if jumpCount1 >= - 10:
        #             if jumpCount1 < 0:
        #                 y += (jumpCount1 ** 2) / 2
        #             else:
        #                 y -= (jumpCount1 ** 2) / 2
        #             jumpCount1 -= 1
        #         else:
        #             isJump = False
        #             jumpCount1 = 10
        #


    # if keyboard == True:
    #
    #     if keys[pygame.K_a] and x > 100:
    #         x -= speed
    #         left = True
    #         right = False
    #     elif keys[pygame.K_d] and x < 1024 - width - 40:
    #         x += speed
    #         right = True
    #         left = False
    #     else:
    #         left = False
    #         right = False
    #         animCount = 0
    #
    #     if not(isJump):
    #
    #         if keys[pygame.K_SPACE]:
    #             isJump = True
    #     else:
    #         if jumpCount >= - 10:
    #             if jumpCount < 0:
    #                 y += (jumpCount ** 2) / 2
    #             else:
    #                 y -= (jumpCount ** 2) / 2
    #             jumpCount -= 1
    #         else:
    #             isJump = False
    #             jumpCount = 10


    def animation(self):
        if self.speedX !=0:
            self.animCount +=1
            if self.animCount == len(runAnimation):
                self.animCount = 0
            self.image = runAnimation[self.animCount]
            if self.speedX>0:
                self.image = pygame.transform.flip(self.image, True, False)


 # if animCount + 1 >= 60:
 #        animCount = 0
 #
 #    if left:
 #        win.blit(runAnimation[animCount // 5], (x, y))  # анимация персонажа
 #        animCount += 1
 #    elif right:
 #        win.blit(runAnimation[animCount // 5], (x, y))
 #        animCount += 1
 #    else:
 #        win.blit(runAnimation[5], (x, y))
 #        animCount = 0
