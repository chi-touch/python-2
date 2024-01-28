
my_tuple = 1,

print(my_tuple)
my_tuple = 1,2,3,'dayo','beejay'
print(my_tuple)
print(my_tuple[0])
print(my_tuple[1])
print(my_tuple[3])
print(my_tuple[-1])
print(len(my_tuple))
print(my_tuple[3] + my_tuple[4])
print()

#u can use this method to unpack the tuple
a,b,c,d,e = my_tuple
print(a)
print(b)
print(c)
print(e)
print(d)
print()

# unpacking the tuple and picking the two and input *others to show that the items are still remaining
x,y, *others = my_tuple
print(x)
print(y)
print(others)
x,*others, y = my_tuple
print(x)
print(y)
print(others)
print()
c='hannnah',5,['a','b',1]
print(c)
c[2]
print(c[2])
c[2].append(2)
print(c)
print(c[2][1])
c[2][1] = 'izu'
print(c)
print()

#you can't add a tuple to a list , but u can add list to a tuple
students = ['muhammed','chichi','dayo','bolaji']
students +=c
print(students)
print()

my_list = [1,2,3,'dayo']
for i in my_list[3]:
	print(i)
print()

for i in my_list:
	print(i)

print()

for i in my_list[3][1:]:
	print(i)
print()

for idx, value in enumerate(my_list):
	print(idx, value)






