###########################################################
#                       Quick Sort                        #
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

## Quick Sort
def quick_sort(data, s, e, screen):
	if s < e:
		pivot = random.choice(data[s:e])
		pivot = partition(data, s, e, pivot, screen)
		quick_sort(data, s, pivot-1, screen)
		quick_sort(data, pivot+1, e, screen)
	 
## partition method   
def partition(data, s, e, pivot, screen):
	data[s], data[pivot] = data[pivot], data[s]
	j = s
	for i in range(s-1):
		if data[i] <= data[s]:
			data[i], data[j] = data[j], data[i]
			j += 1
			screen.fill(BLACK)
			for k in range(len(data)):
				pygame.draw.lines(screen, WHITE, False, [(k, h), (k, h-data[k])], 1)
			pygame.display.update()
	data[s], data[j] = data[j], data[s]
	return j
	
## Main function: Visualize Quick sort
def main():
	pygame.init()
	screen = pygame.display.set_mode((w, h))
	pygame.display.set_caption('Quick sort')
	clock = pygame.time.Clock()
	## generate random data
	data = [random.randint(1, h) for i in range(w)]
	quick_sort(data, 0, len(data)-1, screen)
	running = True
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()

		pygame.display.update()
		
if __name__ == '__main__':
	main()
