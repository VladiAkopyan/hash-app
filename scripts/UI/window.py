from customtkinter import *

class Window(CTk):
    def __init__(self):
        super().__init__()

        self.title("hash-app")
        self.geometry('900x700')
        self.resizable(False, False)