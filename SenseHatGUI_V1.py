# --------------------------------------------------------------------------------------------- #
# ------------------- GUI INTERFACE FOR RASPBERRY PI : SENSE HAT MODULE ----------------------- #
# --------------------------------------------------------------------------------------------- #

# author       : Abhishek Sharma, BioMIP, Ruhr University, Bochum, Germany.
# email        : abhishek.sharma@rub.de
# started      : 11.11.2016
# last updated : 12.11.2016
# Comments     : Thanks to Ankit Izardar for lending me his Sense Hat, and I hope I'll never give
#                him back.

"""
  --- Description ---
  
	-> Creates a GUI interface for Sense Hat module of Raspberry Pi. 
	   Sense Hat consists of following sensors:

	     1. Temperature
	     2. Humidity
	     3. Pressure
	     4. Gyroscope
	     5. Accelerometer
	     6. Magnetometer
	     
	   and LEDMatrix with 8x8 RGB LED's.  
	
	-> Please look for python module: sense_hat API for further detials.   
  
"""

import sys
from time import sleep
import random
import Tkinter as Tk
import tkFont
import numpy as np

try:
	from sense_hat import SenseHat
	
except ImportError:
	raise ImportError('SenseHat NOT FOUND')

sense = SenseHat()
sense.clear()

def horns_LEDMatrix(X, O):
	
	""" Creates Bulls Head on LED Matrix  
       
              +              + 	
	        +           +
	        + + + + + + +
	          + + + + + 
	            + + + 
                    + + + 	
	              + 		
	
	"""
	
	LEDPixels = [O, O, X, O, O, O, X, O,
	             O, X, O, O, O, O, O, X,
	             O, X, X, X, X, X, X, X,
	             O, O, X, X, X, X, X, O,
	             O, O, O, X, X, X, O, O,
	             O, O, O, X, X, X, O, O, 
	             O, O, O, O, X, O, O, O,
	             O, O, O, O, O, O, O, O]
	sense.set_pixels(LEDPixels)
	sleep(0.5)
	sense.clear()
        

def run_LEDMatrix():        
	for i in range(10):
		
		X = (255, 0, 0)
 	        O = (0, 255, 0)
        	                
        	horns_LEDMatrix(X, O)
        	        	
       	        X = (255, 0, 255)
                O = (255, 255, 0) 
        	
                horns_LEDMatrix(X, O)
        	
                X = (255, 255, 255)
                O = (0, 0, 0)
                             
                horns_LEDMatrix(X, O)

	sense.show_message("In Metal, We Trust !!!", text_colour=[255, 0, 0], back_colour=[0, 0, 255])        
	sense.clear()

class RPiSenseHat(Tk.Frame):
	
	def __init__(self, master):
		Tk.Frame.__init__(self, master)
		self.master = master

		# Setting colors for Sense Hat : RGB LEDs Matrix
		# [R, G, B, R+G, G+B, R+B, R+G+B] : Basic Colors 
		self.dark = (0, 0, 0)
		self.r = (255, 0, 0)
		self.g = (0, 255, 0)
		self.b = (0, 0, 255)
		self.rg = (255, 255, 0)
		self.gb = (0, 255, 255)
		self.rb = (255, 0, 255)
		self.rgb = (255, 255, 255)
		self.color = (0, 0, 0)
        		
		# Background : Dark : 0 / White : 1
		self.background = 0
		self.startGUI()
		self.running = False
		
	def startGUI(self):
		self.master.title("RPi SenseHat")
		self.master.grid_rowconfigure(1, weight=1)
		self.master.grid_columnconfigure(1, weight=1)
		
		self.frame = Tk.Frame(self.master)
		self.frame.pack(fill=Tk.X, padx=5, pady=5)
		
		# Setting font size and type
		helv12 = tkFont.Font(family='Helvetica', size=12, weight='bold') 
		
		# Button : Temperature Sensor
		self.button1 = Tk.Button(self.frame, bg = 'white', text="Temperature", height = 2, width = 20,
			command = lambda: self.senseTemperature(), font=helv12)
		self.button1.pack()
		
		# Button : Humidity Sensor
		self.button2 = Tk.Button(self.frame, bg = 'white', text="Humidity", height = 2, width = 20, 
			command = lambda: self.senseHumidity(), font=helv12)
		self.button2.pack()
		
		# Button : Pressure Sensor
		self.button3 = Tk.Button(self.frame, bg = 'white', text="Pressure", height = 2, width = 20,
			command = lambda: self.sensePressure(), font=helv12)
		self.button3.pack()
		
		# Button : Gyroscope
		self.button4 = Tk.Button(self.frame, bg = 'white', text="Gyroscope", height = 2, width = 20,
			command = lambda: self.senseGyro(), font=helv12)
		self.button4.pack()
		
		# Button : Accelerometer
		self.button5 = Tk.Button(self.frame, bg = 'white', text="Accelerometer", height = 2, width = 20,
			command = lambda: self.senseAcc(), font=helv12)
		self.button5.pack()
		
		# Button : Magnetometer
		self.button6 = Tk.Button(self.frame, bg = 'white', text="Magnetometer", height = 2, width = 20,
			command = lambda: self.senseMagF(), font=helv12)
		self.button6.pack()		
		
		# Button : LED Matrix
		self.button7 = Tk.Button(self.frame, bg = 'white', text="LEDMatrix", height = 2, width = 20,
			command = lambda: self.LEDMatrix(), font=helv12)
		self.button7.pack()	
		
	def senseTemperature(self):
		""" Senses Current Temperature """
		print "Sensing Temperature"
		temp = sense.get_temperature()
		self.button1["bg"] = 'orange'
		self.button1["text"] = 'Temperature \n' + str("%.3f" %temp) + ' deg. C'
				
	def senseHumidity(self):
		""" Senses Current Humidity """
		print "Sensing Humidity"
		humid = sense.get_humidity()
		self.button2["bg"] = 'orange'
		self.button2["text"] = 'Humidity \n' + str("%.3f" %humid) + ' %'
		
	def sensePressure(self):
		""" Senses Current Pressure """
		print "Sensing Pressure"
		press = sense.get_pressure()
		self.button3["bg"] = 'orange'
		self.button3["text"] = 'Pressure \n' + str("%.3f" %press) + ' mBar'
	
	def senseGyro(self):
		""" Senses dynamic orientation """
		print "Starting Gyroscope"
		
		helv12 = tkFont.Font(family='Helvetica', size=12, weight='bold') 
		self.Gyro = Tk.Toplevel(self.master)
		self.Gyro.title("Gyroscope")
		self.Gyro.grid_rowconfigure(1, weight=1)
		self.Gyro.grid_columnconfigure(1, weight=1)
		self.frame = Tk.Frame(self.Gyro)
		self.frame.pack(fill=Tk.X, padx=5, pady=5)

		self.l1 = Tk.Label(self.frame, text= "Pitch: ", font=helv12, height = 1, width = 10)
		self.l1.grid(row=1,column=0)
		
		self.l2 = Tk.Label(self.frame, text= "Roll: ", font=helv12, height = 1, width = 10)
		self.l2.grid(row=1,column=1)
		
		self.l3 = Tk.Label(self.frame, text= "Yaw: ", font=helv12, height = 1, width = 10)
		self.l3.grid(row=1,column=2)
		
		self.l4 = Tk.Label(self.frame, text="0", font=helv12, height = 1, width = 10)
		self.l4.grid(row=2,column=0)
		
		self.l5 = Tk.Label(self.frame, text="0", font=helv12, height = 1, width = 10)
		self.l5.grid(row=2,column=1)
		
		self.l6 = Tk.Label(self.frame, text="0", font=helv12, height = 1, width = 10)
		self.l6.grid(row=2,column=2)

		
		# Start button
		self.buttonStart = Tk.Button(self.frame, bg = 'white', text="Start", height = 1, width = 15,
			command = lambda: self.mGyro(1), font=helv12).grid(row=0,column=0)
		
		# Stop button
		self.buttonStop = Tk.Button(self.frame, bg = 'white', text="Stop", height = 1, width = 15,
			command = lambda: self.mGyro(0), font=helv12).grid(row=0,column=1)
		
	
	def mGyro(self, k):
		helv12 = tkFont.Font(family='Helvetica', size=12, weight='bold')
		if k == 1:
			self.running =  True
			while self.running == True:
				orientation = sense.get_orientation()
				pitch = orientation['pitch']
				roll = orientation['roll']
				yaw = orientation['yaw']
				self.l4['text'] = str("%.3f" %pitch)
				self.l5['text'] = str("%.3f" %roll)
				self.l6['text'] = str("%.3f" %yaw)
				root.update()			    
		else:
			self.running = False
			# sys.exit()		
						
		
	def senseAcc(self):
		""" Senses dynamic acceleration """
		print "Sensing Acceleration"
		
		helv12 = tkFont.Font(family='Helvetica', size=12, weight='bold') 
		self.Acc = Tk.Toplevel(self.master)
		self.Acc.title("Accelerometer")
		self.Acc.grid_rowconfigure(1, weight=1)
		self.Acc.grid_columnconfigure(1, weight=1)
		self.frame = Tk.Frame(self.Acc)
		self.frame.pack(fill=Tk.X, padx=5, pady=5)

		self.l1 = Tk.Label(self.frame, text= "X: ", font=helv12, height = 1, width = 10)
		self.l1.grid(row=1,column=0)
		
		self.l2 = Tk.Label(self.frame, text= "Y: ", font=helv12, height = 1, width = 10)
		self.l2.grid(row=1,column=1)
		
		self.l3 = Tk.Label(self.frame, text= "Z: ", font=helv12, height = 1, width = 10)
		self.l3.grid(row=1,column=2)
		
		self.l4 = Tk.Label(self.frame, text="0", font=helv12, height = 1, width = 10)
		self.l4.grid(row=2,column=0)
		
		self.l5 = Tk.Label(self.frame, text="0", font=helv12, height = 1, width = 10)
		self.l5.grid(row=2,column=1)
		
		self.l6 = Tk.Label(self.frame, text="0", font=helv12, height = 1, width = 10)
		self.l6.grid(row=2,column=2)

		
		# Start button
		self.buttonStart = Tk.Button(self.frame, bg = 'white', text="Start", height = 1, width = 15,
			command = lambda: self.mAcc(1), font=helv12).grid(row=0,column=0)
		
		# Stop button
		self.buttonStop = Tk.Button(self.frame, bg = 'white', text="Stop", height = 1, width = 15,
			command = lambda: self.mAcc(0), font=helv12).grid(row=0,column=1)

	def mAcc(self, k):
		helv12 = tkFont.Font(family='Helvetica', size=12, weight='bold')
		if k == 1:
			self.running =  True
			while self.running == True:
				raw = sense.get_accelerometer_raw()
				self.l4['text'] = str("%.3f" %raw['x'])
				self.l5['text'] = str("%.3f" %raw['y'])
				self.l6['text'] = str("%.3f" %raw['z'])
				root.update()			    
		else:
			self.running = False
			# sys.exit()					
		
	def senseMagF(self):
		""" Senses dynamic magnetic field """
		print "Sensing Magnetic Field"

		helv12 = tkFont.Font(family='Helvetica', size=12, weight='bold') 
		self.MagF = Tk.Toplevel(self.master)
		self.MagF.title("Magnetometer")
		self.MagF.grid_rowconfigure(1, weight=1)
		self.MagF.grid_columnconfigure(1, weight=1)
		self.frame = Tk.Frame(self.MagF)
		self.frame.pack(fill=Tk.X, padx=5, pady=5)

		self.l1 = Tk.Label(self.frame, text= "X: ", font=helv12, height = 1, width = 10)
		self.l1.grid(row=1,column=0)
		
		self.l2 = Tk.Label(self.frame, text= "Y: ", font=helv12, height = 1, width = 10)
		self.l2.grid(row=1,column=1)
		
		self.l3 = Tk.Label(self.frame, text= "Z: ", font=helv12, height = 1, width = 10)
		self.l3.grid(row=1,column=2)
		
		self.l4 = Tk.Label(self.frame, text="0", font=helv12, height = 1, width = 10)
		self.l4.grid(row=2,column=0)
		
		self.l5 = Tk.Label(self.frame, text="0", font=helv12, height = 1, width = 10)
		self.l5.grid(row=2,column=1)
		
		self.l6 = Tk.Label(self.frame, text="0", font=helv12, height = 1, width = 10)
		self.l6.grid(row=2,column=2)

		
		# Start button
		self.buttonStart = Tk.Button(self.frame, bg = 'white', text="Start", height = 1, width = 15,
			command = lambda: self.mMag(1), font=helv12).grid(row=0,column=0)
		
		# Stop button
		self.buttonStop = Tk.Button(self.frame, bg = 'white', text="Stop", height = 1, width = 15,
			command = lambda: self.mMag(0), font=helv12).grid(row=0,column=1)

	def mMag(self, k):
		helv12 = tkFont.Font(family='Helvetica', size=12, weight='bold')
		if k == 1:
			self.running =  True
			while self.running == True:
				raw = sense.get_compass_raw()
                                self.l4['text'] = str("%.3f" %raw['x'])
                                self.l5['text'] = str("%.3f" %raw['y'])
				self.l6['text'] = str("%.3f" %raw['z'])
				root.update()			    
		else:
			self.running = False
			# sys.exit()	

	def LEDMatrix(self):
		""" Creating new window for RGB LED matrix"""
		
		self.colorButtons()
		
		self.LEDMat = Tk.Toplevel(self.master)
		self.LEDMat.title("LED Matrix")
		self.LEDMat.grid_rowconfigure(1, weight=1)
		self.LEDMat.grid_columnconfigure(1, weight=1)
		
		self.frame = Tk.Frame(self.LEDMat)
		self.frame.pack(fill=Tk.X, padx=5, pady=5)
		
		self.frame2 = Tk.Frame(self.LEDMat)
		self.frame2.pack(fill=Tk.X, padx=5, pady=5)		
		
		
		# Creating Buttons : 8 x 8 Led Matrix
		self.dim = 8
		self.arr = np.zeros((self.dim, self.dim))
		
		self.buttonGrid = []
		self.buttonClickCount = np.zeros((self.dim, self.dim))
		
		# Setting font size and type
		helv10 = tkFont.Font(family='Helvetica', size=10, weight='bold') 
		
		for i in range(0, self.arr.shape[0]):
			row = []
			for j in range(0, self.arr.shape[1]):
				self.button = Tk.Button(self.frame, bg = 'gray', text = str(i+1)+ str(j+1), font=helv10, 
					command = lambda i=i, j=j: self.turnONLED(i, j), height = 2, width = 3)

				row.append(self.button)
				row[-1].grid(row=i,column=j)
			
			self.buttonGrid.append(row)
				
		# Starting LED Matrix 
		self.startLEDMatrix()
	
	def colorButtons(self):
				
		self.ColorList = Tk.Toplevel(self.master)
		self.ColorList.title("Colors")
		self.ColorList.grid_rowconfigure(1, weight=1)
		self.ColorList.grid_columnconfigure(1, weight=1)
		self.frame = Tk.Frame(self.ColorList)
		self.frame.pack(fill=Tk.X, padx=5, pady=5)
		
		# Button : Red
		self.buttonx1 = Tk.Button(self.frame, activebackground='Red', bg = 'Red', height = 2, width = 4,
			command = lambda: self.setColor(1))
		self.buttonx1.pack()
		
		# Button : Green
		self.buttonx2 = Tk.Button(self.frame, activebackground='Green', bg = 'Green', height = 2, width = 4, 
			command = lambda: self.setColor(2))
		self.buttonx2.pack()
		
		# Button : Blue
		self.buttonx3 = Tk.Button(self.frame, activebackground='Blue', bg = 'Blue', height = 2, width = 4,
			command = lambda: self.setColor(3))
		self.buttonx3.pack()
		
		# Button : Red + Green
		self.buttonx4 = Tk.Button(self.frame, activebackground='Yellow', bg = 'Yellow', height = 2, width = 4,
			command = lambda: self.setColor(4))
		self.buttonx4.pack()
		
		# Button : Green + Blue
		self.buttonx5 = Tk.Button(self.frame, activebackground='Cyan', bg = 'Cyan', height = 2, width = 4,
			command = lambda: self.setColor(5))
		self.buttonx5.pack()
		
		# Button : Red + Blue
		self.buttonx6 = Tk.Button(self.frame, activebackground='Magenta', bg = 'Magenta', height = 2, width = 4,
			command = lambda: self.setColor(6))
		self.buttonx6.pack()		
		
		# Button : Red + Green + Blue
		self.buttonx7 = Tk.Button(self.frame, activebackground='White', bg = 'White', height = 2, width = 4,
			command = lambda: self.setColor(7))
		self.buttonx7.pack()	

	def setColor(self, t):
		"""t= {1: Red}, {2: Green}, {3: Blue}, {4: Yellow}, {5: Cyan}, {6: Magenta}, {7: White} """
		if t==1:
			self.color = self.r
			self.colorname = 'Red'
			
		elif t==2:
			self.color = self.g
			self.colorname = 'Green'
			
		elif t==3:
			self.color = self.b
			self.colorname = 'Blue'
		
		elif t==4:
			self.color = self.rg
			self.colorname = 'Yellow'
			
		elif t==5:
			self.color = self.gb
			self.colorname = 'Cyan'
		
		elif t==6:
			self.color = self.rb
			self.colorname = 'Magenta'
			
		elif t==7:
			self.color = self.rgb
			self.colorname = 'White'
			
		else:
			print "Wrong Color Argument, EXIT"
			sys.exit()
	
	
	def startLEDMatrix(self):
		
		for i in range(self.dim):
			for j in range(self.dim):
				if self.background == 0:
					sense.set_pixel(i, j, self.dark)
				else:
					sense.set_pixel(i, j, self.white)			

	def turnONLED(self, posX, posY):		
		
		print "button : ", (posX+1), " ", (posY+1), " count: ", self.buttonClickCount[posX][posY]
		self.buttonClickCount[posX][posY] += 1	
		
		if self.buttonClickCount[posX][posY]%2 == 1:
			self.buttonGrid[posX][posY]["bg"] = self.colorname
			sense.set_pixel(posX, posY, self.color)
		
		else:
			self.buttonGrid[posX][posY]["bg"] = 'Gray'
			sense.set_pixel(posX, posY, self.dark)
		
if __name__ == "__main__":
	
	run_LEDMatrix()
	root = Tk.Tk()
	app = RPiSenseHat(root) 
	root.mainloop()				

# -------------------------------------------- end - of - file ----------------------------------------------------- #
