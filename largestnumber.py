def largestnumber(numbers):
	biggest_num = numbers(0)

	for num in numbers:
		if num > biggest_num:
			bigest_num = num

	return biggest_num

largestnumber(numbers)
print(largestnumber([1,24,2,13,10,2]))