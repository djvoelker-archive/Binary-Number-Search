import tkinter as tk
import main

window = tk.Tk()
window.title("Binary Number Search")
window.geometry("400x400")

times_played = 0
    
def gen_list():
    global generated_list
    generated_list = main.list_gen(20, 100, 1, 100)

gen_list()

def execute(): 
    global user_response
    global num_index
    global generated_list
    user_response = int(entry1.get())
    num_index = main.search(generated_list, user_response)

def display_index():
    global times_played
    execute()
    answer = main.respond(num_index, user_response)
    display = tk.Text(master=window, width=30, height=2, exportselection=False, wrap="word")
    display.grid(column=0, row=4)

    display.insert(tk.END, answer)    
    
    times_played += 1

#label1 and label3 need to be repeated so they can continuously update.

#label1 = tk.Label(text=f"This program just generated a list of {len(generated_list)} random integers from {generated_list[0]} to {generated_list[-1]}.")
#label1.grid(column=0, row=0)

label2 = tk.Label(text="What number would you like to search for in the list?")
label2.grid(column=0, row=1)

#label3 = tk.Label(text=f"You have played this game {times_played} times.")
#label3.grid(column=0, row=6)

entry1 = tk.Entry(exportselection=False)
entry1.grid(column=0, row=2)

button1 = tk.Button(text="Search for number", command=display_index)
button1.grid(column=0, row=3)

button2 = tk.Button(text="Generate new list", command=gen_list)
button2.grid(column=0, row=5)

window.mainloop()