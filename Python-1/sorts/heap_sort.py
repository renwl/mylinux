'''
This is a pure python implementation of the heap sort algorithm.

For doctests run following command:
python -m doctest -v heap_sort.py
or
python3 -m doctest -v heap_sort.py

For manual testing run:
python heap_sort.py
'''

from __future__ import print_function

import pdb
def heapify(unsorted, index, heap_size):
		#print("in heapify:	", "index=",index,"	list=",unsorted)
		
		largest = index
		left_index = 2 * index + 1
		right_index = 2 * index + 2
		if left_index < heap_size and unsorted[left_index] > unsorted[largest]:
		    largest = left_index
		
		if right_index < heap_size and unsorted[right_index] > unsorted[largest]:
		    largest = right_index
		
		if largest != index:
		    unsorted[largest], unsorted[index] = unsorted[index], unsorted[largest]
		    #print("in heapify:	",unsorted)
		    heapify(unsorted, largest, heap_size)
		
		
def heap_sort(unsorted):
    '''
    Pure implementation of the heap sort algorithm in Python
    :param collection: some mutable ordered collection with heterogeneous
    comparable items inside
    :return: the same collection ordered by ascending

    Examples:
    >>> heap_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]

    >>> heap_sort([])
    []

    >>> heap_sort([-2, -5, -45])
    [-45, -5, -2]
    '''
    #print("in heap_sort:	", "	list=",unsorted)
    n = len(unsorted)
    for i in range(n // 2 - 1, -1, -1):
        heapify(unsorted, i, n)
    for i in range(n - 1, 0, -1):
        unsorted[0], unsorted[i] = unsorted[i], unsorted[0]
        #print("in heap_sort:	",unsorted)
        heapify(unsorted, 0, i)
    return unsorted

if __name__ == '__main__':
	import sys
	import time
	if sys.version_info.major < 3:
	    input_function = raw_input
	else:
	    input_function = input
	tstart=time.clock()
	#pdb.set_trace()
	unsorted=list(range(10000000,1,-1))
	#print(sort(unsorted))   
	heap_sort(unsorted)
	#print(heap_sort(unsorted))
	tend=time.clock()                 
	print("read: %f s" % (tend - tstart))                 
	#user_input = input_function('Enter numbers separated by a comma:\n')
	#unsorted = [int(item) for item in user_input.split(',')]
	#print(heap_sort(unsorted))
                   
                   