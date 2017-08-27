from tkinter import filedialog, END, Toplevel, IntVar,messagebox
import serial
import os
from tkinter import ttk
GCODES=[]
CURRENT_LINE=[]
import serial
from  tkinter import  *
import  threading
def send_gcode(ser,context_text):
    '''Method for sending Gcode to the Arduino'''
    ser.write('C-90'.encode('utf-8'))
    print("initializing codes")
    sent_commands=0
    while sent_commands<len(GCODES):
        x=" "
        try:

            reply=ser.readline()
            reply=reply.decode()
            print(len(reply))
            print("reply for serial {}".format(reply))
            for code in GCODES:
                if code[0] in reply:
                    global GCODE_LINE
                    GCODE_LINE=int(code[0][1:])

                    ser.write(code[1].encode('utf-8'))
                    sent_commands+=1
                    print("code sent is {}".format(code))
        except Exception:


             print("problem with  serialport")
             break;



class Edit:
    def __init__(self, main_program):
        self.root = main_program.window
        self.main_program=main_program
        self.app_name = main_program.app_name
        self.gcode_content = main_program.FrameClass_handler.gcode_content
        self.file_name = None
        self.gcode_content.bind('<Control-f>', self.find_text)
        self.gcode_content.bind('<Control-F>', self.find_text)
        self.gcode_content.bind('<Control-x>', self.cut)
        self.gcode_content.bind('<Control-X>', self.cut)
        self.gcode_content.bind('<Control-c>', self.copy)
        self.gcode_content.bind('<Control-C>', self.copy)
        self.gcode_content.bind('<Control-z>', self.undo)
        self.gcode_content.bind('<Control-Z>', self.undo)
        self.gcode_content.bind('<Control-y>', self.redo)
        self.gcode_content.bind('<Control-Y>', self.redo)
        self.root.bind('<Control-n>', self.new_file)
        self.root.bind('<Control-N>', self.new_file)
        self.root.bind('<Control-s>', self.save)
        self.root.bind('<Control-S>', self.save)
        self.root.bind('<Control-Alt-s>', self.save_as)
        self.root.bind('<Control-Alt-S>', self.save_as)
        self.root.bind('<Control-O>', self.open_file)
        self.root.bind('<Control-o>', self.open_file)
        self.root.bind('<Control-i>', self.import_dxf)
        self.root.bind('<Control-I>', self.import_dxf)

    def cut(self, event=None):
        self.gcode_content.event_generate("<<Cut>>")

    def copy(self, event=None):
        self.gcode_content.event_generate("<<Copy>>")

    def paste(self, event=None):
        self.gcode_content.event_generate("<<Paste>>")

    def undo(self, event=None):
        self.gcode_content.event_generate("<<Undo>>")

    def redo(self, event=None):
        self.gcode_content.event_generate("<<Redo>>")

    def select_all(self, event=None):
        self.gcode_content.tag_add('sel', '1.0', 'end')

    def open_file(self, event=None):
        self.input_file_name =filedialog.askopenfilename(defaultextension=".NC", filetypes=[("Gcode", ".NC")])

        if self.input_file_name:
            self.file_name = self.input_file_name
            self.root.title('{}-{}'.format(os.path.basename(self.app_name), self.file_name))
            self.gcode_content.delete(1.0, END)
            with open(self.file_name) as _file:
                self.gcode_content.insert(1.0, _file.read())


    def save_as(self, event= None):
        self.input_file_name = filedialog.asksaveasfilename(defaultextension=".NC", filetypes=[('gcode', ".NC",
                                                                                                )])


        if self.input_file_name:
            self.file_name = self.input_file_name
            self.write_to_file(self.file_name)
            self.root.title('{} - {}'.format(os.path.basename(self.app_name), self.file_name))

    def save(self, event= None):
        if not self.file_name:
            self.save_as()
        else:
            self.write_to_file(self.file_name)

    def write_to_file(self, file_name):
        self.file_name=file_name
        try:
            self.content = self.gcode_content.get(1.0, END)
            with open(self.file_name, 'w') as the_file:
                print(self.content)
                the_file.write(self.content)

        except IOError:
            pass

    def new_file(self, event= None):
        new_name = 'Untitled'
        self.root.title('{} - {}'.format(os.path.basename(self.app_name), new_name))
        self.file_name = None
        self.gcode_content.delete(1.0, END)

    def  import_dxf(self, event= None):
        self.dxf_file_name=file_name = filedialog.askopenfilename(defaultextension=".dxf", filetypes=[("dxf file", ".dxf")])
        self.main_program.FrameClass_handler.drawing_canvas.delete('all')
        self.main_program.dxf_master.init_components()
        self.main_program.dxf_master.test_lines()

    def find_text(self,event=None):
        self.search_toplevel = Toplevel(self.root)
        self.search_toplevel.title('Find Text')
        self.search_toplevel.geometry("+500+300")
        self.search_toplevel.transient(self.root)
        self.search_toplevel.resizable(False, False)
        ttk.Label(self.search_toplevel, text="Find All:").grid(row=0, column=0, sticky='e')
        self.search_entry_widget = ttk.Entry(self.search_toplevel, width=25)
        self.search_entry_widget.grid(row=0, column=1, padx=2, pady=2, sticky='we')
        self.search_entry_widget.focus_set()
        ignore_case_value = IntVar()
        ttk.Checkbutton(self.search_toplevel, text='IgnoreCase',variable=ignore_case_value).grid(row = 1, column = 1, sticky = 'e', padx = 2, pady = 2)
        self.button_find = ttk.Button(self.search_toplevel, text="Find All", underline=0,command=lambda: self.search_output(self.search_entry_widget.get(), ignore_case_value.get(), self.gcode_content, self.search_toplevel, self.search_entry_widget))
        self.button_find.grid(row=0, column=2, sticky='e' + 'w', padx=2, pady=2)

    def search_output(self, needle, if_ignore_case, gcode_content, search_toplevel, search_box):
        self.gcode_content.tag_remove('match', '1.0', END)
        matches_found = 0
        if needle:
            start_pos = '1.0'
            while True:
                start_pos = gcode_content.search(needle, start_pos, nocase=if_ignore_case, stopindex=END)
                if not start_pos:
                    break
                end_pos = '{}+{}c'.format(start_pos, len(needle))
                gcode_content.tag_add('match', start_pos, end_pos)
                matches_found += 1
                start_pos = end_pos
            gcode_content.tag_config('match', foreground='red', background='yellow')
        search_box.focus_set()
        search_toplevel.title('{} matches found'.format(matches_found))
    def connect_serial(self,port):
         try:
          self.main_program.serial_port=serial.Serial(port,9600)
         except Exception:
             messagebox.showwarning(title='COMPORT',message="comport failed to connect")
    def upload_code(self):
        text2 =self.main_program.FrameClass_handler.gcode_content.get("1.0", END)
        global GCODES
        commands = text2.split('\n')
        for command in range(len(commands) - 1):
            if command == "" or command == " ":
                commands.remove(command)

        print(commands)
        GCODES = []
        size = len(commands)
        for x in range(size):
            GCODES.append(("C{0:04}".format(x), commands[x]))
        print(GCODES)
        if self.main_program.serial_port.is_open:
            send_thread = threading.Thread(target=send_gcode, args=[self.main_program.serial_port, self.main_program.FrameClass_handler.gcode_content],
                            daemon=True)
            send_thread.start()
        else :
            messagebox.showwarning(title='upload_failure',message='sorry the com port was not available prease check if the usb is connected or another programm is using it')


