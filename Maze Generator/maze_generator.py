###########################################################
#                    Maze Generator                       #
###########################################################


## Libraries
import pygame
import random


## Colors & Parameters

## colors
GREEN  = (34, 200, 34)
WHITE  = (255, 255, 255)
GRAY   = (128, 128, 128)
RED    = (200, 0, 0)
BLACK  = (0, 0, 0)
YELLOW = (255, 255, 0)
colors = [GREEN, GRAY, RED, YELLOW]

## Dimensions
w  = 800 # the width of the grid
h  = 500 # the height of the grid
rw = 20  # the width of grid's cells
rh = 20  # the height of the grid's cells


## Cell Class
class Cell:
    def __init__(self, i:int=0, j:int=0, line_width:int=1, color:tuple=BLACK):
        self.i = i
        self.j = j
        self.top_edge = True
        self.bottom_edge = True
        self.right_edge = True
        self.left_edge = True
        self.line_width = line_width
        self.is_viseted = False
        self.color = color
        
            
    def draw(self, screen):
        """draw the cell edges on the screen"""
        if self.top_edge:
            pygame.draw.lines(screen, self.color, False, [(self.i * rw, self.j * rh), ((self.i + 1) * rw, self.j * rh)], self.line_width)
        if self.bottom_edge:
            pygame.draw.lines(screen, self.color, False, [(self.i * rw, (self.j + 1) * rh), ((self.i + 1) * rw, (self.j + 1) * rh)], self.line_width)
        if self.left_edge:
            pygame.draw.lines(screen, self.color, False, [(self.i * rw, self.j * rh), (self.i * rw, (self.j + 1) * rh)], self.line_width)
        if self.right_edge:
            pygame.draw.lines(screen, self.color, False, [((self.i + 1) * rw, self.j * rh), ((self.i + 1) * rw, (self.j + 1) * rh)], self.line_width)


## Maze Class
class Maze:
    def __init__(self):
        self.cells = [[Cell(i=j, j=i) for j in range(w // rw)]  for i in range(h // rh)]
          
    def get_neighbours(self, cell:Cell) -> list:
        """return the neighbours of a cell"""
        neigbours = []
        for i in range(max(0, cell.i - 1), min(len(self.cells[0]), cell.i + 2)):
            for j in range(max(0, cell.j - 1), min(len(self.cells), cell.j + 2)):
                if (i == cell.i or j == cell.j) and not self.cells[j][i].is_viseted:
                    neigbours.append(self.cells[j][i])
        return neigbours
    
    def remove_edge(self, cell1:Cell, cell2:Cell):
        """remove the edge between the cell1 and cell2"""
        i = cell2.i - cell1.i
        j = cell2.j - cell1.j
        if i == 1:
            cell1.right_edge = False
            cell2.left_edge = False
        elif i == -1:
            cell1.left_edge = False
            cell2.right_edge = False
        elif j == 1:
            cell1.bottom_edge = False
            cell2.top_edge = False            
        elif j == -1:
            cell1.top_edge = False
            cell2.bottom_edge = False         
         
    def draw(self, screen):
        """draw the cells edges of the grid on the screen"""
        for row in self.cells:
            for cell in row:
                cell.draw(screen)


## Main Function
def main():
    pygame.font.init()
    ## initiate the screen
    screen = pygame.display.set_mode((w, h))
    pygame.display.set_caption('Maze Generator')
    screen.fill(WHITE)
    clock = pygame.time.Clock()
    font = pygame.font.SysFont('Decorative', 50)
    text = font.render('press any key to start', True, BLACK)   
    screen.blit(text, (w//8, h//2))
    
    ## create a new maze
    maze = Maze()
    start = maze.cells[0][0]
    end = maze.cells[-1][-1]
    
    pygame.display.update()
    
    ## initiate none visited cells
    not_visited = []
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            
            elif event.type == pygame.KEYDOWN:
                current_cell = maze.cells[0][0]
                current_cell.is_viseted = True
                not_visited += [current_cell]      
                while not_visited:
                    current_cell = not_visited.pop()
                    if maze.get_neighbours(current_cell):
                        not_visited.append(current_cell)
                        next_cell = random.choice(maze.get_neighbours(current_cell))
                        maze.remove_edge(current_cell, next_cell)
                        next_cell.is_viseted = True
                        not_visited.append(next_cell)
                    screen.fill(WHITE)
                    coord = (current_cell.i * rw + current_cell.line_width, current_cell.j * rh + current_cell.line_width,
                             rw - current_cell.line_width, rh - current_cell.line_width)
                    pygame.draw.rect(screen, YELLOW, coord)
                    pygame.draw.rect(screen, GREEN, (start.i * rw + start.line_width, start.j * rh + start.line_width,
                                             rw - start.line_width, rh - start.line_width))
                    pygame.draw.rect(screen, RED, (end.i * rw + end.line_width, end.j * rh + end.line_width,
                                             rw - end.line_width, rh - end.line_width))
                    maze.draw(screen)
                    pygame.display.update()
                    clock.tick(10)



if __name__ == '__main__':
    main()
