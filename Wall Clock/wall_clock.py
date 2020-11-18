# # Wall Clock

# ## Libraries

import pygame
from numpy import cos, sin, pi
from time import strftime, localtime


# ## Parameters & Colors

## colors
WHITE = (255,255,255)
BLUE = (28,128,128)
BLACK1 = (10, 30, 30)
BLACK2 = (20, 60, 60)
GRAY = (0,100,100)
RED = (180, 50, 28)
YELLOW = (255,255,50)

## Dimensions
w = 400
h = 600


# ## Clock

class Clock(object):
    
    def __init__(self, center:tuple, time=strftime('%H:%M:%S', localtime()), radius:int=160):
        self.time    = time   ## the local time
        self.radius  = radius ## the radius of the frame
        self.center  = center ## the center of the clock
        self.l_hrs   = 80     ## the lenght of hours pointer
        self.l_mnts  = 100    ## the lenght of minutes pointer
        self.l_scds  = 120    ## the lenght of seconds pointer
        
    def update(self):
        """update the time of the clock"""
        self.time = strftime('%H:%M:%S', localtime())
     
    @property
    def hours(self):
        """return the hours"""
        return int(self.time[0:2])
    
    @property
    def minutes(self):
        """return the minutes"""
        return int(self.time[3:5])
    
    @property
    def seconds(self):
        """return the seconds"""
        return int(self.time[6:8])
    
    def draw_seconds_pointer(self, screen):
        """draw the seconds pointer"""
        xs = self.center[0] + self.l_scds * cos(self.seconds / (3 * pi) - pi/2)
        ys = self.center[1] + self.l_scds * sin(self.seconds / (3 * pi) - pi/2)
        sx = -20 * cos(pi - self.seconds / (3 * pi) - pi/2)
        sy = +20 * sin(pi - self.seconds / (3 * pi) - pi/2)
        pygame.draw.lines(screen, WHITE, False, [self.center, (xs, ys)], 3) 
        pygame.draw.lines(screen, WHITE, False, [self.center, (self.center[0] + sx, self.center[1] + sy)], 3)
    
    def draw_minutes_pointer(self, screen):
        """draw the minutes pointer"""
        xm = self.center[0] + self.l_mnts * cos(self.minutes / (3 * pi) - pi/2)
        ym = self.center[1] + self.l_mnts * sin(self.minutes / (3 * pi) - pi/2)
        pygame.draw.lines(screen, RED, False, [self.center, (xm, ym)], 4)
    
    def draw_hours_pointer(self, screen):
        """draw the hours pointer"""
        xh = self.center[0] + self.l_hrs * cos(self.hours / (3 * pi) - pi/2)
        yh = self.center[1] + self.l_hrs * sin(self.hours / (3 * pi) - pi/2)
        pygame.draw.lines(screen, YELLOW, False, [self.center, (xh, yh)], 5)
        
    def draw_frame(self, screen):
        """draw the frame of the clock on the screen"""
        pygame.draw.circle(screen, BLACK2, self.center, self.radius)
        pygame.draw.circle(screen, GRAY, self.center, self.radius, 5)
        pygame.draw.circle(screen, BLACK2, self.center, self.radius + 10, 10)
        
    def draw_ticks(self, screen):
        """draw the ticks of the clock on the screen"""
        pygame.draw.circle(screen, GRAY, self.center, 10)
        for i in range(1, 13):
            x = self.center[0] + (self.radius - 30) * cos(5 * i / (3 * pi) - pi/2)
            y = self.center[1] + (self.radius - 30) * sin(5 * i / (3 * pi) - pi/2)
            if i % 3 == 0:
                pygame.draw.lines(screen, BLUE, False, [(x, y - 5), (x, y + 5)], 10)
            elif i % 3 != 0:
                pygame.draw.circle(screen, BLACK1, (int(x), int(y)), 3)
        
    def draw(self, screen):
        """draw the clock on the screen"""
        self.draw_frame(screen)
        self.draw_seconds_pointer(screen)
        self.draw_minutes_pointer(screen)
        self.draw_hours_pointer(screen)
        self.draw_ticks(screen)


# ## Main function

def main():
    ## initiate the screen
    pygame.font.init()
    screen = pygame.display.set_mode([w, h])
    screen.fill(BLACK1)
    pygame.display.set_caption('Wall Clock')
    font = pygame.font.SysFont('Decorative', 100)
    
    ## create a new Clock
    clock = Clock(center=(w//2, h//3))
    
    running = True 
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        screen.fill(BLACK1)
        clock.draw(screen)
        text = font.render(clock.time, True, YELLOW)
        screen.blit(text,(w//7, clock.center[1] + clock.radius + 50))
        pygame.draw.lines(screen, BLUE, False,
                          [(10, clock.center[1] + clock.radius + 120), (w - 10, clock.center[1] + clock.radius + 120)], 10)
        pygame.display.update()
        clock.update()
            
    pygame.quit()


if __name__ == '__main__':
    main()



