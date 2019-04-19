#%%
def solution(shield, string):
    
    while len(string) > 0 and string[-1] == 'C':
        string = string[:-1]
        
    beam = 1
    damage = 0
    for action in string:
        if action == 'S':
            damage += beam
        else:
            beam *= 2
    
    swaps = 0
    i = len(string) - 2
    while damage > shield and i >= 0:
        if string[i] == 'C':
            beam = beam // 2
            if string[i + 1] == 'S':
                string[i] = 'S'
                damage -= beam
                swaps += 1
        i -= 1
    if damage <= shield:
        return swaps
    else:
        return "IMPOSSIBLE"
        
t = int(input())
for i in range(1, t+1):
    shield, string = input().split(" ")
    print("Case #{}: {}".format(i, solution(int(shield), list(string)))) 
