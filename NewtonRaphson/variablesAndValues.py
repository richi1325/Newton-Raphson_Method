def variablesAndValues(n,Xi):
	"""This function returns a list of tuples of 2 elements, the first constains the variables x1,x2,...,xn and the second contains the respective value of the variables in X^i
	Parameters:
	  n = Number of variables
	  Xi = List that contains X^i
	"""
	return list(map(lambda element,index: ('x'+str(index+1),element),Xi,list(range(n+1))))