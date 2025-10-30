#Some basic functions that I shouldn't need to import a library to get

def sum(array):
    total = 0
    for i in array:
        total += i
    return total

def array_sum(array1, array2):
    new_array = []
    if len(array1) == len(array2):
        for i in range(len(array1)):
            new_array.append(array1[i] + array2[i])
        return new_array
    else:
        raise Exception("Arrays must be the same length to sum")

def print_array(array, end = '\n'):
    for i in array:
        print(i, end = end)


