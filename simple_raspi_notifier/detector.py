import pigpio


class Detector:
    def __init__(self):
        self.is_detected = False
        self._pi = pigpio.pi()
        self._curr_value = False
        self._prev_value = False

        import os
        from dotenv import load_dotenv

        load_dotenv()
        self._trigger_gpio = int(os.environ["TRIGGER_GPIO"])
        active_level = int(os.environ["ACTIVE_LEVEL"])

        self._pi.set_mode(self._trigger_gpio, pigpio.INPUT)

        if active_level == 1:
            self._pi.set_pull_up_down(self._trigger_gpio, pigpio.PUD_DOWN)
            self._value = self._value_in_pulldown
        else:
            self._pi.set_pull_up_down(self._trigger_gpio, pigpio.PUD_UP)
            self._value = self._value_in_pullup

    def _value_in_pulldown(self):
        if self._pi.read(self._trigger_gpio) == 1:
            return True
        else:
            return False

    def _value_in_pullup(self):
        if self._pi.read(self._trigger_gpio) == 0:
            return True
        else:
            return False

    def update(self):
        self._curr_value = self._value()
        if not self._prev_value and self._curr_value:
            self.is_detected = True

        self._prev_value = self._curr_value

    def clear_is_detected(self):
        self.is_detected = False

    def stop(self):
        self._pi.stop()
