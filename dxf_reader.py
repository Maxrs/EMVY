'''This class deals with reading dxf files'''
import  dxfgrabber
from operator import itemgetter
import math
import tkinter
from dxf_shapes import *

class DXF:
    def __init__(self,file_name,canvas):
        self.drawing=dxfgrabber.readfile(filename=file_name)
        print("Found entities {}".format(len(self.drawing.entities)))
        self.find_margin()
        self.canvas=canvas

    def get_entities(self,type):
        ents=[]
        for e in self.drawing.entities:
            if e.dxftype==type:
                ents.append(e)

        return  ents
    def find_margin(self):
        lines=self.get_entities("POLYLINE")
        lines2=[]
        for x in lines:
            for  y in x.points:
             lines2.append(y)
        lines2=sorted(lines2)
        self.START_POINT=lines2[0]
        self.END_POINT=lines2[-1]
        self.WIDTH=self.END_POINT[0]-self.START_POINT[0]
        self.HEIGHT=self.END_POINT[1]-self.START_POINT[0]
    def test_lines(self):
        lines=self.get_entities("POLYLINE")
        for line in lines:
              x=Polyline(line,self)
              x.parse_lines()
              x.draw_lines(self.canvas)
        print("START:{} END{}: WIDTH{}: HEIGHT{}".format(self.START_POINT,self.END_POINT,self.WIDTH,self.HEIGHT))
if __name__=="__main__":
    root=tkinter.Tk()
    canvas=tkinter.Canvas(root,width=400, height=500,background='black')
    canvas.pack()
    dxf= DXF("drill_dxfFILE.dxf",canvas)
    dxf.test_lines()
    root.mainloop()
