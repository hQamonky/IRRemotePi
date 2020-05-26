# import RPi.GPIO as GPIO
import board
import pulseio
import array
import time

# Set GPIO pins
# TR = 12  # Transmitter GPIO pin
# RR = board.D13  # Receiver GPIO pin

# Initiate GPIO
# GPIO.setmode(GPIO.BCM)
# GPIO.setup(TR, GPIO.OUT)
# p = GPIO.PWM(TR, 38000)
# ir_read = pulseio.PulseIn(RR, maxlen=100, idle_state=True)
# ir_read.pause()