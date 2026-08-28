from customtkinter import *
from datas.hash import *
from scripts.hashing import *


USER_TOTAL_HASH = "You haven't entered anything yet."

class Window(CTk):
    def __init__(self):
        super().__init__()

        self.title("hash-app")
        self.geometry('1000x700')
        self.resizable(False, False)


        self.sidebar = CTkFrame(self, width=250, height=700)
        self.sidebar.pack(side='left')
        self.sidebar.pack_propagate(False)


        CTkLabel(self.sidebar, text='Hash-App', font=("San Francisco", 38, 'bold')).pack(side='top', pady=10) # Title


        self.choice_type_hashing = CTkOptionMenu(self.sidebar, values=HASHTYPES, width=200, height=30, font=("San Francisco", 16, 'bold'))
        self.choice_type_hashing.pack(side='top', pady=30)
        self.choice_type_hashing.set("Select a hashing algorithm.")


        self.input_text_for_hash = CTkEntry(self, width=300, placeholder_text="Enter your text for hashing", font=("San Francisco", 16, 'bold'))
        self.input_text_for_hash.pack(side='top', pady=30)


        self.input_salt_for_hash = CTkEntry(self, width=300, placeholder_text="Enter your salt for text (optional)", font=("San Francisco", 16, 'bold'))
        self.input_salt_for_hash.pack(side='top', pady=30)

        self.total_hash = CTkLabel(self, text=f'Your hash:\n{USER_TOTAL_HASH}', font=("San Francisco", 12, 'bold'))
        self.total_hash.pack(side='top', pady=30)


        self.button_next = CTkButton(self, text='Start', font=("San Francisco", 16, 'bold'), command=self.click_start)
        self.button_next.pack(side='bottom', pady=30)

    def click_start(self):
        if self.input_salt_for_hash.get() == "":
            if self.choice_type_hashing.get() == "SHA-224":
                USER_TOTAL_HASH = hash224(self.input_text_for_hash.get())
                self.total_hash.configure(text=f'Your hash:\n{USER_TOTAL_HASH}')
            if self.choice_type_hashing.get() == "SHA-256":
                USER_TOTAL_HASH = hash256(self.input_text_for_hash.get())
                self.total_hash.configure(text=f'Your hash:\n{USER_TOTAL_HASH}')
            if self.choice_type_hashing.get() == "SHA-384":
                USER_TOTAL_HASH = hash384(self.input_text_for_hash.get())
                self.total_hash.configure(text=f'Your hash:\n{USER_TOTAL_HASH}')
            if self.choice_type_hashing.get() == "SHA-512":
                USER_TOTAL_HASH = hash512(self.input_text_for_hash.get())
                self.total_hash.configure(text=f'Your hash:\n{USER_TOTAL_HASH}')
        else:
            if self.choice_type_hashing.get() == "SHA-224":
                USER_TOTAL_HASH = hash224(self.input_text_for_hash.get(), self.input_salt_for_hash.get())
                self.total_hash.configure(text=f'Your hash:\n{USER_TOTAL_HASH}')
            if self.choice_type_hashing.get() == "SHA-256":
                USER_TOTAL_HASH = hash256(self.input_text_for_hash.get(), self.input_salt_for_hash.get())
                self.total_hash.configure(text=f'Your hash:\n{USER_TOTAL_HASH}')
            if self.choice_type_hashing.get() == "SHA-384":
                USER_TOTAL_HASH = hash384(self.input_text_for_hash.get(), self.input_salt_for_hash.get())
                self.total_hash.configure(text=f'Your hash:\n{USER_TOTAL_HASH}')
            if self.choice_type_hashing.get() == "SHA-512":
                USER_TOTAL_HASH = hash512(self.input_text_for_hash.get(), self.input_salt_for_hash.get())
                self.total_hash.configure(text=f'Your hash:\n{USER_TOTAL_HASH}')