import random

from tkinter import *

# ----------------- CONSTANTS -------------------- #
DARK = "#781C68"
MEDIUM_DARK = "#9A0680"
MEDIUM_LIGHT = "#FFD39A"
LIGHT = "#FFF5E1"
FONT_NAME = "Courier"

# ------- VARIABLE TO CONTROL STARTING AND STOPPING THE TRAINING ------- #
ongoing_training = False


# ------------------ UI FUNCTIONS ------------------- #
def update_speed(new_speed):
    speed_entry.delete(0, END)
    speed_entry.insert(0, new_speed)


# ------------------ TRAINING FUNCTIONS ------------------- #
def get_notes_to_train():
    # Return the notes ticked by the user as a list of strings
    global all_notes
    global note_checkboxes
    to_train = [note for (note, check) in zip(all_notes, note_checkboxes) if check.get() == 1]
    return to_train


def update_display(notes_to_train, training_interval):
    # Choose a random note and number of guitar string and display them
    note = random.choice(notes_to_train)
    string_num = random.randint(1, 6)
    string_str = f"String {string_num}"
    canvas.itemconfig(note_display, text=note)
    canvas.itemconfig(string_number_display, text=string_str)
    window.after(training_interval)
    window.update()


def start_training():
    global ongoing_training
    notes_to_train = get_notes_to_train()
    ongoing_training = True
    training_speed = int(speed_entry.get())
    training_interval = int(60000 / training_speed)
    while ongoing_training:
        update_display(notes_to_train, training_interval)


def stop_training():
    global ongoing_training
    ongoing_training = False


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Fretboard Trainer")
window.config(padx=30, pady=30, bg=MEDIUM_LIGHT)

# Display notes to play and string number
canvas = Canvas(width=300, height=300, bg=MEDIUM_LIGHT, highlightthickness=0)
note_display = canvas.create_text(150, 130, text="A", fill=DARK, font=(FONT_NAME, 90, "bold"))
string_number_display = canvas.create_text(150, 250, text="String 1", fill=DARK, font=(FONT_NAME, 35, "bold"))
canvas.grid(row=0, column=3, columnspan=6)

# Start and stop buttons
start_button = Button(text="Start", command=start_training, bg=LIGHT, fg=MEDIUM_DARK, width=20)
stop_button = Button(text="Stop", command=stop_training, bg=LIGHT, fg=MEDIUM_DARK, width=20)
start_button.grid(row=1, column=1, columnspan=4)
stop_button.grid(row=1, column=7, columnspan=4)

# Speed selection
select_speed_label = Label(text="Select speed (BPM)", bg=MEDIUM_LIGHT, fg=DARK)
select_speed_label.grid(row=2, column=0, columnspan=12)

speed_entry = Entry(window, width=8, bg=MEDIUM_LIGHT)
speed_entry.insert(0, "60")
speed_entry.grid(row=3, column=0, columnspan=2)

speed = IntVar(value=60)
speed_slider = Scale(window,
                     from_=20,
                     to=200,
                     command=update_speed,
                     orient=HORIZONTAL,
                     variable=speed,
                     bg=MEDIUM_LIGHT,
                     troughcolor=LIGHT,)
speed_slider.grid(row=3, column=2, columnspan=10, sticky="ew")

# Sounds selection
select_sounds_label = Label(text="Check the sounds you want to train", bg=MEDIUM_LIGHT, fg=DARK)
select_sounds_label.grid(row=4, column=0, columnspan=12)

all_notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
note_checkboxes = []
for i in range(12):
    note_var = IntVar()
    note_checkboxes.append(note_var)
    box = Checkbutton(window, text=all_notes[i], variable=note_checkboxes[i], bg=MEDIUM_LIGHT)
    box.grid(row=5, column=i)
    box.select()

window.mainloop()
