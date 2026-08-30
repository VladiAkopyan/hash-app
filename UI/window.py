from customtkinter import *
from datas.hash import *
from scripts.hashing import *
import pyperclip




class Window(CTk):
    def __init__(self):
        super().__init__()

        self.USER_TOTAL_HASH = "You haven't entered anything yet."

        self.title("hash-app")
        self.geometry('1400x900')
        self.resizable(False, False)


        self.sidebar = CTkFrame(self, width=400, height=860, corner_radius=50)
        self.sidebar.pack(side='left', padx=20)
        self.sidebar.pack_propagate(False)


        CTkLabel(self.sidebar, text='Hash-App', font=("San Francisco", 38, 'bold')).pack(side='top', pady=10) # Title


        self.choice_type_hashing = CTkOptionMenu(self.sidebar, values=HASHTYPES, width=300, height=30, font=("San Francisco", 16, 'bold'))
        self.choice_type_hashing.pack(side='top', pady=30)
        self.choice_type_hashing.set("Select a hashing algorithm.")


        self.input_text_for_hash = CTkEntry(self, width=300, placeholder_text="Enter your text for hashing", font=("San Francisco", 16, 'bold'))
        self.input_text_for_hash.pack(side='top', pady=30)


        self.input_salt_for_hash = CTkEntry(self, width=300, placeholder_text="Enter your salt for text (optional)", font=("San Francisco", 16, 'bold'))
        self.input_salt_for_hash.pack(side='top', pady=30)

        self.total_hash = CTkLabel(self, text=f'Your hash:\n{self.USER_TOTAL_HASH}', font=("San Francisco", 12, 'bold'))
        self.total_hash.pack(side='top', pady=30)

        self.button_copy = CTkButton(self, text='Copy Hash', font=("San Francisco", 16, 'bold'), command=self.copy_hash)
        self.button_copy.pack(side='top', pady=30)

        self.total_compare = CTkLabel(self, text='', font=("San Francisco", 16, 'bold'))
        self.total_compare.pack(side='top')

        self.button_next = CTkButton(self, text='Start', font=("San Francisco", 16, 'bold'), command=self.click_start)
        self.button_next.pack(side='bottom', pady=30)

    def copy_hash(self):
        if self.USER_TOTAL_HASH == "You haven't entered anything yet.":
            pass
        else:
            pyperclip.copy(self.USER_TOTAL_HASH)

    def compare_hashes(self):
        if self.input_for_compare_hashes.get() == self.USER_TOTAL_HASH: self.total_compare.configure(text='True')
        else: self.total_compare.configure(text='False')

    def click_start(self):
        if self.input_salt_for_hash.get() == "":
            if self.choice_type_hashing.get() == "SHA-224":
                self.USER_TOTAL_HASH = hash224(self.input_text_for_hash.get())
                self.total_hash.configure(text=f'Your hash:\n{self.USER_TOTAL_HASH}')
            if self.choice_type_hashing.get() == "SHA-256":
                self.USER_TOTAL_HASH = hash256(self.input_text_for_hash.get())
                self.total_hash.configure(text=f'Your hash:\n{self.USER_TOTAL_HASH}')
            if self.choice_type_hashing.get() == "SHA-384":
                self.USER_TOTAL_HASH = hash384(self.input_text_for_hash.get())
                self.total_hash.configure(text=f'Your hash:\n{self.USER_TOTAL_HASH}')
            if self.choice_type_hashing.get() == "SHA-512":
                self.USER_TOTAL_HASH = hash512(self.input_text_for_hash.get())
                self.total_hash.configure(text=f'Your hash:\n{self.USER_TOTAL_HASH}')
        else:
            if self.choice_type_hashing.get() == "SHA-224":
                self.USER_TOTAL_HASH = hash224(self.input_text_for_hash.get(), self.input_salt_for_hash.get())
                self.total_hash.configure(text=f'Your hash:\n{self.USER_TOTAL_HASH}')
            if self.choice_type_hashing.get() == "SHA-256":
                self.USER_TOTAL_HASH = hash256(self.input_text_for_hash.get(), self.input_salt_for_hash.get())
                self.total_hash.configure(text=f'Your hash:\n{self.USER_TOTAL_HASH}')
            if self.choice_type_hashing.get() == "SHA-384":
                self.USER_TOTAL_HASH = hash384(self.input_text_for_hash.get(), self.input_salt_for_hash.get())
                self.total_hash.configure(text=f'Your hash:\n{self.USER_TOTAL_HASH}')
            if self.choice_type_hashing.get() == "SHA-512":
                self.USER_TOTAL_HASH = hash512(self.input_text_for_hash.get(), self.input_salt_for_hash.get())
                self.total_hash.configure(text=f'Your hash:\n{self.USER_TOTAL_HASH}')