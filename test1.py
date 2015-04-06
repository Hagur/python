import Adafruit_BBIO.GPIO as GPIO
import smbus
import time

i2c = smbus.SMBus(2) # Si4703 is connected to I2C1

address = 0x10

print "Initial Register Readings"
reg = i2c.read_i2c_block_data(address, 0, 32)
print reg 

#write x8100 to reg 7 to activate oscellitor
list1 = [0,0,0,0,0,0,0,0,0,129,0]
print list1
w6 = i2c.write_i2c_block_data(address, 0, list1)
time.sleep(1) 

#write x4001 to reg 2 to turn off mute and activate IC
list1 = [1]
print list1
w6 = i2c.write_i2c_block_data(address, 64, list1)
time.sleep(.1) 

#write volume
print "Doing Volume lowest setting"
list1 = [1,0,0,0,0,0,1]
print list1
w6 = i2c.write_i2c_block_data(address, 64, list1) 

#write spacing and default volume
print "Setting Spacing and default Volume"
list1 = [1,0,0,0,0,0,17] # last byte: 16+volume(0-15)
w6 = i2c.write_i2c_block_data(address, 64, list1)

#write channel
print "Setting Channel, Radio Eger"
 
# f = s*nc - 87.5MHz
nc = 1013 #this is 101.3
nc *=10
nc -= 8750
nc /= 10 # Used in Europe
 
list1 = [1,128, nc]
#set tune bit and set channel
w6 = i2c.write_i2c_block_data(address, 64, list1)
time.sleep(1) #allow tuner to tune
# clear channel tune bit
list1 = [1,0,nc]
w6 = i2c.write_i2c_block_data(address, 64, list1) 
 
#You should be hearing music now!
#Headphone Cord acts as antenna

# GPIO beallitasok
#GPIO.setup("P9_25", GPIO.OUT)
#GPIO.output("P9_25", GPIO.HIGH)
#value = open('/sys/class/gpio/gpio117/value').read()
#print value
#GPIO.cleanup()
