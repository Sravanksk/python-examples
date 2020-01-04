# Program to find the area of a circle 
# formula -->  radius = pi * radius^2


def area_of_circle(radius) -> float:
    """

    :param radius: radius of circle
    :return: area of circle
    """
    pi = 3.14
    area = pi * (radius * radius)
    return area


if __name__ == "__main__":
    area = area_of_circle(radius=7.7)
    print(area)
