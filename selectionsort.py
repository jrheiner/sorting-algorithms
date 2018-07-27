import numpy


def selectionsort(array):
    for i in range(0, len(array)):
        min = i
        for k in range(i, len(array)):
            if array[k] < array[min]:
                min = k
        array[min], array[i] = array[i], array[min]
    return array


def main():
    print("**Selectionsort**")
    randarray = list(numpy.random.randint(0, 100, 25))
    print("Random array:", randarray)
    print("Sorted array:", selectionsort(randarray))


if __name__ == '__main__':
    main()
