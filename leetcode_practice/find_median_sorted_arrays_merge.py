class Solution:
    def findMedianSortedArrarys(self, A, B):
        lengthA = len(A)
        lengthB = len(B)
        new_arr = []
        i = j  = 0
        while i < lengthA and j < lengthB:
            if A[i] < B[j]:
                new_arr.append(A[i])
                i += 1
            else:
                new_arr.append(B[j])
                j += 1
        while i < lengthA:
            new_arr.append(A[i])
            i += 1
        while j < lengthB:
            new_arr.append(B[j])
            j += 1
        if((lengthA + lengthB)%2 == 1):
            return(new_arr[int((lengthA+lengthB)/2)])
        else:
            return((new_arr[int((lengthA+lengthB)/2)]+new_arr[int((lengthA+lengthB)/2)-1])/2)


