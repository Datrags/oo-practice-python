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
    def __init__(self, start) -> None:
        self.start = start
        self.current = start

    def __repr__(self) -> str:
        return f'start={self.start}, current={self.current}'
    def generate(self) -> int:
        # Generate a new serial number
        self.current += 1
        return self.current
        
    def reset(self) -> None:
        # Reset the serial number to the start value
        self.current = self.start
