def binarySearch(list, idxs, idxe, val):
	if(idxe < idxs):
		return None
	else:
		mid = (idxs + idxe )// 2

		if(val > list[mid]):
			return binarySearch(list, mid+1, idxe, val)
		
		elif(val < list[mid]):
			return binarySearch(list, idxs, mid-1, val)

		else:
			return mid


arr = [23,45,54,767,765]
arr.sort()
print(binarySearch(arr, 0, len(arr)-1, 765))
