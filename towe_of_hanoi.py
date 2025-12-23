import turtle as t

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
  


def TowerOfHanoi(n, from_rod, to_rod, aux_rod):
    if n == 0:
        return
    TowerOfHanoi(n-1, from_rod, aux_rod, to_rod)
    print("Move disk", n, "from rod", from_rod, "to rod", to_rod)
    TowerOfHanoi(n-1, aux_rod, to_rod, from_rod)

if __name__ == '__main__':
    h = Hanoi()
    h.solve()
    
