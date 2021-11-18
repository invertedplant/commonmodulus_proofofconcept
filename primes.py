# 50.042 FCS Lab 6 template
# Year 2021
# Student: Wong Kai-En Matthew Ryan
# SID: 1003809

import random


def square_multiply(a, x, n):
    # usage: calc a**x mod n
    y = 1
    x_but_binary = bin(x)  # 0b....
    x_list = []
    for bit in x_but_binary[2:]:
        x_list.append(int(bit))
    x_length = len(x_but_binary) - 2
    for i in range(x_length):
        y = y**2 % n
        if x_list[i] == 1:
            y = a*y % n
    return y


def miller_rabin(n, a):
    # n = number to be tested
    # a = number of passes
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    # decompose the number into the form (2^r)*d+1
    n_1 = n-1
    r, d = 0, n_1
    while d % 2 == 0:
        d >>= 1  # shift right
        r += 1
    # print(n)
    # print(2**r*d+1)
    # Witness my loop!
    for i in range(a):
        test = random.randint(2, n-2)
        x = square_multiply(test, d, n)
        if x == 1 or x == n-1:
            continue
        for j in range(r):
            x = square_multiply(x, 2, n)
            if x == n-1:
                break
        else:
            return False
    return True


def gen_prime_nbits(n):
    # get yer random bits here
    bits = random.getrandbits(n)

    # use miller rabin to check if it's a prime - if it's not, throw it out and get a new one
    while not miller_rabin(bits, 2):
        bits = random.getrandbits(n)

    # if it is, then we're done here
    return bits


if __name__ == "__main__":
    print('Is 561 a prime?')
    print(miller_rabin(561, 2))
    print('Is 27 a prime?')
    print(miller_rabin(27, 2))
    print('Is 61 a prime?')
    print(miller_rabin(61, 2))

    print('Random number (100 bits):')
    print(gen_prime_nbits(100))
    print('Random number (80 bits):')
    print(gen_prime_nbits(80))


