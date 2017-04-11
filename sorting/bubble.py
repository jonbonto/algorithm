'''
Bubble sort, source: https://en.wikipedia.org/wiki/Bubble_sort
Worst-case performance	{\displaystyle O(n^{2})} O(n^{2})
Best-case performance	{\displaystyle O(n)} O(n)
Average performance	{\displaystyle O(n^{2})} O(n^{2})
Worst-case space complexity	{\displaystyle O(1)} O(1) auxiliary
'''
import time

N = int(input())
a = [int(i) for i in input().split(' ')]
''' start time for measure duration '''
start_time = time.time()

for i in range(N):
	swapped = False
	for j in range(1,N):
		if(a[j-1]>a[j]):
			swapped = True
			temp = a[j-1]
			a[j-1] = a[j]
			a[j] = temp
	if not swapped:
		break
print("--- %s seconds ---" % (time.time() - start_time))
for i in range(N):
	print(a[i],end=' ')

