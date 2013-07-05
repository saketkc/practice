def nextPal(n):
    ns = str(n)
    oddoffset = 0
    if len(ns) % 2 != 0:
        oddoffset = 1

    leftlen = len(ns) / 2 + oddoffset
    lefts = ns[0:leftlen]
    right = lefts[::-1][oddoffset:]
    p = int(lefts + right)
    if p < n:
        ## Need to increment middle digit
        left = int(lefts)
        left += 1
        lefts = str(left)
        right = lefts[::-1][oddoffset:]
        p = int(lefts + right)

    return p
n1=input()
while n1:
    print nextPal(input())
    n1=n1-1
