import math


def recursive1(number_of_guests: int):
    solution = [0, 0, 1, 1]
    for n in range(4, number_of_guests + 1):
        solution.append(math.ceil((n-1)/2) + solution[n-1])
    return solution


def recursive2(number_of_guests: int):
    solution = [0, 0, 1, 1, 3]
    for n in range(5, number_of_guests + 1):
        solution.append(n-1 + solution[n-2])
    return solution


def explicit(number_of_guests: int):
    return [0, 0, 1] + [(2*n**2-1+(-1)**n)//8 - 1 for n in range(3, number_of_guests + 1)]
