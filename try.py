import tkinter as tk
from pathlib import Path

rules_file = Path(r"G:\Vansh\programming\Program\poker\Poker\poker_rules.txt").parent / "poker_rules.txt"

with open(rules_file, "r", encoding="utf-8") as f:
    rules = f.read()

window = tk.Tk()
window.title("Poker Rules")
window.geometry("800x600")

text = tk.Text(window, wrap="word")
text.pack(fill="both", expand=True)

text.insert("1.0", rules)
text.config(state="disabled")  # Makes text read-only

window.mainloop()