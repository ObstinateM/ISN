while n <= k:
    L.append(L[k-n])
    n += 1
while n < len(L):
    L2.append(L[n])
    n += 1