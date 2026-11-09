"""Foundation 0 第 5 题：按记录顺序更新学长的名字。"""

n = int(input())

names = []
for _ in range(n):
    names.append(input())

m = int(input())
for _ in range(m):
    u, v = map(int, input().split())
    names[u - 1] = "I_love_" + names[v - 1]

print(names[0])
