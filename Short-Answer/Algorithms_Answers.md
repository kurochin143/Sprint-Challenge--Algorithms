#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
O(n)
The loop requires n^3 loops before stopping, but since a is incremented by n^2, it reduces the number of loops by n^2. n^3/n^2 = n

b)
O(n^2)
The outer loop loops by n and nested by another n loop which results in n^2. n*n = n^2
This should be less than n^2 because the second n is reduced by j *= 2 considerably

c)
O(n)
n as the number of bunnies
n is reduced by one every recursion, and ending when n is 0, resulting in n as the number of recursion.

## Exercise II

for ef in eggs: # ef is max floor the egg can take
    # min_f is optimum f
    if ef < min_f:
        min_f = ef
return min_f

O(n)
n as the number of eggs