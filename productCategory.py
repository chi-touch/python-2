#write a python program to give 10% discount of price on electronic products and 5% discount on clothing product and 0 #discount on other product

#display te product category, the discount percentage, price before and after discount

product_type = input('Enter electronic product')
price = int(input('whst is the price of the product

disccount_pecentage =0
discount_price =0

if product_type.lower() == 'electronic'
	discount_price = price *0.1
	discount_percentage = 10
elif product_type == 'clothing':
	discount_price = price *0.05
	discount_percentage = 5
else
	discount_price = price


print(f'{product_type}{discount_percentage}{price}{discount_price}{price - discount_price}')

