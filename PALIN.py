def nextPalindrome(n):
    a=True
    while a:
        if str(n)==str(n)[::-1]:
            return n
            a=False

        else:
            n+=1


n=input()
a=[]
while n:
    print nextPalindrome(input())
    n=n-1



