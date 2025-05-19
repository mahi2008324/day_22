name=input("enter the name : ")
count={}
for character in name:
	if character in count:
		count[character]=count[character]+1
	else:
		count[character]=1
for character in count:
	print(character,count[character])