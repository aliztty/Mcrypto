#!/usr/bin/env python3
import time

def Square_And_Multiply(base, exponent, modulus):

    exponent_bin = bin(exponent)[2::]
    result = 1

    for bit in exponent_bin:
        result = result * result % modulus
        if bit == '1':
            result = (result * base) % modulus

    return result

if __name__ == "__main__":
    Time_Start = time.time()
    x = 1234567890
    e = 98765432109876543210
    n = 100000000007
    result = Square_And_Multiply(x, e, n)
    Time_End = time.time()
    Time = Time_End - Time_Start
    print(f'{x}^{e} (mod{n}) = {result}')
    print(f'Time Start - Time End = {Time_Start} - {Time_End} = {Time}')
