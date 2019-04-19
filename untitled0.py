#%%
import math

def get_primes(n):
    cap = math.sqrt(n)
    primes = [i for i in range(0, n + 1)]

    curr = 2
    while curr < cap:
        for i in range(2*curr, n + 1, curr):
            primes[i] = 0
        curr += 1
        while primes[curr] == 0:
            curr += 1
            
    return [p for p in primes if p != 0][2:]
    

def solution(dim, msg):

    t = [0]*(dim[1] + 1)
    
    primes = get_primes(dim[0])
    
    ind = -1
    while ind < len(primes):
        ind += 1
        cand = primes[ind]
        if msg[0] / float(cand) == msg[0] // cand:
            t[0] = msg[0] // cand
            break
    
    for i in range(dim[1]):
        q = msg[i] / float(t[i])
        if q == msg[i] // t[i]:
            t[i + 1] = q
        else:
            t[0] = msg[0] // t[0]
            break
    
    if t[-1] == 0:
        for i in range(dim[1]):
            t[i + 1] = msg[i] // t[i]

    t = [int(n) for n in t]
    
    print(msg)
    print(t)
    
    letters = sorted(list(set(t)))
    print(len(letters))
    d = {}
    for i in range(len(letters)):
        d[letters[i]] = chr(i + 65)

    t = [d[x] for x in t]
    return ''.join(t)

dim = [10000,  25]
msg = '3292937 175597 18779 50429 375469 1651121 2102 3722 2376497 611683 489059 2328901 3150061 829981 421301 76409 38477 291931 730241 959821 1664197 3057407 4267589 4729181 5335543'

print(solution(dim, [int(i) for i in msg.split()]))
#t = int(input())
#for i in range(1, t + 1):
#    dim = [int(s) for s in input().split(" ")]
#    msg = [int(s) for s in input().split(" ")]
#    
#    print("Case #{}: {}".format(i, solution(dim, msg)))