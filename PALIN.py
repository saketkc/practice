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
    a.append(input())
    n=n-1
for n in a:
    print nextPalindrome(n)


