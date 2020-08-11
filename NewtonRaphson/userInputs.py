def insertValuesForX0(n):
	"""This function prompts user to insert the initial values for x1,x2,...,xn and return them to in a list
	Parameters:
	  n = Number of variables
	"""
	print('---------Initial values for X^0---------')
	return [float(input('Insert a value for {}:'.format('x'+str(i)))) for i in range(n)]

def insertIrerations():
	"""This function prompts user to insert the maximum of iterations
	No parameters
	"""
	while True:
		iterations=int(input('Insert maximum number of iterations:'))
		if iterations>0:
			break
		else:
			print('Insert a correct number of iterations!')
	return iterations

def insertTolerance():
	"""This function prompts user to insert the minimum of tolerance
	No parameters
	"""
	while True:
		tolerance=float(input('Insert minimum of tolerance:'))
		if tolerance>0:
			break
		else:
			print('Insert a correct tolerancia!')   
	return tolerance