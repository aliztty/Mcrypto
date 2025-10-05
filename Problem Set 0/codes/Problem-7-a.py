#!/usr/bin/env python3

def Square_And_Multiply(base, exponent, modulus):

    exponent_bin = bin(exponent)[2::]
    result = 1

    for bit in exponent_bin:
        result = result * result % modulus
        if bit == '1':
            result = (result * base) % modulus

   return result

if __name__ == "__main__":

    x = 23
    e = 71
    n = 31
    result = Square_And_Multiply(x, e, n)

    print(f'{x}^{e} (mod{n}) = {result}')
