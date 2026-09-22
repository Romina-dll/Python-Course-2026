def sort_by_last(tuples):
    return sorted(tuples, key=lambda t: t[-1])


if __name__ == '__main__':
    sample1 = [(1, 2), (2, 3), (4, 4), (3, 3), (2, 1)]
    sample2 =  [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
    print(sort_by_last(sample1))
    print(sort_by_last(sample2))