from customtkinter import *
from datas.hash import *

class Window(CTk):
    def __init__(self):
        super().__init__()

        self.title("hash-app")
        self.geometry('1000x700')
        self.resizable(False, False)

        self.sidebar = CTkFrame(self, width=400, height=700)
        self.sidebar.pack(side='left')
        self.sidebar.pack_propagate(False)


        CTkLabel(self.sidebar, text='Hash-App', font=("San Francisco", 38, 'bold')).pack(side='top', pady=10) # Title


        self.choice_type_hashing = CTkOptionMenu(self.sidebar, values=HASHTYPES, width=300, height=40, font=("San Francisco", 16, 'bold'))
        self.choice_type_hashing.pack(side='top', pady=30)