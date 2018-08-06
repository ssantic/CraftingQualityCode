def num_buses(n):
    """ (int) -> int

    Precondition: n >= 0

    Return the minimum number of buses required to transport n people.
    Each bus can hold 50 people.

    >>> num_buses(75)
    2
    """

    if n % 50 == 0:
        buses = n / 50
    else:
        overflow = n % 50
        buses = ((n - overflow) / 50) + 1

    return int(buses)


def stock_price_summary(price_changes):
    """ (list of number) -> (number, number) tuple

    price_changes contains a list of stock price changes. Return a 2-item
    tuple where the first item is the sum of the gains in price_changes and
    the second is the sum of the losses in price_changes.

    >>> stock_price_summary([0.01, 0.03, -0.02, -0.14, 0, 0, 0.10, -0.01])
    (0.14, -0.17)
    """

    total_gains = 0
    total_losses = 0

    for change in price_changes:
        if change > 0:
            total_gains += change
        elif change < 0:
            total_losses += change

    return (total_gains, total_losses)


def swap_k(L, k):
    """ (list, int) -> NoneType

    Precondtion: 0 <= k <= len(L) // 2

    Swap the first k items of L with the last k items of L.

    >>> nums = [1, 2, 3, 4, 5, 6]
    >>> swap_k(nums, 2)
    >>> nums
    [5, 6, 3, 4, 1, 2]
    """

    first_k_items = L[0:k]
    last_k_items = L[-k:]
    middle_items = L[k:-k]

    # Return the flattened swapped list
    L = sum([last_k_items, middle_items, first_k_items], [])

    return L



if __name__ == '__main__':
    import doctest
    doctest.testmod()
