import math
history={0:0}
def findmax(n):
    if n in history:
        return history[n]
    else:
        history[n]=max(n,findmax(n/2)+findmax(n/3)+findmax(n/4))
        return history[n]

a=True
while a :
    try:
        n=input()
        print findmax(n)
    except:
        break;


