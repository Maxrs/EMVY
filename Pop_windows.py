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
        #self.updat()

        #preference manager
        self.gcode_content.config(width=520, height=564, bg=self.getnew('background1'), relief=FLAT,font=(self.getfont('font'),12,self.getfont('font1')))
        self.shortcut_bar_frame.config(bg=self.getnew('background2'), height=25, width=self.root.winfo_screenwidth(), relief=SUNKEN)
        self.drawing_canvas.config(height=1000, width=1000, bg=self.getnew('background3'))
        self.simulation_canvas.config(height=415, width=830, bg=self.getnew('background3'))

    def preference(self):
        self.preference_window = Toplevel(self.root)
        self.preference_window.title('Preferences')
        self.preference_window.geometry('200x100+400+200')
        self.preference_window.transient(self.root)
        self.preference_window.resizable(False, False)
        self.preference_window.grid_propagate()
#background
        self.text = Label(self.preference_window, text="THEMES")
        self.text.grid(row=0,column=1)
        self.defaul = Button(self.preference_window,text='DEFAULT',bg='dark blue',command=self.defaultback)
        self.defaul.grid(row=2,column=1)
        self.clasic = Button(self.preference_window,text='  CLASIC  ',bg='dark green',command=self.clasicback)
        self.clasic.grid(row=4,column=1)
        self.emvthem = Button(self.preference_window,text='   EMVY   ',bg='indigo',command=self.emvback)
        self.emvthem.grid(row=6,column=1)
#font
        self.text = Label(self.preference_window, text="FONT")
        self.text.grid(row=0,column=8)
        self.defaulfont = Button(self.preference_window,text='DEFAULTFONT',bg='dark blue',command=self.defaultfont3)
        self.defaulfont.grid(row=2,column=8)
        self.clasicfont = Button(self.preference_window,text='  CLASIC FONT ',bg='dark green',command=self.defaultfont1)
        self.clasicfont.grid(row=4,column=8)
        self.emvthemfont = Button(self.preference_window,text='   EMVY FONT  ',bg='indigo',command=self.defaultfont2)
        self.emvthemfont.grid(row=6,column=8)

#Background function
    def defaultback(self):
        self.gcode_content.config(bg='#d4d4d4',fg='black')
        self.shortcut_bar_frame.config(bg='#424242', height=25, width=self.root.winfo_screenwidth(), relief=SUNKEN)
        self.drawing_canvas.config(height=1000, width=1000, bg='#d5d5d5')
        self.simulation_canvas.config(height=415, width=830, bg='#d4d4d4')

        self.config=ConfigParser()
        self.config['DEFAULT']={'background1':'#d4d4d4','fontcolor':'black','background2':'#424242','background3':'#d5d5d5'}
        with open('config.ini','w') as configfile:
            self.config.write(configfile)



    def clasicback(self):
        self.gcode_content.config(bg='light green',fg='white')
        self.shortcut_bar_frame.config(bg='red', height=25, width=self.root.winfo_screenwidth(), relief=SUNKEN)
        self.drawing_canvas.config(height=1000, width=1000, bg='pink')
        self.simulation_canvas.config(height=415, width=830, bg='pink')
        self.config=ConfigParser()
        self.config['DEFAULT']={'background1':'light green','fontcolor':'white','background2':'grey','background3':'pink'}
        self.config['CUSTOM']={'font':'roman'}

        with open('config.ini','w') as configfile:
            self.config.write(configfile)

    def emvback(self):
        self.gcode_content.config(bg='brown',fg='red')
        self.shortcut_bar_frame.config(bg='indigo', height=25, width=self.root.winfo_screenwidth(), relief=SUNKEN)
        self.drawing_canvas.config(height=1000, width=1000, bg='gold')
        self.simulation_canvas.config(height=415, width=830, bg='gold')
        config=ConfigParser()
        config['DEFAULT']={'background1':'brown','fontcolor':'red','background2':'brown','background3':'gold'}
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

















