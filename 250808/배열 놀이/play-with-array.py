n, Q = map(int,input().split())
lst = input().split()

for _ in range(n):
    q = input().split()
    if q[0] == '1':
        print(lst[int(q[1])-1])
    elif q[0] == '2':
        idx=0
        for i in range(len(lst)):
            if lst[i] == q[1]:
                idx = i+1
                break
        print(idx)
    else:
        for i in range(int(q[1])-1,int(q[2])):
            print(lst[i],end=' ')
        print()