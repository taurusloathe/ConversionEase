# measurement_converter.py

class MeasurementConverter:
    def __init__(self):
        self.units = {
            'length': {
                'mm': 1,
                'cm': 10,
                'm': 1000,
                'km': 1000000,
                'in': 25.4,
                'ft': 304.8,
                'yd': 914.4,
                'mile': 1609344
            },
            'weight': {
                'mg': 1,
                'g': 1000,
                'kg': 1000000,
                'ton': 1000000000,
                'oz': 28349.5,
                'lb': 453592,
                'stone': 6350293
            },
            'volume': {
                'ml': 1,
                'l': 1000,
                'cup': 240,
                'pt': 473,
                'qt': 946,
                'gal': 3785,
                'fl oz': 29.5735
            }
        }

    def convert(self, category, value, from_unit, to_unit):
        if category not in self.units:
            raise ValueError(f"Unsupported category: {category}")
        if from_unit not in self.units[category] or to_unit not in self.units[category]:
            raise ValueError(f"Unsupported unit conversion: {from_unit} to {to_unit}")
        from_value = self.units[category][from_unit]
        to_value = self.units[category][to_unit]
        return value * from_value / to_value

# Example usage
if __name__ == "__main__":
    converter = MeasurementConverter()
    category = 'length'
    value = 1000
    from_unit = 'm'
    to_unit = 'km'
    result = converter.convert(category, value, from_unit, to_unit)
    print(f"{value} {from_unit} is {result} {to_unit}")
