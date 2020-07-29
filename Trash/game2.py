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
num = 1
pervst = True
vtst = False
main_menu = True
menuButton1x = 100
menuButton1y = 60
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
keys = pygame.key.get_pressed()
#первая кн#
pygame.draw.rect(win, (0, 0, 255), ((width_win / 2-60), (height_win / 2 - 100), menuButton1x, menuButton1y))
#2кн#
pygame.draw.rect(win, (0, 0, 255), ((width_win / 2-60), (height_win / 2), menuButton1x, menuButton1y))
#3кн#
pygame.draw.rect(win, (0, 0, 255), ((width_win / 2-60), (height_win / 2 + 100), menuButton1x, menuButton1y))

def menu_op(win):
	menu_op1 = True
	numOp = 1

	while menu_op1:
		event = pygame.event.get()
		keys = pygame.key.get_pressed()
		if keys[pygame.K_UP]:
			numOp-=1
		if keys[pygame.K_DOWN]:
			numOp +=1

		if numOp == 3:
			numOp = 2
		elif numOp == 0:
			numOp = 1

		if numOp == 1:
			pygame.draw.rect(win, (0, 255, 0), ((width_win / 2-60), (height_win / 2 - 100), menuButton1x, menuButton1y))
			pygame.draw.rect(win, (0, 0, 255), (200, 250, 100, 60))
		elif numOp == 2:
			pygame.draw.rect(win, (0, 0, 255), ((width_win / 2-60), (height_win / 2 - 100), menuButton1x, menuButton1y))
			pygame.draw.rect(win, (0, 255, 0), (200, 250, 100, 60))

		pygame.time.delay(50)
		pygame.display.update()

while  main_menu:
	event = pygame.event.get()
	keys = pygame.key.get_pressed()

	if keys[pygame.K_UP]:
		num-=1
	if keys[pygame.K_DOWN]:
		num +=1

	if num == 4:
		num = 3
	elif num == 0:
		num = 1

	if num == 1:
		pygame.draw.rect(win, (0, 255, 0), ((width_win / 2-60), (height_win / 2 - 100), menuButton1x, menuButton1y))
		pygame.draw.rect(win, (0, 0, 255), (200, 250, 100, 60))
		pygame.draw.rect(win, (0, 0, 255), (200, 350, 100, 60))
	elif num == 2:
		pygame.draw.rect(win, (0, 0, 255), ((width_win / 2-60), (height_win / 2 - 100), menuButton1x, menuButton1y))
		pygame.draw.rect(win, (0, 255, 0), (200, 250, 100, 60))
		pygame.draw.rect(win, (0, 0, 255), (200, 350, 100, 60))
	elif num == 3:
		pygame.draw.rect(win, (0, 0, 255), ((width_win / 2-60), (height_win / 2 - 100), menuButton1x, menuButton1y))
		pygame.draw.rect(win, (0, 0, 255), (200, 250, 100, 60))
		pygame.draw.rect(win, (0, 255, 0), (200, 350, 100, 60))
	if keys[pygame.K_RIGHT]:
		if num == 1:
			main_menu = False
		elif num == 2:
			pygame.draw.rect(win, (0, 0, 0), (200, 150, 100, 60))
			pygame.draw.rect(win, (0, 0, 0), (200, 250, 100, 60))
			pygame.draw.rect(win, (0, 0, 0), (200, 350, 100, 60))
			menu_op(win)


	pygame.time.delay(50)
	pygame.display.update()
#конец кода меню

isJump = False
jumpCount = 10
pygame.joystick.init()

my_joystick = pygame.joystick.Joystick(0)
my_joystick.init()

joysticks = []
for i in range(0, pygame.joystick.get_count()):
	joysticks.append(pygame.joystick.Joystick(i))
	joysticks[-1].init()
cnopk_on = False
run = True
pygame.draw.rect(win, (0, 0, 255), (x, int(y), width, height))
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


	keys = pygame.key.get_pressed()
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



	pygame.time.delay(10)
	pygame.display.update()
pygame.quit()
