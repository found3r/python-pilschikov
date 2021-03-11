def decimal_exponent(exponent, number=1.0):
    number = number * 10 ** exponent
    return number


print('а) -0,00027E+4 = ', decimal_exponent(4, -0.00027))
print('б) 666E-3 = ', decimal_exponent(-3, 666))
print('в) 1Е1 = ', decimal_exponent(1, 1))
