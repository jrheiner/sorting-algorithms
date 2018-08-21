# Sorting algorithms

Implementation and benchmark of common sorting algorithms in Python.

## Results

> average of 50 runs

|    |   Algorithm   |       Complexity      |   n  |   avg. Time   |
|----|:-------------:|:---------------------:|-----:|:-------------:|
| #1 |   Quicksort   | Ω(n log(n)) / O(n^2)  |  500 | **0.00099**96891s |
|    |       ~       |           ~           | 1000 | **0.00200**89149s |
|    |       ~       |           ~           | 5000 | **0.00799**77512s |
| #2 | Insertionsort |     Ω(n) / O(n^2)     |  500 | **0.01301**12171s |
|    |       ~       |           ~           | 1000 | **0.02000**52261s |
|    |       ~       |           ~           | 5000 | **6.00136**75689s |
| #3 | Selectionsort |    Ω(n^2) / O(n^2)    |  500 | **0.01400**54225s |
|    |       ~       |           ~           | 1000 | **0.06499**17125s |
|    |       ~       |           ~           | 5000 | **6.02337**86106s |
| #4 |   Bubblesort  |    Ω(n^2) / O(n^2)    | 500  | **0.04698**49109s |
|    |       ~       |           ~           | 1000 | **0.12095**68977s |
|    |       ~       |           ~           | 5000 | **7.03839**56432s |