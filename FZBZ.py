

def FizzBuzz(x):
	sequence =[]
	for i in range(1,x+1):
		if i%3 and i% 5 ==0:
			sequence.append("FizzBuzz")
		elif  i%3 ==0:
			sequence.append("FIZZ")
		elif i%5 ==0:
			sequence.append("Buzz")
		else:
			sequence.append(str(i))

	return sequence	 

def main():
	print('\n'.join(FizzBuzz(25)))

main()