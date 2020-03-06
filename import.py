# Fibonacci numbers module


#n = int(input('Please enter a number:'))


def fib(n):	#write fibonacci series up to n
	a, b = 0, 1
	while a < n:
		print(a , end=' ')
		a, b = b, a+b
	print()

#Go to Fibonacci Powerpoint

def fib2(n): #return Fibonacci series up to n
	result = []
	a, b = 0, 1
	while a < n:
		result.append(a)
		a, b = b, a+b
	return result


# >>> fib #importantd

import fibonacci

 f = fibonacci.fib
 f(200)

# fibonacci.fib(10000)
# -----------

# from fibonacci import fib, fib2

# f = fib2(500)
# print(f)

# --------------

# from fibonacci import *

# fib(500)
# print fib(2(500))

# ---------------

# import fibonacci as fi

# fi.fib(500)

# -------------------

# from fibonacci import fib as fibonacci
# fibonacci(500)

# fib.py
# https://docs.python.org/3/tutorial/modules.html#packages-in-multiple-directories


# >>> Student (Import Folder)