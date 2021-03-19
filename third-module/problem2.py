#  Copyright (c) 2021.
#  Leonid Zhavoronkov (halfleonlife@gmail.com)


import random

root1 = random.randint(-1000, 1000)
root2 = random.randint(-1000, 1000)

b = -(root1 + root2)
c = root1 * root2

if b < 0:
    if c < 0:
        print(f'Equation: x^2 + ({b})*x + ({c})')
    else:
        print(f'Equation: x^2 + ({b})*x + {c}')
else:
    if c < 0:
        print(f'Equation: x^2 + {b}*x + ({c})')
    else:
        print(f'Equation: x^2 + {b}*x + {c}')

