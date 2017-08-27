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

    def draw_lines(self,canvas):
        WIDTH=int(canvas['width'])
        HEIGHT=int(canvas['height'])
        RATIOX=WIDTH/self.drawing.WIDTH
        RATIOY=HEIGHT/self.drawing.HEIGHT
        #print("RATIO:{}".format(RATIOX))
        for line in self.lines:
            a,b,c,d=self.maginify(line[0][0],RATIOX),self.maginify(line[0][1],RATIOY),self.maginify(line[1][0],RATIOX),self.maginify(line[1][1],RATIOY)
            #print("a{} b{} c{} d{}".format(a,b,c,d))
            line=canvas.create_line(a,b,c,d ,fill='blue')
class Circle:
    def __init__(self, entity, dxf):
        self.entity = entity
        self.drawing = dxf
        self.parse_points()
        self.get_bound_box()
    def maginify(self,point,RATIO):
        mag=int(point * RATIO)
        return mag
    def parse_points(self):
        self.center=self.entity.center
        print("center : {} radius{}".format(self.center,self.entity.radius))
        self.radius=self.entity.radius
        self.center = (self.center[0] - self.drawing.START_POINT[0],
                 self.center[1]- self.drawing.START_POINT[1])


    def get_bound_box(self):
        self.top_left=((self.center[0]-self.radius),(self.center[1]-self.radius))
        print("top left{}".format(self.top_left))
        self.bottom_right=((self.center[0]+self.radius),(self.center[1]+self.radius))
        print("top_right {}".format(self.bottom_right))
    def draw_circle(self,canvas):
        WIDTH=int(canvas['width'])
        HEIGHT=int(canvas['height'])
        RATIOX=WIDTH/self.drawing.WIDTH
        print('WIDTH {}'.format(WIDTH))
        print('HEIGHT:{}'.format(HEIGHT))
        RATIOY=HEIGHT/self.drawing.HEIGHT
        a,b,c,d=self.maginify(self.top_left[0],RATIOX),self.maginify(self.top_left[1],RATIOY),self.maginify(self.bottom_right[0],RATIOX),self.maginify(self.bottom_right[1],RATIOY)
        circle=canvas.create_oval(a,b,c,d)
        print("{},{},{},{}".format(a,b,c,d))
        print("{} ratiox  ratioy {}".format(RATIOX,RATIOY))











