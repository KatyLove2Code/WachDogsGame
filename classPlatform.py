import pygame

class Platform(pygame.sprite.Sprite):
    def __init__(self, groups, x, y, w, h):
        super().__init__(groups)
        self.image = pygame.Surface((w, h))  #Создаём пустую поверхность для отрисовки
        self.rect = self.image.get_rect(x= x, y = y)
        self.image.fill((234,54,222))
