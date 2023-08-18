class Celsius:
    """Descriptor for celsius value."""

    def __init__(self, value=0.0):
        self.value = float(value)

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        self.value = float(value)


class Fahrenheit:
    """Descriptor for farenheit value."""

    def __get__(self, instance, owner):
        return (instance.celsius * 9 / 5) + 32.0

    def __set__(self, instance, value):
        instance.celsius = (value - 32) * 5 / 9


class Temperature:
    celsius = Celsius()
    fahrenheit = Fahrenheit()


e = Temperature()
e.celsius = 10
print(f"{e.celsius} ºC = {e.fahrenheit} ºF")
e.fahrenheit = 45
print(f"{e.celsius} ºC = {e.fahrenheit} ºF")
