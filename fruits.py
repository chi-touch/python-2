fruits = []
count = 0

while count < 5:
	fruit = input('Enter name of fruit:')
#fruits.append(fruit)
fruits.extend([fruit])
#fruits+=[fruit]
count = count + 1

print(fruits)