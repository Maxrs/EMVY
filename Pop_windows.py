from tkinter import *
from tkinter import ttk
# pop

class windows:

    def __init__(self, main_program):
        self.root= main_program.window
        self.height = self.root.winfo_screenheight()
        self.width = self.root.winfo_screenwidth()

    def preference(self):
        self.preference_window = Toplevel(self.root)
        self.preference_window.title('Preferences')
        self.preference_window.geometry('500x400+400+200')
        self.preference_window.transient(self.root)
        self.preference_window.resizable(False, False)
        self.text = Label(self.preference_window, text="Sorry Empty for now")
        self.text.place(x=200, y=200)

    def machine_setting(self):
        self.setting_window = Toplevel(self.root)
        self.setting_window.title('Settings')
        self.setting_window.geometry('500x400+400+200')
        self.setting_window.transient(self.root)
        self.setting_window.resizable(False, False)
        self.text1 = Label(self.setting_window, text="Sorry Empty for now")
        self.text1.place(x=200, y=200)

    def about_window(self):
        self.about_window = Toplevel(self.root)
        self.about_window.title('About Emvi')
        self.about_window.geometry('550x384+400+200')
        self.about_window.transient(self.root)
        self.about_window.resizable(False, False)
        self.top_frame = Frame(self.about_window, height=60)
        self.top_frame.pack(fill=X)
        self.separator = ttk.Frame(self.about_window, height=2)
        self.separator.pack(fill=X, expand=1, side=TOP, anchor=NW)
        self.middle_frame = Frame(self.about_window, height=284, bg= 'light green')
        self.middle_frame.pack_propagate(False)
        self.middle_frame.pack(fill=X)
        self.bottom_frame = Frame(self.about_window, height=40)
        self.bottom_frame.pack_propagate(False)
        self.bottom_frame.pack(fill=X)
        self.image= PhotoImage(file='icons/cnc_machine1600.png')
        self.label_image = Label(self.top_frame, image=self.image)
        self.label_image.pack(side='left', anchor=NW, padx=10)
        self.text_label = Label(self.top_frame, text="EMVI CNC Software", font='Myriad 23')
        self.text_label.pack(side='top', anchor=NW, padx=10, pady=10)

        words = 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit.' \
                'Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque' \
                'penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec' \
                'quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat' \
                'massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. ' \
                'In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum' \
                'felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. Vivamus elementum'

        self.text_label = Text(self.middle_frame, bg='light grey', relief=FLAT, wrap='word')
        self.text_label.insert(1.0, words)
        self.text_label.config(state=DISABLED)
        self.text_label.pack(fill=BOTH)

        self.text_label = Label(self.bottom_frame, text= '@ Copyright 2017 | EMVI')
        self.text_label.pack(side=TOP, anchor=NW, padx= 10, pady=10)


    def jump_to_line(self):
        self.jump_window = Toplevel(self.root)
        self.jump_window.title('Jump to line')
        self.jump_window.geometry('240x70+{}+{}'.format(int(self.width/2-120), int(self.height/2-35)))
        self.jump_window.transient(self.root)
        self.jump_window.resizable(False, False)

        self.label = ttk.Label(self.jump_window, text='Enter line number')
        self.label.place(x=20, y=5)
        self.entry= ttk.Entry(self.jump_window)
        self.entry.place(x=20, y=30.2)
        self.button = ttk.Button(self.jump_window, text='Ok', width=10)
        self.button.place(x=150, y=28)

















