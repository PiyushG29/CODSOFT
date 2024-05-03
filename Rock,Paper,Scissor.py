import sys, random, time
import tkinter as tk
from PIL import Image, ImageTk

class RockPaperScissors:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Rock, Paper, Scissors")
        self.window.geometry("204x510")

        self.wins = 0
        self.losses = 0
        self.ties = 0

        self.create_widgets()

    def create_widgets(self):
        
        self.rock_image = ImageTk.PhotoImage(Image.open("C:/Users/piyush/Downloads/rock.png").resize((100,100)))
        self.paper_image = ImageTk.PhotoImage(Image.open("C:/Users/piyush/Downloads/paper.png").resize((100,100)))
        self.scissors_image = ImageTk.PhotoImage(Image.open("C:/Users/piyush/Downloads/scissors.png").resize((100,100)))
        # Create labels and buttons
        self.label = tk.Label(self.window, text="Rock, Paper, Scissors", font=("Arial", 15,"underline"),fg = 'magenta2',bg = 'cyan1')
        self.label.grid(pady = 2)

        self.rules_label = tk.Label(self.window, text="Rock beats scissors.\nPaper beats rocks.\nScissors beats paper.", font=("Segoe Script", 12),bg = 'lawn green')
        self.rules_label.grid()

        self.score_label = tk.Label(self.window, text="Wins: 0, Losses: 0, Ties: 0", font=("Arial", 12),bg = 'yellow')
        self.score_label.grid(pady = 5)

        self.rock_button = tk.Button(self.window, image=self.rock_image, command=lambda: self.play("ROCK"),bg = 'red')
        

        self.paper_button = tk.Button(self.window, image=self.paper_image, command=lambda: self.play("PAPER"),bg = 'red')
        

        self.scissors_button = tk.Button(self.window, image=self.scissors_image, command=lambda: self.play("SCISSORS"),bg = 'red')
        

        self.quit_button = tk.Button(self.window, text="Quit", command=self.window.destroy,bg = 'DarkOrange2')
        self.rock_button.grid(row=7)
        self.paper_button.grid(row=10)
        self.scissors_button.grid(row=13)
        self.quit_button.grid(row=16,pady = 10)

        # Load images


    def play(self, player_move):
        # Count to three with dramatic pauses:
        self.label.config(text="1...")
        self.window.update()
        time.sleep(0.25)
        self.label.config(text="2...")
        self.window.update()
        time.sleep(0.25)
        self.label.config(text="3...")
        self.window.update()
        time.sleep(0.25)

        # Generate computer move
        computer_move = random.choice(["ROCK", "PAPER", "SCISSORS"])

        # Display computer move
        self.label.config(text=f"Computer chose {computer_move}!")

        # Determine winner
        if player_move == computer_move:
            self.label.config(text="It's a tie!")
            self.ties += 1
        elif (player_move == "ROCK" and computer_move == "SCISSORS") or \
             (player_move == "PAPER" and computer_move == "ROCK") or \
             (player_move == "SCISSORS" and computer_move == "PAPER"):
            self.label.config(text="You win!")
            self.wins += 1
        else:
            self.label.config(text="You lose!")
            self.losses += 1

        # Update score label
        self.score_label.config(text=f"Wins: {self.wins}, Losses: {self.losses}, Ties: {self.ties}")

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = RockPaperScissors()
    game.run()