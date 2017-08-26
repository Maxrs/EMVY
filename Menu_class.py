from tkinter import Menu
from tkinter import LEFT

class MenuClass:
    def __init__(self,main_program):
        self.gcode_content = main_program.FrameClass_handler.gcode_content
        self.root =main_program.window
        self.frameclasshandler = main_program.FrameClass_handler
        self.functionalities_handler = main_program.functionalities
        self.popwindows_handler = main_program.pop_windows
        # Instance Definition
        self.shortcut_bar_frame = main_program.FrameClass_handler.shortcut_bar_frame
        self.menu_bar = Menu(self.shortcut_bar_frame)
        self.file = Menu(self.menu_bar, tearoff=0)
        self.edit = Menu(self.menu_bar, tearoff=0)
        self.machine = Menu(self.menu_bar, tearoff=0)
        self.simulation = Menu(self.menu_bar, tearoff=0)
        self.help = Menu(self.menu_bar, tearoff=0)

        self.file_menu()
        self.edit_menu()
        self.machine_menu()
        self.simulation_menu()
        self.help_menu()

    def file_menu(self):
        # The file menu
        self.menu_bar.add_cascade(label='File', menu=self.file)
        self.file.add_command(label='Open', accelerator='Ctrl+O', compound=LEFT, command=self.functionalities_handler.open_file)
        self.file.add_command(label='New', accelerator='Ctrl+N', compound=LEFT, command=self.functionalities_handler.new_file)
        self.file.add_separator()
        self.file.add_command(label='Save', accelerator='Ctrl+S', compound=LEFT, command=self.functionalities_handler.save)
        self.file.add_command(label='Save as', accelerator='Ctrl+Alt+S', compound=LEFT, command=self.functionalities_handler.save_as)
        self.file.add_command(label='PrintCode', accelerator='Ctrl+P', compound=LEFT)
        self.file.add_separator()
        self.file.add_command(label='Import DXF', accelerator='Ctrl+I', compound=LEFT, command=self.functionalities_handler.import_dxf)
        self.file.add_command(label='Preferences', compound=LEFT, command= self.popwindows_handler.preference)
        self.file.add_command(label='Exit', compound=LEFT, command= self.root.quit)

    def edit_menu(self):
        # Edit menu
        self.menu_bar.add_cascade(label='Edit', menu=self.edit)
        self.edit.add_command(label='Undo', accelerator='Ctrl+Z', compound=LEFT, command= self.functionalities_handler.undo)
        self.edit.add_command(label='Redo', accelerator='Ctrl+Y', compound=LEFT, command= self.functionalities_handler.redo)
        self.edit.add_separator()
        self.edit.add_command(label='Copy', accelerator='Ctrl+C', compound=LEFT, command= self.functionalities_handler.copy)
        self.edit.add_command(label='Cut', accelerator='Ctrl+X', compound=LEFT, command= lambda :
        [self.functionalities_handler.cut(), self.frameclasshandler.on_content_changed()])
        self.edit.add_command(label='Paste', accelerator='Ctrl+V', compound=LEFT, command= self.functionalities_handler.paste)
        self.edit.add_separator()
        self.edit.add_command(label='Select all', accelerator='Ctrl+A', compound=LEFT, command= self.functionalities_handler.select_all)
        self.edit.add_command(label='Find', accelerator='Ctrl+F', compound=LEFT, command= self.functionalities_handler.find_text)
        self.edit.add_command(label='Jump to line', compound=LEFT, command= self.popwindows_handler.jump_to_line)

    def machine_menu(self):
        # Machine menu declaration
        self.menu_bar.add_cascade(label='Machine', menu=self.machine)
        self.machine.add_command(label='Start', compound=LEFT)
        self.machine.add_command(label='Stop', compound=LEFT)
        self.machine.add_command(label='Pause', compound=LEFT)
        self.machine.add_separator()
        self.machine.add_command(label='Settings', compound=LEFT, command=self.popwindows_handler.machine_setting)

    def simulation_menu(self):
        # Simulation menu
        self.menu_bar.add_cascade(label='Simulation', menu=self.simulation)
        self.simulation.add_command(label='Start', compound=LEFT)
        self.simulation.add_command(label='Pause', compound=LEFT)
        self.simulation.add_command(label='Stop', compound=LEFT)
        self.simulation.add_separator()
        self.simulation.add_command(label='Zoom Out', compound=LEFT)
        self.simulation.add_command(label='Zoom In', compound=LEFT)

    def help_menu(self):
        # help menu
        self.menu_bar.add_cascade(label='Help', menu=self.help)
        self.help.add_command(label='About', compound=LEFT, command=self.popwindows_handler.about_window)
        self.help.add_separator()
        self.help.add_command(label='Help', compound=LEFT)
        self.root.config(menu=self.menu_bar)
