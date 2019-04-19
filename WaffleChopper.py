#%%
def num_chips(waffle):
    return sum([sum(row) for row in waffle])

def transpose(m):
    return [[row[i] for row in m] for i in range(len(m[0]))]
    
def col_helper(waffle, h, chips):
    h_sets = []
    if h == 0:
        if num_chips(waffle) == chips:
            h_sets.append([])
    else:
        for i in range(1, len(waffle) - h + 1):
            if num_chips(waffle[:i]) == chips:
                temp_h = col_helper(waffle[i:], h - 1, chips)
                h_sets += [[i] + [i + h for h in h_set] \
                                for h_set in temp_h]
    return h_sets

def subs(waffle, r1, r2, v1, v2):
    return [row[r2:r2] for row in waffle[v1:v2]]

def check(waffle, h_set, v_set, chips):
    h_set = [0] + h_set + [len(waffle)]
    v_set = [0] + v_set + [len(waffle[0])]
    
    for i in range(len(h_set) - 1):
        for j in range(len(v_set) - 1):
            if num_chips(subs(waffle, h_set[i], h_set[i+1], v_set[j], v_set[j + 1])) \
                                                                    != chips:
                return False
    return True
    
def solution(waffle, r, c, h, v):
    
    total_chips = num_chips(waffle)
    chips = total_chips / ((h+1) * (v+1))
    chips_per_row = total_chips / (h+1)

    for i in range(1, c - v + 1):
        v_sets = []
        if num_chips(waffle[:i]) == chips_per_row:
            v_sets = col_helper(transpose(waffle[:i]), v, chips)
            for first_v in set([v[0] for v in v_sets]):
                h_sets = col_helper([row[:first_v] for row in waffle[i:]], \
                                        h - 1, chips)
                h_sets = [[i] + [i + h for h in h_set] \
                            for h_set in h_sets]
                for h_set in h_sets:
                    for v_set in v_sets:
                        if v_set[0] == first_v and \
                                         check(waffle, h_set, v_set, chips):
                            return True
    return False
    
t = int(input())
for i in range(1, t+1):
    (r, c, h, v) = [int(s) for s in input().split(' ')]
    waffle = []
    for j in range(r):
        waffle.append(input())
    waffle = [[1 if x == '@' else 0 for x in row] for row in waffle]
    print("Case #{}: {}".format(i, "POSSIBLE" if solution(waffle, r, c, h, v)\
                                      else "IMPOSSIBLE"))