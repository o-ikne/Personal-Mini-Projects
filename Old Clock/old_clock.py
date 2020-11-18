
# # Old Clock



# ## Libraries

import pygame
from numpy import cos, sin, pi,random
from time import strftime, localtime


# ## Color & Parameters

## colors
GREEN = (34,139,34)
WHITE = (255,255,255)
GRAY = (128,128,128)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
YELLOW = (255,255,0)
BLUE = (28,128,130)
MAGENTA = (128,28,128)

## Dimensions
w = 300
h = 600


# ## Clock

class Clock(object):
    def __init__(self, center:tuple, time=strftime('%H:%M:%S', localtime()), radius=50, l_pointer=300):
        self.x = 0
        self.y = 0
        self.center = center
        self.time = time
        self.radius = radius
        self.teta = 575
        self.l_pointer = l_pointer
        self.dteta = -1
        self.color = BLUE

    def update(self):  
        """update the time and the position of the pointer"""
        self.time = strftime('%H:%M:%S', localtime())
        self.x = self.center[0] + self.l_pointer * cos(self.teta / 360)
        self.y = self.center[1] + self.l_pointer * sin(self.teta / 360) 
        self.teta += self.dteta
        if self.teta <450 or self.teta >680:
            self.dteta = -self.dteta
            self.set_color()
            
    def set_color(self):
        """set a random color"""
        self.color = random.randint(0, 255, 3)
            
    def draw_text(self, screen, font):
        """draw the text on the screen"""
        time_text    = font.render(self.time[:5], True, self.color)
        seconds_text = font.render(self.time[6:8], True, self.color)
        date_text    = font.render(strftime('%Y-%m-%d', localtime()), True, self.color)
        
        screen.blit(seconds_text, (self.x - 10, self.y - 10))
        screen.blit(time_text, (w//3 + 30, h - 100))
        screen.blit(date_text, (w//3, h - 50))
        
    def draw(self, screen):
        """draw the clock on the screen"""
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius, 1)
        pygame.draw.circle(screen, self.color, (int(self.center[0]), int(self.center[1])), 10)


# ## Main function

def main():
    pygame.init()
    screen = pygame.display.set_mode((w, h))
    pygame.display.set_caption('Old Clock')
    pygame_clock = pygame.time.Clock()
    running = True
    clock = Clock(center=(w//2, h//6))
    font = pygame.font.SysFont('Decorative', 30)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        screen.fill(BLACK)
        clock.update()
        clock.draw_text(screen, font)
        clock.draw(screen)
        
        pygame.display.update()
        pygame_clock.tick(250)
             
    pygame.quit()
                


if __name__ == '__main__':
    main()

