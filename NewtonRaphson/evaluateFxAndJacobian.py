from NewtonRaphson.JacobianMatrix import JacobianMatrix
from NewtonRaphson.variablesAndValues import variablesAndValues
from NewtonRaphson.fxVector import Fx

def FxAndJacobianEvaluatedAtXi(Xi,functions):
	"""This function call JacobianMatrix(...) and Fx(...) functions and returns them for simplify structure of main code
	Parameters:
	  Xi = List with the values of x1,x2,...,xn in the ith iteration.
	  functions = List that constains all the functions
	"""
	n=len(Xi)
	variablesandValue=variablesAndValues(n,Xi)
	Jacobian=JacobianMatrix(n,functions,variablesandValue)
	FX=Fx(n,functions,variablesandValue)
	return Jacobian,FX