x,y = map(int,input().split())
num = 0
year = []
for i in range(x,y+1):
    if i % 4==0 and (i % 100!=0 or i % 400==0):
        num+=1
        year.append(i)
print(num)
for i in year:
    print(i,end=' ')