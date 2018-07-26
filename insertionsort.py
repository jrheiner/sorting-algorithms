import numpy


def insertionsort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i
        while j > 0 and key < array[j - 1]:
            array[j] = array[j - 1]
            j -= 1
        array[j] = key
    return array


def main():
    print("**Insertionsort**")
    randarray = list(numpy.random.randint(0, 100, 25))
    print("Random array:", randarray)
    print("Sorted array:", insertionsort(randarray))


if __name__ == '__main__':
    main()
