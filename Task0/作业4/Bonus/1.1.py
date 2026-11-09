'''方式一
x,y,z = map(int,input().split())
max_value = max(x,y,z)
min_value = min(x,y,z)
mid_value = x + y + z - max_value - min_value
print(max_value, mid_value, min_value)'''
'''方式二
x,y,z = map(int,input().split())
if y > x:
    x ,y= y, x
if z > x:
    x ,z= z, x
if z > y:
    y ,z= z, y
print(x, y, z)'''
'''方法三'''
x,y,z = map(int,input().split())
N = [x,y,z]
N.sort(reverse=True)
print(N[0], N[1], N[2])