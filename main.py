from tkinter import *

total=0

def count():
    global total
    total += 1
    counter.config(text=total)



def reset():
    global total
    total = 0
    counter.config(text=total)


window = Tk()
window.title = "Counter"
window.config(padx=75, pady=20)
window.minsize(width=300, height=200)


counter = Label(text="0", font=("Arial", 48))
counter.grid(column=0, row=0, columnspan=3, padx=50, pady=0)

count_button = Button(text="Count", command=count)
count_button.grid(column=1, row=1, pady=50)

reset_button = Button(text="Reset", command=reset)
reset_button.grid(column=2, row=1)







window.mainloop()
