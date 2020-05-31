import RPi.GPIO as GPIO
import board
import pulseio
import array
import time


class IR:
    # Set GPIO pins
    TR_pin = 12  # Transmitter GPIO pin
    RR_pin = board.D13  # Receiver GPIO pin
    IR_TR = None
    IR_RR = None

    def __init__(self):
        # Initiate GPIO
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.TR_pin, GPIO.OUT)
        # Initiate ir transmitter variable
        self.IR_TR = GPIO.PWM(self.TR_pin, 38000)
        self.IR_TR.stop()
        # Initiate ir receiver variable
        self.IR_RR = pulseio.PulseIn(self.RR_pin, maxlen=100, idle_state=True)
        self.IR_RR.pause()

    def start_recording(self):
        self.IR_RR.resume()

    def stop_recording(self):
        self.IR_RR.pause()
        signal = array.array('H', [self.IR_RR[x] for x in range(len(self.IR_RR))])
        signal = [self.IR_RR[x] for x in range(len(self.IR_RR))]
        self.reset_rr()
        return signal

    def reset_rr(self):
        self.IR_RR.clear()

    def send(self, command):
        signal = eval(command)
        c_signal = array.array('H', [signal[x] for x in range(len(signal))])
        on = False
        for timer in c_signal:
            if on:
                self.IR_TR.stop()
                on = False
            else:
                self.IR_TR.start(50)
                on = True
            time.sleep(timer / 1000000)
