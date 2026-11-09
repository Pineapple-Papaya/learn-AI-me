height1 = list(map(int, input().split()))
height2 = int(input())
num = 0
for i in range(len(height1)):
    if height1[i] <= (height2+30):
        num+=1
print(num)
