from time import sleep
import pygame
import pygame_menu
from pygame_menu import themes
import count
 
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

pygame.init()
surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

m = [count.NUMBER]
 
def set_mode(value, mode):
    print(value)
    print(mode)
    m[0] = mode
    
 
def start_the_game():
    c = count.game(surface, m[0])
    c.loop()
 
def Mode_menu():
    mainmenu._open(level)
 
 
mainmenu = pygame_menu.Menu('Welcome', WINDOW_WIDTH, WINDOW_HEIGHT, theme=themes.THEME_DARK)
mainmenu.add.text_input('Name: ', default='username', maxchar=20)
mainmenu.add.button('Play', start_the_game)
mainmenu.add.button('Mode', Mode_menu)
mainmenu.add.button('Quit', pygame_menu.events.EXIT)
 
level = pygame_menu.Menu('Select a Mode', WINDOW_WIDTH, WINDOW_HEIGHT, theme=themes.THEME_DARK)
level.add.selector('mode :', [('Number', 1), ('Letters', 2)], onchange=set_mode)
 
mainmenu.mainloop(surface)