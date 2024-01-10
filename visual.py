import tkinter as tk
import random

class SlotMachineGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Slot Machine Game")

        self.credits = 100
        self.bet_choices = [1, 2, 5, 10]
        self.jackpot = 0

        # Define the PRIZES dictionary
        self.PRIZES = {
            "Cherry1": 1,
            "Cherry2": 2,
            "Cherry3": 3,
            "Lemon3": 5,
            "Lucky73": 7,
            "Bar3": 10,
            "Diamond3": 20,
            "Jackpot3": "Jackpot"
        }

        self.create_widgets()

    def create_widgets(self):
        # Credits label
        self.credits_label = tk.Label(self.master, text=f"Credits: {self.credits}")
        self.credits_label.pack()

        # Bet entry
        self.bet_entry = tk.Entry(self.master)
        self.bet_entry.pack()

        # Spin button
        self.spin_button = tk.Button(self.master, text="Spin", command=self.spin_slots)
        self.spin_button.pack()

        # Jackpot label
        self.jackpot_label = tk.Label(self.master, text=f"Jackpot: {self.jackpot}")
        self.jackpot_label.pack()

        # Result label
        self.result_label = tk.Label(self.master, text="")
        self.result_label.pack()

    def spin_slots(self):
        bet = self.get_bet()
        if bet:
            self.credits -= bet
            self.jackpot += bet

            slots = self.spin_slots_result()
            prize = self.check_result(slots)

            if prize > 0:
                self.credits += prize
                self.jackpot -= prize

            self.update_ui(slots, prize)

    def get_bet(self):
        try:
            bet = int(self.bet_entry.get())
            if bet in self.bet_choices and bet <= self.credits:
                return bet
            else:
                self.result_label.config(text="Invalid bet. Please try again.")
                return None
        except ValueError:
            self.result_label.config(text="Invalid bet. Please enter a number.")
            return None

    def spin_slots_result(self):
        return [random.choice(["Cherry", "Lemon", "Lucky 7", "Bar", "Diamond", "Jackpot"]) for _ in range(3)]

    def check_result(self, result):
        combination = "".join(item[0] for item in result)
        if combination in self.PRIZES:
            return self.PRIZES[combination]
        else:
            return 0

    def update_ui(self, result, prize):
        self.credits_label.config(text=f"Credits: {self.credits}")
        self.jackpot_label.config(text=f"Jackpot: {self.jackpot}")
        self.result_label.config(text=f"Your spin: {result[0]} | {result[1]} | {result[2]}\nPrize: {prize} credits")

if __name__ == "__main__":
    root = tk.Tk()
    app = SlotMachineGUI(root)
    root.mainloop()
