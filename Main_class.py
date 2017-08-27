from tkinter import Tk, ttk
from Menu_class import MenuClass
from Frame_class import FrameClass
from Utils_class import Utils
from Auto_com_port import COMports
from Pop_windows import windows
from Functionalities import Edit
from dxf_reader import DXF


class MainClass:
    def __init__(self, window):
        self.window = window
        self.app_name = 'EMVI CNC'
        self.window.title(self.app_name)
        self.width_size = self.window.winfo_screenwidth()
        self.height_size = self.window.winfo_screenheight()
        self.window.geometry('{0}x{1}'.format(self.width_size, self.height_size))


        # Com port
        self.Com_port = COMports(self)

        # The Frame Class
        self.FrameClass_handler = FrameClass(self)

        # pop windows
        self.pop_windows = windows(self)
        #class for drawing things on a canvas
        self.dxf_master=DXF(self)


        # functionalities
        self.functionalities = Edit(self)

        # The Utils Class
        self.utils_handler = Utils(self)

        # The Menu Class
        self.MenuClass_handler = MenuClass(self)




root = Tk()
Main_app = MainClass(root)
root.mainloop()