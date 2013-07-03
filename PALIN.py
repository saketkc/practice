def mirrors(n):
    l=len(n)
    c=l/2
    if l%2:
        left= n[:c+1]
    else:
        left=n[:c]

    mirror= left+n[0:c][::-1]
    return mirror

def main(n):
    mirror = mirrors(n)
    if int(mirror)>int(n):
        return mirror
    else:
        return mirrors(increment_center(n))



def increment_center(number):
    l=len(number)
    c=len(number)/2
    if l%2:
        return increment_digit(number, c)
    else:
        return increment_digit(number,c-1)
def increment_digit(number,index):
    if number[index]=='9':
        if index==0:
            number = '10' + number[1:]
        else:
            number = number[:index]+'0'+number[index+1:]
            number=increment_digit(number,index-1)
    else:
        number=number[:index]+str(int(number[index]) + 1) + number[index+1:]
    return number


n1=input()
while n1:
    print main(raw_input())
    n1=n1-1



