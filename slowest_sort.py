import time
import numpy as np

def is_sort(array):
	start=0
	next=1
	for _ in range(len(array)-1):
		if(array[start]<=array[next]):
			start+=1					
			next+=1
		else:
			return 0

	return 1



def main():
	start_time= time.time()
	array=[1,2,3,4,5,6,7,8,9,10]
	while(1):
		array=np.random.permutation(array)
		# print(array)
		if(is_sort(array)):
			print("hogya kaam")
			print(time.time()-start_time)
			exit()
		

if __name__ == '__main__':
	main()

