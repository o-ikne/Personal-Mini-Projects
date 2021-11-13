###########################################################
#                      Boule Sort                         #
###########################################################

## Libraries
import pygame
import math
import random

## Dimensions
## width & height
w = 800
h = 500

## Colors
GREEN = (34,139,34)
WHITE = (255,255,255)
GRAY = (128,128,128)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

## Boule Sort
def boule_sort(data, screen):  ##O(n^2)
	for i in range(len(data)):
		for j in range(len(data)-i-1):
			if data[j] > data[j+1]:
				data[j], data[j+1] = data[j+1], data[j]
				screen.fill(BLACK)
				for k in range(len(data)):
					pygame.draw.lines(screen, WHITE, False, [(k, h), (k, h-data[k])], 1)
				pygame.draw.lines(screen, RED, False, [(j, h), (j, h-data[j])], 2)
				pygame.display.update()
	return data
	
## Main function: Boule Sort
def main():
	pygame.init()
	screen = pygame.display.set_mode((w, h))
	pygame.display.set_caption('Boule Sort')
	clock = pygame.time.Clock()
	## generate random data
	data = [random.randint(1, h) for i in range(w)]
	boule_sort(data, screen)
	running = True
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()

		pygame.display.update()

		#clock.tick(1)
		
if __name__ == '__main__':
	main()
