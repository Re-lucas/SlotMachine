import tkinter as tk
from tkinter import messagebox
import random

class SlotMachine:
    def __init__(self, master):
        self.master = master
        self.master.title("Slot Machine")
        self.credits = 100
        self.bet_amount = 0
        self.jackpot = 0
        self.holds = [False, False, False]
        self.result_labels = []

        self.create_widgets()

    def create_widgets(self):
        # Labels
        self.credit_label = tk.Label(self.master, text=f"Credits: {self.credits}")
        self.credit_label.pack()

        self.bet_label = tk.Label(self.master, text="Place your bet:")
        self.bet_label.pack()

        # Bet Buttons
        bet_options = [1, 2, 5, 10]
        for option in bet_options:
            btn = tk.Button(self.master, text=str(option), command=lambda o=option: self.place_bet(o))
            btn.pack()

        # Spin Button
        spin_btn = tk.Button(self.master, text="Spin", command=self.spin)
        spin_btn.pack()

        # Hold Buttons
        for i in range(3):
            hold_btn = tk.Button(self.master, text=f"Hold {i + 1}", command=lambda j=i: self.toggle_hold(j))
            hold_btn.pack()

        # Result Labels
        for _ in range(3):
            label = tk.Label(self.master, text="", font=("Arial", 20))
            self.result_labels.append(label)
            label.pack()

    def place_bet(self, amount):
        if self.credits >= amount:
            self.bet_amount = amount
            self.credit_label.config(text=f"Credits: {self.credits - self.bet_amount}")
        else:
            messagebox.showinfo("Error", "Insufficient credits to place this bet.")

    def toggle_hold(self, slot_index):
        self.holds[slot_index] = not self.holds[slot_index]

    def spin(self):
        if self.bet_amount == 0:
            messagebox.showinfo("Error", "Please place a bet first.")
            return

        if not any(self.holds):
            self.credits -= self.bet_amount

        symbols = ["Cherry", "Lemon", "Lucky 7", "Bar", "Diamond", "Jackpot"]
        results = [random.choice(symbols) if not self.holds[i] else self.result_labels[i].cget("text") for i in range(3)]

        for i in range(3):
            self.result_labels[i].config(text=results[i])

        self.check_winning_combination(results)

    def check_winning_combination(self, results):
        # ... (same as before)

        if "Jackpot" in results:
            self.jackpot += self.bet_amount * 10

        if self.credits <= 0:
            self.end_game()

    def end_game(self):
        messagebox.showinfo("Game Over", f"Total credits: {self.credits}")
        self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    slot_machine = SlotMachine(root)
    root.mainloop()
