# Program to check whether the given number is Armstrong number or not ... 

# Armstrong Number -- > 

# Eg ::   153 
# 		1^3 + 5^3 + 3^3	
# 		1   + 125 + 27
# 		153  ==  153

# 		So the number is armstrong number -- ( Sum of Cubes of all the digits in the number should be equal to the original number)


# 		177 
# 		1^3 + 7^3 + 7^3
# 		1   + 343 + 343
# 		687  !=  687

# 		Not an armstrong number

def check_armstrong(num):
	# small check to accept only integers 
	# throw an error if input number is not an integer
	try:
		armstrong_no = 0
		value = int(num)
		while value > 0:  #153 15 1 ( next iteration value = 0 , so iteration stops )
			reminder = value % 10 # 3 5 1
			armstrong_no += reminder ** 3  # 1st iteration -> 0 + 27 , 2nd iteration -> 27 + 125 , 3rd iteration -> 27 + 125 + 1
			value //= 10 #  15 ( quotient of 153 ) , 1 ( quotient of 15 ) , 0 ( quotient of 1 )

		# iterate over the loop till value > 0 
		# value in the first iteation :: 153 // 10 - > 53
		# value in the second iteation :: 53 // 10 - > 5
		# value in the third iteation :: 5 // 10 - > 0
		# Loop breaks because value = 0 ( i.e value is not > 0 )


		if armstrong_no == int(num) :  
			print ('Armstrong')
		else:
			print('Not an Armstrong')
	except Exception as e:
		print('input is invalid')


if __name__ == '__main__':
	check_armstrong(53)