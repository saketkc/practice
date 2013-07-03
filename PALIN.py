def main(n):
    l=len(n)
    c=l/2
    if l%2:
        left= n[:c]
        center=(n[c])
        right=n[c+1:]
        if right<left:
            palindrome=left+center+right[:-1]+left[0]
            return palindrome
        else:
            center=int(center)
            if center<9:
                return left+(str(int(center)+1))+left[::-1]
            else:
                leftnew=str(int(left)+1)
                return leftnew+leftnew[::-1]
    else:
        left=n[:c]
        right=n[c:]
        leftreverse=left[::-1]
        if leftreverse>right:
            return left+leftreverse
        else:
            leftnew = str(int(left)+1)
            return leftnew+leftnew[::-1]






n=input()
while n:
    print main(raw_input())
    n=n-1



