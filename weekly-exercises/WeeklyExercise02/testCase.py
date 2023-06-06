from unfairDice import *


def test():
    # testCase1
    rolls = biased_rolls([1 / 12, 1 / 4, 1 / 3, 1 / 12, 1 / 12, 1 / 6], 2 ** 32 - 1, 20)
    print(rolls)
    draw_histogram(6, rolls, 50)

    # testCase2
    rolls = biased_rolls([1 / 4, 1 / 6, 1 / 12, 1 / 12, 1 / 4, 1 / 6], 42, 200)
    draw_histogram(6, rolls, 10)

    # testCase3
    rolls = biased_rolls([1 / 3, 1 / 3, 1 / 3], 2 ** 32 - 1, 1000)
    draw_histogram(3, rolls, 10)


if __name__ == '__main__':
    test()