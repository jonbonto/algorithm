''' 
Selection Sort, source : https://en.wikipedia.org/wiki/Selection_sort
Worst-case performance	О(n2)
Best-case performance	О(n2)
Average performance	О(n2)
Worst-case space complexity	О(n) total, O(1) auxiliary
'''
import time

N = int(input())
a = [int(i) for i in input().split(' ')]
''' start time for measure duration '''
start_time = time.time()

for i in range(N-1):
	iMin = i
	for j in range(i+1,N):
		if(a[j] < a[iMin]):
			iMin = j
	if iMin != i:
		temp = a[i]
		a[i] = a[iMin]
		a[iMin] = temp
print("--- %s seconds ---" % (time.time() - start_time))
for i in range(N):
	print(a[i],end=' ')