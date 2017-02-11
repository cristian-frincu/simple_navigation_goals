import math


DENSITY = 1 #samples/meter
f = file ("waypointNodes.csv","r")
rawNodes = f.readlines()
f.close()

nodes=[]
for i in rawNodes:
	#print i
	nodes.append([float(i.split(",")[0]), float(i.split(",")[1])])


if len(nodes) <=1:
	print "Insufficient nodes to create waypoint, at least 2 required"
	exit()



lastNode = nodes[0]
nodes.pop(0)
nodes.append(lastNode)

f = file ("file.csv","a+")

for currentNode in nodes:
	diffX = currentNode[0] - lastNode[0]
	diffY = currentNode[1] - lastNode[1]
	vertexLength = math.sqrt(diffX**2 + diffY**2)
	
	numberOfSubVertices = int(DENSITY * vertexLength)
	subVertexLengthX = diffX / numberOfSubVertices
	subVertexLengthY = diffY / numberOfSubVertices
	
	headingAngle = math.atan(diffY / diffX)

		
	for i in range(numberOfSubVertices):
		xi = lastNode[0] + subVertexLengthX*i	
		yi = lastNode[1] + subVertexLengthY*i	
		f.write(str(xi)+","+str(yi)+","+str(headingAngle)+"\n")
		print xi,yi,headingAngle

	lastNode = currentNode
f.close()
