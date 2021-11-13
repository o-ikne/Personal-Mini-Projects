###########################################################
#                    Selection Sort                       #
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

## Selection Sort
def selection_sort(data, screen):  ## O(nlog(n))
	for i in range(len(data)-1):
		mini = i
		for j in range(i+1, len(data)):
			if data[j] < data[mini]:
				mini = j
		if mini != i:
			data[i], data[mini] = data[mini], data[i]
			screen.fill(BLACK)
			for k in range(len(data)):
				pygame.draw.lines(screen, WHITE, False, [(k, h), (k, h-data[k])], 1)
			pygame.draw.lines(screen, RED, False, [(i, h), (i, h-data[i])], 2)
			pygame.display.update()
	return data
	
## main function: selection Sort
def main():
	pygame.init()
	screen = pygame.display.set_mode((w, h))
	pygame.display.set_caption('Selection Sort')
	clock = pygame.time.Clock()
	## generate random data
	data = [random.randint(1, h) for i in range(w)]
	selection_sort(data, screen)
	running = True
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()

		pygame.display.update()
		
if __name__ == '__main__':
	main()
