## Libraries
import random
from tkinter import *
from tkinter.font import Font
from tkinter import messagebox
from copy import deepcopy

## Dimension 
w = 60 # the width of grid cells
h = 60 # the height og grid cells
 

def is_possible(n, x, y, grid):
	"""check if is it possible to put n in the position (x, y) of the matrix grid ?"""
	for i in range(len(grid)):
		if grid[x][i] == n:
			return False
	for j in range(len(grid[0])):
		if grid[j][y] == n:
			return False
	for i in range(3*(x//3), 3*(x//3+1)):
		for j in range(3*(y//3), 3*(y//3+1)):
			if grid[i][j] == n:
				return False
	return True


def find_empty(grid):
	"""return the next empty cells in the grid"""
	for i in range(len(grid)):
		for j in range(len(grid[0])):
			if grid[i][j] == ' ':
				return (i, j)  # row, col
	return None


def solve_sudoku(grid):
	"""to resolve a given sudoku scheme"""
	for i in range(len(grid)):
		for j in range(len(grid[0])):
			if grid[i][j] == ' ':
				for k in range(1, 10):
					if is_possible(k, i, j, grid):
						grid[i][j] = k
						solve_sudoku(grid)
						grid[i][j] = ' '    
				return
				
				
def solve(grid):
	"""solves a given sudoku grid"""
	find = find_empty(grid)
	if not find:
		return True
	else:
		row, col = find
	for i in range(1,10):
		if is_possible(i, row, col, grid):
			grid[row][col] = i
			if solve(grid):
				return True
			grid[row][col] = ' '
	return False


def create_sudoku(n, m):
	"""returns a random grid of size n x m"""
	grid = [[' ']*n for i in range(n)]
	for i in range(n):
		for j in range(1, n, 2):
			b = random.randint(1 ,9)
			if is_possible(b, i , j, grid):
				grid[i][j] = b
	return grid
	

def clic(event):
	"""return the coordinates & the element on the clicked cell"""
	j=event.x // w
	i=event.y // h
	coord['text']='coords('+str(i+1)+','+str(j+1)+')' + ', element: ' + str(sudoku_copy[i][j])


def play(event):
	"""create the interface to play"""
	j=event.x // w
	i=event.y // h
	x =  w * j + w // 2
	y =  h * i + h // 2
	
	global solution

	if sudoku[i][j] == ' ':
		reponse = Entry(fenetre)
		win = grill.create_window(x, y, height = w-1, width = h-1, window=reponse)
		
		def check(event):
			reponse.pack()
			a = reponse.get()
			if not a.isnumeric() or int(a) > 9 or int(a) < 1:
				messagebox.showerror("Error", "The entry must be a integer between 1 and 9 !")
			else:
				if is_possible(int(a), i, j, sudoku_copy):
					sudoku_copy[i][j] = ' '
					grill.create_rectangle(x-w//2, y-h//2, x+w//2, y+h//2, fill="white", width=1)

					for k in range(3, 7, 3):
						grill.create_line(k*w, 0, k*h, 9*w, width=2)
						grill.create_line(0, k*w, 9*h, k*h, width=2)
						
					grill.create_text(x, y, text = int(a), font=fontStyle)
					sudoku_copy[i][j] = int(a)

				else:
					grill.create_rectangle(x-w//2, y-h//2, x+w//2, y+h//2, fill="white", width=1)
					for k in range(3, 7, 3):
						grill.create_line(k*w, 0, k*h, 9*w, width=2)
						grill.create_line(0, k*w, 9*h, k*h, width=2)
					grill.create_text(x, y, text = int(a), fill = "red", font=fontStyle)
		   
	## if managed to solve !         
	if sudoku_copy == solution:
		messagebox.showinfo("Win","Sa7iiit ;)") 
	reponse.bind("<Return>", check)


def key(event):
	"""manage key events"""
	touche = event.keysym
	if touche == "Up":
		event.x -= w
	if touche == 'Down':
		event.x += w
	if touche == 'Right':
		event.y += h
	if touche == 'Left':
		event.y -= h


def solve_auto():    
	"""automatique solving"""
	global sudoku
	def solve(sudoku):
		find = find_empty(sudoku)
		if not find:
			return True
		else:
			i, j = find
		for k in range(1,10):
			if is_possible(k, i, j, sudoku):
				sudoku[i][j] = k
				grill.create_rectangle(j*w,i*h, (j+1)*w, (i+1)*h, fill="#80FF33", width=1)                    
				grill.create_text(w*j +w//2, h*i+h//2, text=sudoku[i][j], font=fontStyle)
				for l in range(3, 7, 3):
					grill.create_line(l*w, 0, l*h, 9*w, width=2)
					grill.create_line(0, l*w, 9*h, l*h, width=2)
				if solve(sudoku):
					return True
				sudoku[i][j] = ' '
		return False
	solve(sudoku)


## create a grid
sudoku = create_sudoku(9, 3)
## create a copy
sudoku_copy = deepcopy(sudoku)
## empty solution
solution = deepcopy(sudoku)


## 
solve(solution)

# fenêtre Tkinter
fenetre = Tk()
fenetre.title("sudoku")
grill = Canvas(fenetre,height=540,width=540)
grill.pack()
grid = [[grill.create_rectangle((i-1)*w,(j-1)*h, i*w, j*h, fill="#FFFFFF" , width=1)
										for i in range(1, 10)] for j in range(1, 10)]

## define a font style
fontStyle = Font(family="Roman", size=15)

## draw the grid
for i in range(3, 7, 3):
	grill.create_line(i*w, 0, i*h, 9*w, width=2)
	grill.create_line(0, i*w, 9*h, i*h, width=2)
	
## put text in the grid
for i in range(9):
	for j in range(9):
		grill.create_text(w*j + w//2, h*i+ h//2, text=sudoku_copy[i][j], font=fontStyle, fill='gray')

#grill.bind('<ButtonRelease-1>',clic)
grill.bind("<ButtonRelease-1> ", play)

coord = Label(fenetre)
coord.pack(pady='10px')

button_solve = Button(fenetre,text="Solve",command=solve_auto, bg='#80FF33')           
button_solve.pack(side=LEFT)
button_exit = Button(fenetre,text="Exit",command=fenetre.destroy, bg='white', fg ='red')           
button_exit.pack(side=RIGHT)

fenetre.mainloop()
