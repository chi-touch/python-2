#write a python program to check finnd the corresponding day of the week,
#eg user enters1 
#display "The daay of the week is Sunday

day = input('Enter 1 to 7 for the days of the week')

def weekday_checker(day_of_week):
	day = ""

	if day_of_week ==1:
		day = "Sunday"
	elif day_of_week ==2:
		day = 'Monday'
	elif day_of_week ==3:
		day = 'Tuesday'
	elif day_of_week ==4:
		day ='Wednesday' 
	elif day_of_week ==5:
		day = 'Thursday'
	elif day_of_week ==6:
		day = 'Friday'  
	elif day_of_week ==7:
		day = 'Satuday' 
	else:
		day = ' invalid number'
	return f"The day of the week is{day}"

day = input('Enter 1 to 7 for the days of the week')
weekday_checker(day_of_week)

	

#if day_of_week ==1
		#print(Sunday)
	#elif day_of_week ==2:
	#	print(Monday)
	#elif day_of_week ==3:
	#	print(Tuesday)
	#elif day_of_week ==4:
	#	prinnt(Wednesday) 
	#elif day_of_week ==5:
	#	prinnt(Thursday)
	#elif day_of_week ==6:
	#	prinnt(Friday)  
	#elif day_of_week ==7:
	#	prinnt(Satuday) 
	#else:
	#	print(days)