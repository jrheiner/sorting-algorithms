import numpy


def quicksort(array, l, h):
    if (l < h):
        pindex = partition(array, l, h)

        quicksort(array, l, pindex - 1)
        quicksort(array, pindex + 1, h)


def partition(array, l, h):
    pivot = array[h]
    index = l - 1
    for i in range(l, h):
        if array[i] <= pivot:
            index += 1
            array[index], array[i] = array[i], array[index]
    array[index + 1], array[h] = array[h], array[index + 1]
    return index + 1


def main():
    print("**Quicksort**")
    randarray = list(numpy.random.randint(0, 100, 25))
    print("Random array:", randarray)
    quicksort(randarray, 0, len(randarray) - 1)
    print("Sorted array:", randarray)


if __name__ == '__main__':
    main()
