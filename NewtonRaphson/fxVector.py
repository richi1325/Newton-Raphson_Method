def Fx(n,functions,variablesandValues):
	"""This function returns Fx vector evaluate in X^i
	Parameters:
	  n = Number of variables
	  functions = List that constains all the functions
	  variablesandValues = List of tuples of 2 elements, the first constains the variables x1,x2,...,xn and the second contains the respective value of the variables in X^i
	"""
	Fx=list(map(lambda function: float(function.subs(variablesandValues)),functions))
	return Fx