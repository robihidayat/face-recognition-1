#finding centre points of faces
f=open("./group_faces_squares","r")
f2=open("./students_present","r")
node_list=[]
for line in f:
    node_list.append(map(int,line.split(' ')))
    
f1=open("./nodelist","w")
for node in node_list:
	x=node[0]+node[2]/2
	y=node[1]+node[3]/2
	f1.write((str)(node[0])+" "+(str)(node[1])+" "+(str)(node[2])+" "+(str)(node[3])+" "+(str)(x)+" "+(str)(y)+"\n")
f1.close()
f.close()
#end of centre finding

#starting matrix creation
f=open("./nodelist","r")


x=0

node_list=[]
for line in f:
    node_list.append(map(int,line.split(' ')))
    x=x+1
y_factor=2
x_factor=2
matrix=[[0 for i in xrange(x)] for i in xrange(x)] 
for node in node_list:
	left=node[0]-x_factor*node[2]
	right=node[0]+2*x_factor*node[2]
	top=node[1]+node[3]/y_factor
	bottom=node[1]-node[3]-node[3]/y_factor
	for node1 in node_list:
		if((node[4]!=node1[4] or node[5]!=node1[5])):
			if(node1[4]<=right and node1[4]>=left and node1[5]<=top and node1[5]>=bottom):
				matrix[node_list.index(node)][node_list.index(node1)]=1
student_list=[]
for line in f2:
    student_list.append(map(int,line.split(' ')))				
		
for node in node_list:
	temp=[]
	for student in student_list:
		if(student[1]==node[4] and student[2]==node[5]):
			break
	temp=student
	student[0]=student_list[node_list.index(node)][0]
	student[1]=student_list[node_list.index(node)][1]
	student[2]=student_list[node_list.index(node)][2]
	student_list[node_list.index(node)][0]=temp[0]
	student_list[node_list.index(node)][1]=temp[1]
	student_list[node_list.index(node)][2]=temp[2]
f2.close();
f2=open("./students_present","w")	
for student in student_list:
	f2.write((str)(student[0])+" "+(str)(student[1])+" "+(str)(student[2])+"\n")
			
				
f1=open("input.txt","w")
f1.write((str)(x)+"\n")
for row in matrix:
	for i in row:
		f1.write((str)(i)+" ")
	f1.write("\n")
	
