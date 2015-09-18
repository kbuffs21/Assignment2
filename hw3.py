from sys import argv
from hw3_class import *

script, world, heur = argv

if heur != 'manhattan' and heur != 'custom':
	print "last arguement must be manhattan or custom"

matrix = []

with open ( world , 'r') as tm:
	for line in tm:
		line = line.strip()
		if len(line) > 0:
			matrix.append(map(int, line.split()))
rows = len(matrix)-1
cols = len(matrix[0])-1


A = Node()
A.location = [rows,0]
A.distostart = 0
A.heuristic = 160
A.f = A.distostart + A.heuristic

open = []
closed = []
explored = []

open.append(A)
open.extend(recon(A,cols,rows,matrix,heur))
explored.append(A)
open.remove(A)
closed.append(A)

while True:
	tmp_node = Node()
	tmp_node.f = 100000
	for i in open:
		if i.f < tmp_node.f:
			tmp_node = i
			if tmp_node.f == 100000:
				print "stuck"
				break		
	closed.append(tmp_node)	
	if tmp_node.location == [0,cols]:
		break
	open = []
	open.append(tmp_node)
	open.extend(recon(tmp_node,cols,rows,matrix,heur))
	explored.extend(x for x in open if x not in explored)
	open.remove(tmp_node)

for x in explored:
	for y in explored:
		if x != y:
			if x.location == y.location:
				explored.remove(y)

				
print "The cost of the path is:", closed[len(closed)-1].f
print "The path is:"	
for i in closed:
	print i.location
print "The path explores", len(explored), "distinct nodes."	
