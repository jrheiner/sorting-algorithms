import numpy
import time

# generate random arrays


def gen_array(length):
    return list(numpy.random.randint(0, int(length) * 2, int(length)))


def selectionsort(array):
    for i in range(0, len(array)):
        min = i
        for k in range(i, len(array)):
            if array[k] < array[min]:
                min = k
        temp = array[min]
        array[min] = array[i]
        array[i] = temp
    return array


def insertionsort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i
        while j > 0 and key < array[j - 1]:
            array[j] = array[j - 1]
            j -= 1
        array[j] = key
    return array


rand_array = gen_array(1500)

start = time.time()
insertionsort = insertionsort(rand_array)
stop = time.time()
print("Insertionsort => {:.5}ms".format((stop - start) * 1000))

start = time.time()
selectionsort = selectionsort(rand_array)
stop = time.time()
print("Selectionsort => {:.5}ms".format((stop - start) * 1000))
