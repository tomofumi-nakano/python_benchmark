import cdecimal
import cProfile
import decimal
from fractions import Fraction
from gmpy2 import mpz


def bench_init_zero():
    for i in range(1000000):
        f = Fraction(0, 1)
        # d = decimal.Decimal('0')
        # c = cdecimal.Decimal('0')
        # g = mpz('0')
    x = f + f
    # x = d + d
    # x = c + c
    # x = g + g
    return x


def bench_init_one():
    for i in range(1):
        f = Fraction(1, 1)
        d = decimal.Decimal('1')
        c = cdecimal.Decimal('1')
        g = mpz('1')
    return [f, d, c, g]


def bench_add(a):
    f, d, c, g = a
    for i in range(1000000):
        x = f + f
        x = d + d
        x = c + c
        x = g + g
    return x


def bench_add2(a):
    f, d, c, g = a
    for i in range(1000000):
        x = f + f + f
        x = d + d + d
        x = c + c + c
        x = g + g + g
    return x


def bench_mul(a):
    f, d, c, g = a
    for i in range(1000000):
        x = f * f
        x = d * d
        x = c * c
        x = g * g
    return x


def bench_mul2(a):
    f, d, c, g = a
    for i in range(1000000):
        x = f * f * f
        x = d * d * d
        x = c * c * c
        x = g * g * g
    return x


if __name__ == '__main__':
    cProfile.run('bench_init_zero()')
    if (1 == 0):
        a = bench_init_one()
        cProfile.run('bench_add(a)')
        cProfile.run('bench_add2(a)')
    if (1 == 1):
        a = bench_init_one()
        cProfile.run('bench_mul(a)')
        cProfile.run('bench_mul2(a)')
