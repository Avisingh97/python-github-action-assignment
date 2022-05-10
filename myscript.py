def findLongestConseqSubseq(arr, n):
     
    ans = 0
    count = 0
 
    # Sort the array
    arr.sort()
 
    v = []
 
    v.append(arr[0])
    for i in range(1, n):
        if (arr[i] != arr[i - 1]):
            v.append(arr[i])
 
    # Find the maximum length
    # by traversing the array
    for i in range(len(v)):
 
        if (i > 0 and v[i] == v[i - 1] + 1):
            count += 1
             
        # Reset the count
        else:
            count = 1
             
        # Update the maximum
        ans = max(ans, count)
         
    return ans
 
# Driver code
arr = [ 1, 2, 20, 30, 100, 3, 50, 4 ]
n = len(arr)
 
print("Length of the Longest contiguous subsequence is",
       findLongestConseqSubseq(arr, n))
 