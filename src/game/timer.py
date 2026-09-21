class Timer:
    """Timer placeholder."""

    def __init__(self, interval=0.016):
        self.interval = interval
        self.running = False

    def start(self):
        self.running = True

    def stop(self):
        self.running = False
