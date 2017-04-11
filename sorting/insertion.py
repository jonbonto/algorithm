'''
Insertion sort, sourcce : https://en.wikipedia.org/wiki/Insertion_sort
Worst-case performance	О(n2) comparisons, swaps
Best-case performance	O(n) comparisons, O(1) swaps
Average performance	О(n2) comparisons, swaps
Worst-case space complexity	О(n) total, O(1) auxiliary
'''
import time

N = int(input())
a = [int(i) for i in input().split(' ')]
''' start time for measure duration '''
start_time = time.time()

for i in range(1,N):
	j = i
	while j > 0 and a[j-1] > a[j]:
		temp = a[j-1]
		a[j-1] = a[j]
		a[j] = temp
		j = j - 1
print("--- %s seconds ---" % (time.time() - start_time))
for i in range(N):
	print(a[i],end=' ')
