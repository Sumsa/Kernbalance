from pylab import *
import numpy as np
import time
import serial
import msvcrt


filename=str(time.clock())+".npy"
samplerate=1.2
average=25
tit='Mass vs Time'

# configure the serial connections (the parameters differs on the device you are connecting to)
ser = serial.Serial(
	port='COM3', #This should be changed to the correct serial value
	baudrate=1200,
	parity=serial.PARITY_NONE,
	stopbits=serial.STOPBITS_ONE,
	bytesize=serial.EIGHTBITS,
	xonxoff=True,
	timeout=None
)
try :
	ser.close()
except :
    pass
try :
	ser.open()
except :
    pass
ser.isOpen()


def menu():
	print "\n\n---Main menu---"
	print "'q' to quit, 'r' to run,'n' for change filename, 'avg' to change averaging, 'csv' to csv file"
	print "'s' shows the data, 'p' plots the graph, 'ra' change sample rate, 't' change plot title "

#Data gathering routine	


def run(data):
	
	datatemp=zeros((average,2))
	counter=0
	loop=1
	print ">> hold down 'Esc' to stop logging and return to menu\n"
	if len(data)%10==0:
		print ">> Time in seconds  Weight in grams"
	time.sleep(1)
	while loop==1 :
		if msvcrt.kbhit(): #break function 
			if ord(msvcrt.getch()) == 27: #27 is the esc key
				loop=2
				menu()
		out = ''
		#time.sleep(2)
		ser.write(("D05")+chr(13))
		# let's wait one second before reading output (let's give device time to answer)
		time.sleep(samplerate)
		while ser.inWaiting() > 0:
			out += ser.read(1)
		if out != '':
			datatemp[counter%average,0]=float(time.clock()-Timestart)
			datatemp[counter%average,1]=float(out[0:9])
			if counter%average==0 and counter>average:
				data=np.append(data,[[mean(datatemp[:,0]),mean(datatemp[:,1])]],axis=0)
				np.save(filename, data) #saves array
			#data=np.append(data,[[float(time.clock()-Timestart),float(out[0:9])]],axis=0)
			#data=np.append(data,[float(time.clock()-Timestart),float(out[0:9])]),axis=0)
			print ">> " +str(time.clock()-Timestart)+"s " + out
			
			counter+=1



def shower():
	data=np.load(filename)
	print data
def plotter(tit):
	data=np.load(filename)
	plot(data[:,0],data[:,1])
	xlabel('time (s)')
	ylabel('Mass (g)')
	title(tit)
	show()


menu()

input=1
#main userinterface
while 1:
	input = raw_input(">> ")
		# Python 3 users
		# input = input(">> ")
	if input == 'q':
		ser.close()
		exit()
	if input == 'r':
		data=zeros((0,2))
		Timestart= time.clock()
		run(data)
	if input=='n':
		print "write filename"
		filename=raw_input(">> ")+".npy"
		print "filename changed to: "+filename
		menu()
	if input=='p':
		print "plotting the graph"
		plotter(tit)
		menu()
	if input=='s':
		print "showing the data"
		shower()
		menu()
	if input=='ra':
		print "change sample rate 1.2 default"
		samplerate=float(raw_input(">> "))
		menu()
	if input=='avg':
		print "change averaging rage to lessen data burden\n and smooth curves default=25"
		average=int(raw_input(">> "))
		menu()
	if input=='t':
		print "change title of plot"
		title=(raw_input(">> "))
		menu()
	if input=='csv':
		print "write file to comma seperated values"
		savetxt(filename+".txt", np.load(filename))
	
	
