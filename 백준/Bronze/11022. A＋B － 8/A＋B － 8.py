import sys
N = int(sys.stdin.readline())

for i in range(N):
    x, y = map(int, sys.stdin.readline().split())
    print(f"Case #{i+1}: {x} + {y} = {x+y}")