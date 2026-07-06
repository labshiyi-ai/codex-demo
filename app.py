import random

def guess_number():
    """一个简单的猜数字游戏"""
    number = random.randint(1, 100)
    attempts = 0
    
    print("欢迎来到猜数字游戏！")
    print("我已经想好了一个 1-100 之间的数字，来猜猜看吧！")
    
    while True:
        try:
            guess = int(input("请输入你的猜测: "))
            attempts += 1
            
            if guess < number:
                print(f"太小了！再试试。")
            elif guess > number:
                print(f"太大了！再试试。")
            else:
                print(f"恭喜你猜对了！你用了 {attempts} 次尝试。")
                break
        except ValueError:
            print("请输入一个有效的数字！")

if __name__ == "__main__":
    guess_number()
