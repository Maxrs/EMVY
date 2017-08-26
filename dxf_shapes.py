class Polyline:
    def __init__(self,entity,dxf):
        self.entity=entity
        self.lines=[]
        self.drawing=dxf
        self.parse_lines()
    def maginify(self,point,RATIO):
        mag=int(point * RATIO)
        return mag


    def parse_lines(self):
        for point in range(len(self.entity.points)-1):
             start=(self.entity.points[point][0]-self.drawing.START_POINT[0],self.entity.points[point][1]-self.drawing.START_POINT[1])
             end=(self.entity.points[point+1][0]-self.drawing.START_POINT[0],self.entity.points[point+1][1]-self.drawing.START_POINT[1])
             self.lines.append((start,end))
             print((start,end))
    def draw_lines(self,canvas):
        WIDTH=int(canvas['width'])
        HEIGHT=int(canvas['height'])
        RATIOX=WIDTH/self.drawing.WIDTH
        RATIOY=HEIGHT/self.drawing.HEIGHT
        print("RATIO:{}".format(RATIOX))
        for line in self.lines:
            a,b,c,d=self.maginify(line[0][0],RATIOX),self.maginify(line[0][1],RATIOY),self.maginify(line[1][0],RATIOX),self.maginify(line[1][1],RATIOY)
            print("a{} b{} c{} d{}".format(a,b,c,d))
            line=canvas.create_line(a,b,c,d ,fill='red')







