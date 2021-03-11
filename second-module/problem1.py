import cmath
import math

x = 0.3
y = - 1.6
if (cmath.sqrt(x) + cmath.sqrt(y)).real <= float(4):
    print('True')
else:
    print('False')

k = 15
if (k % 7) == (k // 5 - 1):
    print('True')
else:
    print('False')

p = 0.182
if (math.trunc(p * 10) % 2):
   print('True')
else:
    print('False')