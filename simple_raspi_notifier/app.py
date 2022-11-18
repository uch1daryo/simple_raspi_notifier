from simple_raspi_notifier.detector import Detector
from simple_raspi_notifier.notifier import Notifier


class App:
    def __init__(self):
        self.detector = Detector()
        self.notifier = Notifier()

    def run(self):
        self.detector.update()
        if self.detector.is_detected:
            self.notifier.notify()
            self.detector.clear_is_detected()

    def stop(self):
        self.detector.stop()
        self.notifier.stop()
