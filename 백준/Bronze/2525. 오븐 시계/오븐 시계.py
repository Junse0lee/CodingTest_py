H, M = map(int, input().split())
time = int(input())

total_time = H*60 + M 
total_time += time

H= total_time//60
M = total_time%60

if H>23: 
    H-=24
print(H,  M)