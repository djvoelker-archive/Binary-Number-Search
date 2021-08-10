import tkinter as tk

#not sure if I need this
#open("scripts.py")

import scripts

root = tk.Tk()
root.title("Binary Number Search")
root.geometry("600x400")

window = tk.LabelFrame(root, bd=0)
window.grid_columnconfigure

base = tk.LabelFrame(window, bd=0)
options = tk.LabelFrame(window, relief="sunken")

times_played = 0
lists_generated = 0
lists_shown = 0
list_visible = "Show"

label1 = tk.Label(base)
label3 = tk.Label(base)

label4 = tk.Label(options, text="Lower bound of values:")
label5 = tk.Label(options, text="Upper bound of values:")
label6 = tk.Label(options, text="Minimum size of list:")
label7 = tk.Label(options, text="Maximum size of list:")

min_num_scale = tk.Scale(options, from_=1, to=999, orient="horizontal")
max_num_scale = tk.Scale(options, from_=2, to=1000, orient="horizontal")
min_list_size = tk.Scale(options, from_=1, to=999, orient="horizontal")
max_list_size = tk.Scale(options, from_=2, to=1000, orient="horizontal")

min_num_scale.set(1)
max_num_scale.set(100)
min_list_size.set(20)
max_list_size.set(80)

errormessage1 = tk.Label(window)
errormessage2 = tk.Label(window)

def gen_list():
    global generated_list
    global label1
    global lists_generated
    global errormessage1
    global errormessage2
    errormessage1.destroy()
    errormessage2.destroy()
    if min_list_size.get() >= max_list_size.get():
        errormessage1 = tk.Label(window, fg="red", text="ERROR: max size of list must be greater than min size of list!")
        errormessage1.grid(column=0, row=2)
        if min_num_scale.get() >= max_num_scale.get():
            errormessage2 = tk.Label(window, fg="red", text="ERROR: upper bound of values must be greater than lower bound of values!")
            errormessage2.grid(column=0, row=1)
    elif min_num_scale.get() >= max_num_scale.get():
        errormessage2 = tk.Label(window, fg="red", text="ERROR: upper bound of values must be greater than lower bound of values!")
        errormessage2.grid(column=0, row=1)
    else:
        generated_list = scripts.list_gen(min_list_size.get(), max_list_size.get(), min_num_scale.get(), max_num_scale.get())
        label1.config(text=f"This program just randomly generated a list of {len(generated_list)} unique integers from {generated_list[0]} to {generated_list[-1]}.")
        lists_generated += 1


gen_list()

label3.config(text=f"You have searched for {times_played} numbers and generated {lists_generated} lists.")

def makelistdisplay():
    global display2
    display2 = tk.Text(master=base, width=30, height=10, exportselection=False, wrap="word")
    display2.grid(column=0, row=8)
    display2.insert(tk.END, generated_list)

def execute(): 
    global user_response
    global num_index
    global generated_list
    user_response = int(entry1.get())
    entry1.delete(0, len(entry1.get())+1)
    num_index = scripts.search(generated_list, user_response)

def display_index():
    global times_played
    try:
        execute()
        answer = scripts.respond(num_index, user_response)
        display = tk.Text(master=base, width=30, height=2, exportselection=False, wrap="word")
        display.grid(column=0, row=4)
        display.insert(tk.END, answer)
        times_played += 1
    except ValueError:
        return
    label3.config(text=f"You have searched for {times_played} numbers and generated {lists_generated} lists.")

def show_list():
    global lists_shown
    global generated_list
    global list_visible
    global button3
    if list_visible == "Show":
        list_visible = "Hide"
        makelistdisplay()
    else:
        list_visible = "Show"
        display2.destroy()
    button3.config(text=f"{list_visible} list")
    lists_shown += 1
    
def button2_pressed():
    global display2
    gen_list()
    label3.config(text=f"You have searched for {times_played} numbers and generated {lists_generated} lists.")
    if list_visible == "Hide":
        #for some reason you need to use "1.0" instead of 0 and "end" instead of len(generated_list)-1 for the indices.
        display2.delete("1.0", "end")
        display2.insert(tk.END, generated_list)


#widgets in the base LabelFrame
label1.grid(column=0, row=0)
label2 = tk.Label(base, text="What number would you like to search for in the list?")
label2.grid(column=0, row=1)
label3.grid(column=0, row=6)
entry1 = tk.Entry(base, exportselection=False)
entry1.grid(column=0, row=2)
button1 = tk.Button(base, text="Search for number", command=display_index, relief="raised")
button1.grid(column=0, row=3)
button2 = tk.Button(base, text="Generate new list", command=button2_pressed, relief="raised")
button2.grid(column=0, row=5)
button3 = tk.Button(base, text=f"{list_visible} list", command=show_list, relief="raised")
button3.grid(column=0, row=7)
pad1 = tk.Frame(base, width=450, bd=0)
pad1.grid(column=0, row=9)
base.grid(column=0, row=0, sticky="n", padx=0, pady=0)


#widgets in the options LabelFrame
label4.grid(column=0, row=0)
label5.grid(column=0, row=2)
label6.grid(column=0, row=4)
label7.grid(column=0, row=6)
min_num_scale.grid(column=0, row=1)
max_num_scale.grid(column=0, row=3)
min_list_size.grid(column=0, row=5)
max_list_size.grid(column=0, row=7)
options.grid(column=1, row=0, sticky="n")

window.grid(column=0, row=0)

root.mainloop()