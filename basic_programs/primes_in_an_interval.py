# Program to print prime numbers in a given interval


def get_primes(start_value, end_value) -> list:
    """

    :param start_value: interval start_value
    :param end_value:  interval end_value
    :return: List of primes in the given range
    """
    primes_list = []
    for value in range(start_value, end_value + 1):
        if value > 1:
            for n in range(2, value):
                if (value % n) == 0:
                    break
            else:
                primes_list.append(value)
    return primes_list


if __name__ == '__main__':
    primes = get_primes(7, 777)
    print(primes)
