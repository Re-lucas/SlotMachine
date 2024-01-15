import tkinter as tk
from tkinter import messagebox
import random

INITIAL_CREDITS = 100
BET_OPTIONS = [1, 2, 5, 10]
SLOT_SYMBOLS = ["Cherry", "Lemon", "Lucky 7", "Bar", "Diamond", "Jackpot"]
REWARD_MULTIPLIERS = {"Cherry": 3, "Lemon": 5, "Lucky 7": 7, "Bar": 10, "Diamond": 20, "Jackpot": 0}

credits = INITIAL_CREDITS
jackpot = 0
play = True
hold_position = []

def print_slots(slots):
    for slot in slots:
        print(slot, end=" ")
    print()

def check_slots(slots, bet):
    if slots[0] == "Cherry":
        if slots[1] == "Cherry":
            if slots[2] == "Cherry":
                reward = bet * REWARD_MULTIPLIERS["Cherry"]
            else:
                reward = bet * 2
        else:
            reward = bet
    elif slots[0] == slots[1] == slots[2]:
        if slots[0] == "Jackpot":
            reward = jackpot
        else:
            reward = bet * REWARD_MULTIPLIERS[slots[0]]
    else:
        reward = 0
    return reward

def spin_slots():
    global credits, jackpot, hold_position
    bet = int(bet_entry.get())
    
    if bet not in BET_OPTIONS:
        messagebox.showerror("Error", "Invalid bet. Please choose from 1, 2, 5, or 10.")
        return
    if bet > credits:
        messagebox.showerror("Error", f"You don't have enough credits to bet {bet}.")
        return
    
    credits -= bet
    slots = []
    for i in range(3):
        if i in hold_position:
            slots.append(slots[i])
        else:
            slots.append(random.choice(SLOT_SYMBOLS))
    
    print("You spin the slots and get:")
    print_slots(slots)
    
    reward = check_slots(slots, bet)
    if reward == 0:
        print("Sorry, you didn't win anything.")
        jackpot += bet
        try:
            hold = messagebox.askyesno("Hold Slots", "Do you want to hold one or two slots for the next spin?")
            if hold:
                if hold_position:
                    messagebox.showinfo("Hold Error", "You cannot use hold two times in a row.")
                    hold = False
                    hold_position = []
                else:
                    try:
                        hold_position = list(map(int, messagebox.askstring("Hold Slots", "Enter the position(s) of the slot(s) you want to hold (1, 2, or 3, separated by space): ").split()))
                        for pos in hold_position:
                            if pos not in [1, 2, 3]:
                                messagebox.showinfo("Hold Error", "Invalid position. Please choose from 1, 2, or 3.")
                                hold_position = []
                                break
                            else:
                                pos -= 1
                    except ValueError:
                        messagebox.showinfo("Hold Error", "Invalid input. Please enter integers.")
                        hold_position = []
        except ValueError:
            messagebox.showinfo("Hold Error", "Invalid input. Please enter y or n.")
            hold = False
            hold_position = []
    else:
        print(f"Congratulations, you win {reward} credits!")
        credits += reward
        if slots[0] == "Jackpot":
            print("You hit the jackpot!")
            jackpot = 0
        hold_position = []
    
    update_gui()

def update_gui():
    credits_label.config(text=f"You have {credits} credits.")
    jackpot_label.config(text=f"The jackpot is {jackpot} credits.")
    result_label.config(text="Result: Your slot machine result here")

root = tk.Tk()
root.title("Slot Machine Game")

bet_entry = tk.Entry(root, width=5)
bet_entry.grid(row=1, column=1, padx=10)
spin_button = tk.Button(root, text="Spin", command=spin_slots)
spin_button.grid(row=1, column=2, padx=10)
credits_label = tk.Label(root, text="")
credits_label.grid(row=2, column=1, padx=10)
jackpot_label = tk.Label(root, text="")
jackpot_label.grid(row=2, column=2, padx=10)
result_label = tk.Label(root, text="")
result_label.grid(row=3, column=1, columnspan=2, pady=10)

# Run the Tkinter main loop
root.mainloop()
