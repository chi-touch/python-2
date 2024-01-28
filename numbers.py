numbers = []
#type(numbers)

numbers = [1,2,'dayo', True,2.5]
len(numbers)
print(numbers[3])
print(numbers[2])
print(numbers[-1])
print(numbers[0:3])
print(numbers[:3])
print(numbers[:])
copied= numbers[::2]
print(copied)


students=['dayo','praise','hannah']
y = numbers + students
print(y)
students +=['dayo']
print(students)
students[::-2]
print(students)

copys = numbers[:]
numbers == copys
numbers == copied
numbers *=2
numbers
print(copys)
print(numbers)
print(numbers)




s = list[1,2,3]
x= [1,2,3]
name = list('hannah')
print(name)



def double(numbers):
	d =[]
	for number in numbers:
		d.append(number **2)
	return d
print(double(x))


#another way to do this
double(x)
def double2(n):
	y=[]
	for i in n:
		y+=[i **2]
	return y
print(double2(x))


