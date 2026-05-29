def count_in_list(lst, it):
    """
    This count the number of element in a list that is similar to it
    """
    count: int = 0
    for current in lst:
        if current == it:
            count += 1
    return count
