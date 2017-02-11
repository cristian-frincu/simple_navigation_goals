import math


DENSITY = 0.5 #meter/sample
f = file ("waypointNodes.csv","r")
rawNodes = f.readlines()
f.close()

nodes=[]
for i in rawNodes:
	print i
	nodes.append([float(i.split(",")[0]), float(i.split(",")[1])])


if len(nodes) <=1:
	print "Insufficient nodes to create waypoint, at least 2 required"
	exit()



lastNode = nodes[0]
nodes.pop(0)
nodes.append(lastNode)

f = file ("waypoint.csv","a+")

for i in nodes:
	##Characteristics of the line that connects the nodes
	m = (i[1]- lastNode[1])/(i[0]-lastNode[0])
	b = i[1] - m*i[0]
	#print m,b
	dist = math.sqrt((i[0]-lastNode[0])**2+(i[1]-lastNode[1])**2)
	#print dist
	numOfWaypoints = int(dist / DENSITY)
	#print int(numOfWaypoints)
	orientation = math.atan((lastNode[1]-i[1])/(lastNode[0]-i[0]))
	##Generating waypoints to connect the waypoints
	for point in range(numOfWaypoints):
		y = m*(point*DENSITY) + b 
		print lastNode[0]+point*DENSITY, y+lastNode[1],orientation
		f.write(str(lastNode[0]+point*DENSITY)+","+str(y+lastNode[1])+str(orientation)+"\n")
	lastNode = i
	print '----'

f.close()
