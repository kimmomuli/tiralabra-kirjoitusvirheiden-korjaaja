from tkinter import Button, Text, Label
from services.fix_text import FixText

class UI:
    def __init__(self, root):
        self._root = root
        self._label_var = None
        self.__answer_text = None
        self.__txt_area = None
        self.fixer = FixText()

    def start(self):
        self.__txt_area = Text(master=self._root,)

        reset_button = Button(
            master=self._root,
            text='Nollaa',
            command=lambda: self.__reset()
        )

        fix_text_button = Button(
            master=self._root,
            text='Korjaa teksti',
            command=lambda: self.__fix_text()
        )

        fix_text_fastly_button = Button(
            master=self._root,
            text='Korjaa teksti nopeasti',
            command=lambda: self.__fix_text_fastly()
        )

        title = Label(master=self._root, text='Korjattu teksti', font=('Arial', 30))

        self.__answer_text = Text(master=self._root,)
        
        self.__txt_area.grid(row=0, columnspan=3, sticky='nsew')

        reset_button.grid(row=1, column=0)
        fix_text_button.grid(row=1, column=2)
        fix_text_fastly_button.grid(row=2, column=2)
        title.grid(row=2, column=1)
        self.__answer_text.grid(row=3, columnspan=3, sticky='nsew')

    def __fix_text(self):
        input_text = self.__txt_area.get('1.0','end-1c')
        self.__answer_text.delete('1.0','end')
        
        fixed_text = self.fixer.fix_text(input_text)
        self.__answer_text.insert('1.0', fixed_text)
        self.__answer_text.grid(row=3, columnspan=3)

    def __fix_text_fastly(self):
        input_text = self.__txt_area.get('1.0','end-1c')
        self.__answer_text.delete('1.0','end')
        
        fixed_text = self.fixer.fix_text_fast(input_text)
        self.__answer_text.insert('1.0', fixed_text)
        self.__answer_text.grid(row=3, columnspan=3)

    def __reset(self):
        self.__answer_text.delete('1.0','end')
        self.__txt_area.delete('1.0','end')