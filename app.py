import random

def guess_number():
    """一个简单的猜数字游戏，支持重玩"""
    while True:
        number = random.randint(1, 100)
        attempts = 0
        
        print("\n欢迎来到猜数字游戏！")
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
        
        choice = input("\n还想再玩一次吗？(y/n): ").strip().lower()
        if choice != 'y':
            print("谢谢游玩，再见！")
            break

if __name__ == "__main__":
    guess_number()
