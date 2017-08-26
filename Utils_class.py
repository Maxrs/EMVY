import tkinter
# utils

class Utils:
    def __init__(self, main_program):
        self.shortcut_bar = main_program.FrameClass_handler.shortcut_bar_frame
        self.func_handler = main_program.functionalities
        self.icons = ['open', 'save', 'save-as', 'copy', 'paste', 'cut', 'undo', 'redo']
        self.open_file()
        self.save_file()
        self.save_as()
        self.copy_()
        self.paste_()
        self.cut_()
        self.undo_()
        self.redo_()

    def open_file(self):
        self.open_image = tkinter.PhotoImage(file='icons/{}.png'.format(self.icons[0]))
        self.open_btn = tkinter.Button(self.shortcut_bar, image=self.open_image, command=self.func_handler.open_file)
        self.open_btn.config(bg='#424242', relief=tkinter.FLAT)
        self.open_btn.pack(side='left', padx = 10)

    def save_file(self):
        self.save_image = tkinter.PhotoImage(file='icons/{}.png'.format(self.icons[1]))
        self.save_btn = tkinter.Button(self.shortcut_bar, image=self.save_image, command=self.func_handler.save)
        self.save_btn.config(bg='#424242', relief=tkinter.FLAT)
        self.save_btn.pack(side='left', padx = 10)

    def save_as(self):
        self.saveas_image = tkinter.PhotoImage(file='icons/{}.png'.format(self.icons[2]))
        self.saveas_btn = tkinter.Button(self.shortcut_bar, image=self.saveas_image, command=self.func_handler.save_as)
        self.saveas_btn.config(bg='#424242', relief=tkinter.FLAT)
        self.saveas_btn.pack(side='left', padx = 10)

    def copy_(self):
        self.copy_image = tkinter.PhotoImage(file='icons/{}.png'.format(self.icons[3]))
        self.copy_btn = tkinter.Button(self.shortcut_bar, image=self.copy_image, command=self.func_handler.copy)
        self.copy_btn.config(bg='#424242', relief=tkinter.FLAT)
        self.copy_btn.pack(side='left', padx = 10)

    def paste_(self):
        self.paste_image = tkinter.PhotoImage(file='icons/{}.png'.format(self.icons[4]))
        self.paste_btn = tkinter.Button(self.shortcut_bar, image=self.paste_image, command=self.func_handler.paste)
        self.paste_btn.config(bg='#424242', relief=tkinter.FLAT)
        self.paste_btn.pack(side='left', padx = 10)

    def cut_(self):
        self.cut_image = tkinter.PhotoImage(file='icons/{}.png'.format(self.icons[5]))
        self.cut_btn = tkinter.Button(self.shortcut_bar, image=self.cut_image, command=self.func_handler.cut)
        self.cut_btn.config(bg='#424242', relief=tkinter.FLAT)
        self.cut_btn.pack(side='left', padx = 10)

    def undo_(self):
        self.undo_image = tkinter.PhotoImage(file='icons/{}.png'.format(self.icons[6]))
        self.undo_btn = tkinter.Button(self.shortcut_bar, image=self.undo_image, command=self.func_handler.undo)
        self.undo_btn.config(bg='#424242', relief=tkinter.FLAT)
        self.undo_btn.pack(side='left', padx = 10)

    def redo_(self):
        self.redo_image = tkinter.PhotoImage(file='icons/{}.png'.format(self.icons[7]))
        self.redo_btn = tkinter.Button(self.shortcut_bar, image=self.redo_image, command=self.func_handler.redo)
        self.redo_btn.config(bg='#424242', relief=tkinter.FLAT)
        self.redo_btn.pack(side='left', padx = 10)

