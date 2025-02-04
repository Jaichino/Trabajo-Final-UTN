from tkinter import Tk
from controlador.controlador_menuprincipal import ControladorMenuPrincipal

def main():
    root = Tk()
    ControladorMenuPrincipal(root)
    root.mainloop()


if __name__ == '__main__':
    main()
