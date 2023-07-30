"""
CP1404 Practical 08
convert_m_km.py
Estimated time: 15 mins
Actual time: 17 mins
"""

from kivy.app import App
from kivy.lang import Builder

MILES_to_KM = 1.60934

class MilesConversionApp(App):
    """ App converts miles to km """
    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_m_km.kv')
        return self.root

    def handle_convert(self):
        value = self.validate_value()

        result = self.root.ids.input_miles.text * MILES_to_KM
        self.root.ids.output_km.text = str(result)

    def validate_value(self):
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0.0

    def handle_increment(self, change):
        increment = self.root.ids.input_miles.text + change
        self.root.ids.input_miles.text = str(increment)
        self.handle_convert()

MilesConversionApp().run()