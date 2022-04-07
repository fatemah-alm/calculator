
def main():
	#write your code here
	try: 
		x = int(input('Enter the first number: '))
		y = int(input('Enter the second number: '))
	except ValueError: 
			print('invalid input, must be a number')
			return
	operation = input('Choose the operation (+, -, /, *): ') 
	match operation:
			case '+': 
				print(x + y)
			case '-':
				print(x - y)
			case '/':
				result = round(x/y, 2)
				print(result)
			case '*':
				print(x*y)
			case _: 
				print('operation is not valid')



	
	



if __name__ == '__main__':
	main()
