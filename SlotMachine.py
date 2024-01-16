import tkinter as tk
from tkinter import messagebox
import random

class SlotMachine:
    def __init__(self, master):
        self.master = master
        self.master.title("Slot Machine")
        self.credits = 100
        self.bet_amount = 1  # Default bet amount is set to 1
        self.jackpot = 0
        self.holds = [False, False, False]
        self.hold_count = 0  # Count for the number of holds
        self.result_labels = []

        self.create_widgets()

    def create_widgets(self):
        # Left-top: User Credits
        self.credit_label = tk.Label(self.master, text=f"Credits: {self.credits}")
        self.credit_label.grid(row=0, column=0, padx=10, pady=10, sticky='w')

        # Right-top: Potential Winnings (Jackpot)
        self.jackpot_label = tk.Label(self.master, text=f"Jackpot: {self.jackpot}")
        self.jackpot_label.grid(row=0, column=1, padx=10, pady=10, sticky='e')

        # Bet Buttons (1, 2, 5, 10)
        bet_options = [1, 2, 5, 10]
        row_bet_buttons = tk.Frame(self.master)
        row_bet_buttons.grid(row=1, column=0, columnspan=2, pady=10)

        for col, option in enumerate(bet_options):
            btn = tk.Button(row_bet_buttons, text=str(option), command=lambda o=option: self.place_bet(o))
            btn.grid(row=0, column=col, padx=5)

        # Spin Button
        spin_btn = tk.Button(self.master, text="Spin", command=self.spin)
        spin_btn.grid(row=2, column=0, columnspan=2, pady=10)

        # Hold Buttons (Hold 1, Hold 2, Hold 3)
        row_hold_buttons = tk.Frame(self.master)
        row_hold_buttons.grid(row=3, column=0, columnspan=2, pady=10)

        for col, i in enumerate(range(1, 4)):
            hold_btn = tk.Button(row_hold_buttons, text=f"Hold {i}", command=lambda j=i-1: self.toggle_hold(j))
            hold_btn.grid(row=0, column=col, padx=5)

        # Result Labels
        for row in range(4, 7):
            for col in range(3):
                label = tk.Label(self.master, text="", font=("Arial", 20))
                label.grid(row=row, column=col, padx=5)

                self.result_labels.append(label)

    def place_bet(self, amount):
        if self.credits >= amount:
            self.bet_amount = amount
            self.credits -= self.bet_amount
            self.credit_label.config(text=f"Credits: {self.credits}")
        else:
            messagebox.showinfo("Error", "Insufficient credits to place this bet.")

    def toggle_hold(self, slot_index):
        # Allow only two holds
        if self.hold_count < 2 or self.holds[slot_index]:
            self.holds[slot_index] = not self.holds[slot_index]
            self.hold_count += 1 if self.holds[slot_index] else -1

        # Show warning if exceeding hold limit
        if self.hold_count > 2:
            messagebox.showinfo("Warning", "You can only hold two symbols per spin.")

    def spin(self):
        if self.bet_amount == 0:
            messagebox.showinfo("Error", "Please place a bet first.")
            return

        # Always deduct credits when spinning
        self.credits -= self.bet_amount
        self.credit_label.config(text=f"Credits: {self.credits}")

        symbols = ["Cherry", "Lemon", "Lucky 7", "Bar", "Diamond", "Jackpot"]
        results = [random.choice(symbols) if not self.holds[i] else self.result_labels[i].cget("text") for i in range(3)]

        for i in range(3):
            self.result_labels[i].config(text=results[i])

        self.check_winning_combination(results)
        
    def check_winning_combination(self, results):
        # ... (unchanged code)

        if "Jackpot" in results:
            self.jackpot += self.bet_amount * 10
            self.jackpot_label.config(text=f"Jackpot: {self.jackpot}")

        if self.credits <= 0:
            self.end_game()

    def end_game(self):
        messagebox.showinfo("Game Over", f"Total credits: {self.credits}")
        self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    slot_machine = SlotMachine(root)
    root.mainloop()