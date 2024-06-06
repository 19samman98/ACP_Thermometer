######################################################################
# Author: Sam McFarland
#
# Purpose: A program which takes user input and creates a "thermometer" to track donation progress
######################################################################

import tkinter as tk
from tkinter import ttk


# A class for the thermometer
class FundraisingThermometer(tk.Tk):
    def __init__(self, goal):
        super().__init__()
        self.title("Fundraising Goal Thermometer")
        self.geometry("300x600")

        self.goal = goal
        self.current_amount = 0

        self.create_widgets()
        self.update_thermometer()

    def create_widgets(self):
        """
        Creates the widgets to display on the TKinter screen
        :return: None
        """
        # Displays the goal at the top of the window
        self.label_goal = ttk.Label(self, text=f"Goal: ${self.goal}")
        self.label_goal.pack(pady=10)

        # Creates the white bar background of the thermometer
        self.canvas = tk.Canvas(self, width=100, height=400, bg="white")
        self.canvas.pack(pady=10)

        # Creates a fill for the thermometer
        self.fill = self.canvas.create_rectangle(20, 400, 80, 400, fill="red")

        # Creates a label for the current amount donated
        self.label_current = ttk.Label(self, text=f"Current: ${self.current_amount}")
        self.label_current.pack(pady=10)

        # Creates the entry box for the amount donated
        self.entry = ttk.Entry(self)
        self.entry.pack(pady=10)
        self.entry.insert(0, "Enter amount")

        # Creates the button that updates the thermometer with the amount entered
        self.button_update = ttk.Button(self, text="Update Amount", command=self.update_amount)
        self.button_update.pack(pady=10)

    def update_amount(self):
        """
        Sets the amount for the thermometer whenever a new amount (at or above 0) is entered
        :return: None
        """
        # Checks if the entry is an integer and if it's 0 or more
        try:
            new_amount = int(self.entry.get())
            if new_amount >= 0:
                self.current_amount = new_amount
                self.update_thermometer()
            else:
                print("Amount must be positive")

        # If the user enters an invalid input displays a message
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Updates the thermometer with the correct bar
    def update_thermometer(self):
        height = (self.current_amount / self.goal) * 400
        self.canvas.coords(self.fill, 20, 400 - height, 80, 400)
        self.label_current.config(text=f"Current: ${self.current_amount}")


# Runs the program and asks for user input for how much they want to fundraise
if __name__ == "__main__":
    goal_amount = int(input("Enter the dollar amount of your fundraising goal: "))  # Set your fundraising goal here
    app = FundraisingThermometer(goal_amount)
    app.mainloop()
