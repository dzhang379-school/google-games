
import math

def solution(dim, msg):

    t = [0]*(dim[1] + 1)
    t[1] = math.gcd(msg[0], msg[1])
    t[0] = msg[0] // t[1]
    
    for i in range(dim[1]):
        t[i + 1] = msg[i] // t[i]

    letters = sorted(list(set(t)))
    
    d = {}
    for i in range(26):
        d[letters[i]] = chr(i + 65)
    t = [d[x] for x in t]
    return ''.join(t)
        

t = int(input())
for i in range(1, t + 1):
    dim = [int(s) for s in input().split(" ")]
    msg = [int(s) for s in input().split(" ")]
    print("Case #{}: {}".format(i, solution(dim, msg)))
          