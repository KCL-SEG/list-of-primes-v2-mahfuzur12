"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = [2]
    counter = 0
    number = 3
    while counter < number_of_primes - 1:
        for i in range (2, number):
            if (number % i != 0):
                list.append(number)
                counter += 1
                number += 1
            else:
                number += 1

    print(list)
    return list

primes(10)