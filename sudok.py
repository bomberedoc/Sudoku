class Sudoku:
	def __init__(self,grid):
		self.grid=grid

	def check_box(self,digit,r,c):
		b1,b2=int(r/3),int(c/3)
		for i in range(b1*3,b1*3+3):
			for j in range(b2*3,b2*3+3):
				if i!=r and j!=c:
					if self.grid[i][j]==digit:
						return False
		return True	

	def check_vert(self,digit,r,c):
		for i in range(0,9):
			if i!=r:
				if self.grid[i][c]==digit:
					return False
		return True

	def check_hor(self,digit,r,c):
		for j in range(0,9):
			if j!=c:
				if self.grid[r][j]==digit:
					return False
		return True

	def check_grid(self):
		s=0
		for i in range(0,9):
			for j in range(0,9):
				if self.grid[i][j]==0:
					s=1
					break
			if s==1:
				break
		if s==1:
			return False
		return True	

	def sudoku_solver(self):
		if self.check_grid():
			return self.grid
		for i in range(0,9):
			for j in range(0,9):
				if self.grid[i][j]==0:
					for digit in range(1,10):
						if self.check_box(digit,i,j) and self.check_hor(digit,i,j) and self.check_vert(digit,i,j):
							self.grid[i][j]=digit
							self.sudoku_solver()
					if self.check_grid():
						return self.grid
					else:
						self.grid[i][j]=0
						return self.grid



if __name__=="__main__":
	grid=[[0]*9 for i in range(0,9)]
	for i in range(0,9):
		for j in range(0,9):
			grid[i][j]=int(input("sudoku[{}][{}]=".format(i+1,j+1)))

	print("Given sudoku:")
	for i in range(0,9):
		print(grid[i])

	sudoku=Sudoku(grid)
	solved=sudoku.sudoku_solver()
	print('\n')
	print("Solved sudoku:")
	for i in range(0,9):
		print(solved[i])