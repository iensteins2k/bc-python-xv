def evennumbers(low, high):
    result = []
    for x in range(low, len(high)):
    	if x % 2 != 0:
    		result.append(x)
		return result
	else:
		print x + "is an even number"