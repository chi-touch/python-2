#write a function to 1 reverse a string

#def reverse(name)
#	number = len(name)-1
#	name2 =""
#	for num in range(number,-1,-1):
#		name2 += name[num]

#	return name2
#print(reverse('dayo'))

def reverseword(value):
	for word in value[: : -1]:
		print(word, end = "")
reverseword('chichi')