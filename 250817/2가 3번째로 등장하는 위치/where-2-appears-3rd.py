n = int(input())
lst = list(map(int,input().split()))
cnt=0

for i in range(1,n+1):
    if lst[i-1] == 2:
        cnt+=1
    if cnt == 3:
        print(i)
        break