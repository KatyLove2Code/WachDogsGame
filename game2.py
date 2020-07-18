#################################
#ЕСЛИ ХОТИТЕ ЧТО-ТО ИЗМЕНИТЬ ПРЕДУПРЕДИТЕ МЕНЯ!!!!
#################################
import pygame
pygame.init()
width_win = 500
height_win = 500#РАЗМЕР ОКНА ПИШИТЕ СЮДА
win = pygame.display.set_mode((width_win, height_win))
pygame.display.set_caption("Mario")



x = 50
y = 425
width = 40
height = 60
speed = 5

isJump = False
jumpCount = 10
pygame.joystick.init()
cnopk_on = False

my_joystick = pygame.joystick.Joystick(0)
my_joystick.init()

joysticks = []
for i in range(0, pygame.joystick.get_count()):
	joysticks.append(pygame.joystick.Joystick(i))
	joysticks[-1].init()

run = True
pygame.draw.rect(win, (0, 0, 255), (x, int(y), width, height))
keys = pygame.key.get_pressed()
menu = True
num = 1
while  menu:
	if keys[pygame.K_UP]:
		num=1

	if keys[pygame.K_DOWN]:
		num=2

	if num == 1:
		pygame.draw.rect(win, (0, 255, 0), (200, 150, 100, 60))
		pygame.draw.rect(win, (0, 0, 255), (200, 250, 100, 60))
	if num == 2:
		pygame.draw.rect(win, (0, 0, 255), (200, 150, 100, 60))
		pygame.draw.rect(win, (0, 255, 0), (200, 250, 100, 60))


	pygame.time.delay(10)
	pygame.display.update()

while  run:
	pygame.time.delay(10)




	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False


	if my_joystick.get_hat(0) == (-1, -1):
		x -= speed
		y += speed
	if my_joystick.get_hat(0) == (1, 1):
		x += speed
		y -= speed
	if my_joystick.get_hat(0) == (-1, 1):
		x -= speed
		y -= speed
	if my_joystick.get_hat(0) == (1, -1):
		x += speed
		y += speed



	if keys[pygame.K_LEFT] or my_joystick.get_hat(0) == (-1, 0) and x > 5:
		x -= speed

	if keys[pygame.K_RIGHT] or my_joystick.get_hat(0) == (1, 0) and x < 500	 - width - 5:
		x += speed
	if not(isJump):
		if keys[pygame.K_UP] or my_joystick.get_hat(0) == (0, 1) and y > 5:
			y -= speed
		if keys[pygame.K_DOWN] or my_joystick.get_hat(0) == (0, -1) and y < 500 - height - 15:
			y += speed
		if keys[pygame.K_SPACE]:
			isJump = True
	else:
		if jumpCount >= - 10:
			y -= (jumpCount ** 2) / 2
			jumpCount -= 1
		else:
			isJump = False
			jumpCount = 10


	win.fill((0,0,0))
	pygame.draw.rect(win, (0, 0, 255), (x, int(y), width, height))
	pygame.display.update()


pygame.quit()
