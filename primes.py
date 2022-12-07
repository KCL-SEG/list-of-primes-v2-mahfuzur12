"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    count = 0
    number = 2
    list = []
    
    if (number_of_primes <= 0):
        raise ValueError
    
    while count < number_of_primes:
        isPrime = True
        for i in range(2, number):
            if (number % i == 0):
                isPrime = False
        if isPrime:
            list.append(number)
            count += 1
        number += 1
    return list