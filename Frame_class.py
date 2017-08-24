from tkinter import *
from tkinter import ttk

class FrameClass:
    def __init__(self, main):
        self.root =main.window
        self.COMport_handler = main.Com_port
        self.shortcut()
        self.the_panned_windows()
        self.left_pane_components()
        self.right_pane_components()
        self.tab_window()

    def shortcut(self):
        self.shortcut_bar_frame = Frame(self.root)
        self.shortcut_bar_frame.config(bg='#424242', height=25, width=self.root.winfo_screenwidth(), relief=SUNKEN)
        self.shortcut_bar_frame.pack_propagate(False)
        self.shortcut_bar_frame.pack(fill=BOTH)

    def the_panned_windows(self):
        # The main pane components which holds the left pane and right pane
        self.main_pane_window = PanedWindow(self.root)
        self.main_pane_window.config(bg='#424242')
        self.main_pane_window.pack(fill=BOTH, expand=1)

        # Left pane
        self.left_pane_window = PanedWindow(self.main_pane_window, orient=VERTICAL)
        self.left_pane_window.config(bg='#424242', height=695, width=528.5)
        self.left_pane_window.pack_propagate(False)
        self.main_pane_window.add(self.left_pane_window)

        # Right pane
        self.right_pane_window = PanedWindow(self.main_pane_window, orient=VERTICAL)
        self.right_pane_window.config(bg='#424242', height=695, width=830)
        self.right_pane_window.pack_propagate(False)
        self.main_pane_window.add(self.right_pane_window)

    def left_pane_components(self):
        # The COM port Frame
        self.com_port_frame = Frame(self.left_pane_window)
        self.com_port_frame.config(bg='#424242', bd=0.5, height=45, width=528.5, highlightbackground='white',
                                   relief=GROOVE)
        self.com_port_frame.pack_propagate(False)
        self.com_port_frame.pack(fill=X)

        # The Com port Selection(later to be substituted with the return from the COM port function)
        self.port_label = ttk.Label(self.com_port_frame, text='Arduino Port')
        self.port_label.config(foreground='white', background='#424242')
        self.port_label.pack(side=LEFT)

        # The COM port values in the combobox
        self.value_list = self.COMport_handler.serial_ports()
        self.list_of_comports = ttk.Combobox(self.com_port_frame, width=10, values=self.value_list)
        self.list_of_comports.pack(side=LEFT, padx=10)

        # Refresh button
        self.refresh_button = Button(self.com_port_frame)
        self.image = PhotoImage(file='refresh.png')
        self.refresh_button.config(bg='#424242', image=self.image, relief=FLAT, command=self.refresh_ports)
        self.refresh_button.pack(side='left')

        # The Frame which hold the Gcode
        self.gcode_frame = Frame(self.left_pane_window)
        self.gcode_frame.config(height=602, bd=0.5, width=527, bg='#d4d4d4', relief=FLAT)
        self.gcode_frame.pack(fill=BOTH)

        # This will holds the title(G-CODE EDITOR)
        self.title_frame = Frame(self.gcode_frame)
        self.title_frame.config(bg='#05a8f7', bd=0.5, height=30, width=528.5)
        self.title_frame.pack(fill=X)

        # The title
        self.title= ttk.Label(self.title_frame, text='G-Code Editor')
        self.title.config(font=('Helvetica', 12, 'bold'), foreground='white', background='#05a8f7')
        self.title.pack()

        # Line bar  inside the gcode frame
        self.line_bar = Text(self.gcode_frame)
        self.line_bar.config(width=6, height=564, padx=0, background='#6e6e6e', takefocus=0,
                             border=0, state='disabled',
                             wrap='none', foreground='#ffffff')
        self.line_bar.pack(fill="y", side="left")

        # The Gcode Editor inside the gcode frame
        self.gcode_content = Text(self.gcode_frame, wrap='word', undo=True)
        #self.gcode_content.config(width=520, height=564, background='#d4d4d4', relief=FLAT)
        # self.gcode_content.bind('<Control-N>', self.on_content_changed)
        # self.gcode_content.bind('<Control-n>', self.on_content_changed)
        self.gcode_content.pack_propagate(False)
        self.gcode_content.pack(side=LEFT, fill=BOTH)
        self.gcode_content.bind('<Any-KeyPress>', self.on_content_changed)

        # scroll bar
        self.scrollbar = ttk.Scrollbar(self.gcode_content)
        self.gcode_content.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.gcode_content.yview)
        self.scrollbar.pack(side='right', fill='y')

    def right_pane_components(self):
        # The simulation Frame
        self.simulation_frame = Frame(self.right_pane_window)
        self.simulation_frame.config(height=415, width=830, bg='#ffffff')
        self.right_pane_window.add(self.simulation_frame)

        # The notifications Frame
        self.notification_frame = Frame(self.right_pane_window)
        self.notification_frame.config(height=252, width=830, bg='#ffffff')
        self.right_pane_window.add(self.notification_frame)

        # scroll bar

    def tab_window(self):
        style = ttk.Style()
        # Notebook Styling[remove the dashed lines]
        style.layout("Tab",
                     [('Notebook.tab', {'sticky': 'nswe', 'children':
                         [('Notebook.padding', {'side': 'top', 'sticky': 'nswe', 'children':
                             [('Notebook.label', {'side': 'top', 'sticky': ''})],
                                                })],
                                        })]
                     )
        notebook = ttk.Notebook(self.simulation_frame, height=415, width=830)
        self.simulation_frame = Frame()
        self.simulation_frame.config(height=415, width=830, bg='#d4d4d4')
        self.drawing_frame = Frame()
        self.drawing_frame.config(height=415, width=830)
        self.canvas()
        self.drawing = PhotoImage(file='icons/dxf.png')
        self.simulation = PhotoImage(file='icons/cnc_machine.png')
        notebook.add(self.drawing_frame, text="Drawing")
        notebook.add(self.simulation_frame, text="Simulation")
        notebook.tab(self.drawing_frame, compound='left',image=self.drawing)
        notebook.tab(self.simulation_frame, compound='left',image=self.simulation)
        notebook.pack(fill=BOTH, expand=True)

    def canvas(self):
        self.drawing_canvas = Canvas(self.drawing_frame)

        self.drawing_canvas.pack(fill=BOTH, expand=1)
        self.simulation_canvas = Canvas(self.simulation_frame)
        #self.simulation_canvas.config(height=415, width=830, bg='#d5d5d5')
        self.simulation_canvas.pack(fill=BOTH, expand=1)

        self.horizontal_bar= ttk.Scrollbar(self.drawing_canvas, orient=HORIZONTAL)
        self.horizontal_bar.pack(side=BOTTOM, fill=X)
        self.horizontal_bar.config(command=self.drawing_canvas.xview)
        self.drawing_canvas.configure(xscrollcommand=self.horizontal_bar.set)
        self.vertical_bar= ttk.Scrollbar(self.drawing_canvas, orient=VERTICAL)
        self.vertical_bar.pack(side=RIGHT, fill=Y)
        self.vertical_bar.config(command=self.drawing_canvas.yview)
        self.drawing_canvas.configure(yscrollcommand=self.vertical_bar.set)

    def refresh_ports(self):
        self.new_value_list = self.COMport_handler.serial_ports()
        self.list_of_comports.config(values=self.new_value_list)

    def get_line_numbers(self):
        output = ''
        row = self.gcode_content.index("end".split('.'))
        for i in range(1, int(float(row))):
            output += str(i) + '\n'
        return output

    def update_line_numbers(self):
        line_numbers = self.get_line_numbers()
        self.line_bar.config(state='normal')
        self.line_bar.delete('1.0', 'end')
        self.line_bar.insert('1.0', line_numbers)
        self.line_bar.config(state='disabled')

    def on_content_changed(self, event=None):
        self.update_line_numbers()