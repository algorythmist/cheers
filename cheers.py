import math


def list_solutions_recursive1(number_of_guests: int) -> list:
    solution = [0, 0, 1, 1]
    for n in range(4, number_of_guests + 1):
        solution.append(math.ceil((n-1)/2) + solution[n-1])
    return solution


def list_solutions_recursive2(number_of_guests: int) -> list:
    solution = [0, 0, 1, 1, 3]
    for n in range(5, number_of_guests + 1):
        solution.append(n-1 + solution[n-2])
    return solution


def number_of_clinks(number_of_guests: int) -> list:
    n = number_of_guests
    return (2*n**2-1+(-1)**n)//8 - 1


def list_solutions_closed_form(number_of_guests: int) -> list:
    return [0, 0, 1] + [ number_of_clinks(n) for n in range(3, number_of_guests + 1)]


def solutions_in_table(number_of_guests: list) -> str:
    content = '| Guests | Clinks |\n| --- | --- |\n'
    for n in number_of_guests:
        content += f'| {n} | {number_of_clinks(n)} |\n'
    return content


