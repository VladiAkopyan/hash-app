from customtkinter import *

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