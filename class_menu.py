import pygame
from settings import USER_SCREEN_H, USER_SCREEN_W

pygame.init()

# ШРИФТЫ
fontImpact = pygame.font.SysFont("Impact", 72)




BUTTON_H = int(USER_SCREEN_H * 0.25)
BUTTON_W = int(USER_SCREEN_W * 0.40)

BUTTON_H = 260
BUTTON_W = 640

button_base = [
    pygame.Surface((BUTTON_W, BUTTON_H - 50)),
    pygame.Surface((BUTTON_W, BUTTON_H - 50))
]

button_start = [
    pygame.image.load("Tiles/GUI/play_button_passive.764.png").subsurface(0, 200, BUTTON_W, BUTTON_H),
    pygame.image.load("Tiles/GUI/play_button_active.352.png").subsurface(0, 200, BUTTON_W, BUTTON_H),

]

button_exit = [
    pygame.image.load("Tiles/GUI/exit_button_passive.208.png").subsurface(0, 200, BUTTON_W, BUTTON_H),
    pygame.image.load("Tiles/GUI/exit_button_active.139.png").subsurface(0, 200, BUTTON_W, BUTTON_H),

]

button_base[0].fill((100, 100, 100))
button_base[1].fill((255, 0, 0))


class Button(pygame.sprite.Sprite):
    def __init__(self, button_name, y, width=BUTTON_W, height=BUTTON_H):  ### button_name - какая кнопка вызывается
        super().__init__()
        self.button_name = button_name
        self.width = width
        self.height = height

        self.active = False

        if self.button_name == 'START':
            self.images = button_start
        elif self.button_name == 'EXIT':
            self.images = button_exit
        else:
            self.images = button_base

        self.image = self.images[self.active]

        self.rect = self.image.get_rect(centerx=USER_SCREEN_W // 2, y=y)



    def update(self, *args):
        self.image = self.images[self.active]



class Menu():
    def __init__(self, win):
        self.win = win  # Экран для отрисовки

        self.activeButton = 0  # Бывшая переменная num, какая кнопка сейчас активна
        self.buttons = [Button("START", (BUTTON_H) * 0+230),
                        #Button("OPTIONS", (BUTTON_H) * 1),
                        Button("EXIT", (BUTTON_H) * 1+270),
                        ]

    def update(self):
        self.win.fill((56, 67, 128))

        for b in self.buttons:
            b.update()
            self.win.blit(b.image, b.rect)
        pygame.display.update()

    def up(self):
        if self.activeButton != 0:
            self.buttons[self.activeButton].active = False
            self.activeButton -= 1
            self.buttons[self.activeButton].active = True

    def down(self):
        if self.activeButton + 1 != len(self.buttons):
            self.buttons[self.activeButton].active = False
            self.activeButton += 1
            self.buttons[self.activeButton].active = True
