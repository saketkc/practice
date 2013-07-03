def subtract(a,i):
    a[i]=a[i]-1
    a[i+1]=a[i+1]-1
    return a
N=input()
a=[int(i) for i in raw_input().split(" ")]
max_steps=max(a)
max_index=a.index(max_steps)
for i in range(0,max_steps):
    m_index=a.index(max(a))
    if m_index!=max_index:
        a=subtract(a,m_index)
    else:
        a=subtract(a,m_index-1)
s=0
for i in a:
    s+=a[i]

if s==0:
    print "YES"
else:
    print "NO"


