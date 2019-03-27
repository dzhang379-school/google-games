import re

string = "Twas brillig and the slithy tovesDid gyre and gimble in the wadeAll mimsy were the borogovesAnd the mome raths outgrabeBeware the Jabberwock my sonThe jaws that bite the claws that catch Beware the Jubjub bird and shunThe frumious Bandersnatch"
string = string.replace(" ", "")

sum = 0

#string = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
for letter in string:
    val = 0
    isUpper = 1
    if ord(letter) < 97:
        isUpper = 2
    if letter in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
        val = 1
    else:
        ordinance = ord(letter.lower()) - 96
        if ordinance < 5:
            val = ordinance - 1
        if ordinance > 5:
            val = ordinance - 2
        if ordinance > 9:
            val = ordinance - 3
        if ordinance > 15:
            val = ordinance - 4
        if ordinance > 21:
            val = ordinance - 5


    print("{}, {}, {}".format(letter, isUpper, val))
    sum += (isUpper * val)
    print(sum)

print(sum)