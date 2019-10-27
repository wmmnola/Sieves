def sundaram(n):
  m = int(n-2)/2
  marked = [0] * (m+1)
  primes = []
  for i in range(1, m + 1):
    j = i
    while((i + j + 2*i *j) <= m):
      marked[(i + j + 2*i *j)] = 1
      j += 1

  for i in range(1, m +1):
    if (marked[i] == 0):
      primes.append(2*i + 1)
  
  return primes


