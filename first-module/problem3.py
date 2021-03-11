from problem2 import decimal_exponent

try:
    eval('0006')
    print('а) 0006 - Right')
except SyntaxError:
    print('а) 0006 - Wrong')
try:
    eval('-0')
    print('б) -0 - Right')
except SyntaxError:
    print('б) -0 - Wrong')
try:
    eval('7.0')
    print('в) 7,0 - Right')
except SyntaxError:
    print('в) 7,0 - Wrong')
try:
    eval('7')
    print('г) 7 - Right')
except SyntaxError:
    print('г) 7 - Wrong')
try:
    eval('+0.3')
    print('д) +0,3 - Right')
except SyntaxError:
    print('д) +0,3 - Wrong')
try:
    eval('.3')
    print('е) .3 - Right')
except SyntaxError:
    print('е) .3 - Wrong')
try:
    eval('2/3')
    print('ж) 2/3 - Right')
except SyntaxError:
    print('ж) 2/3 - Wrong')
try:
    eval(f'{decimal_exponent(-1)}')
    print('з) E-1 - Right')
except SyntaxError:
    print('з) E-1 - Wrong')
try:
    eval(f'{decimal_exponent(0, 8)}')
    print('и) 8E0 - Right')
except SyntaxError:
    print('и) 8E0 - Wrong')
