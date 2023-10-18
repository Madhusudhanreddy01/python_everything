'''Need to print prime numbers till 100
  ex: 2,3,5,7,11,13.....97'''

n=int(input())
for i in range(2, n+1):
    factors = 0
    for j in range(2, i-1):
        if (i%j)==0:
            factors = factors + 1

    if factors==0:
        print(i)
