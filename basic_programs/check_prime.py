# Program to check if a number is prime or not
# Optimized solution , instead of checking number this will check till √number because,
# a larger factor of number must be a multiple of smaller factor that number which has been already checked

# Source Wikipedia --> https://en.wikipedia.org/wiki/Primality_test


def check_prime(number) -> bool:
    """

    :param number: Number
    :return: bool (True/False)
    """
    if number <= 1:
        return False

    if number <= 3:
        return True

    if number % 2 == 0 and number % 3 == 0:
        return False

    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i = i + 6

    return True


if __name__ == '__main__':
    print(check_prime(7))
