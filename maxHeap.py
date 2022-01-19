def makeMaxHeap(arr, i):

    l = i * 2
    r = 2 * i + 1
    if (l <= len(arr) and arr[l-1] > arr[i-1]):
        largest = l
    else:
        largest = i
    
    if(r <= len(arr) and arr[r-1] > arr[largest-1]):
        largest = r

    if(largest != i):
        temp = arr[i-1]
        arr[i-1] = arr[largest-1]
        arr[largest - 1] = temp
        makeMaxHeap(arr, largest)

def buildHeap(arr):
    for i in reversed(range(len(arr)//2)):
        makeMaxHeap(arr, i+1)
    print('Heap Max',arr)
buildHeap([123,12,1234,44,55])