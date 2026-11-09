#显示状态函数
def display_status(HP1,HP2):
    print(f"【长门】HP: {HP1} / 115")
    print(f"【娜比娅】HP: {HP2} / 105")
#掷色子
def roll_dice(N):
    import random
    point = 0
    for i in range(N):
         point += random.randint(1,6)
    return point


    