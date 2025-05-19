student_info={}
student_number=input("Enter the student number : ")
student_info["student_number"]=student_number
subjects=int(input("Enter the no.of subjects : "))
marks=[]
for i in range(1,subjects+1):
	mark=int(input("Enter the marks in subject {} : ".format(i)))
	marks.append(mark)
student_info["marks"]=marks
sum=0
for mark in marks:
	sum=sum+mark
average=sum/subjects
student_info["Average"]=average


print("\n ---------student_information--------")


for x in student_info:
	print(x,"   ------    ",student_info[x])