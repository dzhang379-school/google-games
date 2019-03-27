import math

def isPrime(num):
    if num > 1:
        # check for factors
        for i in range(2, num):
            if (num % i) == 0:
                return False
        else:

            return True

    # if input number is less than
    # or equal to 1, it is not prime
    else:
        return False

def isCube(a):
    sum = 0
    for elem in a:
        sum += elem % 10
        elem = elem // 10
        sum += elem % 10
        elem = elem // 10
        sum += elem

    if math.pow(sum, 1/3) == math.floor(math.pow(sum, 1/3)):
        return (sum, True)
    return (sum, False)

def main():

    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179]

    for i in primes:
        for j in primes:
            if i != j:
                for k in primes:
                    if i != k and j != k:
                        for l in primes:
                            if i != l and j != l and k != l and (i + j + k + l) < 540:
                                m = 540 - i - j - k - l
                                if m in primes and i != m and j != m and k != m and l != m:
                                    tuple = isCube([i, j, k, l, m])
                                    if tuple[1]:
                                        print(i, j, k, l, m)


main()