from tkinter import *
from tkinter import ttk
from configparser import ConfigParser
# pop

class windows:

    def __init__(self, main_program):
        self.root= main_program.window

        self.height = self.root.winfo_screenheight()
        self.width = self.root.winfo_screenwidth()
        self.frameclasshandler = main_program.FrameClass_handler
        self.gcode_content = main_program.FrameClass_handler.gcode_content
        self.shortcut_bar_frame=main_program.FrameClass_handler.shortcut_bar_frame
        self.drawing_canvas=main_program.FrameClass_handler.drawing_canvas
        self.simulation_canvas=main_program.FrameClass_handler.simulation_canvas
        self.main_pane_window=main_program.FrameClass_handler.main_pane_window
        self.left_pane_window=main_program.FrameClass_handler.left_pane_window
        self.com_port_frame=main_program.FrameClass_handler.com_port_frame
        self.title_frame=main_program.FrameClass_handler.title_frame
        self.title=main_program.FrameClass_handler.title
        self.line_bar=main_program.FrameClass_handler.line_bar
        self.port_label=main_program.FrameClass_handler.port_label
        self.refresh_button=main_program.FrameClass_handler.refresh_button
        self.open_btn=main_program.utils_handler.open_btn
        self.saveas_btn=main_program.utils_handler.saveas_btn
        self.save_btn=main_program.utils_handler.save_btn
        self.copy_btn=main_program.utils_handler.copy_btn
        self.paste_btn=main_program.utils_handler.paste_btn
        self.cut_btn=main_program.utils_handler.cut_btn
        self.undo_btn=main_program.utils_handler.undo_btn
        self.redo_btn=main_program.utils_handler.redo_btn


        #self.updat()

        #preference manager
        self.gcode_content.config(width=520, height=564, bg=self.getnew('background1'), relief=FLAT,font=(self.getfont('font'),12,self.getfont('font1')))
        self.shortcut_bar_frame.config(bg=self.getnew('background2'), height=25, width=self.root.winfo_screenwidth(), relief=SUNKEN)
        self.drawing_canvas.config(height=1000, width=1000, bg=self.getnew('background3'))
        self.simulation_canvas.config(height=415, width=830, bg=self.getnew('background3'))
        self.main_pane_window.config(bg=self.getnew('background4'))
        self.left_pane_window.config(bg=self.getnew('background5'))
        self.com_port_frame.config(bg=self.getnew('background6'))
        self.title_frame.config(bg=self.getnew('background7'))
        self.title.config(background=self.getnew('background8'))
        self.line_bar.config(background=self.getnew('background9'))
        self.port_label.config(foreground='white', background=self.getnew('background10'))
        self.refresh_button.config(bg=self.getnew('background10'))
        self.open_btn.config(bg=self.getnew('background2'))
        self.saveas_btn.config(bg=self.getnew('background2'))
        self.save_btn.config(bg=self.getnew('background2'))
        self.copy_btn.config(bg=self.getnew('background2'))
        self.paste_btn.config(bg=self.getnew('background2'))
        self.cut_btn.config(bg=self.getnew('background2'))
        self.undo_btn.config(bg=self.getnew('background2'))
        self.redo_btn.config(bg=self.getnew('background2'))

    def preference(self):
        self.preference_window = Toplevel(self.root,bg='dark blue')
        self.preference_window.title('Preferences')
        self.preference_window.geometry('200x120+400+200')
        self.preference_window.transient(self.root)
        self.preference_window.resizable(False, False)
        self.preference_window.grid_propagate()
#background label
        self.text = Label(self.preference_window, text="THEMES",bg='dark blue', font=('sans serif',12,'bold'))
        self.text.grid(row=0,column=1)
    #combobox
        self.box_value = StringVar()
        self.box = ttk.Combobox(self.preference_window, textvariable=self.box_value)
        self.box.bind("<<ComboboxSelected>>", self.newselection)
        self.box['values'] = ('DEFAULT', 'CLASIC', 'EMVI ')
        self.box.current(0)
        self.box.grid(column=1, row=1,pady=0)
        self.box.config(width=8)
        self.Apply= Button(self.preference_window,text='SAVE',bg='indigo',command=lambda :[self.ok(),self.okfont()],padx=10)
        self.Apply.grid(row=6,column=1,padx=10,pady=30)


        #fontcombo
        self.box_value1 = StringVar()
        self.box1 = ttk.Combobox(self.preference_window, textvariable=self.box_value1)
        self.box1.bind("<<ComboboxSelected>>", self.newselectionf)
        self.box1['values'] = ('DEFAULT', 'CLASIC', 'EMVI')
        self.box1.current(0)
        self.box1.grid(column=8, row=1,pady=0)
        self.box1.config(width=8)


    #font
        self.text = Label(self.preference_window,bg='dark blue', text="FONT",font=('sans serif',12,'bold'))
        self.text.grid(row=0,column=8)


 #COMBOBOX FUNCTION
    def newselection(self, event):
        self.value_of_combo = self.box.get()


    def ok(self):

        if self.box.get()=='DEFAULT':
            self.defaultback()
        elif self.box.get()=='CLASIC':
            self.clasicback()
        else:
            self.emvback()
    #fontcomb0
    def newselectionf(self, event):
        self.value_of_combo1 = self.box1.get()


    def okfont(self):

        if self.box1.get()=='DEFAULT':
            self.defaultfont3()
        elif self.box1.get()=='CLASIC':
            self.defaultfont1()
        else:
            self.defaultfont2()








            #Background function
    def defaultback(self):
        self.gcode_content.config(bg='#d4d4d4',fg='black')
        self.shortcut_bar_frame.config(bg='#424242', height=25, width=self.root.winfo_screenwidth(), relief=SUNKEN)
        self.drawing_canvas.config(height=1000, width=1000, bg='#d5d5d5')
        self.simulation_canvas.config(height=415, width=830, bg='#d4d4d4')
        self.main_pane_window.config(bg='#424242')
        self.com_port_frame.config(bg='#424242')
        self.left_pane_window.config(bg='#424242')
        self.title_frame.config(bg='#05a8f7')
        self.title.config(background='#05a8f7')
        self.line_bar.config(background='#6e6e6e')
        self.port_label.config(foreground='white', background='#424242')
        self.refresh_button.config(bg='#424242')
        self.open_btn.config(bg='#424242')
        self.open_btn.config(bg='#424242')
        self.saveas_btn.config(bg='#424242')
        self.save_btn.config(bg='#424242')
        self.copy_btn.config(bg='#424242')
        self.paste_btn.config(bg='#424242')
        self.cut_btn.config(bg='#424242')
        self.undo_btn.config(bg='#424242')
        self.redo_btn.config(bg='#424242')


        self.config=ConfigParser()
        self.config['DEFAULT']={'background1':'#d4d4d4','background10':'#424242','fontcolor':'black','background9':'#6e6e6e','background2':'#424242','background8':'#05a8f7','background7':'#05a8f7','background3':'#d5d5d5','background5':'#424242','background4':'#424242','background6':'#424242'}
        with open('config.ini','w') as configfile:
            self.config.write(configfile)



    def clasicback(self):
        self.gcode_content.config(bg='navajowhite4',fg='white')
        self.shortcut_bar_frame.config(bg='lightyellow3', height=25, width=self.root.winfo_screenwidth(), relief=SUNKEN)
        self.drawing_canvas.config(height=1000, width=1000, bg='lightyellow3')
        self.main_pane_window.config(bg='lightyellow3')
        self.simulation_canvas.config(height=415, width=830, bg='navajowhite4')
        self.left_pane_window.config(bg='lightyellow3')
        self.com_port_frame.config(bg='lightyellow3')
        self.title_frame.config(bg='lightyellow3')
        self.title.config(background='lightyellow3')
        self.line_bar.config( background='lightyellow3')
        self.port_label.config(foreground='white', background='lightyellow3')
        self.refresh_button.config(bg='lightyellow3')
        self.open_btn.config(bg='lightyellow3')
        self.open_btn.config(bg='lightyellow3')
        self.open_btn.config(bg='lightyellow3')
        self.saveas_btn.config(bg='lightyellow3')
        self.save_btn.config(bg='lightyellow3')
        self.copy_btn.config(bg='lightyellow3')
        self.paste_btn.config(bg='lightyellow3')
        self.cut_btn.config(bg='lightyellow3')
        self.undo_btn.config(bg='lightyellow3')
        self.redo_btn.config(bg='lightyellow3')
        self.config=ConfigParser()
        self.config['DEFAULT']={'background1':'navajowhite4','background10':'lightyellow3','fontcolor':'white','background9':'lightyellow3','background7':'lightyellow3','background4':'lightyellow3','background8':'lightyellow3','background6':'lightyellow3','background2':'lightyellow3','background5':'lightyellow3','background3':'lightyellow3'}
        self.config['CUSTOM']={'font':'roman'}

        with open('config.ini','w') as configfile:
            self.config.write(configfile)

    def emvback(self):
        self.gcode_content.config(bg='brown',fg='red')
        self.shortcut_bar_frame.config(bg='indigo', height=25, width=self.root.winfo_screenwidth(), relief=SUNKEN)
        self.drawing_canvas.config(height=1000, width=1000, bg='gold')
        self.simulation_canvas.config(height=415, width=830, bg='gold')
        self.main_pane_window.config(bg='lightyellow')
        self.left_pane_window.config(bg='lightyellow3')
        self.com_port_frame.config(bg='lightyellow3')
        self.title_frame.config(bg='lightyellow')
        self.title.config(background='#05a8f7')
        self.line_bar.config( background='lightyellow3')
        self.port_label.config(foreground='white', background='#424242')
        self.refresh_button.config(bg='#424242')
        self.open_btn.config(bg='indigo')
        self.open_btn.config(bg='indigo')
        self.open_btn.config(bg='indigo')
        self.saveas_btn.config(bg='indigo')
        self.save_btn.config(bg='indigo')
        self.copy_btn.config(bg='indigo')
        self.paste_btn.config(bg='indigo')
        self.cut_btn.config(bg='indigo')
        self.undo_btn.config(bg='indigo')
        self.redo_btn.config(bg='indigo')



        config=ConfigParser()
        config['DEFAULT']={'background1':'brown','fontcolor':'red','background10':'#424242','background2':'indigo','backround9':'lightyellow','background8':'#05a8f7','background7':'lightyellow','background9':'lightyellow','background3':'gold','background6':'lightyellow','background4':'lightyellow','background5':'lightyellow3'}
        config['CUSTOM']={'font':'arial'}

        with open('config.ini','w') as configfile:
            config.write(configfile)

    def updat(self):
        config=ConfigParser()
        config['DEFAULT']={'background1':'light green','fontcolor':'red','background2':'brown','background3':'gold'}
        config['CUSTOM']={'font':'arial'}
        with open('configfont.ini','w') as configfile:
            config.write(configfile)




    def getnew(self,parm):
        config=ConfigParser()
        config.read('config.ini')
        return config['DEFAULT'][parm]
#font

    def defaultfont3(self):
        self.gcode_content.config(font=('COMIC SANS',14,'normal'))
        self.config=ConfigParser()
        self.config['CUSTOM']={'font':'COMIC SANS','font1':'normal'}
        with open('configfont.ini','w') as configfile:
            self.config.write(configfile)
    def defaultfont1(self):
        self.gcode_content.config(font=('arial',14,'normal'))
        self.config=ConfigParser()
        self.config['CUSTOM']={'font':'arial','font1':'normal'}
        with open('configfont.ini','w') as configfile:
            self.config.write(configfile)

    def defaultfont2(self):
        self.gcode_content.config(font=('SERIF',14,'italic'))
        self.config=ConfigParser()
        self.config['CUSTOM']={'font':'SERIF','font1':'italic'}
        with open('configfont.ini','w') as configfile:
            self.config.write(configfile)



    def getfont(self,parm):
        config=ConfigParser()
        config.read('configfont.ini')
        return config['CUSTOM'][parm]





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

















