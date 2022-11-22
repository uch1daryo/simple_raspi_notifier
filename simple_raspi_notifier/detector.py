import pigpio
from simple_raspi_notifier.switch import Switch


class Detector:
    def __init__(self):
        self.is_detected = False
        self._pi = pigpio.pi()

        import os
        from dotenv import load_dotenv

        load_dotenv()
        trigger_gpio_num = int(os.environ["TRIGGER_GPIO_NUM"])
        trigger_gpio_pins = os.environ["TRIGGER_GPIO_PINS"]

        pins = trigger_gpio_pins.split(",")
        if len(pins) != trigger_gpio_num:
            return

        self._switches = []
        for i in range(trigger_gpio_num):
            self._switches.append(Switch(self._pi, int(pins[i])))

    def update(self):
        for switch in self._switches:
            switch.update()
            if not switch.prev_value and switch.curr_value:
                self.is_detected = True
            switch.prev_value = switch.curr_value

    def clear_is_detected(self):
        self.is_detected = False

    def stop(self):
        self._pi.stop()
