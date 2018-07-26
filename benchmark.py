import time

import numpy

from insertionsort import insertionsort as insertionsort
from selectionsort import selectionsort as selectionsort


algorithms = [insertionsort, selectionsort]
benchmarks = [25, 100, 1000, 10000]


def gen_array(length):
    return list(numpy.random.randint(0, int(length) * 2, int(length)))


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
        function(randarray)
        print("{}, len = {:6d} >>> {}s".format(function.__name__, i, stop()))
    print("------")


def main():
    for x in algorithms:
        benchmark(x)


if __name__ == '__main__':
    main()
