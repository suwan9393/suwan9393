n = int(input())
result = 0

for i in range(n):
    a = int(input())
    result += a

result = str(result)
print(result[1:]+result[0])