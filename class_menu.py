import pygame
import ctypes

pygame.init()

#ШРИФТЫ
fontImpact = pygame.font.SysFont("Impact", 72)


user32 = ctypes.windll.user32
USER_SCREEN_W, USER_SCREEN_H = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

BUTTON_W = USER_SCREEN_W * 0.75
BUTTON_H = 100


class Button(pygame.sprite.Sprite):
	def __init__(self, text, x, y, width = BUTTON_W, height = BUTTON_H ):
		super().__init__()
		self.width = width
		self.height = height
		self.text = fontImpact.render(text, 1, (0, 100, 0))
		self.textrect = self.text.get_rect(centerx = self.width//2, centery = self.height//2 )
		self.image = pygame.Surface((self.width, self.height))
		self.rect = self.image.get_rect(centerx = USER_SCREEN_W//2, y = y)
		self.active = False
		self.activeColor = (0, 255, 0)
		self.baseColor = (0, 0, 255)




	def update(self, *args):
		if self.active:
			self.image.fill(self.activeColor)
			self.image.blit(self.text, self.textrect)
		else:
			self.image.fill(self.baseColor)
			self.image.blit(self.text, self.textrect)




class Menu():
	def __init__(self, win):
		self.win = win #Экран для отрисовки

		self.activeButton = 0  # Бывшая переменная num, какая кнопка сейчас активна
		self.buttons= [		Button("button1", 50, 50+(BUTTON_H +100)*0),
							Button("button2", 50, 50+(BUTTON_H +100)*1),
							Button("button3", 50, 50+(BUTTON_H +100)*2),
							Button("button4", 50, 50+(BUTTON_H +100)*3),
							Button("button5", 50, 50+(BUTTON_H +100)*4),
						]


	def update(self):
		self.win.fill((56,67,128))


		for b in self.buttons:
			b.update()
			self.win.blit(b.image, b.rect)
		pygame.display.update()

	def up(self):
		if self.activeButton != 0:
			self.buttons[self.activeButton].active = False
			self.activeButton-=1
			self.buttons[self.activeButton].active = True

	def down(self):
		if self.activeButton +1 !=len(self.buttons):
			self.buttons[self.activeButton].active = False
			self.activeButton+=1
			self.buttons[self.activeButton].active = True

