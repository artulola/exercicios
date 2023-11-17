def karatsuba(x, y):
    if x < 10 or y < 10:
        return x * y

    n = max(len(str(x))) + max(len(str(y)))
    m = n // 2

    x_high, x_low = divmod(x, 10**m)
    y_high, y_low = divmod(y, 10**m)

    z0 = karatsuba(x_low, y_low)
    z1 = karatsuba((x_low + x_high), (y_low + y_high))
    z2 = karatsuba(x_high, y_high)

    result = z2 * 10**(2 * m) + ((z1 - z2 - z0) * 10**m) + z0

    return result 

resultado = karatsuba(12341828383838383838383, 56782472342648623424000242)
print(f'Resultado: {resultado}')