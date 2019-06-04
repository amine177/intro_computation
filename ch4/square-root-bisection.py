def findRoot(x, power, epsilon):
    """
        return y as y**power = x
    """

    if x < 0 and power % 2 == 0:
        return None

    low = min(-1.0, x)
    high = max(1.0, x)
    y = (high + low) / 2.0
    while (abs(y**power - x) >= epsilon):
        if y**power > x:
            high = y
        else:
            low = y
        y = (high + low) / 2.0

    return y

if __name__ == "__main__":
    print(findRoot(4, 2, 0.00000000000000001))
    print(findRoot(2, 2, 0.000000000000001))
