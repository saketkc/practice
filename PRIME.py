def get_all_primes():
    low=2
    high=32000#1000000000
    for  i in range(2,high+1,1):
        primes[i]=True
    #print primes
    for i in primes:
        factors = range(i,high+1,i)
        for factor in factors[1:]:
            primes[factor]=False

    return primes
def primer(low,high):
    return [i for i in primes if primes[i]==True and i>=low and i<=high]
#    return True


n1=input()
ins=[]
primes={}
primes[2]=True
while n1:
    raw=raw_input().split(" ")
    ins.append(raw)

    n1=n1-1
get_all_primes()
for r in ins:
    low = int(r[0])
    high = int(r[1])

    #print primer(low,high)
    print ("\n").join( str(v) for v in primer(low,high))
    print
