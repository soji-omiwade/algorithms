'''
array: [-1 2 5 -2 1 -4 2 4]
delts: []
maxsum = 7


'''
def maxsum(arr):
    maxsum = float("-inf")
    csum = float("-inf")
    for i in range(len(arr)):
        csum = max(arr[i], csum + arr[i])
        maxsum = max(csum, maxsum)
    return maxsum

array = [-1, 2, 5, -2, 1, -4, 2, 4]   
array = [x if x < 0 else -x for x in array]
array = [x if x > 0 else -x for x in array]
print(maxsum(array), sum(array)) # 7