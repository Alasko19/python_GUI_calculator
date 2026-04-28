import tkinter as tk


# main window
root = tk.Tk()
root.title("calculator")
root.geometry("400x500")
root.configure(bg="#2e2e2e")
root.resizable(False, False)

# center frame
main_frame = tk.Frame(root, bg="#2e2e2e")
main_frame.place(relx=0.5, rely=0.5, anchor="center")

# calc variaqbles
expression = ""
input_text = tk.StringVar()

# calc functions
def press(value):
    global expression
    expression += str(value)
    input_text.set(expression)

def clear():
    global expression
    expression = ""
    input_text.set("")

def calculate():
    global expression
    try:
        result = str(eval(expression))
        input_text.set(result)
        expression = result
    except:
        input_text.set("math Error")
        expression = ""


# display
display = tk.Entry(
    main_frame,
    textvariable=input_text,
    font=("Arial", 24),
    bg="#3b3b3b",
    fg="white",
    bd=0,
    justify="right",
    insertbackground="white",
    width=18
)
display.grid(row=0, column=0, columnspan=4, pady=15, ipady=10)

# Button style
btn_font=("Arial", 14)
btn_bg ="#4a4a4a"
btn_fg ="white"
btn_active ="#6a6a6a"

def create_button(text, row, col, cmd):
    tk.Button(
        main_frame,
        text=text,
        font=btn_font,
        bg=btn_bg,
        fg=btn_fg,
        activebackground=btn_active,
        activeforeground="white",
        width=5,
        height=2,
        bd=0,
        command=cmd
    ).grid(row=row, column=col, padx=5, pady=5)

# buttons
buttons =[
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("C", 4, 2), ("+", 4, 3),
]

for (text, row, col) in buttons:
    if text == "C":
        create_button(text, row, col, clear)
    else:
        create_button(text, row, col, lambda t=text: press(t))


# equal button
tk.Button(
    main_frame,
    text="=",
    font=("Arial",14),
    bg="#5c8df6",
    fg="white",
    activebackground="#4a7de0",
    width=27,
    height=2,
    bd=0,
    command=calculate
).grid(row=5, column=0, columnspan=4, pady=10)


# run
root.mainloop()