from time import sleep
import pygame
import pygame_menu
from pygame_menu import themes
 
pygame.init()
surface = pygame.display.set_mode((600, 400))
 
def set_mode(value, mode):
    print(value)
    print(mode)
 
def start_the_game():
    pass
 
def Mode_menu():
    mainmenu._open(level)
 
 
mainmenu = pygame_menu.Menu('Welcome', 600, 400, theme=themes.THEME_DARK)
mainmenu.add.text_input('Name: ', default='username', maxchar=20)
mainmenu.add.button('Play', start_the_game)
mainmenu.add.button('Mode', Mode_menu)
mainmenu.add.button('Quit', pygame_menu.events.EXIT)
 
level = pygame_menu.Menu('Select a Mode', 600, 400, theme=themes.THEME_DARK)
level.add.selector('mode :', [('Number', 1), ('Letters', 2)], onchange=set_mode)
 
mainmenu.mainloop(surface)