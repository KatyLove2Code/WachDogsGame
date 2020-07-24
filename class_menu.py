import pygame
pygame.init()
num = 1
main_menu = True
cnopk_on = False

import ctypes
user32 = ctypes.windll.user32
USER_SCREEN_W, USER_SCREEN_H = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

class Menu(win):
    def main_menu(win):
        self.win = win
        menuButton1x = 100
        menuButton1y = 60
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
        		pygame.draw.rect(self.win, (0, 255, 0), ((USER_SCREEN_W / 2-menuButton1y), (USER_SCREEN_H / 2 - menuButton1x), menuButton1x, menuButton1y))
        		pygame.draw.rect(self.win, (0, 0, 255), ((USER_SCREEN_W / 2-menuButton1y), (USER_SCREEN_H / 2), menuButton1x, menuButton1y))
        		pygame.draw.rect(self.win, (0, 0, 255), ((USER_SCREEN_W / 2-menuButton1y), (USER_SCREEN_H / 2 - menuButton1x), menuButton1x, menuButton1y))
        	elif num == 2:
        		pygame.draw.rect(self.win, (0, 0, 255), ((USER_SCREEN_W / 2-menuButton1y), (USER_SCREEN_H / 2 - menuButton1x), menuButton1x, menuButton1y))
        		pygame.draw.rect(self.win, (0, 255, 0), ((USER_SCREEN_W / 2-menuButton1y), (USER_SCREEN_H / 2), menuButton1x, menuButton1y))
        		pygame.draw.rect(self.win, (0, 0, 255), ((USER_SCREEN_W / 2-menuButton1y), (USER_SCREEN_H / 2 - menuButton1x), menuButton1x, menuButton1y))
        	elif num == 3:
        		pygame.draw.rect(self.win, (0, 0, 255), ((USER_SCREEN_W / 2-menuButton1y), (USER_SCREEN_H / 2 - menuButton1x), menuButton1x, menuButton1y))
                pygame.draw.rect(self.win, (0, 255, 0), ((USER_SCREEN_W / 2-menuButton1y), (USER_SCREEN_H / 2), menuButton1x, menuButton1y))
        		pygame.draw.rect(self.win, (0, 255, 0), ((USER_SCREEN_W / 2-menuButton1y), (USER_SCREEN_H / 2 - menuButton1x), menuButton1x, menuButton1y))

            if keys[pygame.K_RIGHT]:
        		if num == 1:
        			main_menu = False
        		elif num == 2:
        			pygame.draw.rect(self.win, (0, 0, 0), ((USER_SCREEN_W / 2-menuButton1y), (USER_SCREEN_H / 2 - menuButton1x), menuButton1x, menuButton1y))
                    pygame.draw.rect(self.win, (0, 0, 0), ((USER_SCREEN_W / 2-menuButton1y), (USER_SCREEN_H / 2 ), menuButton1x, menuButton1y))
        			pygame.draw.rect(self.win, (0, 0, 0), ((USER_SCREEN_W / 2-menuButton1y), (USER_SCREEN_H / 2 - menuButton1x), menuButton1x, menuButton1y))
        			menu_op(self.win)


        	pygame.time.delay(60)
        	pygame.display.update()

    def menu_op(win):
    	menu_op1 = True
    	numOp = 1
        self.win = win
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
    			pygame.draw.rect(self.win, (0, 255, 0), ((USER_SCREEN_W / 2-menuButton1y), (USER_SCREEN_H / 2 - menuButton1x), menuButton1x, menuButton1y))
    			pygame.draw.rect(self.win, (0, 0, 255), ((USER_SCREEN_W / 2-menuButton1y), (USER_SCREEN_H / 2 ), menuButton1x, menuButton1y))
    		elif numOp == 2:
    			pygame.draw.rect(self.win, (0, 0, 255), ((USER_SCREEN_W / 2-menuButton1y), (USER_SCREEN_H / 2 - menuButton1x), menuButton1x, menuButton1y))
    			pygame.draw.rect(self.win, (0, 255, 0), ((USER_SCREEN_W / 2-menuButton1y), (USER_SCREEN_H / 2 ), menuButton1x, menuButton1y))

    		pygame.time.delay(60)
    		pygame.display.update()
