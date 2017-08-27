'''This class deals with reading dxf files'''
import  dxfgrabber
from operator import itemgetter
import math
from tkinter import filedialog
import tkinter
from dxf_shapes import *

class DXF:
    def __init__(self,editor):
        self.editor=editor
    def  init_components(self):
        file_name = self.editor.functionalities.dxf_file_name
        self.drawing = dxfgrabber.readfile(filename=file_name)
        print("Found entities {}".format(len(self.drawing.entities)))
        self.find_margin()
        self.canvas = self.editor.FrameClass_handler.drawing_canvas

    def get_entities(self,type):
        ents=[]
        for e in self.drawing.entities:
            if e.dxftype==type:
                ents.append(e)

        return  ents
    def find_margin(self):
        lines=self.get_entities("POLYLINE")
        lines2=[]
        ylines=[]
        for x in lines:
            for  y in x.points:
             lines2.append(y[0])
             ylines.append(y[1])
        lines2=sorted(lines2)
        ylines=sorted(ylines)
        self.START_POINT=(lines2[0],ylines[0])
        self.END_POINT=(lines2[-1],ylines[-1])
        self.WIDTH=self.END_POINT[0]-self.START_POINT[0]
        self.HEIGHT=self.END_POINT[1]-self.START_POINT[0]
        print('start point {} : end point {}'.format(self.START_POINT,self.END_POINT))
        print('ylast= {}'.format(ylines[-1]))
    def test_lines(self):
        for entity in self.drawing.entities:
            if entity.dxftype=='POLYLINE':
              x=Polyline(entity,self)
              x.parse_lines()
              x.draw_lines(self.canvas)
            if entity.dxftype=='CIRCLE':
             shape=Circle(entity,self)
             shape.draw_circle(self.canvas)
             pass
        print("START:{} END{}: WIDTH{}: HEIGHT{}".format(self.START_POINT,self.END_POINT,self.WIDTH,self.HEIGHT))
if __name__=="__main__":
    root=tkinter.Tk()
    file=filedialog.askopenfilename()
    canvas=tkinter.Canvas(root,width=400, height=500,background='black')
    canvas.pack()
    dxf= DXF(file,canvas)
    dxf.test_lines()
    root.mainloop()
