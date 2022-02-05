from tkinter import Tk
from ui.ui import UI

def main():
    window = Tk()
    window.title("Kirjoitusvirheiden korjaaja")

    ui = UI(window)
    ui.start()

    window.rowconfigure(0, minsize=400, weight=1)
    window.rowconfigure(3, minsize=400, weight=1)
    window.columnconfigure(1, minsize=800, weight=1)
    window.mainloop()

if __name__ == '__main__':
    main()