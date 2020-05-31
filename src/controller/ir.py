# import RPi.GPIO as GPIO
import pigpio
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
        G1 = 12
        pi = pigpio.pi()

        pi.set_mode(G1, pigpio.OUTPUT)

        flash_500 = []  # flash every 500 ms

        #                              ON     OFF  DELAY

        flash_500.append(pigpio.pulse(1 << G1, 0, 500000))
        flash_500.append(pigpio.pulse(0, 1 << G1, 500000))

        pi.wave_clear()  # clear any existing waveforms

        pi.wave_add_generic(flash_500)  # 500 ms flashes
        f500 = pi.wave_create()  # create and save id

        pi.wave_send_repeat(f500)

        time.sleep(4)

        pi.wave_send_repeat(f500)

        time.sleep(4)

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
