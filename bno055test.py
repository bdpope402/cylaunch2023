import adafruit_bno055 as BNO055
import board

i2c = board.I2C()
bno = BNO055.BNO055_I2C(i2c,0x69)
