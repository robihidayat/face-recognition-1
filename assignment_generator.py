f1=open("groups","r")
number_of_groups=0
for line in f1:
	number_of_groups=number_of_groups+1
f2=open("question_bank","r")
number_of_questions=0
for line in f1:
	number_of_questions=number_of_questions+1
number_of_questions /=3
question_number=1
for i in range(1,number_of_groups+1):
	f3=open("./assignments/assignment-group"+(str)(i)+".html","w")
	f3.write("<!DOCTYPE HTML>\n<html>\n<head><title>assignment-group"+(str)(i)+"</title>\n</head><body>")
	for line in f2:
		if(question_number%30==0):
			break
		else:
			f3.write(line+"</br>")
		question_number+=1
	f3.write("</p>\n</body>\n</html>")	
	question_number+=1
