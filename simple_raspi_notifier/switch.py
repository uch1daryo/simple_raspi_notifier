import pigpio


class Switch:
    def __init__(self, pi, pin):
        self._pi = pi
        self._pin = pin
        self.curr_value = False
        self.prev_value = False

        import os
        from dotenv import load_dotenv

        load_dotenv()
        active_level = int(os.environ["ACTIVE_LEVEL"])

        self._pi.set_mode(self._pin, pigpio.INPUT)

        if active_level == 1:
            self._pi.set_pull_up_down(self._pin, pigpio.PUD_DOWN)
            self._value = self._value_in_pulldown
        else:
            self._pi.set_pull_up_down(self._pin, pigpio.PUD_UP)
            self._value = self._value_in_pullup

    def _value_in_pulldown(self):
        if self._pi.read(self._pin) == 1:
            return True
        else:
            return False

    def _value_in_pullup(self):
        if self._pi.read(self._pin) == 0:
            return True
        else:
            return False

    def update(self):
        self.curr_value = self._value()
