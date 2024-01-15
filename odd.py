odd = []
position = int(input("Enter size of list:"))

for i in range(position):
	number = input('Enter element:")
	odd.append(number)
print(odd)

	for i in range(len(odd)):
		if(not(i % 2) )==0:
			print(odd[i])
	
