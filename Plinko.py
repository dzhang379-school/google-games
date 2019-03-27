
probabilities = [[0.226, 0.387, 0.242, 0.107, 0.032, 0.006, 0, 0, 0],
                 [0.193, 0.346, 0.247, 0.137, 0.057, 0.016, 0.003, 0, 0],
                 [0.121, 0.247, 0.241, 0.196, 0.121, 0.054, 0.016, 0.003, 0],
                 [0.054, 0.137, 0.196, 0.226, 0.193, 0.121, 0.054, 0.016, 0.003],
                 [0.016, 0.057, 0.121, 0.193, 0.226, 0.193, 0.121, 0.057, 0.016],
                 [0.003, 0.016, 0.054, 0.121, 0.193, 0.226, 0.196, 0.137, 0.054],
                 [0, 0.003, 0.016, 0.054, 0.121, 0.196, 0.241, 0.247, 0.121],
                 [0, 0, 0.003, 0.016, 0.057, 0.137, 0.247, 0.346, 0.193],
                 [0, 0, 0, 0.006, 0.032, 0.107, 0.242, 0.387, 0.226]]

values = [100, 500, 1000, 0, 10000, 10, 1000, 500, 100]


def main():

    for k in range(4):
        exVal = [[0 for i in range(9)] for j in range(9)]

        for i in range(9):
            for j in range(9):
                exVal[i][j] = probabilities[i][j] * values[j]

        index = 0
        maximum = 0
        for i in range(9):
            summation = sum(exVal[i])
            if summation > maximum:
                maximum = sum(exVal[i])
                index = i

        print("Iteration: {}, Lane: {}, Ex Val: {}".format(k, index + 1, maximum))

        prob = probabilities[index]
        maxIndex = prob.index(max(prob))

        values[maxIndex] = 0


main()