List * []


word = 'programming'


  p  r   o  g  r  a  m  m  i  n  g
  0   1  2  3  4  5  6  7  8  9  10
-11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1







word[0]
word[-2]
word[3:5]
word[4:9]
word[:5]
word[8:]
word[5:-3]
word[:2] + word[3:]


len(word)

# len = length

square = 'square'
 len(word) + len(square)

>>>cube[0]
10
>>> cube[4]
50
>>> cube[3] = 40
>>> cube
[10, 20, 30, 40, 50]

cube[5] = 60 #error out of range
 cube.append(60)
>>> cube
[10, 20, 30, 40, 50, 60]
>>> cube.append(40+5+20+10)
>>> cube
[10, 20, 30, 40, 50, 60, 75]
>>> cube.reverse()
>>> cube
[75, 60, 50, 40, 30, 20, 10]
>>> cube.sort()
>>> cube
[10, 20, 30, 40, 50, 60, 75]
>>> cube.remove(75)
>>> cube
[10, 20, 30, 40, 50, 60]
>>> cube.pop()
60

cube1 = [10, 20, 30, 40, 50]
cube2 = [1, 2, 3, 4, 5]
cube1.extend(cube2)

del cube1[3]
del cube[1:3]
del cube1[:]

ProgramA = ['A', 'B', 'C', 'D', 'E']
ProgramB = ['a', 'b', 'c', 'd', 'e']
ProgramC = ProgramA + ProgramB
ProgramC
['A', 'B', 'C', 'D', 'E', 'a', 'b', 'c', 'd', 'e']
 ProgramD = [1, 2, 3, 4,, 5]
 ProgramC = ProgramC + ProgramD

 ProgramC[9:] = []
 ProgramC[5:9] = ProgramD
 ProgramC

 len(ProgramC)

 a = [10, 20, 30, 40, 50]
 b = [60, 70, 80, 90, 100]
 c = [110, 120, 130, 140, 150]
 x = [a, b, c]
 x