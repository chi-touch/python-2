#write a python program that prints the first 10 fibonacci series


count=0

sum =0

series =1

print (0,1, end = " ")

for number in range(10):
	count = sum
	sum += series
	print(sum,end= " ")
	series = count
	



