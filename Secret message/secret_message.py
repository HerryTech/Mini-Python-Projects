from tkinter import simpledialog, messagebox
from random import choice

def get_task():
    task = simpledialog.askstring("Task", "Do you want to encrypt or decrypt a message?")
    return task

def get_message():
    messaage = simpledialog.askstring("Message", "Enter your secret message")
    return messaage

def encrypt_msg(message):
    alphabet = ["a", "b", "c", "d", "e", "f", "g"]
    encrypted_msg = []
    for letter in range(0, len(message)):
        encrypted_msg.append(message[letter])
        encrypted_msg.append(choice(alphabet))
    new_msg = "".join(encrypted_msg)
    return(new_msg)
    
def decrypt_msg(message):
    even_letters = []
    for letter in range(0, len(message)):
        if letter % 2 == 0:
            even_letters.append(message[letter])
    new_msg = "".join(even_letters)
    print(new_msg)

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
        
