import sys
n = int(sys.stdin.readline().strip())
arr = set()

for _ in range(n) :
    s = sys.stdin.readline().strip()
    arr.add(s)

arr = sorted(list(arr), key=lambda x : (len(x),x))

for c in arr :
    print(c)