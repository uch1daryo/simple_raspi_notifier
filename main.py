#!/usr/bin/env python3
import time
from simple_raspi_notifier.app import App


def main():
    try:
        app = App()
        while True:
            app.run()
            time.sleep(0.5)
    except KeyboardInterrupt:
        pass
    finally:
        app.stop()


if __name__ == "__main__":
    main()
