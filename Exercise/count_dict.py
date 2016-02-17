def count_dict(dic):
	total = 0
	for i in dic.values():
		total = total + len(i)
	return total

mydict = {'a' : ['people', 'person', 'guys', 'egbons'],
		  'b' : ['cars', 'vehicles', 'motor', 'automobile'],
		  'c' : ['plane', 'jet', 'concorde']
		  }
print count_dict(mydict)

def highest_dict(dic):
	highest = 0

	for i in dic.values():
		res = len(i)
		if res > highest:
			highest = res
	return highest
print highest_dict(mydict)


