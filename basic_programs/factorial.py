# Program to find factorial of a given Number 

# eg :: factorial ( 3 ) = 3 * 2 * 1 - > 6
		# factorial ( 5 ) = 5 * 4 * 3 * 2 * 1 = 120 

		# so, factorial(3) = 3 * factorial(2)
		# similarly , factorial(5) = 5 * factorial(4)
		# The following function use the same logic 

def get_factorial(n):
	if n==0 or n==1:
		return 1
	else:
		return n * get_factorial(n-1)

if __name__ == '__main__':
	factorial = get_factorial(5)
	print(factorial)