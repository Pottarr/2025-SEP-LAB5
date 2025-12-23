import turtle as t

class Disk(object):
    def __init__(self, name="", xpos=0, ypos=0, height=20, width=40):
        self.dname = name
        self.dxpos = xpos
        self.dheight = height
        self.dwidth = width
        self.t = t.Turtle()
        self.t.color("brown")
        self.newpos(xpos, ypos)

    def showdisk(self):
        self.t.backward(self.dwidth / 2)
        self.t.begin_fill()
        for i in range(2):
            self.t.forward(self.dwidth)
            self.t.left(90)
            self.t.forward(self.dheight)
            self.t.left(90)
        self.t.end_fill()
        self.t.forward(self.dwidth/2)
        
    def newpos(self, xpos, ypos):
        self.t.penup()
        self.t.goto(xpos, ypos)
        self.t.pendown()

    def cleardisk(self):
        self.t.clear()

class Pole(object):
	def __init__(self, name="", xpos = 0, ypos = 0, thick = 10, length = 100):
		self.t = t.turtle()
		self.pname = name
		self.stack = []
		self.toppos = 0
		self.pxpos = xpos
		self.pypos = ypos
		self.pthick = thick
		self.plength = length

	def showpole(self):
		self.t.forward(self.thick/2)
		self.t.left(90)
		self.t.forward(self.length)
		self.t.left(90)
		self.t.forward(self.thick)
		self.t.left(90)
		self.t.forward(self.length)
		self.t.forward(self.thick/2)
		for d in self.stack:
			d.showdish()
	
	
	def pushdisk(self, disk):
		self.toppos += 1
		disk.newpos(self.xpos, (self.ypos + disk.dheight * self.toppos))
		self.stack.append(disk)
  
	def popdisk(self):
		self.toppos -= 1
		self.stack.pop()
    
    
class Hanoi(object):
    def __init__(self, n=3, start="A", workspace="B", destination="C"):
        self.startp = Pole(start, 0, 0)
        self.workspacep = Pole(workspace, 150, 0)
        self.destinationp = Pole(destination, 300, 0)

        self.startp.showpole()
        self.workspacep.showpole()
        self.destinationp.showpole()

        for i in range(n):
            self.startp.pushdisk(
                Disk(
                    "d" + str(i),
                    0,
                    i * 150,
                    20,
                    (n - i) * 30
                )
            )

    def move_disk(self, start, destination):
        disk = start.popdisk()
        destination.pushdisk(disk)

    def move_tower(self, n, s, d, w):
        if n == 1:
            self.move_disk(s, d)
        else:
            self.move_tower(n - 1, s, w, d)
            self.move_disk(s, d)
            self.move_tower(n - 1, w, d, s)

    def solve(self):
        self.move_tower(3, self.startp, self.destinationp, self.workspacep)

  

if __name__ == '__main__':
    h = Hanoi()
    h.solve()
