import pygame
from pygame.locals import *
import random
import math
import datetime

NUMBER = 1
LETTER = 2

dotVals = {
    1:"one",
    2:"two",
    3:"three",
    4:"four",
    5:"five",
    6:"six",
    7:"seven",
    8:"eight",
    9:"nine",
    10:"ten"
}

class numberDot:
    radius = 40
    def __init__(self, surface: pygame.Surface, num:int, type: int):
        self.surface = surface
        self.x = random.randint(numberDot.radius, surface.get_width()-numberDot.radius)
        self.y = random.randint(numberDot.radius, surface.get_height()-numberDot.radius)
        self.num = num
        self.type = type
        if(type == NUMBER):
            self.text = num
        else:
            self.text = dotVals.get(num)
        

    def draw(self):
        pygame.draw.circle(self.surface, (255, 0, 0), (self.x, self.y), numberDot.radius)
        if self.type == NUMBER:
            textSize = 40
        else:
            textSize = 30
        font = pygame.font.SysFont(None, textSize)
        num = font.render(str(self.text), True, 'white')
        self.surface.blit(num, (self.x-20, self.y-10))
        pass
    
    def isClicked(self, pos: (int, int)) -> bool:

        dist = math.sqrt((pos[0]-self.x)**2 + (pos[1]-self.y)**2)
        if dist > self.radius:
            return False
        return True

class game:

    def __init__(self, surface, type):
        self.surface = surface
        self.lost = False
        self.currentNum = 1
        self.dots = []
        self.score = 0
        for i in range(1, 11):
            self.dots.append(numberDot(surface, i, type))
            pass
        self.clock = pygame.time.Clock()
    
    def loop(self):
        screen = self.surface
        
        while self.lost  == False:
            screen.fill('white')

            # event handling
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.lost = True
                if event.type == MOUSEBUTTONDOWN:
                    for dot in self.dots:
                        if dot.isClicked(pygame.mouse.get_pos()):
                            if(dot.num == self.currentNum):
                                self.score += 10
                                self.currentNum += 1
                            else:
                                self.lost = True
                                f = open("scores/score.txt", "a") # save score
                                # https://stackoverflow.com/questions/7999935/python-datetime-to-string-without-microsecond-component
                                f.write("{date}: {score}\n".format(date=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), score=self.score))
                            self.dots.remove(dot)
            

            for dot in self.dots:
                dot.draw()
             
            self.displayScore()
            pygame.display.flip() 
    
    def displayScore(self):
        font = pygame.font.SysFont(None, 40)
        num = font.render("Score: {score}".format(score = self.score), True, 'black')
        self.surface.blit(num, (20, self.surface.get_height()-40))