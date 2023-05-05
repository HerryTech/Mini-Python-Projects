from tkinter import simpledialog, messagebox

def get_task():
    task = simpledialog.askstring("Task", "Do you want to encrypt or decrypt a message?")
    return task

def get_message():
    messaage = simpledialog.askstring("Message", "Enter your secret message")
    return messaage

def get_even_letters(message):
    even_letters = []
    for letter in range(len(message)):
        if letter % 2 == 0:
            even_letters.append(message[letter])
    return even_letters

def get_old_letters(message):
    old_letters = []
    for letter in range(len(message)):
        if letter % 2 != 0:
            old_letters.append(message[letter])
    return old_letters
    
def swap_letters(message):
    swapped_letters = []
    if len(message) % 2 != 0:
        message += "x"
    old_letters = get_old_letters(message) 
    even_letters = get_even_letters(message)
    for letter in range(0, int(len(message) / 2)):
        swapped_letters.append(old_letters[letter])
        swapped_letters.append(even_letters[letter])
    new_message = "".join(swapped_letters)
    return(new_message)     

while True:
    task = get_task()
    if task == "encrypt":
        message = get_message()
        encrypt = swap_letters(message)
        messagebox.showinfo("Encrypted Message", f"Ciphertext of the secret message is: {encrypt}")
    elif task == "decrypt":
        message = get_message()
        decrypt = swap_letters(message)
        messagebox.showinfo("Decrypted Message", f"Plaintext of the secret message is: {decrypt}")
    else:
        break
        
