from tkinter import *
from tkinter import messagebox



tasks = []
def add_task():
    task_name = entry.get()

    if task_name:
        tasks.append(task_name)
        listbox.insert(END,task_name)
        entry.delete(0,END)
    else:
        messagebox.showwarning("warning","You must enter a task.")


def remove_task():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        task_to_remove = listbox.get(selected_task_index)
        tasks.remove(task_to_remove)
        listbox.delete(selected_task_index)
    else:
        messagebox.showwarning("Warning", "You must select a task to remove.")


def mark_as_complete():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        task_to_complete = listbox.get(selected_task_index)
        tasks[tasks.index(task_to_complete)] += " ---(Task completed)"
        listbox.delete(selected_task_index)
        listbox.insert(selected_task_index,task_to_complete + " ---(Task completed)")
    else:
        messagebox.showwarning("Warning", "You must select a task to mark as complete.")

window = Tk()
window.geometry("400x400")
window.title("TO DO LIST")


frame = Frame(window)
frame.pack(pady=10)


entry = Entry(frame,width=35)
entry.pack(side=LEFT,padx=10)


add_button = Button(frame,text="Add task",command=add_task)
add_button.pack(pady=10)


listbox = Listbox(window,width=50,height=15)
listbox.pack(pady=10)


remove_button = Button(frame,text="Remove task",command=remove_task)
remove_button.pack(pady=5)


complete_button = Button(window,text="Mark as Complete",command=mark_as_complete)
complete_button.pack(pady=5)

window.mainloop()
