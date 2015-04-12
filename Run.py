import serial                                                  #import serial module
import NASA_Conn
from NASA_Conn_TT import check
def read_rfid ():
   ser = serial.Serial ("/dev/ttyAMA0")                           #Open named port 
   ser.baudrate = 9600                                            #Set baud rate to 9600
   data = ser.read(12)                                            #Read 12 characters from serial port to data
   ser.close ()                                                   #Close port
   return data                                                    #Return data

print ("Reading,Type ctrl+z to exit: ")
id = read_rfid ()
id=int(id,16)
check(id)                                              #Function call          
