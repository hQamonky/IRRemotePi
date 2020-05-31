# import RPi.GPIO as GPIO
import pigpio
import board
import pulseio
import array
import time
import subprocess

# Making sure pigpio daemon is started
process = subprocess.run(["sudo", "pigpiod"], check=True, stdout=subprocess.PIPE, universal_newlines=True)


class IR:
    # Set GPIO pins
    TR_pin = 12  # Transmitter GPIO pin
    RR_pin = board.D13  # Receiver GPIO pin
    IR_TR = None
    IR_RR = None

    def __init__(self):
        # Initiate GPIO
        # GPIO.setmode(GPIO.BCM)
        # GPIO.setup(self.TR_pin, GPIO.OUT)

        self.IR_TR = pigpio.pi()
        # Check connection to pigpio
        if not self.IR_TR.connected:
            print("pigpio not connected")
        else:
            # Set pin mode
            self.IR_TR.set_mode(self.TR_pin, pigpio.OUTPUT)
        # Initiate ir transmitter variable
        self.IR_TR.set_PWM_frequency(self.TR_pin, 38000)
        self.IR_TR.set_PWM_dutycycle(self.TR_pin, 128)
        # self.IR_TR = GPIO.PWM(self.TR_pin, 38000)
        # self.IR_TR.stop()

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

        # -- Testing
        pin = 12
        frequency = 38000
        duration = 100
        pi = pigpio.pi()

        pi.set_mode(pin, pigpio.OUTPUT)
        frequency = int((1000 / frequency) * 1000)

        tone = [pigpio.pulse(1 << pin, 0, frequency), pigpio.pulse(0, 1 << pin, frequency)]  # flash every 100 ms

        pi.wave_clear()

        pi.wave_add_generic(tone)  # 100 ms flashes
        tone_wave = pi.wave_create()  # create and save id
        pi.wave_send_repeat(tone_wave)

        if duration == 0:
            return

        sleep_time = duration * .001
        time.sleep(sleep_time)
        pi.wave_tx_stop()  # stop waveform

        pi.wave_clear()  # clear all waveforms

        # c_signal = array.array('H', [signal[x] for x in range(len(signal))])
        # on = False
        # for timer in c_signal:
        #     if on:
        #         self.IR_TR.stop()
        #         on = False
        #     else:
        #         self.IR_TR.start(50)
        #         on = True
        #     time.sleep(timer / 1000000)
        # self.IR_TR.stop()




    def stop_pigpio(self):
        self.IR_TR.stop()
