
class Node:
	def __init__(self):
		self.location = None
		self.distostart = None
		self.heuristic = None
		self.f = None
		self.parent = None

def heursty(ex,wy,heur,cols,rows,matrix):	
	temp = 0
	if heur == 'manhattan':
		temp = 10 * (ex + cols - wy) 
	elif heur == 'custom':
		temp = 10 * pow(pow(ex,2) + pow((cols - wy),2),.5)
		if matrix[ex-1][wy+0] == 2 and matrix[ex-1][wy+1] == 2 and matrix[ex+0][wy+1] == 2:
			temp = temp + 100
		#10 * (ex + cols - wy)
	return temp

def g(i,j,ex,wy,matrix):
	if i == 0 and j == 0:
		return 0
	elif (i + j) == -1 or (i + j) == 1:
		if matrix[ex][wy] == 1:
			return 20
		return 10
	else: 
		if matrix[ex][wy] == 1:
			return 24
		return 14

def recon(self,cols,rows,matrix,heur):
	adj = []
	for i in range(-1,2):
		for j in range(-1,2):
			ex = self.location[0] + i
 			wy = self.location[1] + j
			try:
				if 0 <= ex <= rows and 0 <= wy <= cols and matrix[ex][wy] != 2:
					newnode = Node()
					newnode.location = [ex,wy] 
					newnode.distostart = g(i,j,ex,wy,matrix) + self.distostart
					newnode.heuristic = heursty(ex,wy,heur,cols,rows,matrix)
					newnode.f = newnode.distostart + newnode.heuristic
					newnode.parent = self
					if newnode.location != self.location:
						adj.append(newnode)	
			except:
				pass
	return adj
 
