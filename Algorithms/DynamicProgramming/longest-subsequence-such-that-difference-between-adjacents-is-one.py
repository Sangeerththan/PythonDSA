def longestSubsequence(A, N):
	L = [1]*N
	hm = {}
	for i in range(1,N):
		if abs(A[i]-A[i-1]) == 1:
			L[i] = 1 + L[i-1]
		elif hm.get(A[i]+1,0) or hm.get(A[i]-1,0):
			L[i] = 1+max(hm.get(A[i]+1,0), hm.get(A[i]-1,0))
		hm[A[i]] = L[i]
	return max(L)
A = [1, 2, 3, 4, 5, 3, 2]
N = len(A)
print(longestSubsequence(A, N))
