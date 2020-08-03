import pygame
from settings import USER_SCREEN_H, USER_SCREEN_W

platform_image = pygame.image.load("Tiles/Map/untitled - 2020-08-01T144248.637.png")

class Platform(pygame.sprite.Sprite):
    def __init__(self, groups, x, y, w, h):
        super().__init__(groups)
        self.image = pygame.transform.scale(platform_image, (180 , 180))
        #self.image = pygame.Surface((w, h))  #Создаём пустую поверхность для отрисовки
        self.rect = self.image.get_rect(x= x, y = y)
        #self.image.fill((234,54,222))
