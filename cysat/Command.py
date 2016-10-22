import Queue
class Command:

    def __init__(self, az, el):
        self.az = az
        self.el = el
    def __repr__(self):
        return "w " + "%.03d" % self.az + " " +"%.03d" % self.el

class Choice:
	def __init__(self, q, pt, maxEl):
		self.q = q
		self.pt = pt
		self.maxEl = maxEl
	def __repr__(self):
		return str(self.pt) + " ,and a maximum elevation of " + str(self.maxEl)

	def getTimes(self):
		return self.pt

	def getCommands(self):
		return self.q

	def getMaxElevation(self):
		return self.maxEl

class PassTimes:
	def __init__(self, tr, ts):
		self.tr = tr
		self.ts = ts
	def __repr__(self):
		return "The total pass time is " + str(self.ts-self.tr) + " ,with a rise time of " + str(self.tr) + " ,a set time of " + str(self.ts)

	def getRise(self):
		return self.tr

	def getSet(self):
		return self.ts
