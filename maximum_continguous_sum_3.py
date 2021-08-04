'''
i/o
arr = [4, 9, 1, 20, 3, 4]
width = 3
ans = ([9, 1, 20], 30)

brute-force approach: O(n^2)
sliding window: O(n)

edge case

'''
def max_contig(arr, width):
    widthsum = sum(arr[idx] for idx in range(width))
    maxsum = widthsum
    maxarrstart, maxarrend = 0, width - 1
    for idx in range(width, len(arr)):
        widthsum += arr[idx] 
        widthsum -= arr[idx - width]
        if widthsum > maxsum:
            maxsum = widthsum
            maxarrstart, maxarrend = idx - width + 1, idx
    return arr[maxarrstart:maxarrend + 1], maxsum
        
arr = [4, 9, 1, 20, 3, 4, 50]
width = 3
print(max_contig(arr, width))
width = 4
print(max_contig(arr, width))

