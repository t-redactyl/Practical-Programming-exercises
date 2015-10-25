# Practical Programming Chapter 11 notes

# Linear sorting algorithms are inefficient as they must scan every item in a 
# sequence

# Binary sorting algorithms are much more efficient, BUT:
# The way in which the items are scanned highly affects the time taken (e.g.,
# insertion_sort versus list_sort).
# The actual rearrangement (insertion) takes time as well which can slow
# down the sort algorithm.

# Mergesort is an Nlog2 N algorithm, which means it needs only Nlog2 time to
# figure out where to insert a value
# Built around the idea that taking two sorted lists and merging them is
# proportional to the number of items in both lists.


