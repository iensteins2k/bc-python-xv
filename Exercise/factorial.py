def factrial_red(lst):
	factorial = reduce(lambda x, y: x * y, range(1, lst+1))
	return factorial

def factorial_rec(lst):
	if lst == 1:
		return lst
	else:
		return lst * factorial(lst - 1)