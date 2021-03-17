"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self,start):
        self.start = start-1
        self.current_number = self.start

    def generate(self):
        self.current_number+=1
        return self.current_number

    def reset(self):
        self.current_number = self.start


