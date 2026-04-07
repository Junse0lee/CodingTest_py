import sys

R = int(sys.stdin.readline())
for i in range(R):
    x, y= map(int, sys.stdin.readline().split())
    print(f"Case #{i+1}: {x+y}")