import sys
import math
import ephem
import serial
import Queue
import Command
import time

choice = []

def readingTLE(file):

    TLEfile = open(file,'r')
    # for ever TLE
    for line in TLEfile:
    	line1 = line
    	line2 = TLEfile.next().strip()
    	line3 = TLEfile.next().strip()


    	iss = ephem.readtle(line1, line2, line3)
    	obs = ephem.Observer()
    	obs.lat = '42.02690'
    	obs.long = '-93.65278'

    	for p in range(3):

            try:
                tr, azr, tt, altt, ts, azs = obs.next_pass(iss)
            except ValueError:
                print "llllll"
            finally:
                print "Can not see it"
                sys.exit(1)


            times = Command.PassTimes(tr, ts)
            commands = Queue.Queue(0)


            while tr < ts:
				obs.date = tr
				iss.compute(obs)
				c = Command.Command(math.degrees(iss.az), math.degrees(iss.alt))
				commands.put_nowait(c)
				#print commands.get_nowait()
				tr = ephem.Date(tr + 1.0 * ephem.second)
            choices = Command.Choice(commands, times, altt)
            choice.append(choices)
            obs.date = tr + ephem.minute
	#moveRotor()
	print "--------------"


def options(self):
    return self.choice;


def moveRotor():
    #controllerSerial = serial.Serial(COM3,9600,serial.EIGHTBITS,serial.PARITY_NONE,serial.STOPBITS_ONE)
    c = choice[0]
    b = Queue.Queue(0)
    b = c.getCommands()
    while not b.empty():
        #print q.__name__
        #controllerSerial.write(a)
        print b.get_nowait().__repr__()
        time.sleep(1)


readingTLE('weather.txt')
