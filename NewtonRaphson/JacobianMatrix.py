from sympy import diff

def JacobianMatrix(n,functions,variablesandValues):
    """This function returns the Jacobian matrix evaluate in X^i
	Parameters:
	  n = Number of variables
	  functions = List that constains all the functions
	  variablesandValues = List of tuples of 2 elements, the first constains the variables x1,x2,...,xn and the second contains the respective value of the variables in X^i
    """
    Jacobian=list()
    for function in functions: 
        #The Jacobian list append a list created by casting the map function, first it derivate the function respect x_i and then it substite the function respect the values of X^i, the result is a square matrix
        Jacobian.append(list(map(lambda i: float(diff(function,'x'+str(i+1)).subs(variablesandValues)),list(range(n)))))
    return Jacobian