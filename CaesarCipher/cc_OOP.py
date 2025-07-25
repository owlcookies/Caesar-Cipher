import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        
        #Variables for program
        self.alphabet = list("abcdefghijklmnopqrstuvwxyz")
        self.set_alphabet = set(self.alphabet)
        self.mode = ["encode","decode"]
        self.shift_number = tk.IntVar(self, 7)
        self.current_mode = tk.StringVar(self, self.mode[0])
        
        self.title("Apple")
        self.geometry("1200x800")
        
        self.frm = ttk.Frame(self, padding=(50, 100), border=2)
        self.frm.grid()
        
        #Text on screen 
        self.program_title = ttk.Label(self.frm, text="Caesar Cipher", font=("Comic Sans MS",30)).grid(column=7, row=0)
        self.input_title = ttk.Label(self.frm, text="Input Text",font=("Comic Sans MS", 15)).grid(column=0, row=0,pady=30)
        self.num_on_screen = ttk.Label(self.frm, textvariable=self.shift_number,font=("Comif Sans MS", 20)).grid(column=7,row=1, pady=20)
        self.output_title = ttk.Label(self.frm, text="Output Text", font=("Comic Sans MS", 15)).grid(column=9, row=0,padx=20,pady=30)
        
        #Textbox(input)
        self.text_box = tk.Text(self.frm, width=40, height=20, relief="sunken")
        self.text_box.grid(column=0,row=20,padx=20)
        
        #Textbox(output)
        self.display_box = tk.Text(self.frm, width=40, height=20, relief="sunken",state="disabled")
        self.display_box.grid(column=9,row=20,padx=20,pady=20)
        
        #Buttons
        self.change_mode = ttk.Button(self.frm, textvariable=self.current_mode, command=self.mode_change).grid(column=7,row=2)
        self.shift_num_up = ttk.Button(self.frm, text="+", command=self.shift_up).grid(column=6,row=1)
        self.shift_num_down = ttk.Button(self.frm, text="-", command=self.shift_down).grid(column=8,row=1)
        self.activate_button = ttk.Button(self.frm, text="begin", command=self.encode_decode)
        self.activate_button.grid(column=7,row=7,pady=25)
        
        
        
    def shift_up(self):    
        self.shift_number.set(self.shift_number.get() + 1)
        
    def shift_down(self):
        if self.shift_number.get() <= 1:
           return
    
        self.shift_number.set(self.shift_number.get() - 1)

    def mode_change(self):
        len_modes = len(self.mode)
        mode_number = self.mode.index(self.current_mode.get())
    
        self.current_mode.set(self.mode[(mode_number + 1) % len_modes])
    
    def encode_decode(self):
        new_word = ''
        choice = self.current_mode.get()
        number_to_shift = self.shift_number.get()
    
        word = self.text_box.get("1.0", tk.END)
    
        if choice == "decode":
            number_to_shift *= -1

        for letter in word:
            if letter not in self.set_alphabet and letter.lower() in self.set_alphabet:
                selected_letter = self.alphabet.index(letter.lower())
                encrypted_letter = (selected_letter + number_to_shift) % len(self.alphabet)
                new_word += self.alphabet[encrypted_letter].upper()
            
            elif letter not in self.set_alphabet:
                new_word += letter
            else:
                selected_letter = self.alphabet.index(letter)
                encrypted_letter = (selected_letter + number_to_shift) % len(self.alphabet)
                new_word += self.alphabet[encrypted_letter]
            
        self.display_box.config(state="normal")
        self.display_box.delete(1.0, tk.END)
        self.display_box.insert(1.0,new_word)
        self.display_box.config(state="disabled")
        
        


if __name__ == "__main__":
    app = App()
    app.mainloop() 
        
        
        
