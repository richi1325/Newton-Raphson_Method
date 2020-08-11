from NewtonRaphson.plots import plot2Variables
from NewtonRaphson.userInputs import *
from NewtonRaphson.evaluateFxAndJacobian import FxAndJacobianEvaluatedAtXi
import numpy
import pandas

from sympy import sympify

def NewtonRaphsonModel(n,functions):
	"""This function has all the process of the method, it returns a dataframe with historical values for X in ith iteration and the error in sprectral form
	Parameters:
	  n = Number of variables
	  functions = List that constains all the functions
	"""
	
	#This part plot the functions if they have 2 variables.
	if n==2:
		plot2Variables(functions)


	#This list contains the titles for the DataFrame
	labeledColumns=['x'+str(i) for i in range(n)]+['Error']
	
	Xi=insertValuesForX0(n)
	iterations=insertIrerations()
	tolerance=insertTolerance()

	#This variable keeps values for X in ith iteration
	valuesForDF=list()
	j=0
	#This for loop update the values for Xi until it finds a solution for the system with the tolerance established or when it finishes the number maximum of iterations
	for iteration in range(iterations):
		previousXi=Xi
		
		if iteration==0:
			aux=[i for i in Xi]+['-']
			valuesForDF.append(aux)
			Jacobian,Fx=FxAndJacobianEvaluatedAtXi(Xi,functions)
			aux=[]
		
		j+=1
		#Update the value for Xi
		Xi=numpy.array(Xi).reshape(n,1)-numpy.dot(numpy.linalg.inv(Jacobian),numpy.array(Fx).reshape(n,1))
		Xi=Xi.reshape(1,n)[0].tolist()
		Jacobian,Fx=FxAndJacobianEvaluatedAtXi(Xi,functions)
		
		aux=[i for i in Xi]
		#Spectral norm for the error
		aux.append(numpy.absolute((numpy.array(Xi)-numpy.array(previousXi))).max())
		valuesForDF.append(aux)
		aux=[]
		
		#If in the ith iteration the algorithm reached minimum tolerance it breaks
		if numpy.absolute((numpy.array(Xi)-numpy.array(previousXi))).max()<=tolerance:
			print('Tolerance reached!')
			break
	#Print message if the algortihm reached the maximun of iterations
	if j==iterations:
		print('\nMaximum iterations reached!\n')
	
	return pandas.DataFrame(data=valuesForDF,columns=labeledColumns)