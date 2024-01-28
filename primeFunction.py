#write a function to check if a number is prime


def get_prime(number):
	count = 0
	counter = 1

	while counter <= number:
		if number % counter ==0:
			count +=1
			counter += 1

	return count ==2

print(get_prime(9))