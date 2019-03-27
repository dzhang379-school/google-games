
def fillProb(flag, index, useCount, probs):

    options = { 'a': .25,
                'b': .5,
                'c': 1 - .1 * index,
                'd': .45 }

    if index == 10:
        prod = 1
        for i in probs:
            prod *= i
        if prod != 0 and prod > 0.00045:
            print(probs)
            print(prod)

    else:
        for key in options:
            if flag != 'a' and key == 'b':
                probs[index] = 0
            elif flag == 'c' and key == 'c':
                probs[index] = 0
            elif useCount >= 2 and key == 'd':
                probs[index] = 0
            else:
                probs[index] = options[key]

            if key == 'd':
                useCount += 1

            fillProb(key, index + 1, useCount, probs)

probs = [0] * 10

fillProb('a', 0, 0, probs)
