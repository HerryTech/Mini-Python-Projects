from tkinter import simpledialog, messagebox

def get_task():
    task = simpledialog.askstring("Task", "Do you want to encrypt or decrypt a message?")
    return task

def get_message():
    messaage = simpledialog.askstring("Message", "Enter your secret message")
    return messaage

while True:
    task = get_task()
    if task == "encrypt":
        message = get_message()
        messagebox.showinfo("Message", f"Message to encrypt is: {message}")
    elif task == "decrypt":
        message = get_message()
        messagebox.showinfo("Message", f"Message to decrypt is: {message}")
    else:
        break
