#write a python program that prints the factorial of a given number

def check_factorial(number):
	if number in (0,1):
		return 1
	factorial =1

	for num in range(number, 0,-1):
		factorial *= num

	return factorial
print(check_factorial(5))

