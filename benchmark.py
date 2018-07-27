import time

import numpy

from insertionsort import insertionsort as insertionsort
from quicksort import quicksort as quicksort
from selectionsort import selectionsort as selectionsort

algorithms = [quicksort, insertionsort, selectionsort]
benchmarks = [1000, 10000, 50000, 1000000]


def gen_array(length):
    return list(numpy.random.randint(0, int(length) * 3, int(length)))


def start():
    global tstart
    tstart = time.time()


def stop():
    global tstart
    ttotal = time.time() - tstart
    return ttotal


def benchmark(function):
    for i in benchmarks:
        randarray = gen_array(i)
        start()
        if function == quicksort:
            function(randarray, 0, len(randarray) - 1)
        else:
            function(randarray)
        print("{:13s}, len = {:6d} >>> {}s".format(function.__name__, i, stop()))
    print("------")


def main():
    for x in algorithms:
        benchmark(x)


if __name__ == '__main__':
    main()
