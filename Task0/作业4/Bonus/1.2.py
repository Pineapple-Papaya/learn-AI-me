# i 代表行，1~9
for i in range(1, 10):
    # j代表每一行里面的列，j从1到i
    for j in range(1, i + 1):
        print(f"{j}*{i}={i*j}", end="\t")
    # 一行结束，换行
    print()
