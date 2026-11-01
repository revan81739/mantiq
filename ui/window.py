import tkinter as tk
from tkinter import ttk
from resources import resource_path
import pygame
from logic.errors import format_error
from logic.examples import EXAMPLES
from logic.reporter import Reporter
from logic.verifier import Verifier
from logic.evaluator import Evaluator
from logic.parser import Parser
from PIL import Image, ImageTk
from ui import theme
from logic.lexer import Lexer

class MantiqWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Mantiq - Logical Reasoner")
        self.root.geometry("1000x700")
        self.root.configure(bg=theme.BACKGROUND)

        pygame.mixer.init()
        self.typewriter_sound= pygame.mixer.Sound(resource_path("sound/typewriter.wav"))
        self.typewriter_sound.set_volume(0.5)

        self.current_argument=None
        self.main_frame=tk.Frame(self.root, bg=theme.BACKGROUND)
        self.main_frame.pack(fill="both", expand =True)
        self.left_frame=tk.Frame(self.main_frame, bg=theme.BACKGROUND)
        self.right_frame=tk.Frame(self.main_frame, bg=theme.BACKGROUND, width=250)
        self.left_frame.pack(
            side="left",
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )
        self.right_frame.pack(
            side="right",
            fill="y",
            padx=20,
            pady=20
        )
        tk.Label(
            self.right_frame,
            text="Punch Card Library",
            bg=theme.BACKGROUND,
            font=("Courier", 12, "bold"),
        ).pack(anchor="n")
        self.selected_example=tk.StringVar()
        self.selected_example.set("Select an example...")
        self.dropdown=tk.OptionMenu(
            self.right_frame,
            self.selected_example,
            *EXAMPLES.keys(),
            command=self.load_example
        )
        self.dropdown.config(font=("Courier", 11), width=24)
        self.dropdown.pack(pady=10)

        self.truth_button= tk.Button(
            self.right_frame,
            text= "Generate truth table",
            command= self.show_truth_table,
            bg= theme.BUTTON,
            fg="white",
            font=("Courier", 11)
        )
        self.truth_button.pack(pady=40)

        self.table_frame=tk.Frame(self.right_frame, bg=theme.BACKGROUND)
        self.table_frame.pack(pady=20)
        self.truth_table=ttk.Treeview(
            self.table_frame,
            show="headings",
            height= 8
        )
        self.truth_table.pack()
        self.close_table_button= tk.Button(
            self.table_frame,
            text="Close table",
            command= self.close_truth_table,
            bg=theme.BUTTON,
            fg="white",
            font=("Courier", 10)
            )
        self.close_table_button.pack_forget()



        machine_image=Image.open(resource_path("assets/machine.png"))
        machine_image=machine_image.resize((400,300), Image.Resampling.NEAREST)
        self.machine_photo=ImageTk.PhotoImage(machine_image)
        self.machine_label=tk.Label(
            self.left_frame,
            image=self.machine_photo,
            bg=theme.BACKGROUND
        )
        self.machine_label.pack(pady=20)
        self.input_box=tk.Text(
            self.left_frame,
            height=8,
            width=50,
            bg=theme.PAPER,
            fg=theme.INK,
            font=("Courier", 12)
        )#go listen to math rock yes thats a real genre its so good man
        self.input_box.pack(pady=10)
        self.insert_button=tk.Button(
            self.left_frame,
            text="Insert punch card",
            command=self.insert_card,
            bg=theme.BUTTON,
            fg="white",
            font=("Courier", 12)
        )
        self.insert_button.pack(pady=10)
        self.output_box=tk.Text(
            self.left_frame,
            height=10,
            width=50,
            bg=theme.PAPER,
            fg=theme.INK,
            font=("Courier", 12)
        )
        self.output_box.pack(pady=10)

    def load_example(self, selection):
        if not EXAMPLES[selection]:
            return
        
        self.input_box.delete("1.0", tk.END)
        self.input_box.insert(tk.END, EXAMPLES[selection])
    
    def show_truth_table(self):
        if self.current_argument is None:
            return
        if not self.truth_table.winfo_ismapped():
            self.truth_table.pack()

        
        verifier= Verifier()
        table=verifier.generate_argument_truth_table(self.current_argument)

        for item in self.truth_table.get_children():
            self.truth_table.delete(item)
        variables= sorted(verifier.get_argument_variables(self.current_argument))
        columns= (variables + ["Premises", "Conclusion"])
        self.truth_table["columns"] = columns
        #if you are reading this repent and turn to the Most Merciful
        
        for column in columns:
            self.truth_table.heading(column, text=column)
            self.truth_table.column(
                column, width=70,
                anchor="center"
            )


        for row in table:
            values = []
            for variable in variables:
                values.append(
                    "T"
                    if row["assignment"][variable]
                    else "F"
            )

            values.append(
                "T"
                if all(row["premises"])
                else "F"
            )
            values.append(
                "T"
                if row["conclusion"]
                else "F"
            )
            self.truth_table.insert(
                "",
                tk.END,
                values=values
            )
        if not self.close_table_button.winfo_ismapped():
            self.close_table_button.pack(pady=10)


    def close_truth_table(self):
        self.truth_table.pack_forget()
        self.close_table_button.pack_forget()
        for item in self.truth_table.get_children():
            self.truth_table.delete(item)


    def insert_card(self):
       
        try:
            self.insert_button.config(state="disabled")
            
            self.typewriter_sound.stop()
            self.typewriter_sound.play(loops=-1)
       
            lexer = Lexer()
            text=self.input_box.get("1.0", tk.END)
            tokens=lexer.tokenize(text)
            parser =Parser(tokens)
            argument=parser.parse_argument()
            self.current_argument= argument

            verifier = Verifier()
            valid, counterexample = verifier.verify_argument(argument)

            reporter=Reporter()
            report= reporter.generate(argument, valid, counterexample)
            self.output_box.delete("1.0", tk.END)
            self.full_report= report
            self.current_index = 0
            self.animate_output()
            
        
        except Exception as error:
            self.typewriter_sound.stop()
            self.output_box.delete("1.0", tk.END)
            self.output_box.insert(tk.END, format_error(error))


    def animate_output(self):
        if self.current_index < len(self.full_report):
            self.output_box.insert(
                tk.END,
                self.full_report[self.current_index]
            )
            self.output_box.see(tk.END)
            self.current_index += 1
            self.root.after(25, self.animate_output)
        else:
            self.typewriter_sound.stop()
            self.insert_button.config(state="normal")