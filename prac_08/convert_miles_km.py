"""
CP1404 Practical 8
convert_miles_km.py

"""

from kivy.app import App
from kivy.lang import Builder

MILES_to_KM = 1.60934

class MileKmConversionApp(App):

    def build(self):
        self.title = "Convert Mile to Km"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_convert(self):
        value = self.validate_value()
        result = value * MILES_to_KM
        self.root.ids.output_number.text = str(result)

    def validate_value(self):
        try:
            value = float(self.root.ids.input_number.text)
            return value
        except ValueError:
            return 0.0

    def handle_increment(self, change):
        value = self.validate_value() + change
        self.root.ids.input_number.text = str(value)
        self.handle_convert()

MileKmConversionApp().run()