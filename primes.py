"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    count = 1
    while True:
        if number_of_primes <= 0:
            raise ValueError(f"x={number_of_primes} your input should be positive.")
            break
        if count > 1:
            for i in range(2,count):
                if (count % i) == 0:
                    break
            else:
                list.append(count)
        if (len(list) == number_of_primes):
            print(list)
            break
        else:
            count += 1
            continue
    return list
