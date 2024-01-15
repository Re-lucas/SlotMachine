# 导入 random 模块，用于生成随机数
import random

# 定义常量，表示玩家的初始积分，下注选项，老虎机的图案，奖励倍数
INITIAL_CREDITS = 100
BET_OPTIONS = [1, 2, 5, 10]
SLOT_SYMBOLS = ["Cherry", "Lemon", "Lucky 7", "Bar", "Diamond", "Jackpot"]
REWARD_MULTIPLIERS = {"Cherry": 3, "Lemon": 5, "Lucky 7": 7, "Bar": 10, "Diamond": 20, "Jackpot": 0}

# 定义变量，表示玩家的当前积分，累积奖池，是否继续游戏，是否使用保持功能，以及保持的位置
credits = INITIAL_CREDITS
jackpot = 0
play = True
hold = False
hold_position = []

# 定义一个函数，用于打印老虎机的图案
def print_slots(slots):
    # 用 for 循环遍历 slots 列表，打印每个元素
    for slot in slots:
        print(slot, end=" ")
    # 打印一个换行符
    print()

# 定义一个函数，用于检查老虎机的结果，并返回奖励积分
def check_slots(slots, bet):
    # 用 if-elif-else 语句判断 slots 的组合，根据不同的情况计算奖励积分
    if slots[0] == "Cherry":
        if slots[1] == "Cherry":
            if slots[2] == "Cherry":
                # 三个樱桃，奖励积分为下注乘以樱桃的倍数
                reward = bet * REWARD_MULTIPLIERS["Cherry"]
            else:
                # 前两个樱桃，奖励积分为下注乘以 2
                reward = bet * 2
        else:
            # 只有第一个樱桃，奖励积分为下注
            reward = bet
    elif slots[0] == slots[1] == slots[2]:
        # 三个相同的图案，根据图案的不同计算奖励积分
        if slots[0] == "Jackpot":
            # 三个奖池，奖励积分为累积奖池的全部
            reward = jackpot
        else:
            # 其他三个相同的图案，奖励积分为下注乘以对应的倍数
            reward = bet * REWARD_MULTIPLIERS[slots[0]]
    else:
        # 没有中奖的组合，奖励积分为 0
        reward = 0
    # 返回奖励积分
    return reward

# 用 while 循环实现游戏的主逻辑
while play:
    # 打印玩家的当前积分和累积奖池
    print("You have", credits, "credits.")
    print("The jackpot is", jackpot, "credits.")
    # 提示玩家输入下注积分，用 try-except 语句处理可能的错误
    try:
        bet = int(input("How many credits do you want to bet? (1, 2, 5, or 10) "))
        # 用 if 语句判断下注是否合法，如果不合法，打印错误信息并跳过本次循环
        if bet not in BET_OPTIONS:
            print("Invalid bet. Please choose from 1, 2, 5, or 10.")
            continue
        # 用 if 语句判断下注是否超过玩家的积分，如果超过，打印错误信息并跳过本次循环
        if bet > credits:
            print("You don't have enough credits to bet", bet, ".")
            continue
    except ValueError:
        # 如果输入的不是整数，打印错误信息并跳过本次循环
        print("Invalid input. Please enter an integer.")
        continue
    # 从玩家的积分中扣除下注
    credits -= bet
    # 创建一个空列表，用于存储老虎机的结果
    slots = []
    # 用 for 循环生成三个随机的图案，添加到 slots 列表中
    for i in range(3):
        # 用 if 语句判断当前位置是否被保持，如果是，就沿用上一次的图案，如果不是，就生成一个新的图案
        if i in hold_position:
            slots.append(slots[i])
        else:
            slots.append(random.choice(SLOT_SYMBOLS))
    # 打印老虎机的结果
    print("You spin the slots and get:")
    print_slots(slots)
    # 调用 check_slots 函数，计算奖励积分
    reward = check_slots(slots, bet)
    # 用 if-else 语句判断奖励积分是否为 0，如果是，表示没有中奖，如果不是，表示中奖
    if reward == 0:
        # 没有中奖，打印信息，并将下注加入累积奖池
        print("Sorry, you didn't win anything.")
        jackpot += bet
        # 提示玩家是否使用保持功能，用 try-except 语句处理可能的错误
        try:
            hold = input("Do you want to hold one or two slots for the next spin? (y/n) ").lower() == "y"
            # 用 if 语句判断玩家是否选择使用保持功能，如果是，就继续执行，如果不是，就跳过
            if hold:
                # 用 if 语句判断上一次是否使用了保持功能，如果是，就打印错误信息并禁止使用，如果不是，就继续执行
                if hold_position:
                    print("You cannot use hold two times in a row.")
                    hold = False
                    hold_position = []
                else:
                    # 提示玩家输入要保持的位置，用 try-except 语句处理可能的错误
                    try:
                        hold_position = list(map(int, input("Enter the position(s) of the slot(s) you want to hold (1, 2, or 3, separated by space): ").split()))
                        # 用 for 循环遍历要保持的位置，用 if 语句判断是否合法，如果不合法，就打印错误信息并清空保持的位置
                        for pos in hold_position:
                            if pos not in [1, 2, 3]:
                                print("Invalid position. Please choose from 1, 2, or 3.")
                                hold_position = []
                                break
                            # 如果合法，就将位置减一，以便于后续的索引
                            else:
                                pos -= 1
                    except ValueError:
                        # 如果输入的不是整数，打印错误信息并清空保持的位置
                        print("Invalid input. Please enter integers.")
                        hold_position = []
        except ValueError:
            # 如果输入的不是 y 或 n，打印错误信息并禁止使用保持功能
            print("Invalid input. Please enter y or n.")
            hold = False
            hold_position = []
    else:
        # 中奖，打印信息，并将奖励积分加入玩家的积分
        print("Congratulations, you win", reward, "credits!")
        credits += reward
        # 用 if 语句判断是否中了奖池，如果是，就将累积奖池清零
        if slots[0] == "Jackpot":
            print("You hit the jackpot!")
            jackpot = 0
        # 清空保持的位置
        hold_position = []
  # 提示玩家是否继续游戏，用 try-except 语句处理可能的错误
try:
    play_choice = input("Do you want to play again? (y/n)").lower()
    if play_choice == 'n':
        play = False
    elif play_choice == 'y':
        play = True
    else:
        raise ValueError("Invalid input. Please enter 'y' or 'n'.")
except ValueError as e:
    print(f"Error: {e}")
    play = False
