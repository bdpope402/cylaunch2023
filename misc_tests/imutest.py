import time
import board
import busio
import adafruit_bno055


i2c = busio.I2C(board.SCL, board.SDA)  # uses board.SCL and board.SDA
print(i2c.scan())

# # i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller
sensor = adafruit_bno055.BNO055_I2C(i2c, 105)

# # If you are going to use UART uncomment these lines
# # uart = board.UART()
# # sensor = adafruit_bno055.BNO055_UART(uart)

# last_val = 0xFFFF


# def temperature():
#     global last_val  # pylint: disable=global-statement
#     result = sensor.temperature
#     if abs(result - last_val) == 128:
#         result = sensor.temperature
#         if abs(result - last_val) == 128:
#             return 0b00111111 & result
#     last_val = result
#     return result


# while True:
#     print("Temperature: {} degrees C".format(sensor.temperature))
#     """
#     print(
#         "Temperature: {} degrees C".format(temperature())
#     )  # Uncomment if using a Raspberry Pi
#     """
#     print("Accelerometer (m/s^2): {}".format(sensor.acceleration))
#     print("Magnetometer (microteslas): {}".format(sensor.magnetic))
#     print("Gyroscope (rad/sec): {}".format(sensor.gyro))
#     print("Euler angle: {}".format(sensor.euler))
#     print("Quaternion: {}".format(sensor.quaternion))
#     print("Linear acceleration (m/s^2): {}".format(sensor.linear_acceleration))
#     print("Gravity (m/s^2): {}".format(sensor.gravity))
#     print()

#     time.sleep(1)