from sys import maxsize
from tkinter import Button, Text, Label, font

class UI:
    def __init__(self, root):
        self._root = root
        self._label_var = None

    def start(self):
        txt_area = Text(master=self._root, )

        reset_button = Button(
            master=self._root,
            text='Nollaa',
            command=self._reset
        )

        fix_text_button = Button(
            master=self._root,
            text='Korjaa teksti',
            command=self._fix_text
        )

        title = Label(master=self._root, text='Korjattu teksti', font=('Arial', 30))
        answer_text =  Label(master=self._root, text='Korjattua tekstiä \n \n \n \n \n \n \n \n \n esimerkki')
        
        txt_area.grid(row=0, columnspan=3, sticky="nsew")
        reset_button.grid(row=1, column=0)
        fix_text_button.grid(row=1, column=2)
        title.grid(row=2, column=1)
        answer_text.grid(row=3, columnspan=3)
    
    def _fix_text(self):
        pass

    def _reset(self):
        pass