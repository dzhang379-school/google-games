#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 10:53:37 2019

@author: dzhang379
"""

#%%
def masked(a, mask):
    return [a[i] for i in filter(lambda x: mask & (1 << x), range(len(a)) )]

def get_subsets(n):
    return [masked(range(1, n+1), mask) for mask in range(int(pow(2, n)))]

get_subsets(4)

from itertools import combinations

def findsubsets(a):
    a = range(1, a+1)
    ret = []
    for l in [list(combinations(a, i)) for i in range(len(a) + 1)]:
        ret += [list(x) for x in l]
    return ret

findsubsets(4)
get_subsets(4)

import time
begin = time.time()
findsubsets(20)
end = time.time()
print(end - begin)

begin = time.time()
get_subsets(20)
end = time.time()
print(end - begin)
    
   
#%%
 
d
c
b
c
someone redo?
leave to end

#%%

def compare(a):
    for x in a:
        if x[0] > x[1]:
            print('>')
        else:
            print('<' if x[0] < x[1] else '=')
a = [[10,20], [20,10], [10,10]]
compare(a)


#%%

inputs = [x.split(' ') for x in ['6 3 1 10',
'10 2 1 50',
'50 5 3 14',
'50 6 4 1',
'50 6 3 1',
'1 1 1 1',
'0 0 0 0']]

#3:09

def days_taken(a):
    for [h, u, d, f] in a:
        h = int(h)
        u = int(u)
        d = int(d)
        f = int(f)/float(100)
        
        day = 1
        height = u
        
        while height <= h:
            height -= d
            #print(height, day)
            if height < 0:
                break
            height += (1 - f*(day)) * u
            day += 1
            #print(day, height)
            
        if height > h:
            print(day)
        else:
            print('failed on day {}'.format(day))
    
days_taken(inputs)

#3:29

#%%

#3:34

inputs = [ x.split(' ') for x in 
            [ '3 +z -z',
            '3 +z +y',
            '2 +z',
            '4 +z +y +z',
            '5 No +z No No']]

#print(inputs)

def get_dir(a, b):
    d = 'x'
    sign = '-' if a[0] == b[0] else '+'
        
    if a[1] == 'x':
        d = b[1]
        sign = b[0]
    else:
        if a[1] != b[1]:
            d = a[1]
            sign = a[0]
    return(sign + d)
            
    
def bender(inputs):
    
    for line in inputs:
        #print(line)
        bends = [x for x in line if '+' in x or '-' in x]
        curr = '+x'
        #print(bends)
        for bend in bends:
            #print(curr, bend)
            curr = get_dir(curr, bend)
            
        print(curr)
        
bender(inputs)

#4:21
#%%
#1:15



i = [
'KS QS TH 8H 4H AC QC TC 5C KD QD JD 8D',
'AC 3C 4C AS 7S 4S AD TD 7D 5D AH 7H 5H']

i = [x.split(' ') for x in i]
i = [[x.lower() for x in j] for j in i]

def get_value(hand):
    
    vals = {
        'a': 4,
        'k': 3,
        'q': 2,
        'j': 1 }

    suits = {
        's': 0,
        'h': 0,
        'd': 0,
        'c': 0 }

    points = 0
    sub_points = 0
    
    stopped = {
            's': False,
            'h': False,
            'd': False,
            'c': False
        }
    
    for card in hand:
        val = card[0]
        suit = card[1]
        
        if val in vals:
            points += vals[val]
            sub_points += vals[val]
        suits[suit] = suits[suit] + 1
    
    for key, val in suits.items():
        if val == 0:
            points += 2
        if val == 1:
            points += 2
            for v in ['k', 'q', 'j']:
                if v + str(val) in hand:
                    points -= 1
                    sub_points -= 1
            points += 1
        if val == 2:
            points += 1
            for v in ['q', 'j']:
                if v + str(val) in hand:
                    points -= 1
                    sub_points -= 1
            points += 1
        if val == 3:
            if 'j' + str(val) in hand:
                points -= 1
                sub_points -= 1
    print(points, sub_points)
    
    for suit in suits:
        if 'a' + suit in hand or \
            suits[suit] > 1 and 'k' + suit in hand or \
            suits[suit] > 2 and 'q' + suit in hand:
            
            stopped[suit] = True
    
    no_trump = stopped['s'] and stopped['h'] and stopped['d'] and stopped['c'] 
    
    suit = 'NO-TRUMP' if no_trump else \
        max(suits.keys(), key=lambda k: suits[k]).upper()
    return (points, suit)

def out(i):
    for hand in i:
        (points, suit) = get_value(hand)
        if points < 14:
            print('PASS')
        else:
            print('BID ' + suit)
    
out(i)
        
#1:40
#%%

decks = ['''AC KC QC JC TC 9C 8C 7C 6C 5C 4C 3C 2C AD KD QD JD TD 9D 8D 7D 6D 5D 4D 3D 2D AH KH
QH JH TH 9H 8H 7H 6H 5H 4H 3H 2H AS KS QS JS TS 9S 8S 7S 6S 5S 4S 3S 2S''',

'''AC KC QC JC TC 9C 8C 7C 6C 5C 4C 3C 2C AD KD QD JD TD 9D 8D 7D 6D 5D 4D 3D 2D AH KH
QH JH TH 9H 8H 7H 6H 5H 4H 3H 2H AS KS QS JS TS 9S 8S 7S 6S 5S 4S 3S 2S''']
decks = [deck.split(' ') for deck in decks]

def get_val(c):
    
    return int(c[0]) if c.isnumeric() else 10

def shuffle(deck, y):
    top_pile = deck[:25]
    deck = deck[25:]
    x = get_val(deck[0])
    
    return (top_pile + deck[10 - x + 1:], y + x)

def get_card(deck):
    y = 0
    for i in range(3):
        deck, y = shuffle(deck, y)
    
    return deck[y - 1]

print(decks)
print([get_card(deck) for deck in decks])

#%%
#2:35

i = ['28 51 29 50 52',
'50 26 19 10 27',
'10 20 30 24 26',
'46 48 49 47 50']

i = [line.split(' ') for line in i]

def out(i):
    for x in i:
        print(get_card(x))

def get_card(x):
    hers = x[:3]
    his = x[3:]
    his_highest = max(his)
    his_lowest = min(his)

    h_2 = [card for card in hers if card > his_lowest]
    
    if len(h_2) > 0:
        hers.pop(hers.index(min(h_2)))
    else:
        print(1)
        exit
        
    h_1 = [card for card in hers if card > his_highest]
    
    if len(h_1) > 0 and len(h_2) > 0:
        print(-1)
        exit
    else:
        min_card = int(max(hers)) + 1
        while str(min_card) in his:
            min_card += 1
        print(min_card)
        exit

out(i)
#2:44

print(len(a) == len(list(set(a))))

def get_addends(a):
    l = 0
    r = len(s) - 1
    
    while l < r:
        if a[l] + a[r] == b:
            print(a[l], a[r])
        else:
            if a[l] + a[r] < b:
                l += 1
            else:
                r -= 1
    print('NO SOLUTION')

for addends in range(8,12):
    get_addends(i)

#radix sort

def get_contig(a):
    l = 0
    r = 1
    best = 1
    while r < len(a):
        curr = 1
        if a[r] > a[r - 1]:
            r += 1
            curr += 1
            if curr > best:
                best = curr
        else:
            l = r + 1
            r = l + 1
    return best

