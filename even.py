even = []
position = int(input("Enter the size:"))

for i in range(position):
	number= input("Enter element")
	even.append(number)

print(even)
for i in range(len(even)):
		if(i % 2)==0:
			print(even[i])