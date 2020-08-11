from sympy import plot_implicit

def plot2Variables(functions):
	"""This function plot a list of 2 functions in implicit form to facilitate finding a good point for X^0
	Parameters:
	  functions = List of fuctions in they implicit form
	"""
	print('---------Plotting---------')
	initialPoint=float(input('Insert a lower bound for plot:'))
	finalPoint=float(input('Insert a upper bound for plot:'))
	p1=plot_implicit(functions[0],('x1', initialPoint, finalPoint),adaptive=False,title='Plot of functions',show=False)
	p2=plot_implicit(functions[1],('x1', initialPoint, finalPoint),adaptive=False,show=False)
	p1.extend(p2)
	p1[1].line_color='r'
	p1.show()