import math


def erasto(n):
  primes = [True] * n
  sq = int(math.floor(math.sqrt(n)))
  for i in range(2,sq):
    j = i**2
    while j < n:
      primes[j] = False
      j += i
  return primes

lst = erasto(100)

for i in range(2,len(lst)):
  s = "%d :" % i
  s += "Prime" if lst[i] else "Composite"
  print(s)
