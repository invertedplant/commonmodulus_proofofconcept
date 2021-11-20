# 50.042 FCS CTF testing
# Year 2021
# Student: Wong Kai-En Matthew Ryan
# SID: 1003809

import primes



p = 1009  # smallest 4 digit prime
q = 9973  # largest 4 digit prime
message = 1003809

n = p * q  # 10062757
euler_totient = (p - 1) * (q - 1)  # 10051776
e1 = 13
e2 = 17  # gcd(e1, e2) = 1


# thus, some a and b exist where a*e1 + b*e2 = 1
# from running the formula below, we get
a = 4
b = -3
c1 = primes.square_multiply(message, e1, n)
c2 = primes.square_multiply(message, e2, n)

# thus, m is retrieved from c1 ** a * c2 ** b mod n, but since b is negative
# need to compute multiplicative inverse of c2

c2_inv = pow(c2, -1, n)

m_out = (c1 ** a) * (c2_inv ** -b) % n

def message_decoding(a,b,c1,c2_inverse, message = message):

    factor_a = [1, -1]
    factor_b = [1, -1]

    for i in factor_a:
        for j in factor_b:
            m_out = ((c1 ** (i * a)) * (c2_inv ** (j * b))) % n
            if (m_out == message):
                return m_out
    return "MEssage unfounded"


def bezout(a, b, x=0, prev_x=1, y=1, prev_y=0):  # stolen code
    """
    Calculate the Bézout's identity of 'a' and 'b' recursively
    Using the extended euclidean algorithm
    """

    # 'a' has to be greater than 'b'
    if b > a:
        a, b = b, a

    # calculate the remainder of a/b
    remainder = a % b
    print("Remainder: " + str(remainder))

    # if remainder is 0, stop here : gcd found
    if remainder == 0:
        print(b,x,y)
        return b, x, y
    # returns the GCD, and bezout coefficients of c1 and c2 in some order
    # also, one of the coefficients is negative but this code doesn't tell you which

    # else, update x and y, and continue
    quotient = a // b
    print("Quotient: " + str(quotient))
    prev_x, prev_y, x, y = x, y, quotient * x + prev_x, quotient * y + prev_y
    return bezout(b, remainder, x, prev_x, y, prev_y)


if __name__ == "__main__":
    print(f"Original message is: {message}")
    print(f"The primes are {p} and {q} and their product is {n}.")
    print(f"The Bezout identities (calculated manually) are {a} and {b} respectively")
    print(f"Check the source code to see how it works, plus an implementation of the Extended Euclidean Algorithm")
    #print(bezout(e1, e2)) #- find bezout coefficients
    # print(bezout(c2, n)) - check that c2 and n are coprime, so that an inverse exists
    print(f"The two public keys are ({e1}, {n}) and ({e2}, {n})")
    print(f"The respective encrypted messages are {c1} and {c2}")
    #print("Check the message" +str(message_decoding(a,b,c1, c2_inv, message)))
    print(f"The attack returns the message as {m_out}")
