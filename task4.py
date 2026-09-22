def strings_to_lists(strings):
    return list(map(list, strings))


if __name__ == '__main__':
    words = ['Romina', 'Hz', 'Dortmund']
    print(strings_to_lists(words))