#################################
#ЕСЛИ ХОТИТЕ ЧТО-ТО ИЗМЕНИТЬ ПРЕДУПРЕДИТЕ МЕНЯ!!!!
#################################
import pygame

pygame.init()
win = pygame.display.set_mode((1024, 720))

pygame.display.set_caption("Mario")

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

playerStand = [pygame.image.load("Tiles/Character/Animations/Idle/Armature_Idle_00.png"),
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

bg = pygame.image.load('Tiles/bg/bg.png')


clock = pygame.time.Clock()

padOn = False
keyboard = True


x = 50
y = 425
width = 600
height = 600

x = 5
y = 5
width = 65
height = 65

speed = 5

isJump = False
jumpCount = 10
jumpCount1 = 10
pygame.joystick.init()
left = False
right = False
animCount = 0;




def drawWindow(): # рисование всей карты
	global animCount
	global walkAnim
	global idleAnim

	win.blit(bg, (0, 0))
	
	if animCount + 1 >= 60:
		animCount = 0
	
	if left:
		win.blit(walk[animCount // 5], (x, y)) # анимация персонажа
		animCount += 1
	elif right:
		win.blit(walk[animCount // 5], (x, y))
		animCount += 1
	else:
		win.blit(playerStand[animCount // 5], (x, y))
		animCount += 1


	pygame.display.update()


try:
	my_joystick = pygame.joystick.Joystick(0)
	my_joystick.init()
	joysticks = []
	for i in range(0, pygame.joystick.get_count()):
		joysticks.append(pygame.joystick.Joystick(i))
		joysticks[-1].init()
except:
	print('Joystick not found')
	padOn = False

run = True
while run:
	clock.tick(60)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	keys = pygame.key.get_pressed()

	#if keys[pygame.K_p] and padOn == False:
		#padOn = True
		#keyboard = False
		#print("True")

	if keys[pygame.K_o] and padOn == True:
		padOn = False
		keyboard = True
		print("False")
		isJump = False
	if padOn == True:

		#if my_joystick.get_hat(0) == (-1, -1) and x > 5 and y < 720 - height - 15:
			#x -= speed
			#y += speed
		#if my_joystick.get_hat(0) == (1, 1) and x < 1024 - width - 5 and y > 5:
			#x += speed
			#y -= speed
		#if my_joystick.get_hat(0) == (-1, 1) and x > 5 and y > 5:
			#x -= speed
			#y -= speed
		#if my_joystick.get_hat(0) == (1, -1) and x < 1024 - width - 5 and y < 720 - height - 15:
			#x += speed
			#y += speed
		if my_joystick.get_hat(0) == (-1, 0) and x > 5:
			x -= speed
		if my_joystick.get_hat(0) == (1, 0) and x < 1024 - width - 5:
			x += speed
		#if  my_joystick.get_hat(0) == (0, 1) and y > 5:
			#y -= speed
		#if my_joystick.get_hat(0) == (0, -1) and y < 720 - height - 15:
			#y += speed
		if event.type == pygame.JOYBUTTONDOWN:
			if not(isJump):

				if event.button == 0:
					isJump = True
			else:
				if jumpCount1 >= - 10:
					if jumpCount1 < 0:
						y += (jumpCount1 ** 2) / 2
					else:
						y -= (jumpCount1 ** 2) / 2
					jumpCount1 -= 1
				else:
					isJump = False
					jumpCount1 = 10



	if keyboard == True:

		if keys[pygame.K_a] and x > 5:
			x -= speed
			left = True
			right = False
		elif keys[pygame.K_d] and x < 1024 - width - 5:
			x += speed
			right = True
			left = False
		else:
			left = False
			right = False
			animCount = 0

		if not(isJump):

			if keys[pygame.K_SPACE]:
				isJump = True
		else:
			if jumpCount >= - 10:
				if jumpCount < 0:
					y += (jumpCount ** 2) / 2
				else:
					y -= (jumpCount ** 2) / 2
				jumpCount -= 1
			else:
				isJump = False
				jumpCount = 10

	drawWindow()



pygame.quit()
