# Implement your own print function. It should work on all operating systems. You can't use build-in print function

import sys
my_file = open('print.txt', 'w')


def printing(*args, sep=' ', end='\n', file=sys.stdout):
    """
    Alternative print function
    :param file: if particular file is not specified, *args will be printed to console
    """
    file.write(sep.join(str(arg) for arg in args))
    file.write(end)


if __name__ == '__main__':
    printing('John', 'Bill', 'James', sep='-', file=my_file)
    printing(123456789, end=' ')
    printing('qwerty')


# Implement your realization of the function filter
sequence_1 = [1, 3, 5, 4, 3.5, 4.4, 0.1]
sequence_2 = 'ggdfdgdjjjjhgfghj'
sequence_3 = (1, 3, 5, 6, 'f', 'F', 1.8, 7.7)


def my_filter(filter_condition, sequence):
    """
    :param filter_condition: function with filtering condition
    :param sequence: e.g. - list, tuple, string
    :return: filtered list
    """
    result = []
    for item in sequence: # iterate through sequence of items in sequence
        if filter_condition(item):  # apply filter function
            result.append(item)
    return result


def filter_condition (item):
    if item:  # function require filtering statement
    # if (item % 2) == 0:
    # if 'g' in item:
        return True
    else:
        return False


print(my_filter(filter_condition, sequence_1))
print(my_filter(filter_condition, sequence_2))
print(my_filter(filter_condition, sequence_3))


# Implement your own implementation of the function map

def my_map(callback, sequence):
    """
    The function updates the given sequence: if the given element has 'str' type - the function will convert it
    to upper case, if the given element in the sequence has the type int or float - it will multiply it
    :param callback: function object, which means that you need to pass a function without calling it
    :param sequence: e.g. - list, tuple, string
    :return: updated sequence, by applying a transformation function to every item in the original sequence
    """
    result = []
    for item in sequence:
        result.append(callback(item))
    return result


def callback(item):
    if type(item) is str:
        result = item.upper()
        return result
    elif type(item) is int or type(item) is float:
        result = item * item
        return result


print(my_map(callback, sequence_3))
print(my_map(callback, sequence_2))
print(my_map(callback, sequence_1))
