from math import floor, ceil


def get_first(i, row):
    for j in range(len(row)):
        if i in row[j]:
            return j
    return -1

def get_min(lst):
    if len(lst) != 0:
        return min(lst)
    else:
        return 10000000

def get_max(lst):
    if len(lst) != 0:
        return max(lst)
    else:
        return -1

def solution(packets, recipe):

    possibilities = [[range(int(ceil((packet/1.1) / recipe[i])), int(((packet/0.9) // recipe[i]) + 1))
                      for packet in packets[i]]
                     for i in range(len(packets))]

    mini = get_min([get_min([get_min(lst) for lst in row]) for row in possibilities])
    maxi = get_max([get_max([get_max(lst) for lst in row]) for row in possibilities])

    packages = 0
    i = mini
    while i <= maxi:
        candidates = [get_first(i, row) for row in possibilities]
        if -1 not in candidates:
            for j in range(len(candidates)):
                possibilities[j].pop(candidates[j])
            packages += 1
        else:
            i += 1
    return packages


path = '/home/dzhang379/Downloads/'
fname = 'B-large-practice.in'

with open(path + fname, 'r') as f, open(path + fname[:-3] + '.out', 'w+') as out:
    t = int(f.readline().strip())
    for i in range(1, t + 1):
        types, num_packets = [int(s) for s in (f.readline().strip()).split(' ')]
        recipe = [int(s) for s in (f.readline().strip()).split(' ')]

        packets = []
        for row in range(types):
            packets.append( [int(s) for s in (f.readline().strip()).split(' ')] )

        soln = solution(packets, recipe)
        out.write("Case #{}: {}\n".format(i, soln))
