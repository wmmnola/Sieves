from Sundaram import sundaram
primes = sundaram(100000)
sums = []
for p in primes:
  s = str(p)
  sum =- 0
  for c in s:
    sum += int(c)
  sums.append(sum)

m = max(sums)
probs = [0] * m
for i in range(1,m):
  count = 0
  for s in sums:
    probs[i] += 1 if s == i else 0


f = open("primesums.csv", "a")

for i in range(0, m):
  s = "%d, %d\n"% (i, probs[i])
  f.write(s)
