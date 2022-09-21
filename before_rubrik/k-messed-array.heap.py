import heapq
def sort_k_messed_array(arr, k):
    harr = []
    for i in range(k + 1):
        heapq.heappush(harr, arr[i])
    resarr = []
    for i in range(len(arr)):
        resarr.append(heapq.heappop(harr))
        if i + k + 1 < len(arr):
            heapq.heappush(harr, arr[i + k + 1])
    return resarr
arr = [1, 4, 5, 2, 3, 7, 8, 6, 10, 9, 0]
k = 5
print(sort_k_messed_array(arr, k))