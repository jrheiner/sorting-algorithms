import numpy


def bubblesort(array):
    for i in range(len(array)):
        for k in range(0, len(array) - i - 1):
            if array[k] > array[k + 1]:
                array[k], array[k + 1] = array[k + 1], array[k]
    return array


def main():
    print("**Bubblesort**")
    randarray = list(numpy.random.randint(0, 100, 25))
    print("Random array:", randarray)
    print("Sorted array:", bubblesort(randarray))


if __name__ == '__main__':
    main()
