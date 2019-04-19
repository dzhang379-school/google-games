#%%
import math

def get_primes(n):
    primes = [False, False, True] + [True, False] * (n //2)
    for i in range(3, int(math.ceil(math.sqrt(n))), 2):
        if primes[i]:
            for j in range(3*i, n+1, 2*i):
                primes[j] = False
    return [2] + [i for i in range(3, n+1, 2) if primes[i]]

def solution1(dim, msg):

    t = [0]*(dim[1] + 1)
    for prime in get_primes(dim[0]):
        if msg[0] / float(prime) == msg[0] // prime:
            t[0] = prime
            break
    
    for i in range(dim[1]):
        if msg[i] / float(t[i]) == msg[i] // t[i]:
            t[i + 1] = msg[i] // t[i]
        else:
            break
    
    if t[-1] == 0:
        t[0] = msg[0] / t[0]
        for i in range(dim[1]):
            t[i + 1] = msg[i] // t[i]
    
    letters = sorted(list(set(t)))
    
    d = {}
    for i in range(26):
        d[letters[i]] = chr(i + 65)
    
    
    string = 'AAABACADAEAFAGAHAIAJAKALAMANAOAPAQARASATAUAVAWAXAYAZ'
    print(' '.join([str(letters[ord(string[i]) - 65] * letters[ord(string[i + 1]) - 65]) \
             for i in range(len(string) - 1)]))
    
    t = [d[x] for x in t]
    return ''.join(t)

t = int(input())
for i in range(1, t + 1):
    dim = [int(s) for s in input().split(" ")]
    msg = [int(s) for s in input().split(" ")]
    print("Case #{}: {}".format(i, solution1(dim, msg)))
          
          	
#%%
print(d)