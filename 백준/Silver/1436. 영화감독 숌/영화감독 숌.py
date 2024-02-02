n = int(input())
count = 1
i = 666
while(True) :
    if(count == n) : 
        print(i)
        break
    i = i+1
    if("666" in str(i)) :
        count +=1