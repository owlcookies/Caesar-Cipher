# This script is an implementation of a Caesar cipher, which is an encryption technique that shifts letters in the alphabet by a number we choose.
import tkinter as tk
from tkinter import ttk

alphabet = list("abcdefghijklmnopqrstuvwxyz")
set_alphabet = set(alphabet)
modes = ["encode", "decode"]

# Caesar cipher logic

def shift_up():
    global shift_number
    
    shift_number.set(shift_number.get() + 1)
        
def shift_down():
    global shift_number
    if shift_number.get() <= 1:
        return
    
    shift_number.set(shift_number.get() - 1)

def mode_change():
    global current_mode
    len_modes = len(modes)
    mode_number = modes.index(current_mode.get())
    
    current_mode.set(modes[(mode_number + 1) % len_modes])
    
def encode_decode():
    global display_box
    new_word = ''
    choice = current_mode.get()
    number_to_shift = shift_number.get()
    
    word = text_box.get("1.0", tk.END)
    
    if choice == "decode":
        number_to_shift *= -1

    for letter in word:
        if letter not in set_alphabet and letter.lower() in set_alphabet:
            selected_letter = alphabet.index(letter.lower())
            encrypted_letter = (selected_letter + number_to_shift) % len(alphabet)
            new_word += alphabet[encrypted_letter].upper()
            
        elif letter not in set_alphabet:
            new_word += letter
        else:
            selected_letter = alphabet.index(letter)
            encrypted_letter = (selected_letter + number_to_shift) % len(alphabet)
            new_word += alphabet[encrypted_letter]
            
    display_box.config(state="normal")
    display_box.delete(1.0, tk.END)
    display_box.insert(1.0,new_word)
    display_box.config(state="disabled")

root = tk.Tk()
shift_number = tk.IntVar(root, 7)
current_mode = tk.StringVar(root, value = modes[0])
root.title("CaesarCipher")


frm = ttk.Frame(root, padding=(50, 100), border=2)

frm.grid()

#Text
title = ttk.Label(frm, text="Caesar Cipher", font=("Comic Sans MS",30)).grid(column=7, row=0)
input_title = ttk.Label(frm, text="Input Text",font=("Comic Sans MS", 15)).grid(column=0, row=0,pady=30)
num_on_screen = ttk.Label(frm, textvariable=shift_number,font=("Comif Sans MS", 20)).grid(column=7,row=1, pady=20)
text_box = tk.Text(frm, width=40, height=19, relief="sunken")
text_box.grid(column=0,row=20,padx=20)
output_title = ttk.Label(frm, text="Output Text", font=("Comic Sans MS", 15)).grid(column=9, row=0,padx=20,pady=30)
display_box = tk.Text(frm, width=40, height=20, relief="sunken",state="disabled")
display_box.grid(column=9,row=20,padx=20,pady=20)


#Buttons
change_mode = ttk.Button(frm, textvariable=current_mode, command=mode_change).grid(column=7,row=2)
shift_num_up = ttk.Button(frm, text="+", command=shift_up).grid(column=6,row=1)
shift_num_down = ttk.Button(frm, text="-", command=shift_down).grid(column=8,row=1)
activate_button = ttk.Button(frm, text="begin", command=encode_decode)
activate_button.grid(column=7,row=7,pady=25)


root.mainloop() 
