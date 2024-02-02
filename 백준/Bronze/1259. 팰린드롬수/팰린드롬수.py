import sys

while(True) :
    s = int(sys.stdin.readline().strip())
    if( s == 0) : break

    reserve_s = str(s)[::-1]


    if(s == int(reserve_s)) : print("yes")
    else : print("no")