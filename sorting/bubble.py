N = int(input())
a = [int(i) for i in input().split(' ')]
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
for i in range(N):
	print(a[i],end=' ')

