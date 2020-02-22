


#Boolean Expression

print(20 > 10)
print(20 == 10)
print(20 < 10)
print(boot("Hello World"))
print(boot(20))


Python Conditions

Equals							->	x == y
Not Equals						->	x != y
Less than						->	x < y
Less than or equal to			->	x <= y
Greater than					->	x > y
Greater than or equal to		->	x >= y
Boolean OR 						-> x or y , x | y
Boolean And						-> x and y, x & y
Boolean Not						-> not x

x = 70
 y = 60
 if x > y:
	print("x is greater than y")
else:
	print("x is not greater than y")

x is greater than y
 if x < y:
 	print("x is greater than y")
 else:
	print("x is not greater than y")

x is not greater than y

>>> if x > y:
...     print("x is greater than y")
... elif x >= y:
...     print("x is greater or equal to y")
... elif y < x:
...     print("y is smaller than x")
... else:
...     print("x is nothing")
...
x is greater than y


x is greater than y
>>> if x == y:
...     print("Answer 1")
... elif x < y:
...     print("Answer 2")
... elif x <= y:
...     print("Answwer 3")
... else:
...     print("default")
...
default

#Short Hand if 
if x > y:	print("x is greater than y")

x = 50
y = 150
print(x) if x > y else print(y)

 if x < y and z > x:
...     print("All Conditions are True")
... else:
...     print("Some Conditions are False")
...
Some Conditions are False

#logical operator

 if x > y or z < y:
...     print("one of the condtion is True")
... elif x > y and z > y:
...     print("All conditions are True")
... else:
...     print("nothing else")
...
one of the condtion is True

>>> if x > y and z > y and z > x:
...     print("Answer 1")
... elif x == y or z == y or z > y and x > y:
...     print("Answer 2")
... elif z > y and y < x or z > y:
...     print("Answer 3")
... else:
...     print("default")
...
Answer 1