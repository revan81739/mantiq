import tkinter as tk
from PIL import Image, ImageTk
from ui import theme

class MantiqWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Mantiq - Logical Reasoner")
        self.root.geometry("1000x700")
        self.root.configure(bg=theme.BACKGROUND)
        machine_image=Image.open("assets/machine.png")
        machine_image=machine_image.resize((400,300))
        self.machine_photo=ImageTk.PhotoImage(machine_image, Image.Resampling.NEAREST)
        self.machine_label=tk.Label(
            self.root,
            image=self.machine_photo,
            bg=theme.BACKGROUND
        )
        self.machine_label.pack(pady=20)
        self.input_box=tk.Text(
            self.root,
            height=8,
            width=50,
            bg=theme.PAPER,
            fg=theme.INK,
            font=("Courier", 12)
        )
        self.input_box.pack(pady=10)
        self.insert_button=tk.Button(
            self.root,
            text="Insert punch card",
            command=self.insert_card,
            bg=theme.BUTTON,
            fg="white",
            font=("Courier", 12)
        )
        self.insert_button.pack(pady=10)
        self.output_box=tk.Text(
            self.root,
            height=10,
            width=50,
            bg=theme.PAPER,
            fg=theme.INK,
            font=("Courier", 12)
        )
        self.output_box.pack(pady=10)
    def insert_card(self):
        self.output_box.delete("1.0", tk.END)
        self.output_box.insert(
            tk.END,
            "Processing card...\n\n"
            "Processing complete"
            )
