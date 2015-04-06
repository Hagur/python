import Adafruit_BBIO.GPIO as GPIO
import time
import smbus

i2c = smbus.SMBus(2)

reg = i2c.read_i2c_block_data(0x10, 64, 32)
print reg
