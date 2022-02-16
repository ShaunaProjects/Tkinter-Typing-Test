from tkinter import *
from tkinter import messagebox
import pandas as pd
import random

class App(Tk):
    def __init__(self):
        super().__init__()
        self.title("Classical Typing Test")
        self.config(padx=20, pady=20, bg="#b5dbe9")
        self.fontname = "Calibri"
        self.time_left = 30
        self.text = pd.read_excel("text_samples.xlsx")
        self.title_label = Label(text="Welcome to the Classical Typing Test!",
                                 font=(self.fontname, 18),
                                 bg="#b5dbe9",
                                 wraplength=1000,
                                 justify="center")
        self.title_label.grid(column=0, row=0, columnspan=2)
        self.explanation = Label(text="This will test how quickly you can type using extracts from classical"
                                      " literature. Type as much as you can of the shown passage within 30 seconds. "
                                      "After the time is up, you will be shown your calculated words per minute. Press"
                                      " the start button when you are ready.",
                                 font=(self.fontname, 12),
                                 bg="#b5dbe9",
                                 wraplength=800,
                                 justify="center")
        self.explanation.grid(column=0, row=1, columnspan=2)
        self.start_button = Button(text="Start", width=10, font=(self.fontname, 14), command=self.start_timer)
        self.start_button.grid(column=0, row=3, pady=10, columnspan=2)
        self.timer_label = Label(text=self.time_left, font=(self.fontname, 20), bg="#b5dbe9")
        self.timer_label.grid(column=0, row=2, columnspan=2)
        self.sample_text = Label(text=random.choice(self.text["Sample"]),
                                 font=(self.fontname, 12),
                                 wraplength=500,
                                 justify="left",
                                 borderwidth=1,
                                 relief="solid",)
        self.sample_text.grid(column=0, row=4, sticky="n", padx=10)
        self.entry_box = Text(width=60, height=25, wrap=WORD, font=(self.fontname, 12))
        self.entry_box.grid(column=1, row=4, sticky="n", padx=10)

    def countdown(self):
        if self.time_left > 0:
            self.time_left -= 1
            self.timer_label.configure(text=self.time_left)
            self.after(1000, self.countdown)
        else:
            self.calculate_wpm()

    def start_timer(self):
        self.entry_box.focus()
        self.start_button["state"] = DISABLED
        self.countdown()

    def calculate_wpm(self):
        typed_char = self.entry_box.get(1.0, "end-1c")
        wpm = (len(typed_char) / 5) * 2
        wpm_message = messagebox.askyesno(title="Your Results", message=f"Your WPM is {wpm}!\nWould you like to try"
                                                                        f" again? If no, the program will close.")
        if wpm_message:
            self.entry_box.delete(1.0, "end-1c")
            self.sample_text.configure(text=random.choice(self.text["Sample"]))
            self.start_button["state"] = ACTIVE
            self.time_left = 30
            self.timer_label.configure(text=self.time_left)
        else:
            self.quit()


app = App()
app.mainloop()