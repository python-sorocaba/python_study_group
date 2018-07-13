class Measure:

    units = {"cm": 0.01, "m": 100}

    def __init__(self, value, unit):
        unit = unit.lower()
        if unit not in ('m', 'cm'):
            raise ValueError('Invalid unit!')

        self.value = value
        self.unit = unit

    def convert_units(self, measure):
        return self.units[measure.unit] * measure.value

    def __add__(self, measure):
        return self.value + self.convert_units(measure)

    def __repr__(self):
        return f'Measure({self.value}, {self.unit})'
