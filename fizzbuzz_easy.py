def fizzbuzz(x):

	if x % 3 and x%5 ==0:
		return 'fizzbuzz'
	elif x%3 ==0:
		return 'fizz'
	elif x%5 ==0:
		return 'buzz'
	else:
		return str(x)

print('\n'.join(fizzbuzz(n) for n in xrange(1,26)))