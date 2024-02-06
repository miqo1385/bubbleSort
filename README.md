# bubbleSort

Analysis:

1- Analyze the time complexity of Bubble Sort, emphasizing how the algorithm's iterative 
comparison and swapping mechanism leads to its O(n^2) complexity in the average and 
worst cases.

the repetitive nature of Bubble Sort's comparison and swapping operations, 
combined with its need to perform multiple passes through the array, results in an
O(n2) time complexity in both the average and worst cases. This makes it inefficient for
sorting large datasets compared to more efficient sorting algorithms like Quick Sort 
or Merge Sort.

2- Discuss the space complexity of Bubble Sort and justify why it is considered an 
in-place sorting algorithm.

Bubble Sort operates directly on the input array. It doesn't create any additional 
data structures to store elements or intermediate results. Therefore, it has a space 
complexity of O(1) in terms of the input space. This means that the amount of additional
space used by the algorithm is constant, regardless of the size of the input array.

3- Reflect on the potential stability of Bubble Sort and whether it maintains the order 
of equal elements.

Bubble Sort is typically stable, meaning it maintains the relative order of equal 
elements in the sorted array. This means that if two elements in the original array 
are equal, and one precedes the other, they will remain in the same order after sorting.

